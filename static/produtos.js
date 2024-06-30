import { comunicaPython } from "./comunicacao.js";

const gridBoxes = document.querySelectorAll('#box');
const qtdCompras = document.getElementById('qtdCompras');
const finalizarCompra = document.getElementById('finalizarCompra');
const listaProdutos = [];
const iniciarCompra = document.getElementById("compras");
const dialogoCompras = document.getElementById("dialogoCompras");
const destino = document.getElementById("destino");
const dataList = document.getElementById("destinos");
const produtosTabela = document.getElementById("produtosTabela");
const precoCompra = document.getElementById("precoCompra");


preencherDatalist();
preencherLista();

function criarOptions(bairros){
     bairros.forEach(bairro => {
        const newOption = document.createElement("option");
        newOption.value = bairro;
        dataList.appendChild(newOption);
     })
}

function atualizarPreco(preco, quantidade = 0) {
    const precoAcalcular = preco.slice(3).replace(',', '.'); // Example: "R$ 6,99" => "6.99"
    let precoDaCompra = 0;

    if (quantidade !== 0) {
        precoDaCompra = (parseFloat(precoAcalcular) * parseFloat(quantidade)).toFixed(2);
        console.log("Calculation with quantity:", precoDaCompra);
    } else {
        precoDaCompra = parseFloat(precoAcalcular).toFixed(2);
        console.log("Base price:", precoDaCompra);
    }

    console.log("Computed price:", precoDaCompra);

    const precoCompraAtualTexto = precoCompra.textContent.replace(',', '.');
    const precoCompraAtual = parseFloat(precoCompraAtualTexto) || 0; // Default to 0 if empty or non-numeric
    console.log("Current purchase value:", precoCompraAtual);

    const valorTotal = precoCompraAtual + parseFloat(precoDaCompra);
    console.log("Total value:", valorTotal);

    if (!isNaN(valorTotal)) {
        precoCompra.textContent = valorTotal.toFixed(2); // Format to two decimal places
    } else {
        console.error("Invalid total value computed:", valorTotal);
    }

    console.log("Updated purchase value:", precoCompra.textContent);
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
    localStorage.removeItem("listaProdutos");
    let tudo = []
    tudo.push(listaProdutos)
    tudo.push(destino.value)
    comunicaPython(tudo, '/comprar')
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
        atualizarPreco(produto.preco);


    }
    else {
        const produtoAchado = listaProdutos.find(p => p.nome === nome.textContent);
        produtoAchado.quantidade += 1;
        adicionarProdutoDialog(produtoAchado);
        atualizarPreco(produtoAchado.preco);

    }
    let listaString = JSON.stringify(listaProdutos);
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