// 1. Escreva um programa que imprima no console os
// números de 0 a 10.
// for (let i = 0; i<=10;i++) {
//     console.log(i);
// }

// 2. Escreva um programa que solicite um número inteiro
// positivo e imprima a soma de todos os números inteiros
// de 1 até esse número.
// const num = parseInt(prompt("Digite um numero: "));
// let soma = 0
// for(let i = 1; i<= num; i++) {
//     soma+= i
// }
// console.log(soma);

// 3. Escreva um programa que solicite um número inteiro e
// imprima a tabuada desse número de 1 a 10.
// numero = prompt("Digite um numero: ");
// for(let i = 1; i <=10; i++) {
//     console.log(`${numero} * ${i} = ${numero * i}`);
// }

// 4. Escreva um programa que solicite um número inteiro
// positivo e faça uma contagem regressiva a partir desse
// número até 0.
// let numero = Number(prompt("Numero: "))
// for(let i = numero; i>= 0; i--) {
//     console.log(i);
// }

// 6. Crie um programa que imprima o seguinte padrão no
// console:
// let padrao = '*'
// for(let i = 0; i < 5; i++) {
//     console.log(padrao.repeat(i));
// }

// let texto = 'ola, mundo!'
// for(caractere of texto) {
//     console.log(caractere)
// }

// 1. Escreva um programa que irá solicitar ao usuário uma
// palavra e que imprimirá no console a palavra sem
// vogais.

// let palavra = prompt("Digite uma palavra:").toLowerCase(); // Convertendo a entrada para minúsculas

// const vogais = ['a', 'e', 'i', 'o', 'u'];

// let palavraSemVogais = "";
// for (let i = 0; i < palavra.length; i++) {
//     if (!vogais.includes(palavra[i])) {
//         palavraSemVogais += palavra[i];
//     }
// }

// console.log("Palavra sem vogais: " + palavraSemVogais);


// 2. Escreva um programa que solicite um texto ao usuário e
// verifique quantas vogais e consoantes esse texto tem.
let texto = prompt("Digite um texto:").toLowerCase(); // Convertendo a entrada para minúsculas
let vogais = 0;
let consoantes = 0;

for (let i = 0; i < texto.length; i++) {
    let letra = texto[i];
    if (letra.match(/[aeiou]/)) {
        vogais++;
    } else if (letra.match(/[a-z]/)) {
        consoantes++;
    }
}

console.log("Número de vogais: " + vogais);
console.log("Número de consoantes: " + consoantes);


// 3. Escreva uma programa que irá receber um texto e
// mostrará no console se esse texto é um palíndromo ou
// não. (palíndromos são palavras que são lidas da
// mesma forma de trás pra frente)

let texto_aleatorio = prompt("Digite um texto: ")
