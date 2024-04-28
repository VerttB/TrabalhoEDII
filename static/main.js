var lista = []
testeClick();

window.addEventListener('DOMContentLoaded', (event) =>{
    var tema = localStorage.getItem('theme')
    if(tema != null){
      document.body.classList.add(tema)
    }
    
  });

      document.querySelector("#changeTheme").addEventListener("click", () => {
      document.body.classList.toggle("mudar-tema");
      tema_atual = document.body.classList.contains('mudar-tema') ? 'mudar-tema' : ''
      localStorage.setItem('theme', tema_atual);
});

  function armazenaTexto(){
      let texto = document.querySelector('input').value
      localStorage.setItem('texto', texto);
  }

  window.onload = function(){
    var texto = localStorage.getItem('texto');
    document.querySelector('input').setAttribute('value', texto);
    testeClick();
  }

function testeClick() {
    var lista = document.querySelectorAll('tr');
    lista.forEach(function(elemento) {
        elemento.addEventListener('click', function() {
            console.log(this.innerText);
            filhos = this.getElementsByTagName('td');
            console.log(filhos[2].innerText);
            alert('Produto Adicionado ao Carrinho');
        });
    });
}


