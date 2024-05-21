console.log("EAi");



const secao = document.getElementById('gridMain');
const secaoList = [];


const box = document.getElementById('box');
    for(let i = 1;i<2;i++){
            secaoList.push(box.cloneNode(true));
        } 
    for (let index = 0; index < secaoList.length; index++) {
        secao.appendChild(secaoList[index]);
        
    }
console.log("EAi");