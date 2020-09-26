function solve() {
   let buttons = document.getElementsByTagName('button');
   let textArea = document.getElementsByTagName('textarea')[0];
   let name = document.getElementsByClassName('product-title');
   let money = document.getElementsByClassName('product-line-price');
   let list = [];
   let priceList = [];

   let button1 = (e) => {
      textArea.append(`Added ${name[0].textContent} for ${Number(money[0].textContent).toFixed(2)} to the cart.\n`);
      priceList.push(money[0].textContent);
      if(!list.includes(name[0].textContent)){
         list.push(name[0].textContent);
      }
   };
   
   let button2 = (e) => {    
      textArea.append(`Added ${name[1].textContent} for ${Number(money[1].textContent).toFixed(2)} to the cart.\n`);
      priceList.push(money[1].textContent);
      if(!list.includes(name[1].textContent)){
         list.push(name[1].textContent);
      }
   };

   let button3 = (e) => {
      textArea.append(`Added ${name[2].textContent} for ${Number(money[2].textContent).toFixed(2)} to the cart.\n`);
      priceList.push(money[2].textContent);
      if(!list.includes(name[2].textContent)){
         list.push(name[2].textContent);
      }
   };

   buttons[0].addEventListener('click', button1);

   buttons[1].addEventListener('click', button2);

   buttons[2].addEventListener('click', button3);

   buttons[3].addEventListener('click', (e) => {
      buttons[0].removeEventListener('click', button1);
      buttons[1].removeEventListener('click', button2);
      buttons[2].removeEventListener('click', button3);
      console.log(priceList);
      let sum = 0;
      priceList.forEach(x => sum += Number(x));
      textArea.append(`You bought ${list.join(', ')} for ${sum.toFixed(2)}.`);
   })
}