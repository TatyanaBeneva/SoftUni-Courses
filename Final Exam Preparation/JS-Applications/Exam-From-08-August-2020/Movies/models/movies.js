export default {
    create(data){
        return firebase.firestore().collection('movies').add(data);
    },
    getAll(){
        return firebase.firestore().collection('movies').get();
    },
    get(movieId){
        return firebase.firestore().collection('movies').doc(movieId).get();
    },
    delete(movieId){
        return firebase.firestore().collection('movies').doc(movieId).delete();
    },
    edit(movieId, data){
        return firebase.firestore().collection('movies').doc(movieId).update(data);

    }
}