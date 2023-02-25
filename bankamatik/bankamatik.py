from re import A


isim=input('Isim giriniz:')
hesapNo=1903
print('Merhaba,'+ isim)
bakiye=int(23755)
ekhesap=int(10000)
ct=int(input('cekmek isteginiz tutar:'))

if int(bakiye)>=int(ct):
    print('Paranizi cekebilirsiniz.')
else:
    ek=input('Ek hesap kullanmak ister misiniz?   (e/h)')
    if ek=='e':
        toplam= int(ekhesap)+int(bakiye)
        a= ct-bakiye
        b=ekhesap-a
        print(str(a)+ ' lira ek hesaptan cekildi.')
        print(str(b)+' lira ekhesapta kaldi.')
    else:
        print('Yetersiz bakiye.')
    if toplam>=ct:
        print('Paranizi cekebilirsiniz')
    else:
        print('Yetersiz bakiye')
