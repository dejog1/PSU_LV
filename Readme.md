Zadatak 1 Nadgledno učenje ili regresija: 
linearModel = lm.LinearRegression() linearModel.fit(xtrain, ytrain) ytest_p = linearModel.predict(xtest) MSE_test = mean_squared_error(ytest, ytest_p)
Razrada linearnog modela za regresiju odvija se u sljedećim dijelovima: 
Inicijalizacija modela: linearModel = lm.LinearRegression() 
Treniranje modela: linearModel.fit(xtrain, ytrain) 
Predviđanje na testnom skupu podataka: ytest_p = linearModel.predict(xtest) 
Evaluacija modela: MSE_test = mean_squared_error(ytest, ytest_p)

Evaluacija modela odvija se u sljedećem dijelu koda: MSE_test = mean_squared_error(ytest, ytest_p)

Scikit-learn biblioteka (sklearn) se koristi na nekoliko mjesta: 
Inicijalizacija linearnog regresijskog modela: linearModel = lm.LinearRegression()
Izračun srednje-kvadratne pogreške: MSE_test = mean_squared_error(ytest, ytest_p)

Zadatak 2 Razlika rezultata iz zadatka 1 (u kojem nisu prošireni polinomijalnim članovima) i iz zadatka 2 može biti velika.
Naime, model u 2. zadatku ima mogućnost bolje prilagodbe složenim podacima, ali postoji i određeni rizik od prenaučenosti zbog visokog stupnja polinoma.

Zadatak 4 U datasetu je dostupno 4843 mjerenja. 
Tipovi pojedinih stupaca u dataframe-u su: 
name: string (ime automobila)
year: integer (godina proizvodnje automobila) 
selling_price: float (logaritam cijene u indijskim rupijama) 
km_driven: integer (prijeđeni broj kilometara) 
fuel: string (tip motora: Diesel, Petrol, CNG, LPG) 
seller_type: string (prodavač: individual/dealer) 
transmission: string (tip mjenjača: automatic/manual) 
owner: integer (broj prethodnih vlasnika) 
mileage: float (potrošnja automobila)
engine: integer (zapremnina motora u cm3) 
max_power: float (maksimalna snaga motora u bhp) 
seats: integer (broj sjedala) 
Automobil s najvećom cijenom je onaj koji se prodaje po cijeni koja se nalazi u datasetu, a automobil s najmanjom cijenom je onaj koji se prodaje po najmanjoj cijeni u datasetu.

Zadatak 5 Promjena broja ulaznih veličina može imati različit utjecaj na pogrešku modela na testnom skupu: 
1. Dodavanje relevantnih značajki 
2. Dodavanje nepotrebnih značajki 
3. Uklanjanje relevantnih značajki 
4. Smanjenje broja značajki



