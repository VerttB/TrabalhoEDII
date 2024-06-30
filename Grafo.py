import folium
from igraph import Graph, plot
from geopy.geocoders import Nominatim
import json

localizacoes = {
    "Barra": {"local": [-13.010249, -38.532239], "id_grafo": 0},
    "Pirajá": {"local": [-12.897911, -38.460675], "id_grafo": 1},
    "CAB": {"local": [-12.946825, -38.433177], "id_grafo": 2},
    "Liberdade": {"local": [-12.949713, -38.495420], "id_grafo": 3},
    "Barbalho": {"local": [-12.963536, -38.500784], "id_grafo": 4},
    "Centro": {"local": [-12.985236, -38.501926], "id_grafo": 5},
    "Graça": {"local": [-12.998466, -38.521473], "id_grafo": 6},
    "Imbuí": {"local": [-12.970441, -38.435245], "id_grafo": 7},
    "Pernambués": {"local": [-12.9735, -38.4684], "id_grafo": 8},
    "Patamares": {"local": [-12.952295, -38.404354], "id_grafo": 9},
    "São Cristóvão": {"local": [-12.911661, -38.354020], "id_grafo": 10},
    "Pelourinho": {"local": [-12.971452, -38.510785], "id_grafo": 11},
    "Ondina": {"local": [-13.006646, -38.509368], "id_grafo": 12},
    "Itapuã": {"local": [-12.937259, -38.359962], "id_grafo": 13},
    "Pituba": {"local": [-13.002745, -38.45879], "id_grafo": 14},
    "Rio Vermelho": {"local": [-13.009455, -38.489772], "id_grafo": 15},
    "Caminho das Árvores": {"local": [-12.981745, -38.455479], "id_grafo": 16},
    "Federação": {"local": [-13.000529, -38.509286], "id_grafo": 17},
    "Brotas": {"local": [-12.981728, -38.478233], "id_grafo": 18},
    "Stiep": {"local": [-12.981061, -38.445276], "id_grafo": 19},
    "Cajazeiras": {"local": [-12.897974, -38.408924], "id_grafo": 20},
    "Bonfim": {"local": [-12.925631, -38.508293], "id_grafo": 21},
    "São Caetano": {"local": [-12.931283, -38.474042], "id_grafo": 22},
    "Ribeira": {"local": [-12.920075, -38.499503], "id_grafo": 23},
    "UNEB - Cabula": {"local": [-12.958299, -38.448005], "id_grafo": 24}
}

# UNEB - CABULA
local_inicio = 24 

#----------------------------------------------------------------------------------------------------------------------------

def criaGrafo(destino):
    # Criando o grafo
    grafo = Graph(directed=True)
    grafo.add_vertices(len(localizacoes))

    # Adicionando propriedades aos vértices
    cont = 0
    for id, item in localizacoes.items():
        grafo.vs[cont]["id"] = cont + 1
        grafo.vs[cont]["label"] = str(id) 
        grafo.vs[cont]["coord"] = item["local"]
        cont += 1


    arestas = [(24, 2), (2, 9), (9, 13),(24, 7), (7, 19), (19, 16), (16, 8), (16, 14), (14, 15), (8, 18), (15, 12), (12, 17),
            (17, 6), (6, 0), (18, 5), (5, 17), (5, 11), (11, 4), (4, 3), (3, 21), (21, 23), (3, 22), (22, 1), (1, 20), (13, 10), (20, 10)]

    pesos = [3, 2, 6, 3, 4, 2, 2, 3, 5, 2, 3, 2, 2, 3, 3, 3, 2, 2, 4, 5, 5, 6, 5, 6, 3, 6]

    grafo.add_edges(arestas)
    grafo.es['weight'] = pesos
    grafo.es['label'] = pesos

    # Criando o mapa centrado em Salvador
    m = folium.Map(location=[-12.9714, -38.5014], zoom_start=12)
    
    adicionaLinhasGrafo(grafo, m, destino)
    
    
    frete = {}
    frete["valor"] = calcfrete(grafo, pesos, destino)
    criarFrete(frete)

#----------------------------------------------------------------------------------------------------------------------------

def adicionaLinhasGrafo(grafo, map, destino):
    
    local_destino = acharIDdestino(destino)
    
    rota = grafo.get_shortest_paths(local_inicio, to=local_destino)
    caminho = geraDicioLocais(rota)
    
    cont = 0     
    for id, item in caminho.items():
        folium.Marker(location=item["local"], popup=id, tooltip=id + " - " + str(cont)).add_to(map)
        cont += 1
    
        
    listaCoord = []
    for id, item in caminho.items():
        listaCoord.append(item["local"])
        
        if len(listaCoord) > 1:
            start_coord = listaCoord[len(listaCoord)-2]
            end_coord = listaCoord[len(listaCoord)-1]
            folium.PolyLine(locations=[start_coord, end_coord], color='red').add_to(map)
        
    map.save('static/assets/mapa/mapa_grafo_salvador.html')

#----------------------------------------------------------------------------------------------------------------------------    

def calcfrete(grafo, pesos, destino):
    
    local_destino = acharIDdestino(destino)
    
    # Corrigido para ser um número decimal
    valor_per_peso = 3 
    print(local_destino)

    caminho = grafo.shortest_paths_dijkstra(source=local_inicio, target=local_destino, weights=pesos, mode="OUT")
    distancia = caminho[0][0]
    valor_pagar = valor_per_peso * distancia
    
    return valor_pagar

#----------------------------------------------------------------------------------------------------------------------------

def acharIDdestino(destino):
    # Acha local escolhido
    if type(destino) == str:
        for id, item in localizacoes.items():
            if destino == id: 
                local_destino = item["id_grafo"]
                return local_destino

def geraDicioLocais(rotas):
    dicio_novo = {}
    for num in rotas[0]:
        for id, item in localizacoes.items():
            if num == item["id_grafo"]:
                dicio_novo[id] = item
                break
    return dicio_novo

def criarFrete(dicts):
    with open('static/assets/frete.json', 'w') as arquivo:
        arquivo.write(json.dumps(dicts, indent='\t')) 
    dicts = dict(sorted(dicts.items()))