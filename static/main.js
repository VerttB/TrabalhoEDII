
window.addEventListener('DOMContentLoaded', (event) =>{
    var tema = localStorage.getItem('theme')
    try{
    if(tema != null && tema != ''){
      document.body.classList.add(tema);
    }
  }
  catch(error){
    console.error(error);
  }
  });
      document.querySelector("#changeTheme").addEventListener("click", () => {
      document.body.classList.toggle("mudar-tema");
      tema_atual = document.body.classList.contains('mudar-tema') ? 'mudar-tema' : ''
      localStorage.setItem('theme', tema_atual);
});