const checkbox = document.getElementById('termsCheckbox');
const submitButton = document.getElementById('submitButton');

checkbox.addEventListener('change', function () {
    submitButton.disabled = !checkbox.checked;
});
