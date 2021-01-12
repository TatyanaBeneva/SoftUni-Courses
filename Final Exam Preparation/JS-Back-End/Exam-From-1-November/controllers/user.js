const { User } = require('../models');
const { jwt } = require('../utils');
const { cookie } = require('../config');
const { validationResult } = require('express-validator');

module.exports = {
    get: {
        register(req, res, next) {
            res.render('./user/register');
        },

        login(req, res, next) {
            res.render('./user/login');
        },

        logout(req, res, next) {
            res
                .clearCookie(cookie)
                .redirect('/');
        }
    },

    post: {
        register(req, res, next) {
            const errors = validationResult(req);

            if (!errors.isEmpty()) {
                return res.render('./user/register', {
                    message: errors.array()[0].msg
                })
            }

            // We take the given info that user provide us in the form
            const { username, password, rePassword } = { ...req.body };

            // We use user model to find if the given username is already in registered, and if it is we throw error
            // else we create user with the provided info in database
            User
                .findOne({ username })
                .then(user => {
                    if (user) {
                        throw new Error('The given username is already in use...');
                    }
                    return User.create({ username, password });

                })
                .then(createdUser => {
                    res.redirect('/user/login');
                })
                .catch(e => {
                    console.log(e);
                    res.redirect('/user/register');
                })
        },

        login(req, res, next) {
            const errors = validationResult(req);

            if (!errors.isEmpty()) {
                return res.render('./user/login', {
                    message: errors.array()[0].msg
                })
            }

            const { username, password } = { ...req.body };
            
            // We check if the provided password is the same as we saved
            
            User
                .findOne({ username })
                .then((user) => {
                    return Promise.all([
                        user.comparePasswords(password),
                        user,
                    ])
                })
                .then(([isPasswordsMatched, user]) => {
                    if (!isPasswordsMatched) {
                        throw new Error('The provided password does not matched.');
                    }
                    // if passwords match we created authentication token and save it in cookie

                    const token = jwt.createToken(user._id);

                    res
                        .status(200)
                        .cookie(cookie, token, { maxAge: 3600000 })
                        .redirect('/');

                })
                .catch((e) => {
                    res.render('./user/login', {
                        message: 'Wrong username or password'
                    });
                    console.log(e);
                })
        }
    }
};