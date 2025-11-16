# TSP

ho un grafo connesso, partendo da un nodo voglio visitare tutti gli altri nodi una sola volta (tour) pagando il costo minimo, e tornare a casa

- in generale il grafo non è completo, ma noi possiamo calcolare il cammino minimo ed assumere che esista un lato con quel costo che connette direttamente i due nodi
- noi considereremo quindi un grafo completo

un tour è un cammino che si richiude nel vertice di partenza che visita tutti i nodi una sola volta

Un problema di ottimmizzazione combinatoria è un problema in cui le soluzioni sono finite e devo considerare tutte le combinazioni (di solito talmente tante da essere ingestibili)

Posso rappresentare una soluzione del TSP come un permutazione dei nodi che visito

- scegliendo quindi il nodo di partenza ho n-1! permutazioni

Si risolvono TSP dell'ordine di n ~ 10000

Applicazioni:

- tutte quelle in cui devo spostarmi da un insieme di punti spostandomi da uno all'altro
- robot che deve saldare schede
- ispezionare bulloni/giunzioni/travi/... di punto
- consegna della posta / logistica

Questo è un problema NP-HARD

### Modello per il A-TSP

Partiamo considerando un TSP su grafo orientato (Asymmetric TSP), e come prima completo

Che variabili decisionali usiamo per descrivere il tour?

- definiamo delle variabili binarie xa per ogni arco
- queste valgono 1 se l'arco è attraversato nel tour, 0 altrimenti

Ogni arco ha poi un costo ca

- il costo del tour è quindi sum(ca*xa)
- la funzione obiettivo min di questa sommatoria

Come rappresentiamo i vincoli?

- ogni nodo deve essere visitato una sola volta, e quindi ogni nodo deve avere esattamente un arco entrante ed uno uscente
- con delta+/- definiamo gli archi uscenti/entranti di un nodo (degree constraint)
- abbiamo quindi che per ogni vertice la sum su tutti i suoi archi entranti/uscenti deve valere 1

Questo è sufficente per essere sicuro che il tour parta e finisca nello stesso nodo?

- no, questo modello non è sufficente; mi può portare ad avere dei subtour separati (cicli di lunghezza minore n-1)

Potrei evitare la situazione dei subtour aggiungendo vincoli che vietano i subtour impedendomi di prendere tutti gli archi di una determinata istanza di subtour

- tuttavia anche il numero di subtour è combinatorio e quindi il numero di vincoli diventerebbe enorme, e quindi questi vincoli non mi piacciono tanto
  - per un sottoinsieme di vertici grande k, posso avere (k-1)! subtour
  - dato il primo nodo, ho k-1 scelte per il prossimo e così via

Voglio un vincolo più compatto ed efficace

- tutte le volte che c'è un subtour, c'è un sottoinsieme stretto (non tutti) dei vertici del grafo da cui non stiamo uscendo
- equivalentemente, ci sono dei sottoinsiemi di vertici da cui stiamo prendendo troppi archi (es. tre vertici e tre lati) e quindi i vincoli di grado mi impediscono di uscire

Un vincolo migliore è quindi quello che mi dice che per ogni sottoinsieme S posso prendere al massimo ||S|| - 1 archi

- inoltre, abbiamo un ulteriore vincolo che ci dice che 2 <= || S || <= n - 2
  - notare il minore uguale
  - non c'è bisogno di esprimere i SEC per subtour grandi 1 o n-1 (grande 1 dall'altro lato) dato che i vincoli di grado mi impediscono già soluzioni di questo tipo
- abbiamo dimostrato che questo vincolo seppur combinatorio è più tight di quello sopra e quindi sono sicuramente di meno
  - intuitivamente, prima avevo un vincolo separato per ognuno dei (k-1)! subtour del sottoinsieme di vertici che stavo considerando
  - ora dato un sottoinsieme di vertici ho un unico vincolo
- chiamiamo questa tipologia di vincoli come **subtour elimination constraint**

Quanti sono i subtour elimination constraint?

- ne ho uno per ogni sottoinsieme (tranne alcuni che abbiamo tagliato)
- posso rappresentare un sottoinsieme di un insieme di n elementi come un vettore di variabili binarie lungo n
- i sottoinsiemi possibili sono quindi esattamente 2^n
- noi abbiamo tagliato tutti quelli con cardinalità 2 e n-1
- inoltre non consideriamo il sottoinsieme vuoto e quello con tutti gli elementi
- **il numero di vincoli è quindi esattamente 2^n -2n -2**

Questo è il primo modello che vediamo che ha un numero di vincoli ingestibile. Eppure, abbiamo visto che riusciamo a risolvere TSP di dimensione n=10000

Come facciamo?

- risolviamo un rilassamento in cui ignoriamo i subtour elimination constraint
- vedremo poi che abbiamo un modo per controllare se la soluzione del rilassamento viola o meno uno di questi vincoli
- a questo punto aggiungiamo il vincolo, iteriamo facendo branch and bound, e prima o poi convergiamo

Abbiamo visto la dimostrazione che i subtour elimination constraint nella seconda forma sono equivalenti a quelli nella prima forma

- una conclusione importante è che perchè questo sia vero è che siano presenti i degree constraint
- questo è importante, se i degree constraint non sono presenti e io voglio comunque considerare i subtour, la secoonda forma continua a valere mentre la prima no

### Modello per il TSP

consideriamo ora il caso di grafi non orientati

il modello è molto simile a prima

- i degree constraint ora considerano lati e quindi la somma dei lati incidenti di ogni nodo deve valere 2
- i subtour constraint sono praticamente uguali

Oss: esistono anche dei modelli con un numero polinomiale di vincoli MTZ, ma nella pratica, seppur siano validi, non si riescono a risolvere in tempi ragionevoli
