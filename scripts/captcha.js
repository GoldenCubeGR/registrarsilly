function onLoadCallback() {
    grecaptcha.render('captcha', {
        sitekey: "6LdKSPYpAAAAAMhVOwGhAitTpIvWIdTaLBTurft9",
        callback: successCallback,
    });
}

function successCallback(token) {
    // Send the token to the server
    fetch('https://varying-charity-3feds-registrar-ecab180f.koyeb.app//verify-recaptcha', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `g-recaptcha-response=${token}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Verification successful');
            document.getElementById('regBtnMod').disabled = false;
        } else {
            
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
