// 1) Imprima na tela os número de 1 a 10
let contador = 1

while (contador <= 10) {    
    console.log(contador);
    contador++
}

// 2) Calcule a soma dos números de 1 a 50
let soma = 0
let contador = 1
while (contador <= 50) {
    soma += contador
    console.log(contador)
    contador++
}

console.log(soma);

// 3) Encontre o fatorial de um determinado número
let fat = 1
let num = 5
let contador = 1
while (contador <= num) {
    fat = fat * contador
    contador++
}

console.log(fat);

// 4) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o
// valor seja inválido e continue pedindo até que o usuário informe um valor válido.
let num = Number(prompt("Numero: "))
while (num > 10 || num < 0) {
    alert("Digite numero valido!")
    num = Number(prompt("Numero: "))
}

// 5) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
// ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
let userName = '';
let senha = '';
while (userName == senha) {
    alert("Invalido! Username e senha iguais!")
    userName = prompt('Digite seu nome:');
    senha = prompt('Digite sua senha:');
}

// 6) Faça um programa que calcule o mostre a média aritmética de N notas
let nNotas = parseInt(prompt("Quantidade de notas:"));
let cont = 1
soma = 0
while (cont < nNotas) {
    let nota = parseFloat(prompt(`Nota ${cont}:`));
    soma += nota
}

media = soma / nNotas
console.log(media);

// 7) Faça um programa que peça para 5 pessoas a sua idade, ao final o programa devera
// verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então,
// dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
let cont = 1
let soma = 0
while (cont <= 5) {
    let idade = prompt("Idade: ")
    soma += idade
}

media = soma / 5
if (25 >= media > 0) {
    console.log("Turma Jovem");
} else if (26 >= media >= 60) {
    console.log("Turma Adulta");
} else if (media > 60) {
    console.log("Turma Idosa");
} else {
    console.log("Digite idade valida!");
}
