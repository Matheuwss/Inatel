const Constants = require('../src/utils/constants');
const Validation = require('../src/utils/validation');

it('Caso válido', () => {
    const result = Validation.create({
        nome: "Velozes e Furiosos 7",
        ano: "2015",
        diretor: "James Wan",
        produtora:"Original Film"
    });
    expect(result).toEqual(undefined);
});

it('Caso válido', () => {
    const result = Validation.create({
        nome: "O Rei Leão",
        ano: "2019",
        diretor: "Jon Favreau",
        produtora: "Walt Disney Pictures"
    });
    expect(result).toEqual(undefined);
});

it('Caso inválido - sem o parâmetro nome', () => {
    const result = Validation.create({
        ano: "2009",
        diretor: "James Cameron",
        produtora:"Lightstorm Entertainment"
    });
    expect(result.name).toEqual(Constants.ErrorValidation.name);
});