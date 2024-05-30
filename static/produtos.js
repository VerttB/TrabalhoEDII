const gridBoxes = document.querySelectorAll('#box');
const compras = document.getElementById('compras');
const qtdCompras = document.getElementById('qtdCompras')
const listaProdutos = []

const produto = {
    nome: "",
    preco: "",
    imagemSrc: "",
    quantidade: "",
}

gridBoxes.forEach( (gridBox) =>{
    gridBox.addEventListener('click', () => {
        nome = gridBox.querySelector('#nome');
        preco = gridBox.querySelector('#preco');
        imagemSrc = gridBox.querySelector('img');
        adicionaProdutos(nome,preco,imagemSrc);
        qtdCompras.textContent = Number(qtdCompras.textContent) + 1;
        
    })
})


function adicionaProdutos(nome,preco,imagemSrc){
    

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
}
}