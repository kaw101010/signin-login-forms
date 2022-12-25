document.querySelector("#pw").addEventListener('keyup', function (e){ // Check each time the user presses a key
    let pw = document.querySelector('#pw').value
    let tc = document.querySelector('#tc').checked
    if (pw.length >= 8){ // Checks for length of password
        document.querySelector('#ic1').style.display='none';
        document.querySelector('#c1').style.display = 'inline';
        document.querySelector('#minChars').classList.add('valid-validators')
        document.querySelector('#minChars').classList.remove('validators')
    }
    else{
        document.querySelector('#ic1').style.display='inline';
        document.querySelector('#c1').style.display = 'none';
        document.querySelector('#minChars').classList.remove('valid-validators')
        document.querySelector('#minChars').classList.add('validators')
    }
});