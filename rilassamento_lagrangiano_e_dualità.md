I rilassamenti servono and ottenere upper/lower bound per problemi che non si riescono a risolvere direttamente e per cui bisogna utilizzare approcci tipo branch and bound

Possiamo avere varie tipologie di rilassamento

- constraint elimination
- rilassamento continuo

Ci interessa particolarmente il **rilassamento Lagrangiano**

### Rilassamento Lagrangiano

l'idea è spostare dei vincoli in funzione obiettivo, e penalizzare quest'ultima quando i vincoli vengono violati

a questo punto possiamo eliminare i vincoli e risolvere il problema rilassato

I moltiplicatori sono i pesi che do alla violazione del vincolo e il problema diventa capire quali usare

Il problema rilassato mi da un lower bound valido

- possiamo pensare al fatto che la soluzione ottima del problema non rilassato viene migliorata dai moltiplicatori e quindi il problema rilassato può solo fare meglio

La soluzione del rilassamento non è detta che sia ammissibile, ma se lo è, è ottima anche per il prolbema originale (il rilassamento è un lower bound)

Il problema allora diventa capire quali moltiplicatori usare per ottenere il lower bound maggiore possibile

- in questa maniera la soluzione del rilassamento si avvicina il più possibile alla soluzione ottima per il non rilassato (che ricordiamo essere lower bounded dal rilassamento)
- inoltre, è facile che la soluzione del rilassamento diventi anche ammissibile

### Che cosa succede se voglio fare il rilassamento lagrangiano di un LP in forma standard?

... guarda dalla dispensa ...

sto spostando tutti i vincoli in funzione obiettivo ed **ottengo in questo modo un problema non vincolato**

p è un vettore di moltiplicatori lagrangiani

ottengo un espressione che dipende solo da p

x\* soluzione ottima del problema originale P e c'x* è il suo costo

la soluzione ottima del rilassamento g(p) ci dà un lower bound sul costo della soluzione del problema

- g(p) <= c'x*
- i termini lagrangiani si annullano dato che i vincoli sono rispettati

**problema lagrangiano duale**

massimizzare il valore del lower bound g(p)

il pezzo con il minimo vale:

- zero
- oppure -inf

se quel pezzo vale -inf allora so che il mio problema originale vale più di -inf... non so molto di più di prima

ma allora impongo un ulteriore vincolo in modo che quel pezzo mi da zero

**ottengo il problmea duale dal rilassamento lagrangiano!**

- il problema duale non è altro che la scelta ottima dei moltiplicatori lagrangiani
- le variabili duali non sono altro che i moltiplicatori lagrangiani

**NB**: fino ad adesso non abbiamo utilizzato la linearità da nessuna parte

- infatti anche se il problema fosse di ottimizzazione non lineare (vincoli non lineare con forma diversa da Ax = b)

Possiamo vedere quello che abbiamo fatto come dualità debole

- che sappiamo valere sempre anche per funzioni non lineari

Se sfruttiamo anche la linearità dei vincoli otteniamo la dualità forte

- che vale solo per funzioni convesse

Infine, ora che ho una formula posso anche ricavarmi facilmente tutti gli altri casi del duale

- vedi vincoli con disuguaglianze
