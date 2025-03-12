import numpy as np
import matplotlib.pyplot as plt

# a = np.array([6, 2, 9]) #napravi polje od tri elementa
# print(type(a)) #prikaži tip polja
# print(a.shape) #koliko elemenata ima vektor
# print(a[0], a[1], a[2]) #prikaži prvi, drugi i treći element
# a[1] = 5 #promijeni vrijednost polja na drugom mjestu
# print(a) #prikaži cijeli a
# print(a[1:2]) #izdvajanje
# print(a[1:-1]) #izdvajanje

# b = np.array([[3,7,1],[4,5,6]]) #napravi 2 dimenzionalno polje (matricu)
# print(b.shape) #ispiši dimenzije polja
# print(b) #ispiši cijelo polje b

# print(b[0, 2], b[0, 1], b[1, 1]) #ispiši neke elemente polja
# print(b[0:2,0:1]) #izdvajanje
# print(b[:,0]) #izdvajanje

# c = np.zeros((4,2)) #polje sa svim elementima jednakim 0
# d = np.ones((3,2)) #polje sa svim elementima jednakim 1
# e = np.full((1,2),5) #polje sa svim elementima jednakim 5


# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(0, 6, num=30)
# y= np.sin(x)
# plt.plot(x, y, 'b', linewidth=1, marker=".", markersize=5)
# plt.axis([0,6,-2,2])
# plt.xlabel('x')
# plt.ylabel('vrijednosti funkcije')
# plt.title('sinus funkcija')
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# img = plt.imread("tiger.png")
# img = img[:,:,0].copy()
# print(img.shape)
# print(img.dtype)
# plt.figure()
# plt.imshow(img, cmap="gray")
# plt.show()

#prvi zadatak
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array([1,2,3,3,1])
# y = np.array([1,2,2,1,1])

# plt.plot(x, y, 'g--', linewidth=5, marker=".", markersize=20)
# plt.axis([0,4,0,4])
# plt.xlabel('x')
# plt.ylabel('vrijednosti funkcije')
# plt.title('sinus funkcija')
# plt.show()



#drugi zadatak
# data = np.loadtxt(open("C:\\Users\\student\\Desktop\\lv2grabovac\\mtcars.csv", "rb"), usecols=(1, 2, 3, 4, 5, 6),
#                   delimiter=",", skiprows=1)


# print("min mpg: ", min(data[:, 0]))
# print("max mpg: ", max(data[:, 0]))
# print("avg mpg: ", sum(data[:, 0])/len(data[:, 0]))

# arr = data[:, 1] == 6


# plt.scatter(data[:, 0], data[:, 3], c='lime',
#             ec='k', s=data[:, 5]*16, marker="h")

# for i, label in enumerate(data[:, 5]):
#     plt.text(data[i, 0], data[i, 3]+5, str(data[i, 5]))


# print("min mpg sa 6 cyl: ", min(data[arr, 0]))
# print("max mpg sa 6 cyl: ", max(data[arr, 0]))
# print("avg mpg sa 6 cyl: ", sum(data[arr, 0])/len(data[arr, 0]))

# plt.show()



#treci zadatak

# img = plt.imread("C:\\Users\\student\\Desktop\\lv2grabovac\\tiger.png")
# img = img[:, :, 0].copy()

# img_array = []

# img_array = img + 0.6
# img_array[img_array > 1] = 1

# img1 = np.rot90(img, 3) 

# img2 = np.fliplr(img)  

# img3 = img[::5, ::5] 

# redovi = img.shape[0]  
# stupci = img.shape[1]  
# dg = stupci // 4
# gg = stupci // 2

# pr_img = img.copy()
# for i in range(redovi):
#     for j in range(stupci):
#         if (j < dg or j > gg):
#             pr_img[i][j] = 0

# plt.figure(1)
# plt.title("brightness")
# plt.imshow(img_array, cmap='gray')
# plt.figure(2)
# plt.title("rotirana slika")
# plt.imshow(img1, cmap='gray')
# plt.figure(3)
# plt.title("zrcaljena slika")
# plt.imshow(img2, cmap='gray')
# plt.figure(4)
# plt.title(" smanjena kvaliteta slike")
# plt.imshow(img3, cmap='gray')
# plt.figure(5)
# plt.title(" stupci")
# plt.imshow(pr_img, cmap='gray')
# plt.show()


#cetvrti zadatak


def check(kvadrat, redovi, stupci):
    crne = np.zeros((kvadrat, kvadrat))
    bijele = np.ones((kvadrat, kvadrat)) * 255
    red1 = np.hstack([crne, bijele] * (stupci // 2))
    if stupci % 2 != 0:
        red1 = np.hstack([red1, crne])

    red2 = np.hstack([bijele, crne] * (stupci // 2))
    if stupci % 2 != 0:
        red2 = np.hstack([red2, bijele])

    polje = np.vstack([red1, red2] * (redovi // 2))
    if redovi % 2 != 0:
        polje = np.vstack([polje, red1])
    return polje


img = check(100, 4, 5)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()