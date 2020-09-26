function sortAnArray(input){
    input.sort(function(a,b){
        return a.length - b.length || a.localeCompare(b);    
    });
    input.forEach(element => {
        console.log(element);
    });
}

sortAnArray(['test', 
'Deny', 
'omen', 
'Default']
);