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
dato un digrafo pesato e un nodo di partenza s, trovare per ogni altro vertice v il percorso migliore

proprietà: se il cammino minimo tra vi e vk passa per un vertice vj, allora questo cammino minimo è formato dalla concatenazione dei due cammini minimi (vi,vj) e (vj,vk)
-

arborescenza: sostanzialmente un albero
- digrafo aciclico
- tutti i vertici hanno solamente un arco entrante
- tranne la radice

proprietà 2: i cammini minimi verso gli altri vertici formano un'arborescenza con radice uguale al nodo di partenza

### Algoritmo di Dijkstra:
- l'idea è la stessa di prima, parto da una soluzione parziale (che stavolta è una arborescenza) e man mano aggiungo l'arco migliore (di costo minimo)
- utilizzo la proprietà 1 che mi garantisce che se la prima parte del cammino è ottima, aggiungendo l'arco con costo minimo, continuo ad avere un percorso ottimo
- **ATTENZIONE**: va dimostrato che questo algoritmo da la soluzione ottima!
    - Non sempre vale che un algoritmo in cui si sceglie la prossima cosa da fare considerando solo la scelta ottima locale, porta anche a trovare la soluzione ottima globale (pensa al knapsack).

Dimostrazione:
- punto non chiarissimo: poiché 𝑣 è scelto come nodo con etichetta minima tra quelli non in 𝑆, vale ℓ(h) ≥ ℓ(v).

complessità:
- abbiamo un ciclo while che mi scorre tutti i vertici (n-1)
- dentro devo trovare un minimo tra V\S vertici
- complessità finale = o(n^2)

interessante:
- problemi facili come il cammino minimo di solito si calcolano sul momento.
- Se però questo problema va risolto tante volte per risolvere un problema più complesso, una buona idea può essere precalcolare i cammini minimi è inserire i risultati in una LUT.

# Longest path problem
Questo è un problema difficile! Si risolve con branch&bound con complessità esponenziale











# Critical path method
Method to plan and schedule complex projects
- objective: handle the tasks involved in a given project, so as to determine the minimum time needed to complete the project
- ci interessa anche il critical path, ovvero quella sequenza di attività che se ritardate ritardano tutto il progetto

Project = set of activities of various duration, **with precedence relationships**
- The activities involved in the project are represented through a **weighted directed graph**
    - la direzione degli archi mi rappresenta la direzione del tempo
    - nota che se costruisco un grafo che mi rappresenta delle attività, questo grafo è per costruzione aciclico altrimenti avrei delle attività che iniziano sia dopo che prima di altre attività
- usiamo la convenzione **Activities on Arcs**
    - arcs ah = (vi, vj) represent activities
    - vertices represent the start and end of activities
    - weight d(vi, vj) is the duration of activity (vi, vj)
    - **the graph itself represents precedence relationships**: to impose ai ≺ aj
        - either the ending vertex of ai coincides with the starting vertex of aj, or
        - ∃ a path containing ai before aj

Problem: find the starting time of each activity so that the total duration (**makespan**) is a minimum.

### Algorithm
1. the graph must have
    - a single starting vertex (in-degree = 0);
    - a single ending vertex (out-degree = 0):
    - inizio e fine del progetto che mi rappresentano il mio makespan

2. numeriamo i vertici in maniera tale che per ogni arco (vi, vj): i < j
    - assegno un numero solamente ai nodi che non hanno predecessori (parto dal nodo iniziale)
    - dopo aver assegnato un numero, elimino tutti gli archi verso i successori del nodo appena numerato
        - in questa maniera solamente i nodi senza predecessori possono essere numerati con la garanzia di aver numerato tutt i predecessori (dipendenze) con un numero minore
    - itero finchè non ho numerato tutti i nodi

3. For each event (vertex) vk, find:
    - T_MIN_k: earliest time at which the activity can start without violating its precedences
        - (Makespan (length of the longest path from v0 to vn+1) = T_MIN_(n+1))
    - T_MAX_k latest time at which the activity must terminate without delaying the project
    - Algoritmo:
        - parti con il nodo sorgente e con il trovare i T_MIN di tutti i nodi
            - il T_MIN del nodo sorgente è 0
            - il T_MIN di un nodo è uguale a: massimo tra T_MIN + distanza dei nodi precedenti
            - NB: devo considerare tutti i nodi precedenti
        - etichettati tutti i nodi con il loro T_MIN, si può procedere a calcolare il T_MAX
            - prima si partiva dalla sorgente fino ad arrivare alla destinazione, ora si va a ritroso
            - si parte dalla destinazione, il T_MAX della destinazione è pari al suo T_MIN (se ritardo la fine, ho ritardato il progetto)
            - il calcolo di T_MAX è analogo a quello di T_MAX ma invertito
                - ora si considerano i nodi successori
                - min invece che max
                - sottrazione invece che somma

4. For each activity (arc) ah = (vi, vj), compute
    - Early Start Time: EST(ah) = T_MIN_i
    - Late Start Time: LST(ah) = T_MAX_j − d(vi, vj);
    - Float: S(ah) = LST(ah) − EST(ah) 
        - if LST(ah) = EST(ah) (non posso ritardare l'inizio dell'attività altrimenti ritardo il progetto) then ah is critical;
    - **Critical path** = path from v0 to vn+1 containing only critical activities

    




























