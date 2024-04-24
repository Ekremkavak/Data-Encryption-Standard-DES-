ilk_permutasyon = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]
pc1_tablosu = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
]
expansionbit = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]
pc2_tablosu = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

son_permutasyon = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

anahtar_kaydirma = [1,1,2,2,
                    2,2,2,2,
                    1,2,2,2,
                    2,2,2,1]

s_boxes = [
    # S-box 1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S-box 2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S-box 3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S-box 4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S-box 5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S-box 6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S-box 7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S-box 8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

box_permutasyon_tablosu = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

def bloklara_ayir(text): # uzun girilen metinler için 64 bitlik bloklara bölmemiz lazım
    blocks = []
    for i in range(0,len(text),8):
        block = text[i:i+8]
        blocks.append(block)
    return blocks

def str_to_binary(string_text):

    #String metni binarye çevirmemiz lazım
    binary_metin = ""
    for char in string_text:
        # ASCİ de karşılık değerini alıp ikilik sisteme dönüştürüyorum
        binary_char = format(ord(char),"08b") #Unicode dönüşümünü yapıp ikilik sistemde çevirdim
        binary_metin += binary_char
        binary_metin = binary_metin[:64]

    binary_metin = binary_metin[:64].ljust(64,'0') # burada binary metnimi 64 bite tamamlamaya çalıştım
    return binary_metin

def binary_to_str(binary_text):
    string_metin = ""
    for i in range(0,len(binary_text),8): # binary diziyi 8 bitlik parçalara ayırdım
        byte = binary_text[i:i+8] # 8 bitlik parçalar
        decimal_deger = int(byte,2) # binary değeri ondalık sayıya çevirdim
        char = chr(decimal_deger) # asci deki harf karşılıklarını aldım
        string_metin += char
    return string_metin

def ilk_permutasyon_islemi(binary_metin):
    ilk_p_sonuc = [None] * 64

    for i in range(64):
        ilk_p_sonuc[i] = binary_metin[ilk_permutasyon[i] - 1] # ilk permütasyon işlemimi yapıyorum

    ilk_p_sonuc_str = "".join(ilk_p_sonuc)

    return ilk_p_sonuc_str

def anatar_to_binary():
    orjinal_anahtar = "ekremkav" # her zaman 8 karakter olmalıdır
    binary_anahtar = ""

    for char in orjinal_anahtar:
        anahtar = format(ord(char), "08b") # anahtarı binary değerlere dönüştürüyorum
        binary_anahtar += anahtar

    return binary_anahtar

def round_anahtar_uretme():
    # anahtarı binary e çevirdim
    binary_anahtar = anatar_to_binary()
    pc1_anahtar_str = "".join(binary_anahtar[bit - 1] for  bit in pc1_tablosu) # pc1 permütasyonu

   # 56 bit anahtarı 28 bite ayırma
    c0 = pc1_anahtar_str[:28]
    d0 = pc1_anahtar_str[28:]
    round_anahtarlari = []
    for round_sayisi in range(16):
        c0 = c0[anahtar_kaydirma[round_sayisi]:] + c0[:anahtar_kaydirma[round_sayisi]]
        d0 = d0[anahtar_kaydirma[round_sayisi]:] + d0[:anahtar_kaydirma[round_sayisi]]
        # her raunda belirlenen değerlere göre kaydırma yapıldı

        cd_birlestirme = c0 + d0 # anahtarları birleştirdim

        round_anahtari = "".join(cd_birlestirme[bit - 1 ] for bit in pc2_tablosu) # pc2 permütasyonu
        round_anahtarlari.append(round_anahtari)

    return round_anahtarlari

def sifreleme(blok):
    binary_text = blok
    round_anahtarlari = round_anahtar_uretme() # round keyleri tanımladım

    ilk_perm_sonuc = ilk_permutasyon_islemi(binary_text)

    # blokları 2 gruba ayırıyorum
    Li = ilk_perm_sonuc[:32]
    Ri = ilk_perm_sonuc[32:]

    for round_sayisi in range(16):
        # expansion kısmı ayırdığım 32 biti 48 bite çeviriyorum
        exp_sonuc = [Ri[i - 1] for i in expansionbit]
        #sonucu daha iyi görünmesi için stringe geri çeviriyorum
        exp_sonuc_str = "".join(exp_sonuc)
        roun_anahtari = round_anahtarlari[round_sayisi] # hangi roundaa olduğumuzu öğrenmek için

        xor_sonucu = ""
        #tek tek xor lama işlemini yapıyorum
        for i in range(48):
            xor_sonucu += str(int(exp_sonuc_str[i]) ^ int(roun_anahtari[i]))
        # 48 biti 8 bitlik 6 gruba ayırıyorum
        alti_bitlik_gruplar = [xor_sonucu[i:i+6] for i in range(0,48,6)]

        #substation bit dizim
        s_box_substation = ""

        # her 6 bitlik grup için substation yapıyorum
        for i in range(8):
            sira_bitleri = int(alti_bitlik_gruplar[i][0] + alti_bitlik_gruplar[i][-1],2)
            #1. ve 6. endeksteki bitleri bulup decimal sira bitini elde ettim
            sutun_bitleri = int(alti_bitlik_gruplar[i][1:-1],2)
            #2. 3. 4. 5. bitleri decimal şekilde sutun bitine aktardım

            # Sboxta karşılık gelen değeri buluyorum
            s_box_degeri = s_boxes[i][sira_bitleri][sutun_bitleri]

            # sbox degerini 4 bitlik binary degere dönüstürüüyorum
            s_box_substation += format(s_box_degeri, "04b")

        box_permutasyon_sonuc = [s_box_substation[i - 1] for i in box_permutasyon_tablosu]

        #xor operasyonu için Li yi listeye çevirdim
        Li_list = list(Li)

        # sboxtantan gelen sonuc ri ile li yi xorluoyrum
        yeni_Ri = [str(int(Li_list[i]) ^ int(box_permutasyon_sonuc[i])) for i in range(32) ]

        yeni_Ri_str = "".join(yeni_Ri)

        # artık sonuçları birbirine aktarıyorum
        Li = Ri
        Ri = yeni_Ri_str

    # ikisini birleştiriyorum
    sonuc = Ri + Li

    # son permütasyonu uyguluyorum
    son_sifreleme = [sonuc[son_permutasyon[i] - 1] for i in range(64)]

    son_sifreleme_str = "".join(son_sifreleme)

    sifre = binary_to_str(son_sifreleme_str)
    return sifre

def desifreleme(blok):

    round_anahtarlari = round_anahtar_uretme() # round keyleri tanımladım

    ilk_perm_sonuc = ilk_permutasyon_islemi(blok)



    # blokları 2 gruba ayırıyorum
    Li = ilk_perm_sonuc[:32]
    Ri = ilk_perm_sonuc[32:]

    for round_sayisi in range(16):
        # expansion kısmı ayırdığım 32 biti 48 bite çeviriyorum
        exp_sonuc = [Ri[i - 1] for i in expansionbit]
        #sonucu daha iyi görünmesi için stringe geri çeviriyorum
        exp_sonuc_str = "".join(exp_sonuc)
        roun_anahtari = round_anahtarlari[15 - round_sayisi] # hangi roundaa olduğumuzu öğrenmek için

        xor_sonucu = ""
        #tek tek xor lama işlemini yapıyorum
        for i in range(48):
            xor_sonucu += str(int(exp_sonuc_str[i]) ^ int(roun_anahtari[i]))

        # 48 biti 8 bitlik 6 gruba ayırıyorum
        alti_bitlik_gruplar = [xor_sonucu[i:i+6] for i in range(0,48,6)]

        #substation bit dizim
        s_box_substation = ""

        # her 6 bitlik grup için substation yapıyorum
        for i in range(8):
            sira_bitleri = int(alti_bitlik_gruplar[i][0] + alti_bitlik_gruplar[i][-1],2)
            #1. ve 6. endeksteki bitleri bulup decimal sira bitini elde ettim
            sutun_bitleri = int(alti_bitlik_gruplar[i][1:-1],2)
            #2. 3. 4. 5. bitleri decimal şekilde sutun bitine aktardım

            # Sboxta karşılık gelen değeri buluyorum
            s_box_degeri = s_boxes[i][sira_bitleri][sutun_bitleri]

            # sbox degerini 4 bitlik binary degere dönüstürüüyorum
            s_box_substation += format(s_box_degeri, "04b")

        box_permutasyon_sonuc = [s_box_substation[i - 1] for i in box_permutasyon_tablosu]
        box_permutasyon_sonuc_str = "".join(box_permutasyon_sonuc)


        #xor operasyonu için Li yi listeye çevirdim

        Li_list = list(Li)

        # sboxtantan gelen sonuc ri ile li yi xorluoyrum
        yeni_Ri = [str(int(Li_list[i]) ^ int(box_permutasyon_sonuc[i])) for i in range(32) ]

        yeni_Ri_str = "".join(yeni_Ri)

        # artık sonuçları birbirine aktarıyorum
        Li = Ri
        Ri = yeni_Ri_str

    # ikisini birleştiriyorum
    sonuc = Ri + Li

    # son permütasyonu uyguluyorum

    son_desifreleme = [sonuc[son_permutasyon[i] - 1] for i in range(64)]

    son_sifreleme_str = "".join(son_desifreleme)
    temizlenmis_son_sifre = gereksiz_sifir_sil(son_sifreleme_str)
    sifre = binary_to_str(temizlenmis_son_sifre)
    return sifre

def veriyi_sil():
        global sifrelenecek_binary_metin
        global sifrelenmis_metin
        global desifrelenmis_metin
        global sifrelenecek_text
        global desifrelenmis_metin_str
        global sifrelenmis_metin_tek
        sifrelenecek_text = ""
        desifrelenmis_metin_str = ""
        sifrelenmis_metin_tek = ""
        sifrelenmis_metin = []
        sifrelenecek_binary_metin = []
        desifrelenmis_metin = []
def gereksiz_sifir_sil(text):   # burada 64 bite tamamlamak için 0  eklediğim son blokta gereksiz sıfırları temizledim
    parcalar = [text[i:i+8] for i in range(0, len(text),8)]
    temizlenmis_parcalar = [parca for parca in parcalar if parca != "00000000"]

    temizlenmis_metin = "".join(temizlenmis_parcalar)
    return temizlenmis_metin
def main():
    global sifrelenecek_binary_metin
    global sifrelenmis_metin
    global desifrelenmis_metin
    global sifrelenecek_text
    global desifrelenmis_metin_str
    global sifrelenmis_metin_tek
    veriyi_sil()
    print("Şifrelenecek metin girin(!!! türkçe karakteer kullanmayın bozuluyor!!!)")
    sifrelenecek_text = input("çıkış için "+""+"(Exit) : "+""+"")
    if sifrelenecek_text == "Exit":
        exit()
    bloklar = bloklara_ayir(sifrelenecek_text)
    for blok in bloklar:
        sifrelenecek_binary_metin.append(str_to_binary(blok))
    for i in sifrelenecek_binary_metin:
       sifrelenmis_metin.append(sifreleme(i))
    sifrelenmis_metin_tek = "".join(sifrelenmis_metin)
    print("Şifrelenmiş metin: ",sifrelenmis_metin_tek)

    for i in sifrelenmis_metin:
        desifrelenmis_metin.append(desifreleme(str_to_binary(i)))
    desifrelenmis_metin_str = "".join(desifrelenmis_metin)

    print("Deşifrelenmiş metin: ", desifrelenmis_metin_str)
    veriyi_sil()
    while sifrelenecek_text != "Exit":
        veriyi_sil()
        print("Şifrelenecek metin girin(!!! türkçe karakteer kullanmayın bozuluyor!!!)")
        sifrelenecek_text = input("çıkış için " + "" + "(Exit) : " + "" + "")
        if sifrelenecek_text == "Exit":
            exit()
        bloklar = bloklara_ayir(sifrelenecek_text)
        for blok in bloklar:
            sifrelenecek_binary_metin.append(str_to_binary(blok))
        for i in sifrelenecek_binary_metin:
            sifrelenmis_metin.append(sifreleme(i))
        sifrelenmis_metin_tek = "".join(sifrelenmis_metin)
        print("Şifrelenmiş metin: ", sifrelenmis_metin_tek)
        for i in sifrelenmis_metin:
            desifrelenmis_metin.append(desifreleme(str_to_binary(i)))
        desifrelenmis_metin_str = "".join(desifrelenmis_metin)
        print("Deşifrelenmiş metin: ", desifrelenmis_metin_str)

if __name__ == '__main__':
    main()