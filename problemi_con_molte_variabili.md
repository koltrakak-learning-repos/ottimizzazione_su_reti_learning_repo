la formulazione del VCP con stable set ha tante variabili (proporzionale al numero di stable set)

# Come gestiamo tante variabili?

passiamo per il duale e gestiamo come prime i tanti vincoli

schema di column generation, duale dello schema di row generation che abbiamo già visto

- nuovamente la garanzia è che il metodo converge con poche iterazioni (serve aggiungere poche colonne)
- come prima risolviamo tanti piccoli LP rispetto ad un LP enorme

generare un vincolo violato nel duale, corrisponde a **generare nel primale una variabile con costo ridotto negativo**

- questo è quello che fa l'algoritmo del simplesso ad ogni iterazione: definisce la nuova base aggiungendo la colonna con costo ridotto negativo

NB: stavolta interrompere un algoritmo column generation è sbagliato dato che ottengo un lower bound che non è un vero lower bound

- per avere la certezza della validità del lower bound di un algoritmo di column generation devo arrivare in fondo e NON posso interrompere a metà (come invece potevo fare per algoritmo row generation)

column generation + b&b viene chiamato branch and price
