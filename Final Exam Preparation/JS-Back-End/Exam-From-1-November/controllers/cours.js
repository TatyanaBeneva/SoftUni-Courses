const { Cours, User } = require('../models');
const { validationResult } = require('express-validator');

module.exports = {
    get: {
        create(req, res, next) {
            res.render('./courses/create');
        },

        details(req, res, next) {
            const coursId = req.params.id;
            Cours
                .findOne({ _id: coursId })
                .lean()
                .then(cours => {
                    const isCreator = req.user._id.toString() === cours.creator.toString();
                    const isEnroll = cours.usersEnrolled.filter(x => x.toString() === req.user._id.toString());
                    res.render('./courses/details', { ...cours, isCreator, isEnroll });
                })
                .catch(e => {
                    console.log(e);
                })

        },

        edit(req, res, next) {
            const coursId = req.params.id;
            Cours
                .findOne({ _id: coursId })
                .lean()
                .then(cours => {
                    res.render('./courses/edit', { ...cours });
                })
                .catch(e => {
                    console.log(e);
                })
        },

        enroll(req, res, next) {
            const coursId = req.params.id;
            const userId = req.user._id;

            Cours
                .updateOne({ _id: coursId }, {
                    $set: {
                        usersEnrolled: [userId]
                    }
                })
                .then(result => {
                    return User.updateOne({ _id: userId }, {
                        $set: {
                            enrolledCourses: [coursId]
                        }
                    })
                })
                .then(result => res.redirect(`/cours/details/${coursId}`))
                .catch(e => {
                    console.log(e);
                })
        },

        delete(req, res, next) {
            const { id } = req.params;
            Cours
                .deleteOne({ _id: id })
                .then(result => res.redirect('/'))
                .catch(e => console.log(e));
        }
    },

    post: {
        create(req, res, next) {
            const errors = validationResult(req);

            if (!errors.isEmpty()) {
                return res.render('./courses/create', {
                    message: errors.array()[0].msg
                })
            }

            Cours
                .create({ ...req.body, createdAt: new Date().toString(), creator: req.user._id })
                .then(createdCours => {
                    res.redirect('/');
                })
                .catch(e => {
                    console.error(e);
                })
        },

        edit(req, res, next) {
            const coursId = req.params.id;

            Cours
                .updateOne({ _id: coursId }, {
                    $set: {
                        ...req.body
                    }
                })
                .then(result => res.redirect(`/cours/details/${coursId}`))
                .catch(e => console.log(e));
        }
    }
};