const Carro = require('../application/carro_service');
const Utils = require('../utils/utils');

const route = '/carro';

module.exports = (app) => {
    app.post(`${route}/create`, async (req, res) => {
        const response = await Carro.create(req.body);
        res.status(Utils.responseStatus(response.plate));
        res.json(response);
    });

    app.put(`${route}/update`, async (req, res) => {
        const response = await Carro.update(req.body);
        res.status(Utils.responseStatus(response.plate));
        res.json(response);
    });

    app.get(`${route}/list`, async (req, res) => {
        const response = await Carro.list();
        res.status(Utils.responseStatus(response.plate));
        res.json(response);
    });

    app.patch(`${route}/listCarro`, async (req, res) => {
        const response = await Carro.getByPlate(req.body);
        res.status(Utils.responseStatus(response.plate));
        res.json(response);
    });
    
    app.delete(`${route}/delete/:plate`, async (req, res) => {
        const data = req.body;
        const { plate } = req.params;
        data.plate = plate;
        const response = await Carro.delete(data);
        res.status(Utils.responseStatus(response.plate));
        res.json(response);
    });
};