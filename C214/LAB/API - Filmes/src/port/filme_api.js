const Filme = require('../application/filme_service');
const Utils = require('../utils/utils');

const route = '/filme';

module.exports = (app) => {
    app.post(`${route}/create`, async (req, res) => {
        const response = await Filme.create(req.body);
        res.status(Utils.responseStatus(response.name));
        res.json(response);
    });
    app.put(`${route}/update`, async (req, res) => {
        const response = await Filme.update(req.body);
        res.status(Utils.responseStatus(response.name));
        res.json(response);
    });
    app.get(`${route}/list`, async (req, res) => {
        const response = await Filme.list();
        res.status(Utils.responseStatus(response.name));
        res.json(response);
    });
    app.patch(`${route}/listFilmes`, async (req, res) => {
        const response = await Filme.listByProdutora(req.body);
        res.status(Utils.responseStatus(response.name));
        res.json(response);
    });
    app.delete(`${route}/delete/:nome`, async (req, res) => {
        const data = req.body;
        const { nome } = req.params;
        data.nome = nome;
        const response = await Filme.delete(data);
        res.status(Utils.responseStatus(response.name));
        res.json(response);
    });
};