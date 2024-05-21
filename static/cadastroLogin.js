

function mostrarSenha(){
    const mostrarSenha = document.getElementById('mostrarSenha');
    const senha = document.getElementById('inputSenha');

    if(mostrarSenha.checked){
        senha.type = 'text';
    }
    else{
        senha.type = 'password'
    }

}

