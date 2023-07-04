const Filmes = require('../src/application/filme_service');
const Constants = require('../src/utils/constants');
const Utils = require('../src/utils/utils');
const FilmesRepository = require('../src/port/filme_repository');

jest.mock('../src/port/filme_repository');

it('CREATE - Dado válido', async () => {
    const data = {
        nome: "Os Vingadores",
        ano: "2012",
        diretor: "Joss Whedon",
        produtora: "Marvel Studios"
    }

    const id = Utils.generateUuid();

    FilmesRepository.create.mockResolvedValue({ ...data, id });

    const result = await Filmes.create(data);
    expect(result).toEqual({ ...data, id });
})

it('CREATE - Dado duplicado', async () => {
    const data = {
        nome: "Os Vingadores",
        ano: "2012",
        diretor: "Joss Whedon",
        produtora: "Marvel Studios"
    }

    const id = Utils.generateUuid();

    FilmesRepository.create.mockResolvedValue({ code: 11000 });

    const result = await Filmes.create(data);
    expect(result).toEqual(Constants.ErrorDuplicate);
})