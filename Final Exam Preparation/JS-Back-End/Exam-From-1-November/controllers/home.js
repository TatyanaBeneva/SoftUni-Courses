const { Cours } = require('../models');

module.exports = {
    get: {
        home(req, res, next) {
            // we take the input for search and make object with searched property
            
            const { search } = req.query;
            let query = {};
            if (search) { query.title = new RegExp(search, 'i'); }
            
            Cours
                .find(query)
                .lean()
                .then(courses => {
                    courses.sort((a, b) => new Date(a.createdAt) - new Date(b.createdAt));
                    res.render('./home/home', { courses })
                })
                .catch(e => {
                    console.log(e);
                })

        },
    }
};