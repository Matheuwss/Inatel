import java.util.ArrayList;
import java.io.*;

public class Arquivo {

    //FUNÇÃO PARA ESCREVER
    public void escrever(Seriado s1) {

        OutputStream os = null;
        OutputStreamWriter osr = null;
        BufferedWriter bw = null;
        String linhaEscrever;

        try {
            os = new FileOutputStream("seriados.txt", true); //SALVAR NO ARQUIVO
            osr = new OutputStreamWriter(os);   //CONVERSOR
            bw = new BufferedWriter(osr);       //O QUE VAI DIGITAR

            //tratamento
            if(s1.getTemporadas() > 1){
                bw.write("Seriado");
                bw.newLine();
                bw.write(s1.getNome() + "\n");
                bw.write(s1.getStreaming() + "\n");
                bw.write(s1.getTemporadas() + "\n");
                bw.write(s1.getAno() + "\n");
            }

        } catch (Exception e) {
            System.out.println(e);
        } finally {
            try {
                bw.close();
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }

    //FUNÇÃO PARA LER
    public ArrayList<Seriado> ler() {

        InputStream is = null;
        InputStreamReader isr = null;
        BufferedReader br = null;
        ArrayList<Seriado> acheiNoArquivo = new ArrayList<>();
        String linhaLer;

        try {
            is = new FileInputStream("seriados.txt");
            isr = new InputStreamReader(is);
            br = new BufferedReader(isr);

            linhaLer = br.readLine();
            while(linhaLer != null) {
                if(linhaLer.contains("Seriado")) {
                    Seriado aux = new Seriado();
                    aux.setNome(br.readLine());
                    aux.setStreaming(br.readLine());
                    aux.setTemporadas(Integer.parseInt(br.readLine()));
                    aux.setAno(Integer.parseInt(br.readLine()));
                    acheiNoArquivo.add(aux);
                }
                linhaLer = br.readLine();
            }
        } catch (Exception e) {
            System.out.println(e);
        } finally {
            try {
                br.close();
            } catch (Exception e) {
                System.out.println(e);
            }
        }
        return acheiNoArquivo;
    }

}