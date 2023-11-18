let p = document.getElementsByTagName('p')[0].textContent = 'Ola, mundo!'


function adicionarParagrafo() {
    let element = document.createElement('p')
    element.textContent = 'Texto personalizado '

    let div1 = document.getElementById('div1')
    div1.appendChild(element)
}


function criarLista() {
    let ul = document.createElement('ul');
    let element = document.createElement('li');
    let entrada = document.getElementById('entrada').value; // Corrigido para obter o valor da entrada

    element.textContent = entrada;

    ul.appendChild(element);

    let div1 = document.getElementById('div1');
    div1.appendChild(ul);
}