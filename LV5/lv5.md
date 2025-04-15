1. a) Na dijagramu raspršenja mogli bismo primijetiti obrasce u podacima, poput međusobne povezanosti između mjerenja temperature i CO2, te razdvojenost između klase 0 (prazna prostorija) i klase 1 (zauzeta prostorija). Također, moguće je da će podaci za različite klase biti grupirani u različite dijelove dijagrama, dok će se preklapanje između njih smanjiti, ovisno o kvaliteti i jasnosti podataka.

b) Broj podatkovnih primjera iz csv datoteke može se dobiti analizom broja redaka u datoteci. Pretpostavljam da skup podataka sadrži nekoliko stotina do tisuća redaka, s obzirom na to da se podaci prikupljaju tijekom 4 dana.

c) Razdioba podatkovnih primjera po klasama može biti neuravnotežena, jer bi u realnim uvjetima prostorija mogla biti često prazna, a zauzeta rjeđe. Ako su podaci neuravnoteženi, može biti korisno primijeniti tehnike poput naduzorkovanja manjinske klase ili balansiranja kroz ponderiranje prilikom treniranja modela.

2. e) Veći broj susjeda može smanjiti osjetljivost modela na šum i prenaučenost, ali može dovesti do podmodeliranja, jer će model postati previše generaliziran.
   Manji broj susjeda može dovesti do previše osjetljivih predviđanja koja će biti podložna šumu, tj. model može previše pratiti specifične značajke podataka.

f) Bez skaliranja, atributi s većim rasponima (npr. CO2, ako su mjerenja u većim vrijednostima) mogu dominirati u računu udaljenosti između točaka, što može negativno utjecati na performanse modela, budući da K-NN algoritam koristi udaljenost između primjera kao ključnu metriku.

3. b) Manja dubina stabla može dovesti do podmodeliranja, jer stablo neće imati dovoljno grananja za pravilnu klasifikaciju.
   Veća dubina može dovesti do prenaučenosti, jer će stablo previše prilagoditi trenirane podatke, a time gubi sposobnost generalizacije na nepoznate podatke.

c) Bez skaliranja, atributi s različitim mjerama skale mogu negativno utjecati na način na koji stablo odlučivanja donosi odluke. Iako stablo odlučivanja nije toliko osjetljivo na skaliranje kao neki drugi algoritmi, i dalje može postojati manja osjetljivost na razlike u veličinama atributa.

4. Logistička regresija može imati slične rezultate kao K-NN ili stablo odlučivanja, no s obzirom na prirodu problema, može biti podložna problemima s neravnotežom klasa. Ako su podaci neuravnoteženi, to može utjecati na performanse, jer će model preferirati većinsku klasu. S obzirom na to, moguće je da će model imati slabiju preciznost u prepoznavanju manjinske klase (zauzeta prostorija). Korištenje regularizacije i balansiranje podataka može pomoći u poboljšanju rezultata.
