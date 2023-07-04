const Constants = require('../src/utils/constants');
const Validation = require('../src/utils/validation');

it('Caso válido', () => {
    const result = Validation.create({
        plate: "LSN0000",
        fabricante: "Volkswagen",
        modelo: "Saveiro",
        ano: "2020"
    });
    expect(result).toEqual(undefined);
});

it('Caso inválido - sem o parâmetro plate', () => {
    const result = Validation.create({
        fabricante: "Ford",
        modelo: "F-250",
        ano: "2012"
    });
    expect(result.name).toEqual(Constants.ErrorValidation.name);
});