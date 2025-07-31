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

### api/app.py
File utama yang akan dijalankan oleh Vercel. Menggunakan inline templates untuk menghindari masalah path di serverless environment.

### api/index.py (backup)
File backup dengan external templates (mungkin menyebabkan masalah path di Vercel).

### requirements.txt
Daftar dependencies Python yang akan diinstall oleh Vercel.

## Troubleshooting

1. **Deployment Failed**: 
   - Coba gunakan api/app.py (dengan inline templates) sebagai entry point
   - Pastikan vercel.json mengarah ke file yang benar
   - Hapus runtime.txt jika menyebabkan konflik
   - Gunakan konfigurasi vercel.json yang sederhana

2. **Error 500 FUNCTION_INVOCATION_FAILED**: 
   - Pastikan tidak ada masalah dengan path templates dan static files
   - Gunakan inline templates sebagai solusi alternatif
   - Cek logs di Vercel dashboard untuk detail error

3. **Error 404**: Pastikan vercel.json sudah benar dan file entry point ada
 
 4. **Template not found**: 
    - Gunakan inline templates (api/app.py) untuk menghindari masalah path
    - Jika menggunakan external templates, pastikan path absolut benar
 
 5. **Static files tidak load**: 
    - Inline CSS/JS (seperti di api/app.py) adalah solusi terbaik untuk Vercel
    - Alternatif: tambahkan build configuration untuk static files
 
 6. **Module not found**: Pastikan semua dependencies ada di requirements.txt

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