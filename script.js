function checkPasswordStrength() {
    var password = document.getElementById("password").value;
    var strength = checkPasswordStrengthRules(password);
    var strengthPercentage = strength * 20;

    var strengthBar = document.getElementById("strength-bar");
    var strengthLabel = document.getElementById("strength-label");

    if (strengthPercentage < 40) {
        strengthBar.style.backgroundColor = 'red';
    } else if (strengthPercentage < 60) {
        strengthBar.style.backgroundColor = 'orange';
    } else if (strengthPercentage < 80) {
        strengthBar.style.backgroundColor = 'yellow';
    } else {
        strengthBar.style.backgroundColor = '#00ff00';  // Bright green
    }

    strengthLabel.innerHTML = "Strength: " + strengthPercentage + "%";
}

function checkPasswordStrengthRules(password) {
    // Implement your password strength rules here
    // For simplicity, let's assume a minimum length requirement
    return password.length >= 8 ? 5 : 0;
}
