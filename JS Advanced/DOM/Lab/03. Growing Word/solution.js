function growingWord() {
  if(document.getElementsByTagName('p')[2].style.color === 'blue'){
    document.getElementsByTagName('p')[2].style.color = 'green';
    document.getElementsByTagName('p')[2].style.fontSize = '4px';
  }else if(document.getElementsByTagName('p')[2].style.color === 'green'){
    document.getElementsByTagName('p')[2].style.color = 'red';
    document.getElementsByTagName('p')[2].style.fontSize = '8px';
  }else{
    document.getElementsByTagName('p')[2].style.color = 'blue';
    document.getElementsByTagName('p')[2].style.fontSize = '2px';
  }  
}