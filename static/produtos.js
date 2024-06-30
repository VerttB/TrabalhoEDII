import { comunicaPython } from "./comunicacao.js";

const gridBoxes = document.querySelectorAll('#box');
const qtdCompras = document.getElementById('qtdCompras')
const finalizarCompra = document.getElementById('finalizarCompra')
const listaProdutos = []
const iniciarCompra = document.getElementById("compras")
const dialogoCompras = document.getElementById("dialogoCompras")
const destino = document.getElementById("destino")
const destinatario = document.getElementById("destinatario")
const dataList = document.getElementById("destinos")
const produtosTabela = document.getElementById("produtosTabela")
let listaBairros = []
 

preencherDatalist();

 function criarOptions(bairros){
     console.log(bairros)
     bairros.forEach(bairro => {
        console.log(bairro)
        const newOption = document.createElement("option");
        newOption.value = bairro;
        dataList.appendChild(newOption);
     })
}



function preencherLista() {
    let lista = localStorage.getItem("listaProdutos") || [];
    if (lista.length !== 0) {
    let listaAntiga = JSON.parse(lista);
        console.log(listaAntiga);
        listaAntiga.forEach(produto => {
            listaProdutos.push(produto);
            qtdCompras.textContent = Number(qtdCompras.textContent) + produto.quantidade;
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
    localStorage.removeItem("listaProdutos");
    let tudo = []
    tudo.push(listaProdutos)
    tudo.push(destino.value)
    tudo.push(destinatario.value)
    comunicaPython(tudo, '/comprar')
})

gridBoxes.forEach((gridBox) => {
    gridBox.addEventListener('click', () => {
        const nome = gridBox.querySelector('#nome');
        const preco = gridBox.querySelector('#preco');
        const imagemSrc = gridBox.querySelector('img');
        adicionaProdutos(nome, preco, imagemSrc);
        qtdCompras.textContent = Number(qtdCompras.textContent) + 1;

    })
})


function adicionaProdutos(nome, preco, imagemSrc) {
    console.log("destinatario", destinatario.value);
    console.log("destino",destino.value);
    console.log(destinatario);
    const produto = {
        nome: "",
        preco: "",
        imagemSrc: "",
        quantidade: "",
    }


    if (!listaProdutos.some(p => p['nome'] === nome.textContent)) {
        produto.nome = nome.textContent;
        produto.preco = preco.textContent;
        produto.imagemSrc = imagemSrc.src;
        produto.quantidade = 1;
        console.log("Entrei aqui");
        listaProdutos.push(produto);

    }
    else {
        const produtoAchado = listaProdutos.find(p => p.nome === nome.textContent);
        produtoAchado.quantidade += 1;
        console.log("Quantidade ")
    }
    let listaString = JSON.stringify(listaProdutos)
    localStorage.setItem("listaProdutos", listaString);
    adicionarProdutoDialog();
}

function adicionarProdutoDialog(){
listaProdutos.forEach((produto) => {
        if(!verificaAumentoQuantidade(produto)){
            console.log("produto adicionado");
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
    })
}


function verificaAumentoQuantidade(p){
    console.log("entrei onde devia");
    const produtosTabelaLista = produtosTabela.querySelectorAll('.produtoDados');
    for (let i = 0; i < produtosTabelaLista.length; i++){
        const div = produtosTabelaLista[i]
        if(div.getAttribute("produto") === p.nome ){
            const quantidade = div.querySelectorAll("div")[2];
            quantidade.textContent = parseInt(quantidade.textContent) + 1;
            return true;
        }
    }
    

    return false
   
}