document.addEventListener("DOMContentLoaded", () => {
    console.log("JavaScript is working!"); // Debugging log
    const darkModeToggle = document.getElementById("darkModeToggle");
    if (!darkModeToggle) {
        console.error("Dark mode button not found!"); // Cek elemen tombol
        return;
    }

    // Cek LocalStorage
    if (localStorage.getItem("dark-mode") === "enabled") {
        console.log("Dark mode was enabled previously."); // Debugging log
        document.body.classList.add("dark-mode");
        darkModeToggle.textContent = "☀️ Light Mode";
    }

    darkModeToggle.addEventListener("click", () => {
        console.log("Dark mode toggle clicked!"); // Debugging log
        document.body.classList.toggle("dark-mode");

        // Simpan preferensi
        if (document.body.classList.contains("dark-mode")) {
            localStorage.setItem("dark-mode", "enabled");
            darkModeToggle.textContent = "☀️ Light Mode";
        } else {
            localStorage.setItem("dark-mode", "disabled");
            darkModeToggle.textContent = "🌙 Dark Mode";
        }
    });
});
