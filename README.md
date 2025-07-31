# Password Generator - Deploy ke Vercel

Aplikasi Flask untuk mengecek kekuatan password dan membuat password yang aman.

## Langkah-langkah Deploy ke Vercel

### 1. Persiapan File
Pastikan struktur folder seperti ini:
```
Project PassGenerator/
├── api/
│   └── index.py          # File utama untuk Vercel
├── static/
│   ├── script.js
│   └── style.css
├── templates/
│   └── check.html
├── app.py                # File Flask original
├── requirements.txt      # Dependencies Python
├── vercel.json          # Konfigurasi Vercel
└── README.md            # File ini
```

### 2. Install Vercel CLI
```bash
npm install -g vercel
```

### 3. Login ke Vercel
```bash
vercel login
```

### 4. Deploy Aplikasi
Di folder root project, jalankan:
```bash
vercel
```

Atau untuk deploy langsung:
```bash
vercel --prod
```

### 5. Konfigurasi Environment (Opsional)
Jika ada environment variables, tambahkan di dashboard Vercel atau gunakan:
```bash
vercel env add
```

## Alternatif: Deploy via GitHub

1. Push code ke GitHub repository
2. Buka [vercel.com](https://vercel.com)
3. Login dan klik "New Project"
4. Import repository GitHub Anda
5. Vercel akan otomatis mendeteksi sebagai Python project
6. Klik "Deploy"

## File Penting untuk Vercel

### vercel.json
File konfigurasi yang memberitahu Vercel cara menjalankan aplikasi Python/Flask.

### api/index.py
File utama yang akan dijalankan oleh Vercel. Ini adalah copy dari app.py dengan penyesuaian path untuk template dan static files.

### requirements.txt
Daftar dependencies Python yang akan diinstall oleh Vercel.

## Troubleshooting

1. **Error 404**: Pastikan vercel.json sudah benar dan file api/index.py ada
2. **Template not found**: Pastikan path template_folder dan static_folder di api/index.py sudah benar
3. **Module not found**: Pastikan semua dependencies ada di requirements.txt

## Fitur Aplikasi

- ✅ Cek kekuatan password
- ✅ Generate password aman
- ✅ Dark/Light mode toggle
- ✅ Responsive design
- ✅ Local storage untuk preferensi tema

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Vercel
- **Storage**: LocalStorage untuk preferensi tema