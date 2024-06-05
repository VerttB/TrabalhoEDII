import { comunicaPython } from "./comunicacao.js";


var itens = [];
var elementoSelecionado = null;
var listaTratada = [];

const headsTabela = document.querySelectorAll('th');
let headWasClicked = localStorage.getItem('headWasClicked');
const comunicacao = document.getElementById('comunicacao');
const enviarPython = document.getElementById('enviarPython');

console.log(headWasClicked)
headsTabela.forEach(head => {
  head.addEventListener('click', (event) =>{
    const elemento = event.target;
    let lista = [];
    if(headWasClicked === elemento.id){
      lista = [elemento.textContent, 'decrescente'];
      headWasClicked = null;
      localStorage.removeItem('headWasClicked');
    }
    else{
        lista = [elemento.textContent,'crescente'];
        headWasClicked = elemento.id;
        localStorage.setItem('headWasClicked', headWasClicked);

    }

    console.log(lista)
    // comunicacao.value = `${lista[0]}|${lista[1]}`
    comunicacao.value = lista[0]
    comunicacao.value += "|"
    comunicacao.value += lista[1]

    
    console.log(comunicacao.textContent)
    enviarPython.click()
    //comunicaPython(lista, '/catalogo')

  })
})
  

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
            const filhos = this.getElementsByTagName('td');
            itens = filhos
        });
    });
   
}

 function deleteOnPy(){
     let button = document.getElementById('deletar');
     button.addEventListener('click', function(){
        console.log("Poisé: " + itens[0].innerText);
        comunicaPython(itens[0].innerText, '/delete');
     });
 }

 function modifyOnPy() {
  const button = document.getElementById('modificar');
  const prompt_button = document.getElementById('prompt_button');

  button.addEventListener('click', function() {
    document.getElementById('prompt_titulo').textContent = "Modificando produto";
    document.getElementById('prompt_descricao').style.display = 'none'
    document.getElementById('prompt_box').style.display = 'flex';
    setNomeProdutoPrompt();
    prompt_button.removeEventListener('click', addValues);
    prompt_button.addEventListener('click', modValues);
  });

}


function modValues() {
  var lista = document.querySelectorAll('#prompt_input');
  listaTratada = [];
  if (itens !== undefined && itens.length > 1) listaTratada.push(itens[0].innerText);
  lista.forEach(function(elemento) {
    listaTratada.push(elemento.value);
  });
  console.log(listaTratada);
  comunicaPython(listaTratada, '/modifica');
}

function AddOnPy() {
  const button = document.getElementById('adicionar');
  const prompt_button = document.getElementById('prompt_button');

  button.addEventListener('click', function() {
    document.getElementById('prompt_titulo').textContent = "Adicionando Produtos";
    document.getElementById('prompt_box').style.display = 'flex';
    document.getElementById('prompt_descricao').style.display = 'inline-block';
    prompt_button.removeEventListener('click', modValues);
    prompt_button.addEventListener('click', addValues);
  });

}

function addValues() {
  let lista = document.querySelectorAll('#prompt_input');
  let descricao = document.querySelector('#prompt_descricao');
  listaTratada = [];
  
  lista.forEach(function(elemento) {
    listaTratada.push(elemento.value);
  });
  listaTratada.push(descricao.value);
  comunicaPython(listaTratada, '/adiciona'); 
}

function setNomeProdutoPrompt(){
  const produto = document.getElementById('produto_prompt')
  if (itens !== undefined && itens.length > 1) {
   console.log('teste');
   
   produto.innerText = itens[1].innerText;
}
}

function fecharPrompt(){
  const prompt_x = document.getElementById('prompt_fechar');

  prompt_x.onclick = function(event){
    document.getElementById('prompt_box').style.display = 'none';
  }
}


pegarInfo();
clicavel();
deleteOnPy();
modifyOnPy();
AddOnPy();
fecharPrompt();



