import extend from '../utils/helper.js';
import models from '../models/index.js';
import docModifyer from '../utils/docModifyer.js';
import notification from '../utils/callNotifications.js';

export default {
    get: {
        create(context) {
            extend(context).then(function () {
                this.partial('../Views/Movies/createMovie.hbs');
            })
        },
        details(context) {
            const { movieId } = context.params;
            models.movies.get(movieId).then((response) => {
                const movie = docModifyer(response);
                Object.keys(movie).forEach(key => {
                    context[key] = movie[key];
                });
                context.isHeLikeAlready = movie.likes.includes(localStorage.getItem('email'));
                context.isCreator = movie.uid === localStorage.getItem('userId');
                context.numOfLikes = movie.likes.length;
                extend(context).then(function () {
                    this.partial('../Views/Movies/details.hbs');
                })
            });
        },
        edit(context){

            const {movieId} = context.params;
            models.movies.get(movieId).then((response) => {
                const movie = docModifyer(response);
                Object.keys(movie).forEach(key => {
                    context[key] = movie[key];
                });
                extend(context).then(function () {
                    this.partial('../Views/Movies/editMovie.hbs');
                })
            });
            
        }
    },

    post: {
        create(context) {

            const data = {
                ...context.params,
                uid: localStorage.getItem('userId'),
                likes: [],
                creator: localStorage.getItem('email')
            };

            models.movies.create(data).then((response) => {
                notification(1, "Created successfully!", context, '#/home');
            }).catch((e) => {
                console.error(e);
                notification(0, "Invalid input!", context);
            });
        }
    },

    del: {
        delete(context) {
            const { movieId } = context.params;

            models.movies.delete(movieId).then((response) => {
                    notification(1, "Movie is deleted successfully!", context, '#/home');
            }).catch(e => {
                console.error(e);
            });
        }
    },

    put: {
        likes(context){
            const { movieId } = context.params;
            models.movies.get(movieId)
                .then((response) => {
                    const movie = docModifyer(response);
                    movie.likes.push(localStorage.getItem('email'));
                    return models.movies.edit(movieId, movie);
                })
                .then((response) => {
                    notification(1, "Liked successfully", context, `#/details/${movieId}`);
                }).catch(e => {
                    console.error(e);
                    notification(0, "Something ment wrong!", context);
                });
        },

        edit(context){
            const {movieId} = context.params;
            const data = {...context.params};
            
            models.movies.edit(movieId, data).then((response) => {
                notification(1, "Edit successfully", context, `#/details/${movieId}`);
            }).catch(e => {
                console.error(e);
                notification(0, "Invalid input!", context);
            })
        }
    }
}
