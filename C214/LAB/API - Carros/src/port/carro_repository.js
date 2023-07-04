const { CarroModel } = require('../infrastructure/database');

const CarroRepository = {
    async create(data) {
        try {
            const model = new CarroModel(data);
            const response = await model.save();
            return response.toObject();
        } catch (e) {
            return e;
        }
    },

    async update(data) {
        try {
            const update = {
                plate: data.plate,
                fabricante: data.fabricante,
                modelo: data.modelo,
                ano: data.ano
            };
            const options = { new: true };
            const filter = { plate: data.plate };
            const result = await CarroModel.findOneAndUpdate(filter, update, options).exec();
            if (result === null) return []
            return result.toObject();
        } catch (e) {
            return e;
        }
    },

    async list() {
        try {
            const result = await CarroModel.find().exec();
            return result;
        } catch (error) {
            return error;
        }
    },

    async getByPlate(data) {
        try {
            const result = await CarroModel.findOne({ plate: data.plate }).exec();
            return result;
        } catch (e) {
            return e;
        }
    },

    async delete(data) {
        try {
            const result = await CarroModel.deleteOne({ plate: data.plate }).exec();
            return result.deletedCount;
        } catch (error) {
            return error;
        }
    },
};

module.exports = CarroRepository;