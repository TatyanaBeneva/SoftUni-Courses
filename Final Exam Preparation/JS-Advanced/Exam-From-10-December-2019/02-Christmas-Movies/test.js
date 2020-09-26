let assert = require('chai').assert;
let ChristmasMovies = require('./02. Christmas Movies_Resources');

describe('ChristmasMovies class behavior', ()=>{
    let christmasMovies;

    beforeEach(function(){
        christmasMovies = new ChristmasMovies();
    });

    describe('Constructor', ()=>{
        it('no params', ()=> {
            assert.deepEqual(christmasMovies, new ChristmasMovies());
        });

        it('movie collection for empty array', ()=>{
            assert.deepEqual(christmasMovies.movieCollection, []);
        });

        it('watched for empty object', ()=>{
            assert.deepEqual(christmasMovies.watched, {});
        });

        it('actors for empty array', ()=>{
            assert.deepEqual(christmasMovies.actors, []);
        });
    });

    describe('buyMovie method', ()=>{
        it('if the name of movie do not exist in movieCollection', ()=>{
            assert.deepEqual(christmasMovies.buyMovie('Banda', ['Alan','Meri']), 
            `You just got Banda to your collection in which Alan, Meri are taking part!`);
        });

        it('if the name of movie exist in movieCollection', ()=>{
            christmasMovies.movieCollection = [{name: 'Banda', actors: ['Alan','Mari']}];
            assert.throw(() => christmasMovies.buyMovie('Banda', ['Alan','Meri']), 
            `You already own Banda in your collection!`);
        });
    });

    describe('discardMovie method', ()=>{
        it('if the movie do not exist', ()=>{
            christmasMovies.movieCollection = [{name: 'Banda', actors: ['Alan','Mari']}];
            assert.throw(() => christmasMovies.discardMovie('Lala'), `Lala is not at your collection!`);
        });

        it('if the movie exist and is in the watched object', ()=>{
            christmasMovies.movieCollection = [{name: 'Banda', actors: ['Alan','Mari']}];
            christmasMovies.watched = {'Banda': 1};
            assert.deepEqual(christmasMovies.discardMovie('Banda'), `You just threw away Banda!`);
        });

        it('if the movie exist and it is not in the watched object', ()=>{
            christmasMovies.movieCollection = [{name: 'Banda', actors: ['Alan','Mari']}, 
            {name: 'Lala', actors: ['Ben', 'Ash']}];
            christmasMovies.watched = {'Banda': 1};
            assert.throw(() => christmasMovies.discardMovie('Lala'), `Lala is not watched!`);
        });
    });

    describe('watchMovie method', ()=>{
        it('if we have movie in the movieCollection but not in the watched', ()=>{
            christmasMovies.movieCollection = [{name: 'Banda', actors: ['Alan','Mari']}, 
            {name: 'Lala', actors: ['Ben', 'Ash']}];
            christmasMovies.watched = {'Lala': 1};
            christmasMovies.watchMovie('Banda');
            assert.deepEqual(christmasMovies.watched, {'Lala': 1, 'Banda': 1});
        });

        it('if we have movie in the movieCollection and in the watched', ()=>{
            christmasMovies.movieCollection = [{name: 'Banda', actors: ['Alan','Mari']}, 
            {name: 'Lala', actors: ['Ben', 'Ash']}];
            christmasMovies.watched = {'Banda': 1};
            christmasMovies.watchMovie('Banda');
            assert.deepEqual(christmasMovies.watched, {'Banda': 2});
        });

        it('if movie not exits in the movieCollection', ()=>{
            christmasMovies.movieCollection = [{name: 'Banda', actors: ['Alan','Mari']}];
            assert.throw(()=> christmasMovies.watchMovie('Lala'), 'No such movie in your collection!');
        });
    });

    describe('favouriteMovie method', ()=>{
        it('if we have movie in watched list',()=>{
            christmasMovies.movieCollection = [{name: 'Banda', actors: ['Alan','Mari']}, 
            {name: 'Lala', actors: ['Ben', 'Ash']}];
            christmasMovies.watched = {'Banda': 1, 'Lala': 2};
            assert.deepEqual(christmasMovies.favouriteMovie(), 
            `Your favourite movie is Lala and you have watched it 2 times!`);
        });

        it('if we do not have movie in watched list throw an error', ()=>{
            christmasMovies.movieCollection = [{name: 'Banda', actors: ['Alan','Mari']}, 
            {name: 'Lala', actors: ['Ben', 'Ash']}];
            assert.throw(()=> christmasMovies.favouriteMovie(), 'You have not watched a movie yet this year!');
        });
    });

    describe('mostStarredActor method', ()=>{
        it('if we do not have movies in movieCollection throw an error', ()=>{
            assert.throw(()=> christmasMovies.mostStarredActor(), 'You have not watched a movie yet this year!');
        });

        it('if we have movies in movieCollection', ()=>{
            christmasMovies.movieCollection = [{name: 'Banda', actors: ['Alan','Mari']}, 
            {name: 'Lala', actors: ['Ben', 'Alan']}];
            assert.deepEqual(christmasMovies.mostStarredActor(), 
            `The most starred actor is Alan and starred in 2 movies!`);
        });
    })
});