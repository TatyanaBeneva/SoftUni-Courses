function usernames(data){
    let array = [...new Set(data)];
    array.sort((a,b) => {
        if(a.length !== b.length){
            return a.length - b.length;
        }

        return a.localeCompare(b);
    });

    console.log(array.join('\n'));
}

usernames(['Ashton',
'Kutcher',
'Ariel',
'Lilly',
'Keyden',
'Aizen',
'Billy',
'Lilly',
'Braston']
);