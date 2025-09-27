questi problemi iniziali sono importanti perchè spesso saltano fuori in problemi più complessi come sotto-problemi

# Shortest Spanning Tree (albero ricoprente di costo minimo)
Un'albero è un grafo, **connesso**, che non contiene circuiti (per ogni coppia di nodi esiste un **percorso** (ricorda che i percorsi non hanno ripetizioni di vertici) che li connette)
- equivalentemente
    - un grafo connesso che contiene n-1 lati (altrimenti circuiti)
    - oppure, per ogni coppia di vertici, esiste un solo cammino che li connette

Uno Spanning Tree (ST) di un grafo
- è un sottografo con gli stessi vertici di quest'ultimo
    - l'albero deve toccare **tutti** i vertici
- ma con un sottoinsieme dei lati tale da renderlo un albero

Lo Shortest Spanning Tree problem (SST) si chiede:
- dato un grafo connesso e pesato,
- qual'è lo ST con la somma dei pesi dei lati minima?
- applicazione: connect towns through (water, gas, ...) pipelines at minimum cost;

### Teorema di Prim:
- Dato un grafo, considera un suo sottografo che forma un albero di copertura parziali
- considera il lato di costo minimo tra quelli che hanno un vertice appartenente all'albero parziale, e l'altro appartenente ai nodi non ancora considerati
- lo spanning tree ottimo del grafo, che contiene l'albero parziale corrente, conterrà anche questo lato
    - se l'albero parziale è ottimo, anche l'albero parziale con questo nuovo lato continuerà ad essere ottimo
- `questo teorema ci dice che possiamo risolvere SST partendo da un vertice e aggiungendo volta per volta il lato migliore tra quelli rimasti (greedy)`
    - troviamo l'ottimo globale facendo scelte ottime locali

### Algoritmo Naive:
In pratica applico il teorema di Prim
- parto con un vertice e basta (per forza ottimo)
- continuo ad aggiungere il lato minimo fino a che non ho visitato tutti i vertici

Complessità:
- ho n vertici e devo trovare per n-1 volte il lato minimo
- i grafi connessi in generale hanno o(n^2) lati
    - ad esempio, se il grafo è completo, ed ho visitato k vertici e me ne rimangono h da visitare, allora ho k*h lati (o(n^2)) tra cui cercare quello minimo
- con un algoritmo semplice la complessità è o(n^3) cerco tra tutti i lati (n^2) quello più corto per n volte (finch'è non ho tutti i vertici)

### Algoritmo di Prim
un'algoritmo più intelligente per SST:
- uso un nuovo concetto di **predecessore**, il vertice che ho già visitato più vicino a me
    - il predecessore di un vertice che non ho visitato (v), è un vertice appartenente a quelli che ho già visitato (u) tale che il costo del lato (u, v) è il minimo possibile
- ogni nodo non visitato viene etichettati a priori con il suo predecessore
- adesso, cerchiamo il prossimo vertice da aggiungere considerando solo i predecessori e non tutti i lati
    - consideriamo sempre il lato di costo minimo
- aggiunto il nuovo vertice, scorro tutti i vertici rimasti per aggiornare le etichette in caso il nuovo vertice sia un predecessore migliore

Complessità:
- ho sempre n-1 vertici da aggiungere
- prima mi esploravo o(n^2) lati ad ogni operazione
- ora controllo/aggiorno solamente i predecessori che sono V\W (o(n))
    - non devo considerare tutti i nodi già aggiunti, solo il predecessore
    - quando aggiorno i predecessori devo solo fare un confronto con il nuovo vertice aggiunto
- complessità finale è quindi o(n^2)






# Data structures for representing graphs
sostanzialmente mi devo chiedere se il mio grafo è denso o è sparso (molti lati / pochi lati) per decidere quale struttura dati usare

se il grafo è denso -> matrice di adiacenza
- occupa potenzialmente tanta memoria
- ma mi permette di accedere ai dati (sapere se c'è un lato tra due vertici) in tempo costante

se il grafo è sparso -> liste di adiacenza (non so perchè nella slide non viene chiamata in questo modo)
- forward star == per ogni vertice quelli su cui posso arrivare
- backward star == per ogni vertice quelli che possono arrivare da me
- questa struttutra dati mi occupa spazio proporzionale al numero di lati
- ma per accedere ad un lato devo scorrere la lista (magari con ricerca binaria se la lista è ordinata)
    - interessante, se voglio fare ricerca binaria non posso rappresentare la lista come linked list






# Shortest path problem (problema del cammino minimo)

proprietà: se il cammino minimo passa per un vertice vj, allora il cammino minimo totale è uguale alla concatenazione dei due cammini minimi

arborescenza: ...

proprietà 2: i cammini minimi formano un'arborescenza



algoritmo di Dijkstra:
- l'idea è la stessa di prima, parto da una soluzione parziale (che stavolta è una arborescenza) e man mano aggiungo il lato migliore
- utilizzo la proprietà 1 che mi garantisce la prima parte del cammino è ottima e quindi posso aggiungere un'altro pezzo
- ATTENZIONE: qua va dimostrato che questo algoritmo mi da la soluzione ottima! Non vale sempre che un algoritmo in cui si sceglie la prossima cosa da fare considerando solo la scelta ottima locale, porta anche a trovare la soluzione ottima globale (pensa al knapsack).

teorema che mi dimostra la correttezza dell'algoritmo

complessità:
- abbiamo un ciclo while che mi scorre tutti i vertici (n-1)
- dentro devo trovare un minimo dentro a (V/S)

interessante: problemi facili come il cammino minimo di solito si calcolano sul momento. Se però questo problema va risolto tante volte per risolvere un problema più complesso, una buona idea può essere precalcolare i cammini minimi è inserire i risultati in una LUT.

# Longest path problem
si risolve con branch&bound

# Critical path method
se costruisco un grafo che mi rappresenta delle attività, questo grafo è per costruzione aciclico



