// Tunggu hingga seluruh halaman selesai dimuat
document.addEventListener("DOMContentLoaded", () => {
    console.log("JavaScript loaded successfully!"); // Debugging log

    // Ambil tombol toggle dark mode
    const darkModeToggle = document.getElementById("darkModeToggle");

    // Cek apakah tombol ditemukan
    if (!darkModeToggle) {
        console.error("Dark mode toggle button not found!"); // Debugging log
        return;
    }

    // Periksa preferensi sebelumnya dari LocalStorage
    const darkModePreference = localStorage.getItem("dark-mode");
    if (darkModePreference === "enabled") {
        enableDarkMode(darkModeToggle); // Aktifkan dark mode
    } else {
        disableDarkMode(darkModeToggle); // Nonaktifkan dark mode
    }

    // Tambahkan event listener untuk tombol
    darkModeToggle.addEventListener("click", () => {
        // Toggle dark mode saat tombol diklik
        if (document.body.classList.contains("dark-mode")) {
            disableDarkMode(darkModeToggle); // Nonaktifkan dark mode
            localStorage.setItem("dark-mode", "disabled"); // Simpan preferensi
        } else {
            enableDarkMode(darkModeToggle); // Aktifkan dark mode
            localStorage.setItem("dark-mode", "enabled"); // Simpan preferensi
        }
    });
});

// Fungsi untuk mengaktifkan dark mode
function enableDarkMode(toggleButton) {
    document.body.classList.add("dark-mode");
    toggleButton.textContent = "☀️ Light Mode"; // Ubah teks tombol
    console.log("Dark mode enabled!"); // Debugging log
}

// Fungsi untuk menonaktifkan dark mode
function disableDarkMode(toggleButton) {
    document.body.classList.remove("dark-mode");
    toggleButton.textContent = "🌙 Dark Mode"; // Ubah teks tombol
    console.log("Dark mode disabled!"); // Debugging log
}
