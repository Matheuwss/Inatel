const mongoose = require('mongoose');

const uri = `mongodb+srv://matheusmartins:matheus00@cluster0.tjzqsra.mongodb.net/?retryWrites=true&w=majority`;

mongoose.connect(uri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

const { Schema } = mongoose;

const FilmeSchema = new Schema({
    id: {
        type: String,
        index: true,
        unique: true,
    },
    nome: String,
    ano: String,
    diretor: String,
    produtora: String
});

const FilmeModel = mongoose.model('FilmeModel', FilmeSchema);

module.exports = {
    FilmeModel,
};