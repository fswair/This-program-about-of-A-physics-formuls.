# basic physics formuls
# hız formülü
# v=hız x=yol t=zaman

a = "*"
print(a*15)

x = float(input("Yol değerini giriniz..:"))
t = float(input("Zaman değerini giriniz..:"))

def hizHesapla(ax,at):
    v = x / t
    print("Sorunun cevabı & Hız değeri..:",v,"V")

hizHesapla(x,t)
print(a*15)

v = float(input("Hız değerini giriniz..:"))
t = float(input("Zaman değerini giriniz..:"))

def yolHesapla(ax,at):
    x = v * t
    print("Sorunun cevabı & Yol değeri..:",x,"X")

yolHesapla(v,t)

print(a*15)
x = float(input("Yol değerini giriniz..:"))
v = float(input("Hız değerini giriniz..:"))

def zamanHesapla(ax,at):
    t = x / v
    print("Sorunun cevabı & Zaman değeri..:",t,"T")

zamanHesapla(x,v)

print(a*15)
print("\n")
print(a*15)

# basic physics formuls
# ivme formülü
# a = v / t


vx = float(input("Hız Değişimi değerini giriniz..:"))
tx = float(input("Zaman değerini giriniz..:"))

def ivmeAl(y,z):
    a = vx / tx

    print("Sorunun cevabı & İvme değeri..:",a,"A")

ivmeAl(vx,tx)
a = vx / tx

print(a*15)

a = float(input("İvme değerini giriniz..:"))
tx = float(input("Zaman değerini giriniz..:"))

def hizdegisimAl(y,z):
    vx = tx * a

    print("Sorunun cevabı & Hiz değişim değeri..:",vx,"V")

hizdegisimAl(vx,tx)
