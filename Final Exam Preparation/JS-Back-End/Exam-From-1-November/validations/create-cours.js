const { body } = require('express-validator');

module.exports = [
    body('title',
        'The title should be at least 4 characters!')
        .isLength({ min: 4 }),

    body('description',
        'The description should be at least 20 characters long!')
        .isLength({ min: 20 }),

    body('imageUrl',
        'Image Url should start with http ot https!')
        .custom(value => {
            if (!value.startsWith('http') && !value.startsWith('https')) {
                throw new Error('Image Url should start with http ot https!');
            }

            return true;
        })
]