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
