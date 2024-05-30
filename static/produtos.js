import { comunicaPython } from "./comunicacao.js";

const gridBoxes = document.querySelectorAll('#box');
const compras = document.getElementById('compras');
const qtdCompras = document.getElementById('qtdCompras')
const finalizarCompra = document.getElementById('finalizarCompra')
const listaProdutos = []


finalizarCompra.addEventListener('click', () => {
    comunicaPython(listaProdutos, '/comprar')
})

gridBoxes.forEach( (gridBox) =>{
    gridBox.addEventListener('click', () => {
        const nome = gridBox.querySelector('#nome');
        const preco = gridBox.querySelector('#preco');
        const imagemSrc = gridBox.querySelector('img');
        adicionaProdutos(nome,preco,imagemSrc);
        qtdCompras.textContent = Number(qtdCompras.textContent) + 1;
        
    })
})


function adicionaProdutos(nome,preco,imagemSrc){
    
const produto = {
        nome: "",
        preco: "",
        imagemSrc: "",
        quantidade: "",
    }
    

if(!listaProdutos.some(p => p['nome'] === nome.textContent)){
    produto.nome = nome.textContent;
    produto.preco = preco.textContent;
    produto.imagemSrc = imagemSrc.src;
    produto.quantidade = 1;
    console.log("Entrei aqui");
    listaProdutos.push(produto);

}
else{
  const produtoAchado = listaProdutos.find(p => p.nome === nome.textContent);
  produtoAchado.quantidade +=1;
  console.log("Quantidade ")
}
}
