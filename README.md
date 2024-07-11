# Library
Kütüphane Yönetim Sistemi
Bu proje, bir kütüphane yönetim sistemini simüle eden Python sınıflarını içermektedir. Bu sistem, öğrencileri ve kitapları yönetmeyi, kitap ödünç almayı ve iade etmeyi sağlar.

İçindekiler
Özellikler
Kurulum
Kullanım
Sınıf Detayları
Student Sınıfı
Library Sınıfı
Book Sınıfı
TakenBook Sınıfı
Katkıda Bulunma
Lisans
Özellikler
Öğrenci ekleme ve silme
Kitap ekleme ve mevcut kitapları listeleme
Öğrencilerin kitap ödünç alabilmesi
Alınan kitapların listesini görüntüleme
Öğrencilerin aktiflik durumlarını değiştirebilme
Kurulum
Bu projeyi yerel makinenize klonlayın:
bash
Kodu kopyala
git clone https://github.com/kullanıcı_adı/kütüphane-yönetim-sistemi.git
Proje dizinine gidin:
bash
Kodu kopyala
cd kütüphane-yönetim-sistemi
Kullanım
Projeyi çalıştırmak için aşağıdaki adımları izleyin:

Python dosyasını çalıştırın:

bash
Kodu kopyala
python library_system.py
Örnek kodu kullanarak, öğrenci ve kitap ekleyebilir, kitap ödünç alabilir ve mevcut bilgileri görüntüleyebilirsiniz.

Örnek Kullanım
python
Kodu kopyala
from library_system import Library, Student, Book

# Öğrenci oluşturma
irem = Student('İrem', 'Kaya', 2003)
akif = Student('Akif', 'Kaya', 2017)
volkan = Student('Volkan', 'Taşcı', 1980)

# Kütüphane oluşturma
library = Library('Kütüphane')

# Kitap ekleme
book1 = library.add_book(Book('Python', 'Volkan Taşçı', 2019))
library.add_book(Book('JAVA', 'Volkan TAŞÇI', 2020))
library.add_book(Book('C', 'Volkan TAŞÇI', 2020))
library.add_book(Book('C++', 'Volkan TAŞÇI', 2020))
library.add_book(Book('C#', 'Volkan TAŞÇI', 2020))

# Öğrenci ekleme
library.add_student(irem)
library.add_student(akif)
library.add_student(volkan)

# Kitap ödünç alma
library.get_book(book1, irem)

# Alınan kitapları görüntüleme
print(library.get_taken_books())
Sınıf Detayları
Student Sınıfı
first_name: Öğrencinin adı
last_name: Öğrencinin soyadı
birth_year: Öğrencinin doğum yılı
toggle_active(token): Öğrencinin aktiflik durumunu değiştirir (token 'secret' olmalıdır)
__str__(): Öğrencinin ad ve soyadını döndürür
Library Sınıfı
name: Kütüphanenin adı
add_book(book): Kütüphaneye kitap ekler
get_books(): Tüm kitapları döndürür
get_available_books(): Mevcut (ödünç verilebilir) kitapları döndürür
get_book(book, student): Bir kitabı bir öğrenciye ödünç verir
add_student(student): Kütüphaneye öğrenci ekler
get_students(): Tüm öğrencileri döndürür
get_active_students(): Aktif öğrencileri döndürür
del_student(student): Bir öğrenciyi kütüphaneden siler
get_taken_books(): Alınan kitapların listesini döndürür
Book Sınıfı
title: Kitabın başlığı
author: Kitabın yazarı
year: Kitabın basım yılı
toggle_available(token): Kitabın mevcutluk durumunu değiştirir (token 'secret' olmalıdır)
__str__(): Kitabın başlık ve yazarını döndürür
TakenBook Sınıfı
book: Alınan kitap
student: Kitabı alan öğrenci
__str__(): Kitap ve öğrencinin bilgilerini döndürür
Katkıda Bulunma
Katkıda bulunmak için lütfen bir pull request gönderin veya bir issue açın.
