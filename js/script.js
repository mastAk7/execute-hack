const checkbox = document.getElementById('termsCheckbox');
const submitButton = document.getElementById('submitButton');

checkbox.addEventListener('change', function () {
    submitButton.disabled = !checkbox.checked;
});


function handleCredentialResponse(response) {
    // Decode JWT token to get user details
    const user = parseJwt(response.credential);

    // Store user info in localStorage to persist login
    localStorage.setItem('user', JSON.stringify(user));

    // Update UI
    updateUI(user);
}

function updateUI(user) {
    // Hide login section & show user section
    document.getElementById('login-section-2').style.display = 'none';
    document.getElementById('login-section').style.display = 'none';
    document.getElementById('user-section').style.display = 'block';

    // Update user info in UI
    document.getElementById('user-pic').src = user.picture;
    document.getElementById('user-name').innerText = `Hello, ${user.name}!`;
    document.getElementById('user-email').innerText = user.email;

    window.location.href = "index.html";
}

function logout() {
    // Clear user session
    localStorage.removeItem('user');

    // Show login section & hide user section
    document.getElementById('login-section').style.display = 'block';
    document.getElementById('login-section-2').style.display = 'block';
    document.getElementById('user-section').style.display = 'none';

    window.location.href = "index.html";
}

// Function to decode JWT token
function parseJwt(token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(atob(base64).split('').map(function (c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
}

// Keep user logged in after page refresh
window.onload = function () {
    const savedUser = localStorage.getItem('user');
    if (savedUser) {
        updateUI(JSON.parse(savedUser));
    }
};