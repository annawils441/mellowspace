function validateCheckboxes() {
    const termsChecked = document.getElementById('terms').checked;
    const privacyChecked = document.getElementById('privacy').checked;

    document.getElementById('register-btn').disabled =
        !(termsChecked && privacyChecked);
}

function togglePassword(fieldId, button) {
    const field = document.getElementById(fieldId);

    if (field.type === "password") {
        field.type = "text";
        button.textContent = "🙈";
    } else {
        field.type = "password";
        button.textContent = "👁️";
    }
}