const { CarroModel } = require('../src/infrastructure/database');
const carro = require('../src/port/carro_repository');

describe('create', () => {
    it('Valid Carro', async () => {
        CarroModel.prototype.save = jest.fn().mockImplementation(() => ({
            toObject: () => ({
                id: 1,
                plate: "OPU-1844",
                fabricante: "Volkswagen",
                modelo: "Gol",
                ano: "2018"
            }),
        }));

        expect(await carro.create({
            id: 1,
            plate: "OPU-1844",
            fabricante: "Volkswagen",
            modelo: "Gol",
            ano: "2018"
        })).toEqual(
            expect.objectContaining({
                id: expect.any(Number),
                plate: expect.any(String),
                fabricante: expect.any(String),
                modelo: expect.any(String),
                ano: expect.any(String)
            }),
        );
    });
});

describe('editCarro', () => {
    it('Valid edit', async () => {
        CarroModel.findOneAndUpdate = jest.fn().mockImplementation(() => ({
            exec: () => ({
                toObject: () => ({
                    id: 1,
                    plate: "GKK-1003",
                    fabricante: "Volkswagen",
                    modelo: "Nivus",
                    ano: "2022"
                }),
            }),
        }));

        expect(await carro.update({
            plate: 'GKK-1003',
            ano: '2022',
        })).toEqual(
            expect.objectContaining({
                id: expect.any(Number),
                plate: expect.any(String),
                fabricante: expect.any(String),
                modelo: expect.any(String),
                ano: expect.any(String)
            }),
        );
    });
});

describe('listCarros', () => {
    it('Valid list', async () => {
        CarroModel.find = jest.fn().mockImplementation(() => ({
            exec: () => ({
                id: 1,
                plate: 'YWX-0948',
                fabricante: 'Ford',
                modelo: 'F-250',
                ano: '2012'
            }),
        }));

        expect(await carro.list()).toEqual(
            expect.objectContaining({
                id: expect.any(Number),
                plate: 'YWX-0948',
                fabricante: 'Ford',
                modelo: 'F-250',
                ano: '2012'
            }),
        );

    });
});

describe('getByPlate', () => {
    it('Valid list', async () => {
        CarroModel.findOne = jest.fn().mockImplementation(() => ({
            exec: () => ({
                id: 1,
                plate: 'YWX-0948',
                fabricante: 'Ford',
                modelo: 'F-250',
                ano: '2012'
            }),
        }));

        expect(await carro.getByPlate({
            plate: 'YWX-0948'
        })).toEqual(
            expect.objectContaining({
                id: expect.any(Number),
                plate: 'YWX-0948',
                fabricante: 'Ford',
                modelo: 'F-250',
                ano: '2012'
            }),
        );

    });
});

describe('deleteCarro', () => {
    it('Valid delete', async () => {
        CarroModel.deleteOne = jest.fn().mockImplementation(() => ({
            exec: () => ({
                deletedCount: 1,
            }),
        }));

        expect(await carro.delete({
            plate: 'MDM-7885',
        })).toEqual(1);
    });
});