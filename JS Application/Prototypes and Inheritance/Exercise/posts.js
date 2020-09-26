(()=>{
    class Post{
        constructor(title, content){
            this.title = title;
            this.content = content;
        }

        toString(){
            return `Post: ${this.title}\nContent: ${this.content}`;
        }
    }

    class SocialMediaPost extends Post{
        constructor(title, content, likes, dislikes){
            super(title, content);
            this.likes = likes;
            this.dislikes = dislikes;
            this.comments = [];
        }

        addComment(c){
            this.comments.push(c);
        }

        toString(){
            let output = super.toString() + "\n";
            output += `Rating: ${this.likes - this.dislikes}\n`;

            if(this.comments.length > 0){
                output += `Comments:\n`;
                output += this.comments.map(c => ` * ${c}`).join('\n');
            }

            return output.trim();
        }
    }

    class BlogPost extends Post{
        constructor(title, content, views){
            super(title, content);
            this.views = views;
        }

        view(){
            this.views++;
            return this;
        }

        toString(){
            let output = super.toString() + "\n";
            output += `Views: ${this.views}`;
            return output;
        }
    }

    return {
        Post,
        SocialMediaPost,
        BlogPost
    }
})