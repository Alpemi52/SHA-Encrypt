import random as rnd
import hashlib as sh

print("*" * 5 + "Şifreleme Uygulamasına Hoşgeldiniz" + "*" * 5)
kontrol = True
while (kontrol):
    print(
        "Lütfen bir depolama sistemi seciniz:\n1. Birinci Depolama Sistemi\n2. İkinci Depolama Sistemi\n3. Üçüncü Depolama Sistemi\n4. Dördüncü Depolama Sistemi\n5. Beşinci Depolama Sistemi")
    secim = int(input("Seçim:"))
    if (secim > 0 and secim < 6):
        print(str(secim) + ". secildi giris sayfasına aktarılıyorsunuz." + "\nLütfen giriş yapınız...")
        kontrol = False
    else:
        print("Secimler dısında bir sayı girdiniz. Lütfen tekrar deneyin!")

## Password.txt dosyasını içe alıyoruz
credentials = []
with open("Password.txt", "r") as f:
    credentials = f.readlines()

## Ad Soyad - Password formatında split ediyoruz
splitted = []
for user in credentials:
    splitted.append(user.split(","))  # okuduğumuz dosyayı işlemlerimizi yapmak için ayırıyoruz

durum = True
while (durum):  # Kullanıcıdan doğru kullanıcı adı ve sifreyi alana kadar girmesini isteyen while döngüsü
    username = input("Username:")  # Kullanıcı adı girisi
    password = input("Password:")  # Kullanıcı adı girisi
    for user in splitted:
        if (user[0] == username and str(user[1]).replace("\n", "")[1:] == password):
            print("Başarıyla giriş yapıldı!")
            durum = False
            break
        else:
            print(
                "Kullanıcı adınız ve / veya şifreniz doğru değil. Lütfen tekrar deneyin!")  # Yanlışsa mesaj verdirip döngüye devam eder
            break

## Uniqe id + password haline getiriyoruz
kimlik = "BIL008-2020"
veritabani1 = []
for i in range(len(splitted)):
    uniqe_id = kimlik + str(rnd.randint(10000, 99999))
    veritabani1.append([uniqe_id, splitted[i][1]])

## veritabani1 dizimizi kaydediyoruz
with open("Veritabani1.txt", "w") as veri:
    for x in veritabani1:
        veri.writelines(x)

## Uniqe id + hash haline getiriyoruz
kimlik2 = "BIL008-2020"
veritabani2 = []
for i in range(len(veritabani1)):
    new_uniqe_id = kimlik2 + str(rnd.randint(10000, 99999))
    veritabani2.append([new_uniqe_id, " " + sh.md5(veritabani1[i][1].encode('utf-8')).hexdigest() + "\n"])

## veritabani2 dizimizi kaydediyoruz
with open("Veritabani2.txt", "w") as veri:
    for x in veritabani2:
        veri.writelines(x)

    ## Saltımızı xor işlemi ixin binarye cevirdik
salt = "9ahd37dn4hd82jdlf753"
xor = ""
for j in salt:
    xor += ''.join(format(ord(j), '08b'))

## Şireleri binarye ceviriyoruz
res = []
for x in splitted:
    dizi = []
    for j in x[1].replace("\n", "")[1:]:
        dizi.append("".join(format(ord(str(j)), '08b')))
    res.append(dizi)

# Şifrelerin 160lı bloklara bölünmüş hali   
passwords_binary = []
for f in res:
    str1 = ""
    for k in f:
        str1 += k
    passwords_binary.append(str1)

## Şifrelere XOR işlemi uyguluyoruz
xor_passes = []

for passw in passwords_binary:
    xorredpass = []
    for i in range(len(passw)):
        if passw[i] == xor[i]:
            xorredpass.append(0)
        else:
            xorredpass.append(1)
    xor_passes.append(xorredpass)

## XOR halinde 160lık bloklar haline getiriyoruz
passwords_160 = []
for xorp in xor_passes:
    str2 = ""
    for binary in xorp:
        str2 += str(binary)
    passwords_160.append(str2)

## Uniqe id + hash haline getiriyoruz
kimlik3 = "BIL008-2020"
veritabani3 = []
for i in range(len(passwords_160)):
    new_uniqe_id = kimlik3 + str(rnd.randint(10000, 99999))
    veritabani3.append([new_uniqe_id, " " + sh.sha512(str(passwords_160[i]).encode('utf - 8')).hexdigest() + "\n"])

## veritabani2 dizimizi kaydediyoruz
with open("Veritabani3.txt", "w") as veri:
    for x in veritabani3:
        veri.writelines(x)

## Random saltımızı oluşturuyoruz
characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
salt = rnd.sample(characters, 20)

xor = ""
for x in salt:
    xor += ''.join(format(ord(x), '08b'))

## Kendi saltımız ile XOR işlemi yapıyoruz 
ownxor_passes = []

for passw in passwords_binary:
    xorredpass = []
    for i in range(len(passw)):
        if passw[i] == xor[i]:
            xorredpass.append(0)
        else:
            xorredpass.append(1)
    ownxor_passes.append(xorredpass)

## XOR halinde 160lık bloklar haline getiriyoruz
new_passwords_160 = []
for xorp in ownxor_passes:
    str2 = ""
    for binary in xorp:
        str2 += str(binary)
    new_passwords_160.append(str2)

## SHA3 işlemi uyguluyoruz
kimlik4 = "BIL008-2020"
veritabani4 = []
for i in range(len(new_passwords_160)):
    new_uniqe_id = kimlik4 + str(rnd.randint(10000, 99999))
    veritabani4.append([new_uniqe_id, " " + sh.sha3_224(str(new_passwords_160[i]).encode('utf-8')).hexdigest() + "\n"])

with open("Veritabani4.txt", "w") as veri:
    for x in veritabani4:
        veri.writelines(x)

## 20 adet salt oluşturuyoruz
salts = []
for i in range(20):
    salts.append(rnd.sample(characters, 20))

## Saltımızı sectik ve binarye cevirdik
salt = rnd.choice(salts)

xor = ""
for x in salt:
    xor += ''.join(format(ord(x), '08b'))

## XOR'luyoruz

xor_passwords = []

for passw in passwords_binary:
    xorredpass = []
    for i in range(len(passw)):
        if passw[i] == xor[i]:
            xorredpass.append(0)
        else:
            xorredpass.append(1)
    xor_passwords.append(xorredpass)

## XOR halinde 160lık bloklar haline getiriyoruz
passwords_160_2 = []
for xorp in xor_passwords:
    str2 = ""
    for binary in xorp:
        str2 += str(binary)
    passwords_160_2.append(str2)
## saltlarımızı string list sekline getiriyoruz
salts_list = []
for salt in salts:
    str3 = ""
    for s in salt:
        str3 += str(s)
    salts_list.append(str3)

## sha3_384 işlemi uyguluyoruz
kimlik5 = "BIL008-2020"
veritabani5 = []
for i in range(len(passwords_160_2)):
    new_uniqe_id = kimlik5 + str(rnd.randint(10000, 99999))
    salt = ""
    if i < 20:
        salt = salts_list[i]
    else:
        salt = ""
    veritabani5.append(
        [new_uniqe_id, " " + sh.sha3_384(str(passwords_160_2[i]).encode('utf-8')).hexdigest(), " " + salt + "\n"])

## Veritabanı5'i kaydediyoruz
with open("Veritabani5.txt", "w") as veri:
    for x in veritabani5:
        veri.writelines(x)