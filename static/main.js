
var itens = []
var elementoSelecionado = null
var listaTratada = []
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
    clicavel();
    deleteOnPy();
    modifyOnPy();
    AddOnPy();
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

 function modifyOnPy() {
  const button = document.getElementById('modificar');
  const prompt = document.getElementById('prompt_box');
  button.addEventListener('click', function() {
    prompt.style.display = 'flex';
    setNomeProdutoPrompt();
  });

  const prompt_button = document.getElementById('prompt_button');
  prompt_button.removeEventListener('click', addValues);
  prompt_button.addEventListener('click', modValues);
}

function AddOnPy() {
  const button = document.getElementById('adicionar');
  const prompt = document.getElementById('prompt_box');
  const input = document.getElementById('prompt_descricao');
  const titulo = document.getElementById('prompt_titulo');

  button.addEventListener('click', function() {
    titulo.value = 'Adicionando Produtos';
    prompt.style.display = 'flex';
    input.style.display = 'inline-block';
    // Remove the event listener for modValues if it was previously added
    const prompt_button = document.getElementById('prompt_button');
    prompt_button.removeEventListener('click', modValues);
    // Add the event listener for addValues
    prompt_button.addEventListener('click', addValues);
  
  });
}

function modifyOnPy() {
  const button = document.getElementById('modificar');
  const prompt = document.getElementById('prompt_box');

  button.addEventListener('click', function() {
    prompt.style.display = 'flex';
    setNomeProdutoPrompt();
    // Remove the event listener for addValues if it was previously added
    const prompt_button = document.getElementById('prompt_button');
    prompt_button.removeEventListener('click', addValues);
    // Add the event listener for modValues
    prompt_button.addEventListener('click', modValues);
  });
}

function addValues(prompt) {
  const input = document.getElementById('prompt_descricao');
  let lista = document.querySelectorAll('#prompt_input');
  let descricao = document.querySelector('#prompt_descricao');
  listaTratada = [];
  lista.forEach(function(elemento) {
    listaTratada.push(elemento.value);
  });
  listaTratada.push(descricao.value);
  console.log('eae do adicionar:' + listaTratada);
  comunicaPython(listaTratada, '/adiciona');
  prompt.style.display = 'none';
  input.style.display = 'none';
  //window.location.reload();
}


// function modifyOnPy() {
//   const button = document.getElementById('modificar');
//   const prompt = document.getElementById('prompt_box');
//   button.addEventListener('click', function() {
//       prompt.style.display = 'flex';
//       setNomeProdutoPrompt();
//       // document.getElementById('prompt_button').style.display = 'inline-block';
//       // document.getElementById('prompt_adicionar_button').style.display = 'none';
//   });

//   const prompt_button = document.getElementById('prompt_button');
//   prompt_button.removeEventListener('click',addValues);
//   prompt_button.addEventListener('click', modValues());
  
// }
 function modValues(){
       var lista = document.querySelectorAll('#prompt_input');
       listaTratada = [];
       if (itens !== undefined && itens.length > 1) listaTratada.push(itens[0].innerText);
       lista.forEach(function(elemento) {
           listaTratada.push(elemento.value);
       });
       console.log('oi do modificar' + listaTratada);
       comunicaPython(listaTratada, '/modifica');
       prompt.style.display = 'none'
      
       window.location.reload()
 }

// function AddOnPy() {
//   const button = document.getElementById('adicionar');
//   const prompt = document.getElementById('prompt_box');
//   const input = document.getElementById('prompt_descricao');
//   const titulo = document.getElementById('prompt_titulo');
//   button.addEventListener('click', function() {
//       titulo.value = 'Adicionando Produtos';
//       prompt.style.display = 'flex';
//       input.style.display = 'inline-block';
//       // document.getElementById('prompt_adicionar_button').style.display = 'inline-block';
//       // document.getElementById('prompt_button').style.display = 'none';
//   });

//   // const prompt_adicionar_button = document.getElementById('prompt_adicionar_button');
//   prompt_button = document.getElementById('prompt_button')
//   prompt_button.removeEventListener('click', modValues);
//   prompt_button.addEventListener('click', addValues(prompt));
// }

// function addValues(prompt){
//     let lista = document.querySelectorAll('#prompt_input');
//     let descricao = document.querySelector('#prompt_descricao');
//     listaTratada = [];
//     lista.forEach(function(elemento) {
//           listaTratada.push(elemento.value);
//       });
//     listaTratada.push(descricao.value);
//     console.log('eae do adicionar:' + listaTratada);
//     comunicaPython(listaTratada, '/adiciona');
//     prompt.style.display = 'none';
//     input.style.display = 'none';
//     window.location.reload()
// }



function comunicaPython(mensagem, rota){
  var xhr = new XMLHttpRequest();
  xhr.open("POST", rota, true); 
  xhr.setRequestHeader("Content-Type", "application/json"); 
  xhr.onreadystatechange = function () {
      if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
             
              console.log("Resposta do Python:", xhr.responseText);
          } else {
              console.error("Erro ao enviar mensagem para o Python");
          }
      }
  };
  xhr.send(JSON.stringify({ mensagem: mensagem }));
}


function setNomeProdutoPrompt(){
  const produto = document.getElementById('produto_prompt')
  if (itens !== undefined && itens.length > 1) {
   console.log('teste');
   
   produto.innerText = itens[1].innerText;
}
}
