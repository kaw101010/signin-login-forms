document.querySelector('#pw').addEventListener('focus', () => {
    document.querySelector('form > div').style.display = 'block'
});

document.querySelector('#pw').addEventListener('focusout', () => {
    document.querySelector('form > div').style.display = 'none'
});


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

    let lower_re = /[a-z]/g // Regex pattern for lowercase characters
    if (lower_re.test(pw)){ // Checks if password matches regex
        document.querySelector('#ic2').style.display='none';
        document.querySelector('#c2').style.display = 'inline';
        document.querySelector('#lower').classList.add('valid-validators')
        document.querySelector('#lower').classList.remove('validators')
    }
    else{
        document.querySelector('#ic2').style.display='inline';
        document.querySelector('#c2').style.display = 'none';
        document.querySelector('#lower').classList.remove('valid-validators')
        document.querySelector('#lower').classList.add('validators')
    }

    let upper_re = /[A-Z]/g // Regex pattern for uppercase characters
    if (upper_re.test(pw)){ // Checks if password matches regex
        document.querySelector('#ic3').style.display='none';
        document.querySelector('#c3').style.display = 'inline';
        document.querySelector('#upper').classList.add('valid-validators')
        document.querySelector('#upper').classList.remove('validators')
    }
    else{
        document.querySelector('#ic3').style.display='inline';
        document.querySelector('#c3').style.display = 'none';
        document.querySelector('#upper').classList.remove('valid-validators')
        document.querySelector('#upper').classList.add('validators')
    }

    let numChars_re = /[0-9]/g // Regex pattern for numbers from 0 to 9
    if (numChars_re.test(pw)){ // Checks if password matches regex
        document.querySelector('#ic4').style.display='none';
        document.querySelector('#c4').style.display = 'inline';
        document.querySelector('#num').classList.add('valid-validators')
        document.querySelector('#num').classList.remove('validators')
    }
    else{
        document.querySelector('#ic4').style.display='inline';
        document.querySelector('#c4').style.display = 'none';
        document.querySelector('#num').classList.remove('valid-validators')
        document.querySelector('#num').classList.add('validators')
    }

    let special_re = /[#?!@$%^&*-]/g // Regex pattern for special characters
    if (special_re.test(pw)){ // Checks if password matches regex
        document.querySelector('#ic5').style.display='none';
        document.querySelector('#c5').style.display = 'inline';
        document.querySelector('#specialChars').classList.add('valid-validators')
        document.querySelector('#specialChars').classList.remove('validators')
    }
    else{
        document.querySelector('#ic5').style.display='inline';
        document.querySelector('#c5').style.display = 'none';
        document.querySelector('#specialChars').classList.remove('valid-validators')
        document.querySelector('#specialChars').classList.add('validators')
    }
});