importanti perchè spesso saltano fuori in problemi più complessi come sotto-problemi

# Shortest spanning tree (albero ricoprente di costo minimo)
Un'albero è un grafo, connesso, che non contiene circuiti
- equivalentemente, un grafo connesso che contiene n-1 lati (altrimenti circuiti)
- equivalentemente, per ogni coppia di vertici, esiste un solo cammino che li connette

Uno spanning tree è un sottografo con gli stessi vertici ma con un sottoinsieme dei lati che lo rende un albero

teorema di Prim:
- considera un sottografo che è un albero
- considera i vertici vicini non facenti parte dell'albero
- costruisci un nuovo albero, prendendo il lato di costo minimo che prende uno di questi vertici

Algoritmo:
- i grafi connessi in generale hanno o(n^2) lati 
- con un algoritmo semplice la complessità è o(n^3) cerco tra tutti i lati (n^2) quello più corto per n volte (finch'è non ho tutti i vertici)

un'algoritmo più intelligente (algoritmo di prim):
- uso un nuovo concetto di predecessore, il vertice che ho già visitato più vicino a me
    - prima mi focalizzavo sui lati, che sono sempre o(n^2)
    - ora, aggiorno i predecessori, ...
- uso delle etichette che mi tengono traccia del predecessore di ogni vertice

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



