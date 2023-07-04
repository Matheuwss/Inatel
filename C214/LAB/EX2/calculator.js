const readline = require('readline-sync');  //BIBLIOTECA READLINE-SYNC, QUE PERMITE LER AS ENTRADAS DO USUÁRIO NO CONSOLE


//FUNÇÃO (CALCULADORA) QUE REALIZA AS OPERAÇÕES DE ADIÇÃO, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO E RESTO.
function calculadora() {
  console.log('BEM-VINDO(A) A CALCULADORA!');
  
  const op = readline.question('DIGITE A OPERAÇÃO DESEJADA (+, -, *, /, %): ');
  
  const num1 = Number(readline.question('Digite o primeiro número: '));
  const num2 = Number(readline.question('Digite o segundo número: '));
  
  
  //VERIFICA SE AMBOS OS NÚMEROS INSERIDOS PELO USUÁRIO SÃO VÁLIDOS (OU SEJA, SÃO NÚMEROS), usando a função isNaN. 
  //Se pelo menos um dos números não for válido, ele imprime UMA MENSAGEM DE ERRO.
  if (isNaN(num1) || isNaN(num2)) {
    console.log('Pelo menos um dos números inseridos não é válido!');
    return;
  }
  
  //Caso ambos os números sejam válidos, o código UTILIZA UMA ESTRUTURA SWITCH P/ REALIZAR A OPERAÇÃO DESEJADA!
  //O resultado é armazenado na variável resultado e, depois, é impresso.
  let resultado;
  
  switch (op) {
    case '+':
      resultado = num1 + num2;
      break;
    case '-':
      resultado = num1 - num2;
      break;
    case '*':
      resultado = num1 * num2;
      break;
    case '/':
      resultado = num1 / num2;
      break;
    case '%':
      resultado = num1 % num2;
      break;
    default:
      console.log('OPERAÇÃO INVÁLIDA!');
      return;
  }
  
  console.log(`O resultado de ${num1} ${op} ${num2} é: ${resultado}.`);
}

calculadora();  //CHAMA A FUNÇÃO, PERMITINDO QUE O USUÁRIO EXECUTE A CALCULADORA.