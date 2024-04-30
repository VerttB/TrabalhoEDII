var itens = []
var elementoSelecionado = null
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
    pegarInfo();
    deleteOnPy();
    clicavel();
    modifyOnPy();
    clicavel();
  }

function clicavel(){
    var tabela = document.querySelectorAll('tr');
    tabela.forEach(function(elemento){
      elemento.onclick = function(){
        toggleSelecao(elemento);
      };
    });
  }
    function toggleSelecao(elemento) {
  
      // Alterna a seleção do elemento atual
      if (elemento === elementoSelecionado) {
          // 3 === é para ver se é do mesmo tipo
          elemento.style.backgroundColor = ''; // Volta a cor de fundo original
          elementoSelecionado = null;
      } else {
          
          elemento.style.backgroundColor = 'rgb(214, 90, 49)';
          elementoSelecionado = elemento;
      }
  }

function pegarInfo() {
    var lista = document.querySelectorAll('tr');
    lista.forEach(function(elemento) {
        elemento.addEventListener('click', function() {
            console.log(this.innerText);
            filhos = this.getElementsByTagName('td');
            itens = filhos
        });
    });
   
}

 function deleteOnPy(){
     let button = document.getElementById('deletar');
     button.addEventListener('click', function(){
        console.log("Poisé: " + itens[0].innerText);
        comunicaPython(itens[0].innerText, '/delete');
        window.location.reload();
     });
 }

function modifyOnPy(){
    let button = document.getElementById('modificar');
    button.addEventListener('click', function(){
        console.log("Poisé: " + itens[0].innerText);
        var mensagem = itens[0].innerText + ' 2' + ' 100'
        comunicaPython(mensagem, '/modifica');
        window.location.reload();
    });
}



  // Fazer uma solicitação AJAX para enviar a mensagem para o servidor Python
function comunicaPython(mensagem, rota){
  var xhr = new XMLHttpRequest();
  xhr.open("POST", rota, true); // Rota Flask para receber a mensagem
  xhr.setRequestHeader("Content-Type", "application/json"); // Definir o tipo de conteúdo como JSON
  xhr.onreadystatechange = function () {
      if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
              // Resposta do servidor Python
              console.log("Resposta do Python:", xhr.responseText);
          } else {
              console.error("Erro ao enviar mensagem para o Python");
          }
      }
  };
  xhr.send(JSON.stringify({ mensagem: mensagem }));
}


  