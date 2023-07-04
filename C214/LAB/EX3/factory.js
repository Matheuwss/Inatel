//FACTORY
const Carro = (fabricante, modelo, ano) => ({
    fabricante,
    modelo,
    ano,
    getDados: () => `Carro: ${fabricante} ${modelo} ${ano}`
})

//USO DA FACTORY
const meuCarro = Carro('Volkswagen', 'Saveiro', 2022);
console.log(meuCarro.getDados());