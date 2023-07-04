const mongoose = require('mongoose');

const uri = `mongodb+srv://matheusmartins:matheus00@cluster0.tjzqsra.mongodb.net/?retryWrites=true&w=majority`;

mongoose.connect(uri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

const { Schema } = mongoose;

const CarroSchema = new Schema({
    id: {
        type: String,
        index: true,
        unique: true,
    },
    plate: {
        type: String,
        unique: true,
    },
    fabricante: String,
    modelo: String,
    ano: String
});

const CarroModel = mongoose.model('CarroModel', CarroSchema);

module.exports = {
    CarroModel,
};