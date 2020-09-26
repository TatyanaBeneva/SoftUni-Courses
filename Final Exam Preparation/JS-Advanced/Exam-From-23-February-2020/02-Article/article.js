class Article{
    counter;
    _comments;
    _likes;
    constructor(title, creator){
        this.title = title;
        this.creator = creator;
        this._comments = [];
        this._likes = [];
        this.counter = 1;
    }

    get likes(){
        if(this._likes.length === 0){
            return `${this.title} has 0 likes`;
        } else if(this._likes.length === 1){
            return `${this._likes[0]} likes this article!`;
        }

        return `${this._likes[0]} and ${this._likes.length - 1} others like this article!`;
    }

    like(username){
        if(this._likes.includes(username)){
            throw new Error("You can't like the same article twice!");
        } else if(username === this.creator){
            throw new Error("You can't like your own articles!");
        }

        this._likes.push(username);
        return `${username} liked ${this.title}!`;
    }

    dislike(username){
        if(!this._likes.includes(username)){
            throw new Error("You can't dislike this article!");
        }

        let index = this._likes.indexOf(username);
        this._likes.splice(index, 1);
        return `${username} disliked ${this.title}`;
    }

    comment(username, content, id){
        
        if(id === undefined || Number(id) >= Number(this.counter)){
            this._comments.push({
                Id: this.counter,
                Username: username,
                Content: content
            });
            this.counter++;

            return `${username} commented on ${this.title}`;
        } 

        this._comments.map(x => {
            if(x.Id === id){
                if(x.hasOwnProperty('Replies')){
                    x.Replies.push({
                        Id: x.Replies.length + 1,
                        Username: username,
                        Content: content
                    })
                }else{
                    x.Replies = [{
                        Id: 1,
                        Username: username,
                        Content: content
                    }]
                }
            }
        })
        this.repCounter++;

        return `You replied successfully`;
    }

    toString(sortingType){
        let result = [];
        if(sortingType === 'asc'){
            for (const iterator of this._comments) {
                if(iterator.hasOwnProperty('Replies')){
                    iterator.Replies.sort((a,b) =>{
                        return a.Id - b.Id;
                    })
                }
            }
            this._comments.sort((a,b) =>{
                return a.Id - b.Id;
            })
        } else if(sortingType === 'username'){
            for (const iterator of this._comments) {
                if(iterator.hasOwnProperty('Replies')){
                    iterator.Replies.sort((a,b) =>{
                        return a.Username.localeCompare(b.Username);
                    })
                }
            }
            this._comments.sort((a,b) =>{
                return a.Username.localeCompare(b.Username);
            })
        } else if(sortingType === 'desc'){
            for (const iterator of this._comments) {
                if(iterator.hasOwnProperty('Replies')){
                    iterator.Replies.sort((a,b) =>{
                        return b.Id - a.Id;
                    })
                }
            }
            this._comments.sort((a,b) =>{
                return b.Id - a.Id;
            })
        }

        result.push(`Title: ${this.title}`);
        result.push(`Creator: ${this.creator}`);
        result.push(`Likes: ${this._likes.length}`);
        result.push('Comments:');

        for (const current of this._comments) {
            result.push(`-- ${current.Id}. ${current.Username}: ${current.Content}`);
            if(current.hasOwnProperty('Replies')){
                for (const rep of current.Replies) {
                    result.push(`--- ${current.Id}.${rep.Id}. ${rep.Username}: ${rep.Content}`);
                }
            }
        }

        return result.join('\n');
    }
}

let art = new Article("My Article", "Anny");
art.like("John");
art.like("Ivan");
art.like("Steven");
console.log(art.likes);
console.log(art.comment("Anny", "Some Content"))
console.log(art.comment("Ammy", "New Content", 1));
console.log(art.comment("Zane", "Reply", 2));
art.comment("Jessy", "Nice :)");
art.comment("SAmmy", "Reply@", 2);
art.comment("MAam", "Reply@", 2)
console.log(art.toString('asc'));