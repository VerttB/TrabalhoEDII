import { comunicaPython } from "./comunicacao.js";

const gridBoxes = document.querySelectorAll('#box');
const qtdCompras = document.getElementById('qtdCompras')
const finalizarCompra = document.getElementById('finalizarCompra')
const listaProdutos = []
const iniciarCompra = document.getElementById("compras")
const dialogoCompras = document.getElementById("dialogoCompras")


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
}

preencherLista();
function preencherDialog() {
    listaProdutos.forEach(produto => {
        const div = document.createElement("div");
        div.innerHTML = `${produto.nome}|${produto.preco}|${produto.quantidade}`;
        dialogoCompras.appendChild(div);
    })
}

iniciarCompra.addEventListener("click", () => {
    preencherDialog();
    dialogoCompras.classList.add("showDialogoCompras")
    dialogoCompras.showModal();
    console.log("eae");
})

finalizarCompra.addEventListener('click', () => {
    localStorage.removeItem("listaProdutos");
    //comunicaPython(listaProdutos, '/comprar')
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
}
