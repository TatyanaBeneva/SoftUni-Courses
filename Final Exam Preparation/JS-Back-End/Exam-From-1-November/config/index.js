const env = process.env.NODE_ENV || 'development';

const config = {
    development: {
        port: process.env.PORT || 3000,
        dbUrl: ``,
        cookie: 'x-auth-token',
        secret: 'wearethebestinwhatwedo',
        saltRounds: 53
    }
};

module.exports = config[env];