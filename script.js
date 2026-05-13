function validateForm() {
    let inputs = document.querySelectorAll("input");

    for (let i = 0; i < inputs.length; i++) {
        let val = inputs[i].value.trim();

        // empty check
        if (val === "") {
            alert("❌ Please fill all fields!");
            inputs[i].focus();
            return false;
        }

        // numeric check
        if (isNaN(val)) {
            alert("❌ Only numeric values allowed!");
            inputs[i].focus();
            return false;
        }
    }

    return true;
}

// real-time color feedback
document.addEventListener("DOMContentLoaded", () => {
    let inputs = document.querySelectorAll("input");

    inputs.forEach(input => {
        input.addEventListener("input", () => {
            if (input.value === "" || isNaN(input.value)) {
                input.style.borderColor = "red";
            } else {
                input.style.borderColor = "green";
            }
        });
    });
});