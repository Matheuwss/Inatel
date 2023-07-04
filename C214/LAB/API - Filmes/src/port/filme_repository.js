const { FilmeModel } = require('../infrastructure/database');

const FilmeRepository = {
    async create(data) {
        try {
            const model = new FilmeModel(data);
            const response = await model.save();
            return response.toObject();
        } catch (e) {
            return e;
        }
    },

    async update(data) {
        try {
            const update = {
                nome: data.nome,
            };
            const options = { new: true };
            const filter = { ano: data.ano };
            const result = await FilmeModel.findOneAndUpdate(filter, update, options).exec();
            if (result === null) return []
            return result.toObject();
        } catch (e) {
            return e;
        }
    },

    async list() {
        try {
            const result = await FilmeModel.find().exec();
            return result;
        } catch (error) {
            return error;
        }
    },

    async getByProdutora(data) {
        try {
            const result = await FilmeModel.findOne({ produtora: data.produtora }).exec();
            return result;
        } catch (e) {
            return e;
        }
    },

    async delete(data) {
        try {
            const result = await FilmeModel.deleteOne({ id: data.nome }).exec();
            return result.deletedCount;
        } catch (error) {
            return error;
        }
    },
};

module.exports = FilmeRepository;