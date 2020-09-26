function delimiter(input){
    let delimiter = input.pop();
    console.log(input.join(`${delimiter}`));
}

delimiter(['One', 
'Two', 
'Three', 
'Four', 
'Five', 
'-']
);