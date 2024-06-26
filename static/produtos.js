import { comunicaPython } from "./comunicacao.js";

const gridBoxes = document.querySelectorAll('#box');
const qtdCompras = document.getElementById('qtdCompras');
const finalizarCompra = document.getElementById('finalizarCompra');
const listaProdutos = [];
const iniciarCompra = document.getElementById("compras");
const dialogoCompras = document.getElementById("dialogoCompras");
const destino = document.getElementById("destino");
const produtosTabela = document.getElementById("produtosTabela");
const precoCompra = document.getElementById("precoCompra");
const frete = document.getElementById("frete");
const verMapa = document.getElementById("verMapa");

preencherDatalist();
preencherLista();
verMapa.setAttribute("disabled", "true");
finalizarCompra.setAttribute("disabled", "true");
verMapa.addEventListener("click", () => {
    window.open("static/assets/mapa/mapa_grafo_salvador.html", "_blank");
})
function lerFrete(){
    fetch("static/assets/frete.json")
    .then(reponse => reponse.json())
    .then(dado => {frete.textContent = dado.valor; console.log(dado)})
    .catch(err => console.error(err));

    
}

destino.addEventListener("change", (event) => {
    comunicaPython(event.target.value,"/frete", false);
    setTimeout( () => lerFrete(), 50);
    verMapa.removeAttribute("disabled");
    finalizarCompra.removeAttribute("disabled");
    verMapa.classList.add('coloridoButao');
    
})


function criarOptions(bairros){
     bairros.forEach(bairro => {
        const newOption = document.createElement("option");
        newOption.value = bairro;
        newOption.textContent = bairro.toString();
        destino.appendChild(newOption);

     })
}

function atualizarPreco(preco, quantidade = 0) {
    const precoAcalcular = preco.slice(3).replace(',', '.'); 
    let precoDaCompra = 0;

    if (quantidade !== 0) {
        precoDaCompra = (parseFloat(precoAcalcular) * parseFloat(quantidade)).toFixed(2);
    } else {
        precoDaCompra = parseFloat(precoAcalcular).toFixed(2);
    }
    const precoCompraAtualTexto = precoCompra.textContent.replace(',', '.');
    const precoCompraAtual = parseFloat(precoCompraAtualTexto) || 0; // Default to 0 if empty or non-numeric
    const valorTotal = precoCompraAtual + parseFloat(precoDaCompra);

    if (!isNaN(valorTotal)) {
        precoCompra.textContent = valorTotal.toFixed(2); // Format to two decimal places
    } else {
        console.error("Invalid total value computed:", valorTotal);
    }

}


function preencherLista() {
    let lista = localStorage.getItem("listaProdutos") || [];
    if (lista.length !== 0) {
    let listaAntiga = JSON.parse(lista);
        listaAntiga.forEach(produto => {
            listaProdutos.push(produto);
            qtdCompras.textContent = Number(qtdCompras.textContent) + produto.quantidade;
            atualizarPreco(produto.preco, produto.quantidade);
            adicionarProdutoDialog(produto);
        })
    }

    console.table(listaProdutos);
}

function preencherDatalist(){
    fetch('static/assets/localizacoes.json')
    .then(response => response.json())
    .then(itens => {
        criarOptions(Object.keys(itens))

    })
    .catch(error => console.error('Error:', error));
}






iniciarCompra.addEventListener("click", () => {
    dialogoCompras.classList.add("showDialogoCompras")
    dialogoCompras.showModal();
})

finalizarCompra.addEventListener('click', () => {
    if(!(listaProdutos.length === 0)){
        localStorage.removeItem("listaProdutos");
        let tudo = []
        tudo.push(listaProdutos)
        tudo.push(destino.value)
        comunicaPython(tudo, '/comprar')
    }
    else{
        document.getElementById("warn").style.display = "inline"
    }
})

gridBoxes.forEach((gridBox) => {
    gridBox.addEventListener('click', () => {
        const nome = gridBox.querySelector('#nome');
        const preco = gridBox.querySelector('#preco');
        adicionaProdutos(nome, preco);
        qtdCompras.textContent = Number(qtdCompras.textContent) + 1;

    })
})


function adicionaProdutos(nome, preco) {

    const produto = {
        nome: "",
        preco: "",
        quantidade: "",
    }


    if (!listaProdutos.some(p => p['nome'] === nome.textContent)) {
        produto.nome = nome.textContent;
        const precoNovo = preco.textContent.replace(',','.');
        produto.preco = precoNovo;
        produto.quantidade = 1;
        listaProdutos.push(produto);
        adicionarProdutoDialog(produto);
        atualizarPreco(produto.preco);


    }
    else {
        const produtoAchado = listaProdutos.find(p => p.nome === nome.textContent);
        produtoAchado.quantidade += 1;
        adicionarProdutoDialog(produtoAchado);
        atualizarPreco(produtoAchado.preco);

    }
    let listaString = JSON.stringify(listaProdutos);
    document.getElementById("warn").style.display = 'none';
    localStorage.setItem("listaProdutos", listaString);
    
}

function adicionarProdutoDialog(produto){
        if(!verificaAumentoQuantidade(produto)){
            const produtoDados = document.createElement("div");
            produtoDados.setAttribute(`produto`, produto.nome);
            const produtoNomeDiv = document.createElement("div");
            const produtoPrecoDiv = document.createElement("div");
            const produtoQuantidadeDiv = document.createElement("div");
            
            produtoNomeDiv.setAttribute('name', produto.nome);
            produtoPrecoDiv.setAttribute('price', produto.preco);
            produtoQuantidadeDiv.setAttribute("quantidade", produto.quantidade);

            produtoNomeDiv.textContent = produto.nome;
            produtoPrecoDiv.textContent = produto.preco;
            produtoQuantidadeDiv.textContent = produto.quantidade;

            produtoDados.appendChild(produtoNomeDiv);
            produtoDados.appendChild(produtoPrecoDiv);
            produtoDados.appendChild(produtoQuantidadeDiv);

            produtoDados.classList.add("produtoDados");
        

            produtosTabela.appendChild(produtoDados);
        }
}


function verificaAumentoQuantidade(p){
    const produtosTabelaLista = produtosTabela.querySelectorAll('.produtoDados');
    for (let i = 0; i < produtosTabelaLista.length; i++){
        const div = produtosTabelaLista[i]
        if(div.getAttribute("produto") === p.nome){
            const quantidade = div.querySelectorAll("div")[2];
            quantidade.textContent = parseInt(quantidade.textContent) + 1;
            return true;
        }
    }
    

    return false
   
}