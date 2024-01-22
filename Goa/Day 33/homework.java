document.getElementById("regForm").onsubmit = function(event) {
    event.preventDefault();

    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    if(username.length < 4) {
        alert("Username must be at least 4 characters long.");
        return false;
    }

    if(password.length < 6) {
        alert("Password must be at least 6 characters long.");
        return false;
    }

    // Add more validations as needed

    // If everything is valid, submit the form
    // Here you would typically send the data to a server
    alert("Registration Successful!");
    return true;
};
