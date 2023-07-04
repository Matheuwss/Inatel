//CLASSE CONVENCIONAL
class Carro {
    constructor (fabricante, modelo, ano){
        this.fabricante = fabricante;
        this.modelo = modelo;
        this.ano = ano;
    }

    getDados(){
        return `Carro: ${this.fabricante} ${this.modelo} ${this.ano}`;
    }
}

//USO DA CLASSE CONVENCIONAL
const meuCarro = new Carro('Volkswagen', 'Saveiro', 2022);
console.log(meuCarro.getDados());