# BLM101_24360859079_IlaydaGundogdu
# Bilgisayar Mühendisliğine Giriş Dönem Projesi
# İlayda GÜNDOĞDU 24360859079
# Proje Konu Başlığım:'Python ile Otomatik HTML Sayfası Oluşturucu'
# YouTube linkim: https://youtu.be/yzzrRdvKp5c?si=nCmjkLM7MkEpxkKG

# Proje Açıklaması
Bu proje, Python programlama dili kullanılarak kullanıcıdan alınan bilgilerin
otomatik olarak bir HTML web sayfasına dönüştürülmesini amaçlamaktadır.
Program çalıştırıldığında kullanıcıdan ad, alınan dersler ve biyografi bilgileri
istenir. Girilen bu bilgiler kullanılarak basit CSS renklendirmesine sahip,
başlıklı ve listeli bir web sayfası oluşturulur.
Oluşturulan web sayfası `index.html` adıyla kaydedilir ve tarayıcıda açıldığında
kullanıcının girdiği bilgiler düzenli bir şekilde görüntülenir.

Kod Ne Yapar?;
- Kullanıcıdan ad, dersler ve biyografi bilgilerini alır.
- Bu bilgileri kullanarak HTML ve CSS kodlarını Python içerisinde oluşturur.
- Alınan dersleri liste formatında HTML sayfasına ekler.
- Oluşturulan HTML kodunu `index.html` adlı bir dosyaya yazar.
- Program sonunda kullanıcıya dosyanın başarıyla oluşturulduğunu bildirir

Kod Nasıl Çalıştırılır?;
Bu proje Python programlama dili ile geliştirilmiştir.  
Kod, **PyCharm** geliştirme ortamı kullanılarak yazılmıştır ancak farklı Python
editörlerinde de çalıştırılabilir.

Gereksinimler;
- Python 3.x sürümü
Ekstra bir kütüphane veya kurulum gerekmemektedir.

Çalıştırma Adımları;
1. Python dosyasını (`.py`) bilgisayarınıza kaydedin.
2. PyCharm veya herhangi bir Python editörü ile dosyayı açın.
3. Programı çalıştırın.
4. Konsolda sorulan soruları sırasıyla cevaplayın.
5. Program çalışmasını tamamladığında aynı klasörde `index.html` dosyası oluşacaktır.
6. Oluşan `index.html` dosyasını tarayıcıda açarak sonucu görüntüleyin.

Kodun Çalışma Mantığı;
Programın ilk bölümünde `input()` fonksiyonu kullanılarak kullanıcıdan gerekli
bilgiler alınır. Bu bilgiler Python değişkenlerinde saklanır.
Daha sonra HTML sayfasının yapısı Python içerisinde bir string değişkeni olarak
oluşturulur. Bu string içerisinde HTML etiketleri ve sayfanın görünümünü düzenleyen
basit CSS kodları yer alır.
Kullanıcının girdiği dersler bilgisi virgül karakterine göre ayrılarak bir listeye
dönüştürülür. `for` döngüsü kullanılarak her bir ders HTML sayfasına liste elemanı
olarak eklenir.
Son aşamada Python’un dosya yazma özelliği kullanılarak oluşturulan HTML kodu
`index.html` adlı dosyaya yazılır. Böylece kullanıcıdan alınan bilgilerle
dinamik olarak oluşturulmuş bir web sayfası elde edilir.
# Sonuç
Bu proje sayesinde Python kullanılarak basit bir web sayfasının otomatik olarak
oluşturulabileceği gösterilmiştir. Proje, Python’un string işlemleri ve dosya
yazma özelliklerinin pratik bir kullanımını sunmaktadır.
