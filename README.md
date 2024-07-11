# Library Management System

Bu proje, bir kütüphane yönetim sistemi uygulamasıdır. Kullanıcılar, bu sistem aracılığıyla kitap ekleyebilir, ödünç alabilir, öğrenci ekleyebilir ve mevcut kitap ve öğrencileri yönetebilirler.

## İçindekiler

- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Sınıf Detayları](#sınıf-detayları)
- [Katkıda Bulunma](#katkıda-bulunma)


## Özellikler

- Kitap ekleme ve listeleme
- Öğrenci ekleme ve listeleme
- Kitap ödünç alma ve geri verme
- Mevcut ve ödünç alınmış kitapları görüntüleme
- Aktif öğrencileri listeleme

## Kurulum

Projeyi yerel makinenize kurmak için aşağıdaki adımları izleyin:

1. Bu projeyi klonlayın:
    ```bash
    git clone https://github.com/irem-kaya/Library.git
    ```

2. Proje dizinine gidin:
    ```bash
    cd Library
    ```

3. Gerekli bağımlılıkları yükleyin (varsa):
    ```bash
    pip install -r requirements.txt
    ```

## Kullanım

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. Ana dosyayı çalıştırın:
    ```bash
    python main.py
    ```

2. Program başlatıldığında, kullanıcı arayüzü üzerinden kitap ekleyebilir, ödünç alabilir, öğrenci ekleyebilir ve mevcut kitap ve öğrencileri yönetebilirsiniz.

### Örnek Kullanım

```python
from library_system import Library, Book, Student

# Kütüphane oluşturma
library = Library('Kütüphane')

# Öğrenci ekleme
irem = Student('İrem', 'Kaya', 2003)
library.add_student(irem)

# Kitap ekleme
book1 = library.add_book(Book('Python', 'Volkan Taşçı', 2019))

# Kitap ödünç alma
library.get_book(book1, irem)

# Ödünç alınmış kitapları listeleme
print(library.get_taken_books())
