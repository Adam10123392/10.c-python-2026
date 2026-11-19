szo = 'Ez egy szó'

lista = ["alma", "körte", "banán", "narancs", "mandarin", "citrom", "lime", "grapefruit", "szőlő", "eper", "málna", "szeder", "áfonya", "cseresznye", "meggy", "barack", "nektarin", "szilva", "görögdinnye", "sárgadinnye", "ananász", "mangó", "kivi", "papaya", "gránátalma", "füge", "datolyaszilva", "kókuszdió", "avokádó", "maracuja", "paradicsom", "paprika", "uborka", "sárgarépa", "petrezselyemgyökér", "burgonya", "édesburgonya", "vöröshagyma", "fokhagyma", "lilahagyma", "káposzta", "kelkáposzta", "karfiol", "brokkoli", "cukkini", "padlizsán", "retek", "cékla", "spenót", "saláta", "zöldborsó", "zöldbab", "kukorica", "sütőtök", "zeller", "póréhagyma", "spárga", "articsóka", "kelbimbó", "mángold", "édeskömény", "paszternák", "torma", "karalábé", "csicsóka", "endívia", "rukola", "madársaláta", "vízitorma", "chili", "okrá", "patisszon", "rebarbara", "birsalma", "naspolya", "ribizli", "egres", "som", "kajszi", "kaki", "licsi", "guava", "pomelo", "kumkvat", "sárkánygyümölcs", "csillaggyümölcs", "jackfruit", "durian", "longán", "csipkebogyó", "bodza", "áfonya", "fehérrépa", "vajretek", "fekete retek", "paszternák", "pak choi", "jégsaláta"

]

print("lista, sep''")

#validálás

print(f"A lista hossza: {len(lista)}\nA lista utlsó eleme: {lista[-1]}\nA lista első eleme: {lista[0]}\n")

#for elem in lista:
    #print(elem)

s_lista = []
for elem in lista:
    if elem[0] == "s" and elem[1] != "z":
        s_lista.append(elem)

print("s_lista,sep=' - 'end=' - s-sel kezdődő gyümölcsök")

print("\n5 vagy kevesebb betűből álló szavak")
ot_vagy_kevesebb = []
for elem in lista:
    if len(elem) <=5:
        ot_vagy_kevesebb.append(elem)

print("ot_vagy_kevesebb,sep=','")