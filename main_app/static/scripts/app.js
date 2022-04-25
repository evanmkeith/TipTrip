
const settings = document.querySelector('#settings');
const edit_page = document.querySelector('#edit_page');
const by_me = document.querySelector('#by_me');
const reviews_ive_written = document.querySelector('.reviews_ive_written');
const about_me = document.querySelector('#about_me');
const reviews_about_me = document.querySelector('.reviews_about_me');


settings.addEventListener('click', function(e){
    e.preventDefault();
    if(edit_page.style.display === 'none'){
        edit_page.style.display =  'flex';
    } else{
        edit_page.style.display =  'none';
    };
})

by_me.addEventListener('click', function(e){
    e.preventDefault();
    if(by_me.style.backgroundColor === '#ECBABA'){
    } else {
        about_me.style.backgroundColor = '#BA7D85';
        reviews_about_me.style.display = 'none';

        by_me.style.backgroundColor = '#ECBABA';
        reviews_ive_written.style.display = 'flex'; 
    }
})

about_me.addEventListener('click', function(e){
    e.preventDefault();
    if(about_me.style.backgroundColor === '#ECBABA'){
    } else {
        by_me.style.backgroundColor = '#BA7D85';
        reviews_ive_written.style.display = 'none'; 

        about_me.style.backgroundColor = '#ECBABA';
        reviews_about_me.style.display = 'flex';
    }
})
