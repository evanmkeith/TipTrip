
const settings_btn = document.querySelector('#settings');
const settings_div = document.querySelector('#edit_page');
const body = document.querySelector('body');

settings.addEventListener('click', function(e){
    e.preventDefault();
    if(edit_page.style.display === 'none'){
        edit_page.style.display =  'flex';
    } else{
        edit_page.style.display =  'none';
    };
})
