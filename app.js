'use strict';
const switcher = document.querySelector('.btn'); //Referencia de botao

switcher.addEventListener('click', function() {     //Manipulador de evento
    document.body.classList.toggle('light-theme');
    document.body.classList.toggle('dark-theme');

    const className = document.body.className;
    if(className == "light-theme") {
        this.textContent = "Dark";
    } else {
        this.textContent = "Light";
    }
    console.log('current class name: ' + className);
});
