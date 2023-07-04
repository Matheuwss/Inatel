package poo_projetoFinal;

import java.io.OutputStreamWriter;
import java.io.FileOutputStream;
import java.io.BufferedWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class Principal {

    public static void main(String[] args) {

        ArrayList<Cliente> clientes = new ArrayList<>();
        ArrayList<Conta> contas = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        Cliente cliente;
        Conta conta;
        int opc;
        do {
            System.out.println("==================================");
            System.out.println("Olá, bem vindo ao SISTEMA BANCÁRIO");
            System.out.println("---------- MENU ----------");
            System.out.println("1 - Adicionar um cliente");
            System.out.println("2 - Criar contas");
            System.out.println("3 - Dados Bancários");
            System.out.println("4 - Consultar saldo");
            System.out.println("5 - Sacar");
            System.out.println("6 - Depositar");
            System.out.println("7 - Atualizar dados");
            System.out.println("8 - Encerrar contas");
            System.out.println("9 - Sair");
            System.out.println("---------------------------");
            System.out.println("==================================");

            System.out.println("ESCOLHA UMA OPÇÃO:");
            opc = Integer.parseInt(scanner.nextLine());

            switch (opc){
                case 1:
                    //ADICIONAR UM CLIENTE
                    System.out.println("Digite o nome do cliente: ");
                    String nomeCliente = scanner.nextLine();
                    System.out.println("Digite o CPF do cliente: ");
                    String cpfCliente = scanner.nextLine();
                    System.out.println("Digite o telefone do cliente: ");
                    String telCliente = scanner.nextLine();
                    System.out.println("Digite o endereço do cliente: ");
                    String endCliente = scanner.nextLine();

                    cliente = new Cliente(nomeCliente, cpfCliente, endCliente, telCliente);
                    clientes.add(cliente);
                    System.out.println("---------------------------");
                    break;

                case 2:
                    //CRIAR UMA CONTA
                    System.out.println("ESCOLHA O CLIENTE DA CONTA:");
                    for(Cliente c : clientes){
                        System.out.println(c.getIdCliente() + " - " + c.getNomeCliente());
                    }
                    int id = Integer.parseInt(scanner.nextLine());
                    System.out.println("DIGITE O TIPO DA CONTA:");
                    String tipo = scanner.nextLine();
                    System.out.println("DIGITE O SALDO DA CONTA:");
                    Double saldo = Double.parseDouble(scanner.nextLine());

                    conta = new Conta((clientes.get(id - 1)), tipo, saldo);
                    contas.add(conta);
                    System.out.println("---------------------------");
                    break;

                case 3:
                    //DADOS BANCÁRIOS
                    System.out.println("ESCOLHA A CONTA:");
                    for (Conta c : contas){
                        System.out.println(c.getNumero() + " - " + c.getCliente().getNomeCliente());
                    }
                    int idDados = Integer.parseInt(scanner.nextLine());
                    contas.get(idDados - 1).MostrarDadosBancarios();
                    break;

                case 4:
                    //CONSULTAR SALDO
                    System.out.println("ESCOLHA A CONTA");
                    for (Conta c : contas){
                        System.out.println(c.getNumero() + " - " + c.getCliente().getNomeCliente());
                    }
                    int idSaldo = Integer.parseInt(scanner.nextLine());
                    System.out.println("Seu saldo é de: " + contas.get(idSaldo - 1).getSaldo() + " reais");
                    System.out.println("---------------------------");
                    break;

                case 5:
                    //SACAR
                    System.out.println("ESCOLHA A CONTA");
                    for (Conta c : contas){
                        System.out.println(c.getNumero() + " - " + c.getCliente().getNomeCliente());
                    }
                    int idSaque = Integer.parseInt(scanner.nextLine());
                    System.out.println("Digite o valor do saque:");
                    Double valorSaque = Double.parseDouble(scanner.nextLine());
                    contas.get(idSaque - 1).sacar(valorSaque);
                    System.out.println("---------------------------");
                    if (valorSaque <= contas.get(idSaque - 1).getSaldo()){
                        try {
                            FileOutputStream os = new FileOutputStream("C:\\Users\\mathe\\Desktop\\PROJETOS\\Algoritmo Bancário\\src\\main\\java\\poo_projetoFinal\\historico", true);  //SALVAR NO ARQUIVO
                            OutputStreamWriter osw = new OutputStreamWriter(os);                             //CONVERSOR
                            BufferedWriter bw = new BufferedWriter(osw);                                     //O QUE VAI DIGITAR
                            bw.write("-----------------------------------------------");
                            bw.newLine();
                            bw.write("O cliente " + contas.get(idSaque - 1).getCliente().getNomeCliente()
                                    + " com o ID '" + contas.get(idSaque - 1).getCliente().getIdCliente() + "' "
                                    + "sacou R$" + valorSaque + " reais de sua CONTA de número '" + contas.get(idSaque - 1).getNumero() + "'\n"
                                    + "SALDO ANTERIOR: " + (contas.get(idSaque - 1).getSaldo() + valorSaque) + "\n"
                                    + "SALDO ATUAL: " + contas.get(idSaque - 1).getSaldo());
                            bw.newLine();
                            bw.close();

                        }catch (Exception e){
                            System.out.println("Acorreu um erro:" + e);
                        }
                    }
                    break;

                case 6:
                    //DEPOSITAR
                    System.out.println("ESCOLHA A CONTA");
                    for (Conta c : contas){
                        System.out.println(c.getNumero() + " - " + c.getCliente().getNomeCliente());
                    }

                    int idDeposito = Integer.parseInt(scanner.nextLine());
                    System.out.println("Digite o valor do depósito:");
                    Double valorDeposito = Double.parseDouble(scanner.nextLine());
                    contas.get(idDeposito - 1).depositar(valorDeposito);
                    System.out.println("---------------------------");

                    if (valorDeposito > 0){
                        try {
                            FileOutputStream os = new FileOutputStream("C:\\Users\\mathe\\Desktop\\PROJETOS\\Algoritmo Bancário\\src\\main\\java\\poo_projetoFinal\\historico", true);  //SALVAR NO ARQUIVO
                            OutputStreamWriter osw = new OutputStreamWriter(os);                             //CONVERSOR
                            BufferedWriter bw = new BufferedWriter(osw);                                     //O QUE VAI DIGITAR
                            bw.write("-------------------------------------");
                            bw.newLine();
                            bw.write("O cliente " + contas.get(idDeposito - 1).getCliente().getNomeCliente()
                                    + " com o ID '" + contas.get(idDeposito - 1).getCliente().getIdCliente() + "' "
                                    + "depositou R$" + valorDeposito + " reais na CONTA de número '" + contas.get(idDeposito - 1).getNumero() + "'\n"
                                    + "SALDO ANTERIOR: " + (contas.get(idDeposito - 1).getSaldo() - valorDeposito) + "\n"
                                    + "SALDO ATUAL: " + contas.get(idDeposito - 1).getSaldo());
                            bw.newLine();
                            bw.close();

                        }catch (Exception e){
                            System.out.println("Acorreu um erro:" + e);
                        }
                    }
                    break;

                case 7:
                    //ATUALIZAR DADOS DO CLIENTE
                    System.out.println("ESCOLHA O CLIENTE NO QUAL DESEJA ATUALIZAR OS DADOS:");
                    for(Cliente c : clientes){
                        System.out.println(c.getIdCliente() + " - " + c.getNomeCliente());
                    }
                    int idAtualizar = Integer.parseInt(scanner.nextLine());
                    System.out.println("Digite o novo nome do cliente: ");
                    String novoNome = scanner.nextLine();
                    System.out.println("Digite o novo endereço: ");
                    String novoEnd = scanner.nextLine();
                    System.out.println("Digite o novo telefone: ");
                    String novoTel = scanner.nextLine();

                    clientes.get(idAtualizar - 1).updateCliente(novoNome, novoTel, novoEnd);
                    System.out.println("Dados do cliente atualizados com sucesso!");
                    break;

                case 8:
                    //EXLCUIR CONTA
                    System.out.println("ESCOLHA A CONTA QUE DESEJA EXCLUIR");
                    for (Conta c : contas){
                        System.out.println(c.getNumero() + " - " + c.getCliente().getNomeCliente());
                    }
                    int idExcluir = Integer.parseInt(scanner.nextLine());
                    contas.get(idExcluir - 1).encerrarConta();
                    break;

                case 9:
                    //SAIR
                    System.out.println("Desconectando...");
                    System.out.println("SESSÃO ENCERRADA!!");
                    break;

                default:
                    System.out.println("OPÇÃO INVÁLIDA!");
                    System.out.println("---------------------------");
                    break;
            }

        } while (opc != 9);

    }

}