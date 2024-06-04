export function comunicaPython(mensagem, rota){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", rota, true); 
    xhr.setRequestHeader("Content-Type", "application/json"); 
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
               
               // console.log("Resposta do Python:", xhr.responseText);
               //window.location.reload()

            } else {
                console.error("Erro ao enviar mensagem para o Python");
            }
        }
    };
    xhr.send(JSON.stringify({ mensagem: mensagem }));
  }

  