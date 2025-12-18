# Kullanıcıdan gerekli bilgileri input fonksiyonu ile alıyoruz
isim = input("Adiniz nedir?: ")
dersler = input("Aldiginiz dersleri yaziniz (virgulle ayiriniz): ")
bio = input("Biografiniz nedir?: ")

# HTML sayfasini tutacak string degiskenini olusturuyoruz
# Bu string icerisinde HTML ve CSS kodlari bulunmaktadir
html = f"""
<!doctype html>
<html lang="tr">
<head>
    <meta charset="utf-8">
    <title>{isim} - Kisisel Sayfa</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #F3E8FF;
            padding: 30px;
        }}

        .kart {{
            background-color: white;
            max-width: 700px;
            margin: auto;
            padding: 25px;
            border-radius: 12px;
        }}

        h1 {{
            color: #5b21b6;
            border-bottom: 2px solid #ddd6fe;
            padding-bottom: 10px;
        }}

        h2 {{
            color: #6d28d9;
            margin-top: 25px;
        }}

        p, li {{
            color: #3f3f46;
        }}

        ul {{
            padding-left: 20px;
        }}

        li {{
            margin-bottom: 6px;
        }}
    </style>
</head>

<body>
    <div class="kart">
        <h1>{isim}</h1>

        <h2>Aldiginiz Dersler</h2>
        <ul>
"""

# Kullanicinin girdigi dersleri virgule gore ayirip liste haline getiriyoruz
ders_listesi = dersler.split(",")

# Ders listesindeki her bir dersi HTML listesine ekliyoruz
for ders in ders_listesi:
    html += f"            <li>{ders.strip()}</li>\n"

# HTML sayfasinin kalan kisimlarini ekliyoruz
html += f"""
        </ul>

        <h2>Biyografi</h2>
        <p>{bio}</p>
    </div>
</body>
</html>
"""

# HTML kodunu index.html adli dosyaya yaziyoruz
with open("index.html", "w", encoding="utf-8") as dosya:
    dosya.write(html)

# Programin basariyla calistigini kullaniciya bildiriyoruz
print("index.html basariyla olusturuldu!")
