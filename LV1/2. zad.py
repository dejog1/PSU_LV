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
