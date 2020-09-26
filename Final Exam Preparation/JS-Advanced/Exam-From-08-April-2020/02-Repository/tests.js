let { Repository } = require("./solution.js");
let assert = require("chai").assert;

describe("Tests …", function () {
    let rep;
    let properties = {
        name: "string",
        age: "number",
        birthday: "object"
    };

    let entity = {
        name: "Pesho",
        age: 22,
        birthday: new Date(1998, 0, 7)
    }

    beforeEach(function (){
        rep = new Repository(properties);
    })
    describe("constructor", function () {
        it("parameter of the class", function () {
            assert.isObject(rep.props);
        });

        it("get props id the input object", function () {
            assert.deepEqual(rep.props, properties);
        });

        it("is id increase", function () {
            rep.nextId();
            let id = rep.nextId();
            assert.deepEqual(id, 1);
        });

        it("get count return size of the entities", function () {
            rep.data.set(1, entity);
            assert.deepEqual(rep.count, 1);
        });

        it('is nextId function', ()=>{
            assert.isFunction(rep.nextId)
        })

        it('chek if data is object', ()=>{
            assert.deepEqual(rep.data, new Map());
        })
    });

    describe('add method', ()=>{
        it('adding entity to map return id', ()=>{
            assert.deepEqual(rep.add(entity), 0);
        })

        it('is entity object', ()=>{
            rep.add(entity);
            assert.isObject(entity);
        })

        it('add to the Map', ()=>{
            rep.add(entity);
            assert.deepEqual(rep.data.get(0), {name: "Pesho", age: 22, birthday: new Date(1998, 0, 7)});
        })
    })

    describe('_validate method', ()=>{
        it('throw error if entity does not have samo of the props', ()=>{
          let ent = {name: "Pesho", age: 22};
          assert.throw(()=> rep._validate(ent), "Property birthday is missing from the entity!") 
        })

        it('throw error if entity does not have samo of the props', ()=>{
            let ent = {age: 22, birthday: new Date(1998, 0, 7)};
            assert.throw(()=> rep._validate(ent), "Property name is missing from the entity!") 
        })
        it('throw error if entity does not have samo of the props', ()=>{
            let ent = {name: "Pesho", birthday: new Date(1998, 0, 7)};
            assert.throw(()=> rep._validate(ent), "Property age is missing from the entity!") 
        })

        it('throw error if entity type is incorrect', ()=>{
            let ent = {name: "Pesho", age: "Pr", birthday: new Date(1998, 0, 7)};
            assert.throw(()=> rep._validate(ent), "Property age is not of correct type!");
        })

        it('throw error if entity type is incorrect', ()=>{
            let ent = {name: 54, age: 22, birthday: new Date(1998, 0, 7)};
            assert.throw(()=> rep._validate(ent), "Property name is not of correct type!");
        })

        it('throw error if entity type is incorrect', ()=>{
            let ent = {name: "Pesho", age: 22, birthday: 1987};
            assert.throw(()=> rep._validate(ent), "Property birthday is not of correct type!");
        })
    })

    describe('getId method', ()=>{
        it('throw error if id id not exist', ()=>{
            let id = rep.nextId();
            rep.data.set(id, entity);
            assert.throw(()=> rep.getId(2), "Entity with id: 2 does not exist!");
        })

        it('reurn data of the given id',()=>{
            let id = rep.nextId();
            rep.data.set(id, entity);
            assert.deepEqual(rep.getId(0), {name: "Pesho", age: 22, birthday: new Date(1998, 0, 7)})
        })
    })

    describe('update method', ()=>{
        it('throw error if goven id does not exist',()=>{
            let id = rep.nextId();
            rep.data.set(id, entity);
            let newEnt = {name: "Pesho", age: 15, birthday: new Date(1998, 0, 7)};
            assert.throw(()=> rep.update(2, newEnt), "Entity with id: 2 does not exist!");
        })

        it('update the entity with given id',()=>{
            let id = rep.nextId();
            rep.data.set(id, entity);
            let newEnt = {name: "Pesho", age: 15, birthday: new Date(1998, 0, 7)};
            rep.update(0, newEnt)
            assert.deepEqual(rep.data.get(0), {name: "Pesho", age: 15, birthday: new Date(1998, 0, 7)});
        })
    })

    describe('del method',()=>{
        it('throw error if given id does not exist', ()=>{
            let id = rep.nextId();
            rep.data.set(id, entity);
            assert.throw(()=> rep.del(2), "Entity with id: 2 does not exist!");
        })

        it('delete the entity if id exist', ()=>{
            let id = rep.nextId();
            rep.data.set(id, entity);
            rep.del(0);
            assert.deepEqual(rep.data.size, 0);
        })
    })
    
});
