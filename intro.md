# ripasso

molto importante: le matrici hanno M righe (vincoli) ed N colonne (variabili)

interessante: se trovo due soluzioni ottime, ed una in realtà mi piace di più dell'altra, allora significa che il nostro modello non è stato in grado di catturare la differenza tra le due soluzioni.

- può andarmi bene così oppure bisogna cambiare il modello e raffinarlo

altra cosa interessante: trasformare il problema in forma standard fa crescere la dimensione di quest'ultimo (aumentano il numero di vincoli e variabili)

perchè è importante il duale?

- utile per dimostrare l'ottimalità di una soluzione
- se si vuole risolvere un problema con un numero esponenziale di vincoli esistono techiche per risolverlo. Tuttavia, la stessa cosa non è vera per un problema con un numero esponenziale di variabili
- in questo caso, si può passare dal duale, trasformando il numero esponenziale di variabili in altrettanti vincoli, riconducendosi ad un caso noto

Queand'è che non è immediato sapere che una soluzione è ottima?

- in programmazione lineare è facile, basta usare criterio di ottimalità
- in questo corso non si passa sempre per un modello come quello del tableau; in questo caso si utilizzano altre techine come la dualità

super interessante l'origine del concetto della dualità: rilassamento lagrangiano

- se il problema di ottimizzazione non è vincolato, basta studiare dove la derivata si annulla
- sarebbe bello ricondursi a questo caso
- possiamo allora spostare i vincoli nella funzione obiettivo aggiungendo dei pesi che peggiorano la mia funzione obiettivo nelle posizioni non ammissibili, e la migliorano nelle posizioni ammissibili

complementary slackness mi dice una cosa super semplice:

- una coppia di soluzioni primale-duale è ottima se e solo se la violazione del vincolo duale/primale moltiplicata per la corrispondente variabile primale/duale vale 0 per ogni i/j
- molto utile per dimostrare l'ottimalità di una soluzione

unimodularità in questo corso è utile

- problemi con matrice dei vincoli totalmente unimodulare hanno soluzione ottima dell'ILP == a quella del rilassamento, e quindi basta risolvere il rilassamento

algoritmi pseudopolinomiali:

- se mi limito a rappresentare dati da 8bit allora KP-DP è polinomiale
- ma se arriva uno con una capacità c più grande di 8 bit il mio algoritmo non funziona

### parte sui grafi

...

terminologia

- multigrafi non aggiungono tanto e quindi gli ignoriamo

- la differenza tra lati e archi non deve confondere per quanto riguarda l'essere un multigrafo o meno

- abbiamo anche il concetto di gamma(v) oltre che a delta(v), in cui consideriamo i vertici e non i lati

- un cammino è una sequenza di **LATI/ARCHI**, non di vertici
- un cammino **NON ha ripetizioni di vertici**

Un cammino con delle ripetizioni di vertici viene detto catena (?)

**IMPORTANTE**
con n si intende il numero di vertici di un grafo
con m si intende il numero di lati

- 𝑁 +(𝑣) = { 𝑢 ∈ 𝑉 : (𝑣 , 𝑢) ∈ A } i successori di 𝑣
  - (vertici raggiungibili da 𝑣 con un arco uscente).

- 𝑁 −(𝑣) = { 𝑢 ∈ 𝑉 : (𝑢 , 𝑣) ∈ A } i predecessori di 𝑣
  - (vertici che hanno un arco entrante in 𝑣).

- 𝑁 (𝑣)
  - i vicini (o vertici adiacenti) di 𝑣 v, indipendentemente dalla direzione.
