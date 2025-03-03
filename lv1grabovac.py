# 1. Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je plaćen po radnom satu. Koristite ugrađenu
# Python metodu input(). Nakon toga izračunajte koliko je korisnik zaradio i ispišite na ekran. Na kraju prepravite
# rješenje na način da ukupni iznos izračunavate u zasebnoj funkciji naziva total_euro.


# def total_euro(brojSati, satnica):
#     return brojSati * satnica


# 35
# brojSati = float(input("Unesite broj odradjenih sati:"))
# satnica = float(input("Unesite vasu satnicu:"))



# total= total_euro(brojSati, satnica)

# print(f"Zarada: {total} eura")



# 2. Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja nekakvu ocjenu i nalazi se između 0.0 i
# 1.0. Ispišite kojoj kategoriji pripada ocjena na temelju sljedećih uvjeta:
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe). Također, ako je
# broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovarajuću poruku.



# try:
#     n = float(input(" Unesite jedan broj u intervalu 0.0 - 1.0: "))
#     if 0.0 <= n <= 1.0:
  
#      if n<0.6:
#       print("Ocjena F")
#      elif 0.6<= n <0.7:
#       print("Ocjena D")
#      elif 0.7 <= n <0.8:
#       print("Ocjena C")
#      elif 0.8 <= n<0.9 :
#       print("Ocjena B")
#      elif n>=0.9:
#       print("Ocjena A")

#     else: print("Dogodila se greška")
    
# except ValueError:
#  print("Greska")



# 3. Napišite program koji od korisnika zahtijeva unos brojeva u beskonačnoj petlji sve dok korisnik ne upiše „Done“ (bez
# navodnika). Pri tome brojeve spremajte u listu. Nakon toga potrebno je ispisati koliko brojeva je korisnik unio, njihovu
# srednju, minimalnu i maksimalnu vrijednost. Sortirajte listu i ispišite je na ekran.
# Dodatno: osigurajte program od pogrešnog unosa (npr. slovo umjesto brojke) na način da program zanemari taj unos i
# ispiše odgovarajuću poruku.



# brojevi = []

# while True:
#     unos = input("Unesite broj (ili 'Done' za kraj): ")
    
#     if unos.lower() == "done":
#         break

#     try:
#         broj = float(unos)
#         brojevi.append(broj)

#     except ValueError:
#         print("Greška: unesite ispravan broj")

# if brojevi:
#         print(f"Ukupno unesenih brojeva: {len(brojevi)} ")
#         print(f"Srednja vrijednost: {sum(brojevi)/ len(brojevi)}")
#         print(f"Minimalna vrijednost: {min(brojevi)}")
#         print(f"Maksimalna vrijednost: {max(brojevi)}")

#         brojevi.sort()
#         print("Sortirana lista:", brojevi)
# else:
#      print("Niste unijeli nijedan broj")



# 4. Napišite program koji od korisnika zahtijeva unos imena tekstualne datoteke. Program nakon toga treba tražiti linije
# oblika:
# Primijenjeno strojno učenje – laboratorijske vježbe – VJEŽBA 1 7
# X-DSPAM-Confidence: <neki_broj>
# koje predstavljaju pouzdanost korištenog spam filtra. Potrebno je izračunati srednju vrijednost pouzdanosti. Koristite
# datoteke mbox.txt i mbox-short.txt
# Primjer
# Ime datoteke: mbox.txt
# Average X-DSPAM-Confidence: 0.894128046745
# Ime datoteke: mbox-short.txt
# Average X-DSPAM-Confidence: 0.750718518519



# def izracunaj_pouzdanost(datoteka):
#     try:
#         with open(datoteka, 'r') as file:
#             linije = file.readlines()
        
        
#         pouzdanosti = []
        
#         for linija in linije:
#             if linija.startswith("X-DSPAM-Confidence:"):
#                 try:
                    
#                     broj = float(linija.split(':')[1].strip())
#                     pouzdanosti.append(broj)
#                 except ValueError:
#                     continue 
        
      
#         if pouzdanosti:
#             srednja_pouzdanost = sum(pouzdanosti) / len(pouzdanosti)
#             return srednja_pouzdanost
#         else:
#             return None

#     except FileNotFoundError:
#         print(f"Datoteka {datoteka} nije pronađena.")
#         return None



# ime_datoteke = input("Ime datoteke: ")

# srednja_pouzdanost = izracunaj_pouzdanost(ime_datoteke)

# if srednja_pouzdanost is not None:
#     print(f"Average X-DSPAM-Confidence: {srednja_pouzdanost}")
# else:
#     print("Nema dostupnih podataka za izračunavanje.")



# 5. Napišite Python skriptu koja će učitati tekstualnu datoteku naziva song.txt. Potrebno je napraviti rječnik koji kao
# ključeve koristi sve različite riječi koje se pojavljuju u datoteci, dok su vrijednosti jednake broju puta koliko se svaka
# riječ (ključ) pojavljuje u datoteci. Koliko je riječi koje se pojavljuju samo jednom u datoteci? Ispišite ih.


