const emailbox = document.getElementById('emailbox');
const email_form = document.getElementById('email-form');
const close_form = document.getElementById('close_form');
const thank_message = document.getElementById('thank-message');

close_form.addEventListener('click', (event) => {
    emailbox.remove();
});

email_form.addEventListener('submit', (event) => {
    thank_message.style.display = 'block'
    email_form.style.display = 'none'
});