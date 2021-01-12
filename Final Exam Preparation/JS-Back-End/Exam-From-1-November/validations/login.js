const { body } = require('express-validator');

module.exports = [
    body('username',
        'The username should be at least 5 characters and should consist only english letters and digits!')
        .isLength({ min: 5 })
        .isAlphanumeric('en-GB'),

    body('password',
        'The password should be at least 5 characters and should consist only english letters and digits!')
        .isLength({ min: 5 })
        .isAlphanumeric('en-GB')
]