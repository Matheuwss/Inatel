const validate = require('validate.js');

const Utils = require('../utils/utils');
const Constants = require('../utils/constants');
const CarroRepository = require('../port/carro_repository');
const Constraints = require('../utils/carro_validation');
const Validation = require('../utils/validation');

const Carro = {
    async create(data) {
        try {
            const validation = Validation.create(data);
            if (validation) {
                return validation;
            }

            data.id = Utils.generateUuid();

            const response = await CarroRepository.create(data);

            if (response.code === 11000) {
                const result = Constants.ErrorDuplicate;
                return result;
            }
            return response;
        } catch (error) {
            return error;
        }
    },

    async update(data) {
        try {
            const validation = validate.validate(data, Constraints.update);
            if (validation) {
                const response = Constants.ErrorValidation;
                response.message = validation;
                return response;
            }

            const response = await CarroRepository.update(data);

            if (response === []) {
                const result = Constants.ErrorNotFound;
                return result;
            }
            return response;
        } catch (error) {
            return error;
        }
    },

    async delete(data) {
        try {
            const validation = validate.validate(data, Constraints.deleteBy);
            if (validation) {
                const response = Constants.ErrorValidation;
                response.message = validation;
                return response;
            }

            const response = await CarroRepository.delete(data);

            return response;
        } catch (error) {
            return error;
        }
    },

    async getByPlate(data) {
        try {
            const validation = validate.validate(data, Constraints.get);
            if (validation) {
                const response = Constants.ErrorValidation;
                response.message = validation;
                return response;
            }

            const response = await CarroRepository.getByPlate(data);

            return response;
        } catch (error) {
            return error;
        }
    },

    async list() {
        try {
            const response = await CarroRepository.list();

            return response;
        } catch (error) {
            return error;
        }
    },
};
module.exports = Carro;