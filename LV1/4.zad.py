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
