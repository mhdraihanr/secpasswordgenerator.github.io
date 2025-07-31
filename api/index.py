from flask import Flask, request, jsonify, render_template_string
import random
import string
import os

app = Flask(__name__)

# Template HTML inline
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Strength Checker</title>
    <style>
        :root {
            --bg-color: #ffffff;
            --text-color: #000000;
            --box-shadow-light: 0 4px 10px rgba(0, 0, 0, 0.1);
            --box-shadow-dark: 0 4px 10px rgba(86, 86, 86, 0.3);
        }
        body.dark-mode {
            --bg-color: #272525;
            --text-color: #ffffff;
            --button-bg: #1f1f1f;
            --button-text: #007bff;
        }
        body {
            font-family: Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        .container {
            width: 90%;
            max-width: 500px;
            background-color: var(--bg-color);
            color: var(--text-color);
            padding: 20px;
            border-radius: 8px;
            box-shadow: var(--box-shadow-light);
            text-align: center;
        }
        body.dark-mode .container {
            box-shadow: var(--box-shadow-dark);
        }
        h1 {
            font-size: 24px;
            margin-bottom: 20px;
            color: #fa1212;
        }
        h2 {
            font-size: 18px;
            margin-bottom: 10px;
            color: var(--text-color);
        }
        .form-container {
            margin-bottom: 20px;
        }
        input[type="text"], input[type="number"] {
            width: calc(100% - 20px);
            padding: 10px;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 14px;
        }
        button {
            background-color: #00cfda;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            width: 100%;
        }
        button:hover {
            background-color: #00b8c4;
        }
        .result {
            background-color: var(--bg-color);
            color: var(--text-color);
            padding: 10px;
            border-radius: 4px;
            border: 1px solid #d4edda;
            margin-top: 10px;
        }
        .creator {
            font-size: 0.8em;
            color: var(--text-color);
            margin-top: 10px;
            text-align: center;
            opacity: 0.7;
        }
        #darkModeToggle {
            position: absolute;
            top: 20px;
            right: 20px;
            background-color: #007bff;
            color: white;
            border: none;
            padding: 8px 12px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 12px;
            width: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <button id="darkModeToggle">🌙 Dark Mode</button>
        <h1>Alat Pembuat Password yang Aman</h1>

        <div class="form-container">
            <form method="post">
                <h2>Memeriksa Keamanan Passwordmu</h2>
                <input type="text" name="password" placeholder="Enter your password" required>
                <button type="submit" name="check">Check</button>
            </form>
        </div>

        <div class="form-container">
            <form method="post">
                <h2>Membuat Password yang Aman</h2>
                <input type="number" name="length" placeholder="Password length (min 8)" min="8" required>
                <button type="submit" name="generate">Hasilkan</button>
            </form>
        </div>

        {% if password %}
            <div class="result">
                <h2>Hasil:</h2>
                <p><strong>Password:</strong> {{ password }}</p>
                <p><strong>Tingkat Keamanan:</strong> {{ strength }}</p>
            </div>
        {% endif %}

        <p class="creator">Created by 4bdul</p>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const darkModeToggle = document.getElementById("darkModeToggle");
            
            const darkModePreference = localStorage.getItem("dark-mode");
            if (darkModePreference === "enabled") {
                enableDarkMode(darkModeToggle);
            } else {
                disableDarkMode(darkModeToggle);
            }
            
            darkModeToggle.addEventListener("click", () => {
                if (document.body.classList.contains("dark-mode")) {
                    disableDarkMode(darkModeToggle);
                    localStorage.setItem("dark-mode", "disabled");
                } else {
                    enableDarkMode(darkModeToggle);
                    localStorage.setItem("dark-mode", "enabled");
                }
            });
        });
        
        function enableDarkMode(toggleButton) {
            document.body.classList.add("dark-mode");
            toggleButton.textContent = "☀️ Light Mode";
        }
        
        function disableDarkMode(toggleButton) {
            document.body.classList.remove("dark-mode");
            toggleButton.textContent = "🌙 Dark Mode";
        }
    </script>
</body>
</html>
'''

def check_password_strength(password):
    length_score = len(password) >= 12
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    strength_score = sum([length_score, has_uppercase, has_lowercase, has_digit, has_special])
    
    if strength_score == 5:
        return "Sangat Kuat"
    elif strength_score == 4:
        return "Kuat"
    elif strength_score == 3:
        return "Sedang"
    else:
        return "Lemah"

def generate_secure_password(length=12):
    if length < 8:
        raise ValueError("Panjang password minimal adalah 8 karakter.")
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    mandatory_chars = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    remaining_length = length - len(mandatory_chars)
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    random_chars = [random.choice(all_characters) for _ in range(remaining_length)]
    password_list = mandatory_chars + random_chars
    random.shuffle(password_list)
    return ''.join(password_list)

@app.route("/", methods=["GET", "POST"])
def index():
    strength = None
    password = None
    if request.method == "POST":
        if "generate" in request.form:
            length = int(request.form.get("length", 12))
            password = generate_secure_password(length)
            strength = check_password_strength(password)
        elif "check" in request.form:
            password = request.form["password"]
            strength = check_password_strength(password)
    return render_template_string(HTML_TEMPLATE, strength=strength, password=password)

# Export app untuk Vercel
app = app

if __name__ == "__main__":
    app.run(debug=True)