I problemi di flusso vengono definiti su:

- **digrafi**
- con archi che hanno associata una **capacità**
  - assumo che le capacità siano intere
- ogni arco ha poi un ulteriore grandezza che rappresenta il flusso che **"scorre"** su quell'arco
  - le capacità misurano il flusso massimo di un qualcosa che fluisce all'interno degli archi del grafo
    - ricorda che il flusso è una dimensione istantanea (è una densità)
    - ad esempio, flusso d'acqua in un tubo si misura in litri/s

Vogliamo mandare un flusso da una sorgente (s) a una destinazione (t), con s e t due nodi del grafo

Un flusso su una rete è **ammissibile** solo se

- i flussi non superano le capacità
- vale la conservazione del flusso
  - il flusso che esce dalla sorgente e quello che entra nella destinazione sono uguali con segno opposto
  - il flusso che attraverso ogni nodo intermedio vale 0
  - quanto detto sopra viene espresso per ogni nodo i come differenza tra suo flusso uscente e suo flusso entrante

### Tagli

Un taglio s-t è una partizione dei vertici in due sottoinsiemi in cui, il primo sottoinsieme contiene s e l'altro contiene t

- il taglio separa i due vertici s e t in partizioni distinte
- il taglio è definito dall'insieme di vertici che compongono le due partizioni
- oppure anche dagli archi che uniscono le due partizioni

Il **valore di un taglio** misura la somma delle capacità degli archi che vanno da V1 a V2

- attenzione, non contiamo gli archi che vanno da V2 a V1. **Il verso conta**

**NB**: i tagli sono importanti dato che mi rappresentano i colli di bottiglia della mia rete di flusso

- il taglio minimo (quello di valore più piccolo) mi definisce il flusso massimo che riesco a mandare da s a t
- intuitivamente il taglio minimo mi mostra i punti che formano il collo di bottiglia dato che non riesco a mandare più flusso di quello che le capacità del taglio minimo riescono a gestire
- vedi meglio dopo

# Teorema di Ford-Fulkerson

Quello che è stato detto sopra: ```il taglio minimo (quello di valore più piccolo) mi definisce il flusso massimo che riesco a mandare da s a t```

La dimostrazione ci convince del fatto che il taglio minimo definisce anche il flusso massimo che si riesce a mandare

- potrebbe venire il dubbio che il flusso che si riesce a mandare sia minore del taglio minimo. Non è questo il caso, le due quantità sono strettamente uguali

### DIM

- partiamo con un taglio che contiene solo s in V1 e un flusso ammissibile per la rete
- poi cominciamo ad aggiungere vertici a V1 fino a quando:
  - ci sono archi con capacità residua (e_ij < q_ij) tra vertici in V1 e V2
  - oppure fino a quando esiste un vj che ha flusso all'indietro (e_ji > 0)
    - i flussi che tornano indietro non ci piacciono dato che sembra essere un zero sum game
    - se qualcosa torna indietro è strettamente una perdita.
    - (te ne convincio continuando)
- smetto di aggiungere vertici in V1 in due situazioni:
    1. sono riuscito a raggiungere t
        - questo significa che c'è una catena (che chiameremo aumentante) di archi tutti con della capacità residua/flussi negativi dato che aggiungo solo vertici di questo tipo
        - ora **posso aumentare il flusso** dove ho capacità residua e diminuirlo dove mi torna indietro
            - il valore per cui posso aumentare il flusso è definito come delta = min{delta1, delta2}
                - con delta1 = min{capacità residue dei forward arc}
                - con delta2 = min{flussi negativi dei backward arc}
            - aumento il flusso totale di un valore pari a delta
                - incrementando di delta i flussi dei forward arc
                - decrementando di delta i flussi dei backward arc
                - intuitivamente, devo considerare il minimo di tutto dato che
                    - non posso incrementare di delta se la capacità mi limita
                    - non posso decrementare di delta se arrivo prima a zero
            - la dimostrazione ci convince del fatto che questo mantiene l'ammissibilità del flusso
        - a questo punto sono contento dato che ho migliorato la mia rete di flusso, possiamo ricominciare da capo e vedere dove finiamo
        - **NB**:
            - chiamiamo **catena aumentante** la catena di vertice con archi che hanno un flusso migliorabile
            - chiamiamo **forward arc** un arco che collega vi con vj e che ha verso a_ij
            - chiamiamo **backward arc** un arco che collega vi con vj e che ha verso a_ji

    2. non ho raggiunto t
        - questo significa che per tutti gli archi tra V1 e V2: il flusso è uguale alla loro capacità, oppure che il flusso all'indietro vale 0
        - ma allora il valore del flusso da s a t vale quanto il taglio
            - ho costruito il taglio popolando V1 e togliendo da V2
            - le capacità associate agli archi del taglio sono massimizzate
        - **abbiamo trovato il flusso ottimo!**
            - abbiamo incrementato iterativamente il flusso con il caso 1, fino a convergere nell'ottimo con il caso 2
        - **NB**: notiamo che una volta che troviamo il taglio, identifichiamo gli archi che rappresentano il collo di bottiglia per il flusso (sono proprio quelli del taglio)

