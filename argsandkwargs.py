def kwarguments (**kwargument):
	print("-"*5,"Kullanıcı verileri:","-"*5)
	print(kwargument)
	print(f"İsminiz:{kwargument["isim"]}")
	print(f"Soyisminiz:{kwargument["soyisim"]}")
	print(f"Yasiniz:{kwargument["yas"]}")

	if kwargument["yas"] < 18:
		print("Yaşınız 18'den küçük olduğu için maalesef devam edemiyorsunuz!")

İsim = input("İsminiz Nedir?")
Soyisim = input("Soyisminiz Nedir?")
Yas = int(input("Yasiniz Nedir?"))
kwarguments(isim=İsim,soyisim=Soyisim,yas=Yas)