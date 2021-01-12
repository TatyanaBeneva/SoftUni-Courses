const { saltRounds } = require('../config');

module.exports = (mongoose, bcrypt) => {

    const { Schema, model: Model } = mongoose;
    const { String, ObjectId } = Schema.Types;

    const userSchema = new Schema({
        username: {
            type: String,
            required: true,
            unique: true
        },
        password: {
            type: String,
            required: true,
        },
        enrolledCourses: [
            {
                type: ObjectId,
                ref: "Cours"
            }
        ]
    });

    userSchema.methods = {
        comparePasswords(password) {
            return bcrypt.compare(password, this.password);
        }
    };

    userSchema.pre('save', async function (next) {
        // Before we save the new user, we should crypt the password and save it like that

        if (!this.isModified('password')) {
            next();
            return;
        }
        
        try {
        const salt = await bcrypt.genSalt(10);
        const hash = await bcrypt.hash(this.password, salt);
        this.password = hash;
        next();
        } catch (error) {
            console.error(error);
        }
        
    })

    return Model('User', userSchema);
}