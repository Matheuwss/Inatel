package br.inatel.cdg.algebra.scene;

import br.inatel.cdg.algebra.reta.Ponto;
import br.inatel.cdg.algebra.reta.Reta;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class ScenePrincipal {

    private Button btnCalcCoefAngular, btnCalcCoefLinear;                               //Button    - REPRESENTA BOTÕES
    private Label lblP1X, lblP1Y, lblP2X, lblP2Y;                                       //Label     - REPRESENTA RÓTULOS
    private TextField txtP1X, txtP1Y, txtP2X, txtP2Y, txtCoefAngular, txtCoefLinear;    //TextField - REPRESENTA ÁREAS DE TEXTO

    public void criaScenePrincipal(Stage stage){

        //Criando os labels para os pontos e os campos de texto para os dados
        lblP1X = new Label("Ponto P1.X");           //RÓTULOS
        txtP1X = new TextField();                      //ÁREAS DE TEXTO

        lblP1Y = new Label("Ponto P1.Y");
        txtP1Y = new TextField();

        lblP2X = new Label("Ponto P2.X");
        txtP2X = new TextField();

        lblP2Y = new Label("Ponto P2.Y");
        txtP2Y = new TextField();

        //HBox é usado para agrupar elementos horizontalmente
        //Criando quatro grupos horizontais com RÓTULO e ÁREAS DE TEXTO para as coordenadas
        HBox hboxP1X = new HBox(lblP1X, txtP1X);
        HBox hboxP1Y = new HBox(lblP1Y, txtP1Y);
        HBox hboxP2X = new HBox(lblP2X, txtP2X);
        HBox hboxP2Y = new HBox(lblP2Y, txtP2Y);

        //VBox é usada para agrupar elementos verticalmente
        //No construtor passamos todos os elementos que serão agrupados
        VBox vboxEntradaCoord = new VBox(hboxP1X,hboxP1Y,hboxP2X,hboxP2Y);//Agrupando verticalmente as caixas dos PONTOS para o usuário entrar com as coordenadas dos mesmos.

        //Caixas de texto que apresentaremos o resultado
        txtCoefAngular = new TextField();
        txtCoefAngular.setEditable(false);          //Definimos como "false" para evitar que o usuário digite nessas caixas
        txtCoefAngular.setText("Coef Angular: ");

        txtCoefLinear = new TextField();
        txtCoefLinear.setEditable(false);
        txtCoefLinear.setText("Coef Linear: ");

        //Agrupando as áreas onde apresentaremos o resultado
        HBox hboxRespostas = new HBox(txtCoefAngular,txtCoefLinear);

        //Criamos o botão
        btnCalcCoefAngular = new Button("Calcula Coeficiente Angular");
        //Criamos a ação que o botão RESPONDERÁ AO SER PRESSIONADO
        btnCalcCoefAngular.setOnAction(evento -> {
            Reta reta = construirReta();
            txtCoefAngular.setText("Coef Angular: " + reta.calcCoeficienteAngular());//Acessamos o componente textCoefAngular para colocar o resultado do cálculo
        });

        btnCalcCoefLinear = new Button("Calcula Coeficiente Linear");
        btnCalcCoefLinear.setOnAction(evento -> {
            Reta reta = construirReta();
            txtCoefLinear.setText("Coef Linear: " + reta.calcCoeficienteLinear());  //Acessamos o componente textCoefLinear para colocar o resultado do cálculo
        });

        //Agrupa os botões verticalmente
        HBox hBoxBotoes = new HBox(btnCalcCoefAngular,btnCalcCoefLinear);


        //Finalmente criamos o layout vertical final!
        VBox layoutFinal = new VBox(vboxEntradaCoord,hboxRespostas, hBoxBotoes);

        //Criando a Scene
        Scene scene = new Scene(layoutFinal, 300 , 200);

        stage.setTitle("Software Para Cálculos de Álgebra Linear");
        stage.setScene(scene);
        stage.show();
    }

    //FUNÇÃO INTERNA QUE CRIA UMA RETA!
    private Reta construirReta(){
        Ponto p1 = new Ponto(Double.parseDouble(txtP1X.getText()),
            Double.parseDouble(txtP1Y.getText()));

        Ponto p2 = new Ponto(Double.parseDouble(txtP2X.getText()),
            Double.parseDouble(txtP2Y.getText()));

        Reta reta = new Reta(p1,p2);
        return reta;
    }

}