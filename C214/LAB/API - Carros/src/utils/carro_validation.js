const create = {
    plate: {
        presence: {
            allowEmpty: false,
        },
        type: 'string',
    },
    fabricante: {
        presence: {
            allowEmpty: false,
        },
        type: 'string',
    },
    modelo: {
        presence: {
            allowEmpty: false,
        },
        type: 'string',
    },
    ano: {
        presence: {
            allowEmpty: false,
        },
        type: 'string',
    }
};

const update = {
    plate: {
        presence: {
            allowEmpty: false,
        },
        type: 'string',
    },
    fabricante: {
        presence: {
            allowEmpty: false,
        },
        type: 'string',
    },
    modelo: {
        presence: {
            allowEmpty: false,
        },
        type: 'string',
    },
    ano: {
        presence: {
            allowEmpty: false,
        },
        type: 'string',
    }
};

const get = {
    plate: {
        presence: {
            allowEmpty: false,
        },
        type: 'string',
    },
};

const deleteBy = {
    plate: {
        presence: {
            allowEmpty: false,
        },
        type: 'string',
    },
};

module.exports = {
    update,
    create,
    get,
    deleteBy,
};