document.addEventListener("DOMContentLoaded", function () {
    const generateBtn = document.getElementById("generate-keys-btn");

    if (generateBtn) {
        generateBtn.addEventListener("click", function () {
            const algorithmSelect = document.getElementById("algorithm");
            const algorithm = algorithmSelect ? algorithmSelect.value : "rsa";
            const route = `/generate_${algorithm}_keys`;

            fetch(route)
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
