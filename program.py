import random
import colorama
from colorama import Fore, Back, Style
colorama.init()

giris = """
Kayseri Üniversitesi / Bilgisayar Programcılığı - 1. Final Ödevi


Furkan Berkehan



"""

sorular = """

(1) Klavyeden girilen bir sayının Armstrong sayısı olup olmadığını söyleyen bir program yazınız.
Program sonunda kullanıcıya devam edip etmeyeceğini sorunuz. Kullanıcı “Hayır” cevabını verene kadar yeni sayı girişi ile hesaplamaya devam ediniz.


(2) Klavyeden girilen alt sınır ve üst sınır değerleri arasında bilgisayar bir rastgele sayı üretecektir ancak kullanıcıya bu sayıyı söylemeyecektir. Kullanıcı tahminde bulunacaktır. Kullanıcı tahmini ile bilgisayarın tuttuğu sayı karşılaştırılacak ve kullanıcıya AKLIMDAKİ SAYIDAN BÜYÜK! veya AKLIMDAKİ SAYIDAN KÜÇÜK! şeklinde bilgi verilecektir. Kullanıcı bilgisayarın ürettiği sayıyı doğru tahmin ettiğinde oyun sona erecektir. Oyun sonunda kullanıcının kaç denemede sayıyı bulduğu ekranda görüntülenecektir. Bu oyunun çözümüne ait programı yazınız.


(3) Bir ve kendisinden başka tamsayıya tam bölünemeyen tamsayılara “asal sayı” denir. Klavyeden girilen üst sınır kadar olan asal sayıları listeleyen programı C veya Python dilinde yazınız

"""

print(giris)
print(sorular)
dongu = 1

while dongu == 1:
	print(Fore.BLUE)
	soru = input(
	    "Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")
	print(Style.RESET_ALL)

	if soru == "q":
		print(Fore.RED)
		print("çıkılıyor...")
		print(Style.RESET_ALL)
		break

	elif soru == "1":
		dongu = 0
		while dongu == 0:
			birdaha = "Aşağıdan programı tekrar kullanabilirsin!\n\n"
			arm = input("Armstrong Kontrol\nTest için sayı gir: ")
			top = 0
			for i in range(len(arm)):
				top += int(arm[i])**len(arm)
			if top == int(arm):
				print(Fore.GREEN)
				print("Bu sayı armstrong sayısıdır.\n\n")
				print(Style.RESET_ALL)
				tekrar = input("Tekrar denemek ister misin? (evet/hayır): ")
				if tekrar == "evet":
					dongu = 0
					print("Tamamdır tekrar başlıyoruz.\n\n", birdaha)
				elif tekrar == "hayır":
					dongu = 1
					print("Pekala başa dönelim.\n\n")
				else:
					dongu = 1
					print("Hatalı Giriş\n Ana sayfaya dönüyorum.\n")

			else:
				print(Fore.RED)
				print("Malesef bu sayı bir Armstrong sayısı değil..\n\n")
				print(Style.RESET_ALL)
				tekrar = input("Tekrar denemek ister misin? (evet/hayır): ")
				if tekrar == "evet":
					dongu = 0
					print("Tamamdır tekrar başlıyoruz.\n\n", birdaha)
				elif tekrar == "hayır":
					dongu = 1
					print("Pekala başa dönelim.\n\n")
				else:
					dongu = 1
					print("Hatalı Giriş\n Ana sayfaya dönüyorum.\n")

	elif soru == "2":
		print(Fore.YELLOW)
		print(
		    "Sayı Tahmin Programı \n\n Şimdi size bir alt ve bir üst değer seçtireceğim. Bu sayılar arasında bir sayı tahmin edeceğim. bakalım bilebilecek misiniz?\n\n"
		)
		print(Style.RESET_ALL)

		altDeger = int(input("Bir alt değer giriniz."))
		ustDeger = int(input("Bir üst değer giriniz."))
		print("Tamamdır. Bir sayı tuttum. Tahmin ediniz.")

		sayiTahmin = random.randint(altDeger, ustDeger)

		tahminDongusu = 0
		tahminSayaci = 0
		while tahminDongusu == 0:
			tahminSayaci = tahminSayaci + 1
			kullaniciTahmin = int(input("Tahmininizi giriniz: "))

			if kullaniciTahmin < altDeger:
				print(Fore.RED)
				print(
				    "\nMaalesef :/\ntekrar deneyin.", tahminSayaci,
				    ".Deneme. \nİpucu: Tahmin ettiğim sayı ", altDeger, "ile ",
				    ustDeger,
				    "Arasında bir sayı ve seçtiğiniz sayı tahminimden daha küçük."
				)
				print(Style.RESET_ALL)

			elif kullaniciTahmin > ustDeger:
				print(Fore.RED)
				print(
				    "\nMaalesef :/\ntekrar deneyin.", tahminSayaci,
				    ".Deneme. \nİpucu: Tahmin ettiğim sayı ", altDeger, "ile ",
				    ustDeger,
				    "Arasında bir sayı ve seçtiğiniz sayı tahminimden daha büyük."
				)
				print(Style.RESET_ALL)

			elif kullaniciTahmin > sayiTahmin:
				print(Fore.RED)
				print(
				    "\nMaalesef :/\ntekrar deneyin.",
				    tahminSayaci,
				    ".Deneme. \nİpucu: seçtiğiniz sayı tahmin ettiğim sayıdan büyük!",
				)
				print(Style.RESET_ALL)

			elif kullaniciTahmin < sayiTahmin:
				print(Fore.RED)
				print(
				    "\nMaalesef :/\ntekrar deneyin.",
				    tahminSayaci,
				    ".Deneme. \nİpucu: seçtiğiniz sayı tahmin ettiğim sayıdan küçük!",
				)
				print(Style.RESET_ALL)

			elif kullaniciTahmin == sayiTahmin:
				tahminDongusu = 1
				print(Fore.GREEN)
				print(
				    "\nTebrikler Harika Tahmin!", tahminSayaci,
				    ". Denemede Doğru sayıyı buldunuz! \n\n Ana sayfaya dönüyorum. \n\n"
				)
				print(Style.RESET_ALL)

	elif soru == "3":
		print(Fore.YELLOW)
		print(
		    "Şimdi bir sayı seçeceksiniz ve o sayıya kadar olan asal sayıları bulacağım.\n\n"
		)
		print(Style.RESET_ALL)

		sayiAsal = int(input("Sayi Giriniz:"))
		sayac = 0
		toplam = 0
		sayacTop = 0

		for i in range(2, (sayiAsal + 1)):
			sayac = 0
			for j in range(2, i):
				if (i % j == 0):
					sayac = sayac + 1
					break
			if (sayac == 0):
				print(i)
				sayacTop = sayacTop + 1

		print(Fore.GREEN)
		print("Toplam ", sayacTop, " adet asal sayı var.")
		print(Style.RESET_ALL)

	else:
		print(Fore.RED)
		print("Yanlış giriş.")
		print("Aşağıdaki seçeneklerden birini giriniz:", sorular)
		print(Style.RESET_ALL)
