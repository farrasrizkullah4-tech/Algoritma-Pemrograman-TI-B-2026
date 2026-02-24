import myOOP

#INHERITANCE
print(myOOP.ProdukElektronik("Microwave",10000000,"2 tahun").info_produk())
print (myOOP.ProdukMakanan("roti",5000,"2029-9-2").info_produk())

#POLYMORPHISM
print(myOOP.NotifikasiEmail("Anda memiliki email baru.").kirim())
print(myOOP.NotifikasiSMS("Anda memiliki SMS baru.").kirim())

#ENCAPSULATION
m1 = myOOP.Mahasiswa("CristianoUjang", 88)
m1.set_nilai(-1)
print(m1.get_nilai())
