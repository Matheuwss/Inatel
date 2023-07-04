public class Jogador {

    String nome;
    String email;
    Personagem[] personagens;

    Jogador() {
        personagens = new Personagem[20];
    }

    void mostrarInfo() {
        System.out.println("Nome: " + nome);
        System.out.println("Email: " + email);
        for (int i = 0; i < personagens.length; i++) {
            if(personagens[i] != null) {
                personagens[i].mostrarInfo();
            }
        }
    }

    void adicionaPersonagem(Personagem personagem) {
        for (int i = 0; i < personagens.length; i++) {
            if(personagens[i] == null) {
                personagens[i] = personagem;
                break;
            }
        }
    }

    int calculaMagia() {
        int nMagia = 0;
        for (int i = 0; i < personagens.length; i++) {
            if(personagens[i] != null) {
                if(personagens[i].usaMagia) {
                    nMagia++;
                }
            }
        }
        return nMagia;
    }

    void mostraMediaNivel() {
        double soma = 0.0;
        int n = 0;
        for (int i = 0; i < personagens.length; i++) {
            if(personagens[i] != null) {
                soma += personagens[i].nivel;
                n++;
            }
        }
        double media = soma/n;
        System.out.println("Media dos niveis: " + media);
    }

}