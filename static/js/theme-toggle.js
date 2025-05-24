document.addEventListener("DOMContentLoaded", function () {
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
});
