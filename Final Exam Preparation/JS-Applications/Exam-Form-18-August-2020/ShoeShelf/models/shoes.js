export default {
    create(data){
        return firebase.firestore().collection('shoes').add(data);
    },
    getAll(){
        return firebase.firestore().collection('shoes').get();
    },
    get(shoeId){
        return firebase.firestore().collection('shoes').doc(shoeId).get();
    },
    delete(shoeId){
        return firebase.firestore().collection('shoes').doc(shoeId).delete();
    },
    edit(shoeId, data){
        return firebase.firestore().collection('shoes').doc(shoeId).update(data);

    }
}