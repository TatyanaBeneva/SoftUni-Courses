
export default {
    create(data){
        return firebase.firestore().collection('couses').add(data);
    },
    getAll(){
        return firebase.firestore().collection('couses').get();
    },
    get(couseId){
        return firebase.firestore().collection('couses').doc(couseId).get();
    },
    close(couseId){
        return firebase.firestore().collection('couses').doc(couseId).delete();
    },
    donate(couseId, data){
        return firebase.firestore().collection('couses').doc(couseId).update(data);

    }
}