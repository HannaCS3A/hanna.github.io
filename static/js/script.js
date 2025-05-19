document.addEventListener("DOMContentLoaded", function () {
    // Theme toggle
    const toggleBtn = document.getElementById("toggle-theme");
    const body = document.body;

    if (toggleBtn) {
        toggleBtn.addEventListener("click", () => {
            body.classList.toggle("dark-mode");
            body.classList.toggle("light-mode");

            const theme = body.classList.contains("dark-mode") ? "dark" : "light";
            localStorage.setItem("theme", theme);
        });
    }

    const storedTheme = localStorage.getItem("theme");
    if (storedTheme === "dark") {
        body.classList.add("dark-mode");
        body.classList.remove("light-mode");
    }

    // RSA key generation
    const generateBtn = document.getElementById("generate-keys-btn");

    if (generateBtn) {
        generateBtn.addEventListener("click", function () {
            fetch("/generate_keys")
                .then(response => response.json())
                .then(data => {
                    const publicKeyArea = document.getElementById("public_key");
                    const privateKeyArea = document.getElementById("private_key");

                    if (publicKeyArea && privateKeyArea) {
                        publicKeyArea.value = data.public_key;
                        privateKeyArea.value = data.private_key;
                    }
                })
                .catch(error => {
                    alert("Error generating keys: " + error.message);
                });
        });
    }
});
