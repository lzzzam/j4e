const emailbox = document.getElementById('emailbox');
const email_form = document.getElementById('email-form');
const close_form = document.getElementById('close_form');
const thank_message = document.getElementById('thank-message');

if (close_form) {
    // set hidden_subscribe_box and hide email box
    close_form.addEventListener('click', (event) => {
        emailbox.remove();

        // send POST request with AJAX to overcome 
        // iOS bug with 204 status code response 
        $.ajax({
            type: "POST",
            url: "/cookies",
            data: JSON.stringify({
                hidden_subscribe_box: '1'
            }),
            contentType: "application/json",
            encode: true,
        });
    });
}

if (email_form) {
    email_form.addEventListener('submit', (event) => {
        thank_message.style.display = 'block'
        email_form.style.display = 'none'
    });
}
