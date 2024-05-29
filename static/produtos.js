const gridBoxes = document.querySelectorAll('#box');
listaProdutos = []

const produto = {
    nome: "nome",
    preco: "preco",
    imagemSrc: "path"
};

gridBoxes.forEach( (gridBox) =>{
    gridBox.addEventListener('click', () => {
        nome = gridBox.querySelector('#nome');
        preco = gridBox.querySelector('#preco');
        imagemSrc = gridBox.querySelector('img');
        produto.nome = nome.textContent
        produto.preco = preco.textContent
        produto.imagemSrc = imagemSrc.src
        listaProdutos.push(produto)
    })
})