### Algoritmo

- i vertici possono essere etichettati ed esplorati o meno

- s è etichettato ma non esplorato quando ha valore \[+s, +inf\]
- delta(vi) mi rappresenta quanto flusso sono riuscito a portare al vertice i

### Complessità dell'algoritmo

- **pseudopolinomiale** per floyd-fulkerson
  - ricorda che pseudopolinomiale si traduce nell'avere una complessità che dipende dalla grandezza delle costanti in gioco
    - lo stesso problema con costanti diverse ha complessità diversa
  - la complessità per calcolare un cammino aumentante è o(n^2)
  - di cammini aumentanti ne devo calcolare un numero proporzionale al flusso
- prendendo la catena aumentante minima toglo il termine pseudo polinomiale
- lo stato dell'arte è o(n^3)

### other max-flow problems

**molteplici sorgenti e molteplici sinks** si gestiscono aggiungendo una super sorgente e un super sink fittizzio

se aggiungiamo anche **capacità sui vertici** sto dicendo che un determinato nodo riesce a gestire solamente una determinata capacità di flusso f

- può entrare/uscire da quel vertice al massimo un flusso pari a f
- posso sdoppiare i vertici e togliere le capacità sui vertici
- **NB**: questa idea del sdoppiare i vertici è molto flessibile è quindi è importante da ricordare

# Minimum cost flow problem

qua vogliamo calcolare un flusso che abbia almeno un certo valore u minimizzando il costo

- qui gli archi, oltre alla capacità, hanno anche un costo per unità di flusso

### Idea

- trova un flusso ammissibile di valore u
  - posso usare floyd-fulkerson stoppandolo non quando non riesco più a raggiungere t (ho trovato il flusso massimo)
  - piuttosto, quando con le catene incrementali riesco a raggiungere una rete di flusso di valore u
- modifica iterativamente la rete di flusso trovata preservandone il valore ma facendone diminuire il costo ad ogni iterazione

Per il secondo punto utilizziamo un **grafo incrementale ausiliario**

- costruito basandosi sul grqfo corrente e sul flusso corrente
- il grafo incrementale rappresenta le possibilità che abbiamo di aumentare/diminuire il flusso corrente
- abbiamo due insiemi di archi nel grafo incrementale
  - gli archi in avanti mi rappresentano il fatto che posso incrementare il flusso di x
    - Genero un arco forward se c'è della capacità residua
  - gli archi all'indietro che posso diminuire il flusso
    - genero un arco forward se c'è del flusso

**OSS**: l'algoritmo di labeling di FF è un modo per trovare un cammino in questo grafo incrementale

- la catena incrementale era composta da archi in avanti dove potevo aumentare il flusso
- e da archi all'indietro dove potevo diminuire il flusso

l'idea è:

- trovare dei circuiti con costi negativi nel grafo incrementale
- posso percorrere questo circuiti fino a qundo il flusso è ammissibile
- modificare il flusso nel grafo originale con i costi che percorriamo nel grafo incrementale

### algoritmo

in una prima fase si costruisce un flusso di valore u

nella seconda fase cerca circuiti di costo negativo nel grafo incrementale

### complessità

pseudo polinomiale dato che modifico il flusso per un numero di volte proprorzionale alle capacità degli archi
