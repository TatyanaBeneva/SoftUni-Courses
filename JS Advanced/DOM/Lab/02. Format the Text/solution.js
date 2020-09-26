function solve() {
  let pharagraph = document.getElementById('input').textContent;
  const array = pharagraph.split('.');
  const arrayOfSentences = [];
  array.forEach(element => {
    if(element.length > 0){
      arrayOfSentences.push(element);
    }
  });

  console.log(arrayOfSentences);

  let numberOfSentences = arrayOfSentences.length;
  let count = 0;

  for(let i = 0; i < Math.ceil(numberOfSentences / 3); i++){
    let createPharagraph = document.createElement('p');
    for(let j = 0 + count; j < 3 + count; j++){
      if(arrayOfSentences[j] !== undefined){
        createPharagraph.textContent += arrayOfSentences[j] + '.';
      }
    }
    document.getElementById('output').appendChild(createPharagraph);
    count += 3
  }
}