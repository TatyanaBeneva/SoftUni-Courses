module.exports = (mongoose) => {

    const { Schema, model: Model } = mongoose;
    const { String, ObjectId } = Schema.Types;

    const coursSchema = new Schema({
        title: {
            type: String,
            required: true,
            unique: true
        },
        imageUrl: {
            type: String,
            required: true,
        },
        description: {
            type: String,
            required: true,
            max: 50
        },
        duration: {
            type: String,
            required: true
        },
        createdAt: {
            type: String,
            required: true
        },
        creator: {
            type: ObjectId,
            ref: 'User'
        },
        usersEnrolled: [
            {
                type: ObjectId,
                ref: 'User'
            }
        ]
    });

    return Model('Cours', coursSchema);
};