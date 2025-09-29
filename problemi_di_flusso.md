i problemi di flusso vengono definiti su
- digrafi
- con archi che hanno associata una capacità 
    - assumo che le capacità siano intere
- le capacità misurano il flusso massimo di un qualcosa che fluisce all'interno degli archie del grafo
    - ricorda che il flusso è una dimensione istantanea (è una densità)
    - ad esempio, flusso d'acqua in un tubo si misura in litri/s

vogliamo mandare un flusso da una sorgente (s) a una destinazione (t), con s e t due nodi del grafo
- oltre alle capacità, gli archi hanno anche un flusso associato

un flusso su una rete è ammissibile solo se
- i flussi non superano le capacità
- vale la conservazione del flusso
    - il flusso che esce dalla sorgente e quello che entra nella destinazione sono uguali con segno opposto
    - il flusso che attraverso ogni nodo intermedio vale 0
    - quanto detto sopra viene espresso per ogni nodo i come differenza tra suo flusso uscente e suo flusso entrante

Un taglio s-t è una partizione dei vertici in due sottoinsiemi in cui, il primo sottoinsieme contiene s e l'altro contiene t
- il taglio separa i due vertici s e t

Il valore di un taglio è una grandezza che ci interessa che misura la somma delle capacità degli archi che vanno da V1 a V2
- attenzione, non contiamo gli archi che vanno da V2 a V1. Il verso conta

NB: i tagli sono importanti dato che mi rappresentano i colli di bottiglia
- il taglio minimo (quello di valore più piccolo) mi definisce il flusso massimo che riesco a mandare da s a t

### Teorema di Ford-Fulkerson
... quello che è stato detto sopra

la dimostrazione ci convince del fatto che il taglio minimo definisce anche il flusso massimo che si riesce a mandare
- potrebbe venire il dubbio che il flusso che si riesce a mandare sia minore del taglio minimo. Non è questo il caso

DIM:
- partiamo con un taglio che contiene solo s in V1
- poi cominciamo ad aggiungere vertici a V1 fino a che 
    - ci sono archi con capacità residua (< stretto) tra vertici in v1 e v2
    - oppure fino a quando esiste un vj che ha flusso all'indietro
        - i flussi che tornano indietro non ci piacciono dato che sembra essere un zero sum game, se qualcosa torna indietro è strettamente una perdita. (te ne convincio continuando)
- concludiamo il processo con due situazioni
    - ho raggiunto t
        - questo significa che c'è una catena (aumentante) di archi tutti con capacità residua -> posso aumentare il flusso
        - ora posso aumentare il flusso dove ho capacità residua e diminuirlo dove mi torna indietro
            - la dimostrazione ci convince del fatto che questo mantiene l'ammissibilità del flusso
        - possiamo ricominciare da capo e vedere dove finiamo
    - non ho raggiunto t
        - questo significa che c'è un arco il cui flusso è uguale alla sua capacità
        - oppure che il flusso all'indietro vale 0 
        - in questo caso il flusso vale quanto il taglio
        - siccome il flusso non può essere maggiore del valore del taglio (siamo limitati dalla capacità), abbiamo trovato il flusso ottimo
            - abbiamo incrementato iterativamente il flusso con il caso 1, fino a convergere nell'ottimo con il caso 2
    - NB: notiamo che una volta che troviamo il taglio, identifichiamo gli archi che rappresentano il collo di bottiglia per il flusso

Che differenza c'è tra cammino e catena?

Algoritmo:
- i vertici possono essere etichettati ed esplorati o meno

- s è etichettato ma non esplorato quando ha valore \[+s, +inf\]
- delta(vi) mi rappresenta quanto flusso sono riuscito a portare al vertice i

Complessità dell'algoritmo:
- pseudopolinomiale per floyd-fulkerson
    - ricorda che pseudopolinomiale si traduce nell'avere una complessità che dipende dalla grandezza delle costanti in gioco
        - lo stesso problema con costanti diverse ha complessità diversa
    - la complessità per calcolare un cammino aumentante è o(n^2)
    - di cammini aumentanti ne devo calcolare un numero proporzionale al flusso
- prendendo la catena aumentante minima toglo il termine pseudo polinomiale
- lo stato dell'arte è o(n^3)


### other max-flow problems

molteplici sorgenti e molteplici sinks si gestiscono aggiungendo una super sorgente e un super sink fittizzio


se aggiungiamo anche capacità sui vertici sto dicendo che un determinato nodo riesce a gestire solamente una determinata capacità di flusso f
- può entrare/uscire da quel vertice al massimo un flusso pari a f
- posso sdoppiare i vertici e togliere le capacità sui vertici
- **NB**: questa idea del sdoppiare i vertici è molto flessibile è quindi è importante da ricordare





# Minimum cost flow problem
qua vogliamo calcolare un flusso che abbia almeno uncerto valore minimizzando il costo
- gli archi hanno un costo per unità di flusso

Genero un grafo incrementale
- Genero un arco forward se c'è della capacità residua
- genero un arco forward se c'è del flusso
oss: l'algoritmo di labeling di FF è un modo per trovare un cammino in questo grafo incrementale

l'idea è trovare dei circuiti con costi negativi

















