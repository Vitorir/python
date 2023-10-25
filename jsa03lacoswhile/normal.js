// Exercício 1: Implemente um programa que conta regressivamente a partir de um número
// informado pelo usuário até zero.
let num = Number(prompt("Digite um numero: "))
for(let i = num; i > 0; i--) {
    console.log(i);
}

// Exercício 2: Faça um programa que sorteie um número entre 0 e 10 e que solicite ao
// usuário que tente adivinhá-lo. O programa deve rodar em loop, mostrando o número de
// tentativas e deve mostrar a mensagem quando o usuário acertar.

let sorteado = Math.floor(Math.random() * 10)
let tentativas = 0

while (true) {
    let palpite = Number(prompt("De seu palpite: "))

    if (palpite == sorteado) {
        alert("Parabéns!");
        break
    } else {
        tentativas++
        alert("Digite outro numero")
    }
}


// Exercício 3: Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e
// calcule a tabuada de N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = N, 2 x N = 2N, ..., 10
// x N = 10N.

let numero = Number(prompt("Numero: "))
for(let i = 1; i <= 10; i++) {
    alert(`${numero} * ${i} = ${numero * i}`)
}

// Exercício 4: Faça um programa que receba caracteres do usuário, um por vez, e
// concatene-os para formar uma palavra. O programa deve mostrar o resultado quando
// o usuário enviar um caractere em branco.
let palavra = ''

while (true) {
    let caractere = prompt("Digite um caractere: ")

    if (caractere != ' ') {
        palavra += caractere
    } else {
        break
    }
}

console.log(palavra);