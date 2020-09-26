(() => {
    let myObj = {
        extend: function(template) {
            Object.keys(template).forEach(key =>{
                if(typeof template[key] === "function"){
                    Object.getPrototypeOf(this)[key] = template[key];
                } else{
                    this[key] = template[key];
                }
            });
        }
    }

    myObj.extend({
        someKey: '999',
        someKey2: 123,
        someFunc: function() {console.log(this.someKey)}
    });

    return myObj;
});