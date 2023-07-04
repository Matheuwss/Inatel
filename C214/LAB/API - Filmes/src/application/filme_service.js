const validate = require('validate.js');

const Utils = require('../utils/utils');
const Constants = require('../utils/constants');
const FilmeRepository = require('../port/filme_repository');
const Constraints = require('../utils/filme_validation');
const Validation = require('../utils/validation');

const Filme = {
    async create(data) {
        try {
            const validation = Validation.create(data);
            if (validation) {
                return validation;
            }

            data.id = Utils.generateUuid();

            const response = await FilmeRepository.create(data);

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

            const response = await FilmeRepository.update(data);

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

            const response = await FilmeRepository.delete(data);

            return response;
        } catch (error) {
            return error;
        }
    },

    async listByProdutora(data) {
        try {
            const validation = validate.validate(data, Constraints.get);
            if (validation) {
                const response = Constants.ErrorValidation;
                response.message = validation;
                return response;
            }

            const response = await FilmeRepository.getByProdutora(data);

            return response;
        } catch (error) {
            return error;
        }
    },

    async list() {
        try {
            const response = await FilmeRepository.list();

            return response;
        } catch (error) {
            return error;
        }
    },
};
module.exports = Filme;