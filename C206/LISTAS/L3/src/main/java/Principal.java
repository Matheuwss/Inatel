public class Principal {

    public static void main(String[] args) {

        Pessoa p1 = new Pessoa("Matheus", 1234, 2);
        Endereco e1 = new Endereco("Av. Barão do Rio Branco", "Centro", 111);
        Endereco e2 = new Endereco("Av. João de Camargo", "Centro", 510);
        p1.addEndereco(e1);
        p1.addEndereco(e2);

        Pessoa p2 = new Pessoa("Calos", 5678, 2);
        Endereco e3 = new Endereco("Tiradentes", "Centro", 244);
        p2.addEndereco(e3);

        p1.mostraInfo();
        p2.mostraInfo();
    }

}