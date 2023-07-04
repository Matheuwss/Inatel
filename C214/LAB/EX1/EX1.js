class Veiculo {
    placa;
    ano;

    //constructor() {}
    constructor(placa, ano){
        this.placa = placa;
        this.ano = ano;
    }

    setPlaca(placa){
        this.placa = placa;
    }

    setAno(ano){
        this.ano = ano;
    }

    getPlaca() {
        return this.placa;
    }

    getAno() {
        return this.ano;
    }

    exibirDados(){
        console.log(`DADOS DO VEÍCULO (COMUM):\n PLACA: ${this.placa}\n Ano de fabricação: ${this.ano}\n`);
    }
}


class Onibus extends Veiculo{
    assentos;

    constructor(placa, ano, assentos){
        super(placa, ano);
        this.assentos = assentos;
    }

    setAssentos(assentos) {
        this.assentos = assentos;
    }

    getAssentos() {
        return this.assentos;
    }

    exibirDados(){
        console.log(`DADOS DO VEÍCULO (ÔNIBUS):\n PLACA: ${this.placa}\n Ano de fabricação: ${this.ano}\n Quantidade de assentos: ${this.assentos}\n`);
    }
}


class Caminhao extends Veiculo{
    eixos;
    
    constructor(placa, ano, eixos){
        super(placa, ano);
        this.eixos = eixos;
    }

    setEixos(eixos) {
        this.eixos = eixos;
    }

    getEixos() {
        return this.eixos;
    }

    exibirDados(){
        console.log(`DADOS DO VEÍCULO (CAMINHÃO):\n PLACA: ${this.placa}\n Ano de fabricação: ${this.ano}\n Quantidade de eixos: ${this.eixos}\n`);
    }
}


const veiculoComum = new Veiculo('HPO-2842', 2022);
veiculoComum.exibirDados();

const onibus = new Onibus('MGU-9989', 2018, 30);
onibus.exibirDados();

const caminhao = new Caminhao('PNN-4444', 2010, 4);
caminhao.exibirDados();