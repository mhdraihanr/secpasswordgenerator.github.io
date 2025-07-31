from flask import Flask, render_template, request
import random
import string
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# fungsi untuk mencheck kekuatan passwordnya
def check_password_strength(password):
    length_score = len(password) >= 12
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    # skor dihitung berdasarkan jumlah kategori
    strength_score = sum([length_score, has_uppercase, has_lowercase, has_digit, has_special])

    # penentuan level kekuatan berdasarkan skor
    if strength_score == 5:
        return "Sangat Kuat"
    elif strength_score == 4:
        return "Kuat"
    elif strength_score == 3:
        return "Sedang"
    else:
        return "Lemah"

# fungsi untuk membuat password yang aman 
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

# Route untuk halaman utama
@app.route("/", methods=["GET", "POST"])
def check_strength():
    strength = None
    password = None
    if request.method == "POST":
        if "generate" in request.form:  # Jika pengguna menekan tombol "Generate Password"
            length = int(request.form.get("length", 12))
            password = generate_secure_password(length)
            strength = check_password_strength(password)
        elif "check" in request.form:  # Jika pengguna menekan tombol "Periksa Kekuatan"
            password = request.form["password"]
            strength = check_password_strength(password)
    return render_template("check.html", strength=strength, password=password)

# Handler untuk Vercel
def handler(request):
    return app(request.environ, lambda status, headers: None)

if __name__ == "__main__":
    app.run(debug=True)