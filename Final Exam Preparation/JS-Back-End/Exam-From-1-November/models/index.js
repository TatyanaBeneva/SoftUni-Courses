const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

const getUserModel = require('./User');
const getCoursModel = require('./Cours');

module.exports = {
    User: getUserModel(mongoose, bcrypt),
    Cours: getCoursModel(mongoose)
};