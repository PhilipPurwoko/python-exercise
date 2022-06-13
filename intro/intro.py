def penjumlahan():
    ''' Buatlah fungsi yang mereturn hasil penjumlahan dari variabel bilangan_1 dan bilangan_2 '''
    bilangan_1 = 10
    bilangan_2 = 30
    # Tulis kode dibawah baris ini, jangan ubah kode diatas
    return bilangan_1+bilangan_2

def perkalian():
    ''' Buatlah fungsi yang mereturn hasil perkalian dari variabel bilangan_1 dan bilangan_2 '''
    bilangan_1 = 10
    bilangan_2 = 20
    # Tulis kode dibawah baris ini, jangan ubah kode diatas
    return bilangan_1*bilangan_2

def perpangkatan():
    ''' Buatlah fungsi yang mereturn hasil dari bilangan_1 pangkat bilangan_2 '''
    bilangan_1 = 12
    bilangan_2 = 5
    # Tulis kode dibawah baris ini, jangan ubah kode diatas
    return bilangan_1**bilangan_2

def deret_bilangan_ganjil():
    ''' Buatlah fungsi yang mereturn deret yang berupa 10 bilangan ganjil pertama, dimulai dari 1 '''
    # Tulis kode dibawah baris ini, jangan ubah kode diatas
    hasil = []
    for i in range(20):
        if i%2!=0:
            hasil.append(i)
    return hasil

def deret_bilangan_genap():
    ''' Buatlah fungsi yang mereturn deret yang berupa 10 bilangan genap pertama, dimulai dari 2 '''
    # Tulis kode dibawah baris ini, jangan ubah kode diatas
    hasil = []
    for i in range(1,21):
        if i%2==0:
            hasil.append(i)
    return hasil

def deret_bilangan_prima():
    ''' Buatlah fungsi yang mereturn deret yang berupa 10 bilangan prima pertama, dimulai dari 1 '''
    # Tulis kode dibawah baris ini, jangan ubah kode diatas
    