1.
import pandas as pd
import numpy as np

mtcars = pd.read_csv('mtcars.csv')


max_potrosnja=mtcars.sort_values(by="mpg",ascending=False).head(5)
print(max_potrosnja)

trojka=mtcars[mtcars.cyl ==8].sort_values(by="mpg",ascending=False).head(3)
print(trojka)


sestak= mtcars[mtcars['cyl'] ==6]['mpg'].mean()
print(sestak)


cetiri=mtcars[(mtcars['cyl']==4) & (mtcars['wt']>= 2.000) & (mtcars['wt'] <= 2.200)]
print(cetiri["mpg"].mean()) 


mjenjac=mtcars[(mtcars['am']==1)]
print("broj automatika:", mjenjac.shape[0])

mjenjac=mtcars[(mtcars['am']==0)]
print("broj manualaca:", mjenjac.shape[0])


mjenjac=mtcars[(mtcars['am']==1) & (mtcars['hp']>100)]
print(mjenjac.shape[0])


masa=mtcars['wt']
print(round(masa*1000/2.2 ),2)







2.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


mtcars = pd.read_csv('mtcars.csv')


mtcars['cyl'] = mtcars['cyl'].astype('category')


mtcars['am'] = mtcars['am'].astype('category')


plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
sns.barplot(x='cyl', y='mpg', data=mtcars, ci=None)
plt.title("Potrošnja automobila s 4, 6 i 8 cilindara")
plt.xlabel("Broj cilindara")
plt.ylabel("Miles per gallon (MPG)")


plt.subplot(2, 2, 2)
sns.boxplot(x='cyl', y='wt', data=mtcars)
plt.title("Distribucija težine automobila s 4, 6 i 8 cilindara")
plt.xlabel("Broj cilindara")
plt.ylabel("Težina (1000 lbs)")


plt.subplot(2, 2, 3)
sns.barplot(x='am', y='mpg', data=mtcars, ci=None)
plt.title("Potrošnja automobila s ručnim vs automatskim mjenjačem")
plt.xlabel("Vrsta mjenjača (0=Automatski, 1=Ručni)")
plt.ylabel("Miles per gallon (MPG)")


plt.subplot(2, 2, 4)
sns.scatterplot(x='qsec', y='hp', hue='am', style='am', data=mtcars)
plt.title("Odnos ubrzanja i snage automobila")
plt.xlabel("Ubrzanje (1/4 milje, sekunde)")
plt.ylabel("Snaga (HP)")


plt.tight_layout()
plt.show()



3.
import requests
import pandas as pd
from datetime import datetime


def get_air_quality_data(year, city):
    url = f"http://iszz.azo.hr/iskzl/rest/ispitivanjapodataka/getAll?p_godina={year}&p_grad={city}&_={int(datetime.now().timestamp())}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['items']
    else:
        print("Greška pri dohvaćanju podataka.")
        return None


data = get_air_quality_data(2017, "Osijek")

if data:
   
    df = pd.DataFrame(data)
    
    
    df['Datum'] = pd.to_datetime(df['Datum'])

    
    pm10_osijek_2017 = df[(df['Datum'].dt.year == 2017) & (df['Grad'] == 'Osijek') & (df['Parameter'] == 'PM10')]
    print("Mjerenja dnevne koncentracije lebdećih čestica PM10 za 2017. godinu za grad Osijek:")
    print(pm10_osijek_2017)


    top_3_dates = pm10_osijek_2017.nlargest(3, 'Vrijednost')['Datum']
    print("\nTri datuma u 2017. godini kada je koncentracija PM10 bila najveća:")
    print(top_3_dates)
