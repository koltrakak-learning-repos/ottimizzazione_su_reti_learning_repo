# ripasso modello

per ogni ciclo, la somma degli archi deve essere <= |C| - 1

- devo avere un arco in meno rispetto al numero di vertici del ciclo

un vincolo più forte è considerare al posto di cicli sottoinsiemi di vertici

- più forte dato che consideriamo tutti gli archi (variabili) che ci possono essere tra s vertici, non solo quelli del circuito
- numero di vincoli è o(2^n), proporzionale al numero di sottoinsiemi di vertici

# Come gestiamo un numero esponenziale di vincoli?

## metodo con cutting plane

non so risolvere il problema e quindi ne considero un rilassamento

rilasso in due modi:

- faccio un rilassamento continuo
- continuo ad avere il numero espnenziale di SEC e quindi tolgo anche tutti i SECs e trovo la soluzione ottima del rilassamento: x~

mi chiedo: x~ soddisfa i SECs?

- se si, a posto ho trovato una soluzione ottima anche per il problema originale
  - ricorda che le soluzioni ottime dei rilassamenti sono per forza sempre non peggiori di quelle dei problemi originali
- se no, aggiungo il primo vincolo violato che trovo e itero
- conclusione: non risolvo considerando tutti i SEC, ma solo quelli che sono violati

Si osserva che nella pratica si converge con poche iterazioni

- il numero di SEC importanti sono pochi
- risolvo un problema con un numero esponenziale di vincoli, risolvendo tanti problemi piccoli risolvibili

In questo algoritmo abbiamo due manopole con cui giocare:

- il numero di SEC iniziali
- il numero di SEC che aggiungiamo ad ogni iterazione

Nella pratica cambia poco le scelte che si fanno in questi due punti.

The crucial part of the algorithm is how to effectively find the violated constraints una volta che ho risolto il rilassamento.

- this step is generally called **Separation**

## Problema di separazione

**Come faccio a sapere se un SEC e violato? se si, come faccio a sapere quale SEC è violato?**

tipicamente cerchiamo il vincolo più violato, quello che da più fastidio alla soluzione corrente

**Cerchiamo il vincolo massimamente violato risolvendo un problma di programmazione lineare intera**

Come modelliamo l'ILP del problema di separazione?

... in breve guarda dalla dispensa

Le variabili decisionali modellano se un vertice appartiene o no ad un sottoinsieme di vertici: y

- queste sono le variabili che mi definiscono il subset di vertici per cui il SEC è eventualmente violato
- ce ne è una per ogni vertice del grafo

Abbiamo poi bisogno di un ulteriore insieme di variabili decisionali che mi dicono se un arco tra i vertici nel sottoinsieme è preso o meno: z

- ce ne è una per ogni arco del grafo
- queste non mi servono a modellare la soluzione ma a descrivere il vincolo violato sotto forma di equazione (modellare i vincoli)

dobbiamo legare le variabili y alle variabili z, l'arco che collega due vertici deve collegare due vertici appartenenti al sottoinsieme

**After having solved the complete ILP**

- if the optimal solution (y', z') takes a value >= 1, this means that all constraints (51) are satisfied by the given x*!
  - abbiamo la soluzione del rilassamento continuo dell'ATSP
- Otherwise, the subset S*:= {i appartenenti V : y_i' = 1} defines the constraint (51) that is most violated by x*, and that is added to the current set of (active) constraints

**NB**: stiamo facendo una cosa che sembra super inefficente:

- abbiamo modellato l'ATSP come un ILP con un numero esponenziale di SEC
- ignoriamo momentaneamente l'interezza delle variabili e cerchiamo la soluzione del suo rilassamento continuo
- per trovare la soluzione ottima del rilassamento continuo utilizziamo uno schema in cui
  - eliminiamo i SEC
  - risolviamo il LP rimanente (doppiamente rilassato)
  - cerchiamo un SEC violato risolvendo un ILP (separiamo i SEC violati)
  - se ne troviamo qualcuno dalla soluzione del ILP di separazione, lo aggiungiamo al modello LP e iteriamo
- **Di fatto stiamo risolvendo molteplici ILP per trovare la soluzione, non del ATSP, ma del suo rilassamento continuo**
- questo schema però funziona bene, incredibile

**NB**: invece di scandire tutti i vincoli (impossibile), risolvo un ILP che mi dice direttamente qual'è il vincolo più violato. Se il vincolo più violato non è violato allora la soluzione di partenza è ammissibile (e ottima) anche per il problema originale

### Oss sui lower bound

It is easy to observe that during the “row generation” algorithm above the optimal value c^T x* of the reduced LP is always smaller than (or equal to) that of the full LP (rilassamento continuo con tutti i SEC). Thus, it is a valid lower bound on the optimal value of the ILP associated (ATSP), if any.

This observation implies that even if the “row generation” algorithm is prematurely interrupted (because of a time limit or because the separation problem is solved heuristically
and no more violated constraints are found) a valid lower bound is available.

Questo è interessante in uno schema di branch and bound per la risoluzione dell'ATSP intero

# alternativa al risolvere un ILP

Il problema di separazione è facile alla prima iterazione:

- nel caso di x~ intero (come alla prima iterazione), posso controllare gli uni dentro a x~ e vedere se torno al vertice 1 toccando tutti i vertici o meno (problema di raggiungiblità)

Nelle altre iterazioni è più difficili

- conviene esprimere i SEC in forma di archi uscenti (connessione)
- il vincolo di connessione lo posso modellare come un problema taglio minimo, ovvero di flusso massimo
  - la sorgente è il vertice 1
  - la destinazione è un qualunque altro vertice k
  - **NB**: sto considerando solo gli archi definiti dalla mia soluzione corrente x*, con capacità massime definite dal valore della componente
  - i SEC mi impongono che per qualunque altro vertice k il flusso massimo deve essere >= 1
    - questo mi garantisce che la mia soluzione corrente x* denota una sottografo connesso (riesco a raggiungere qualsiasi vertice a partire da qualsiasi vertice)
    - nota: sottografo dato che ho meno archi, non perchè ho meno vertici

risolvo un problema di flusso massimo per ogni vertice arbitrario k fuori dal mio sottoinsieme corrente

- se trovo un flusso massimo < 1 trovo un vincolo violato che posso aggiungere al mio rilassamento (problema di separazione risolto)
- se tutti i flussi sono >= 1, la soluzione corrente è ottima per l'intero rilassamento continuo

La complessità di questo algoritmo di separazione è polinomiale dato che

- devo risolvere un problema di flusso massimo che ha complessità o(n^3), per tutti i k-possibili che sono n-1
- se non trovo alcun flusso massimo < 1, ho già finito; altrimenti devo aggiungere il vincolo violato e iterare
- potrebbe sembrare che nel caso peggiore devo aggiungere un vincolo alla volta (e ne ho un numero esponenziale)
- è stato dimostrato che il numero di iterazioni di questo algoritmo (numero di vincoli che devo aggiungere) è polinomiale

Conclusione: la soluzione del rilassamento continuo dell'ATSP richiede un numero polinomiale di iterazioni di separazione, ciascuna delle quali richiede un tempo polinomiale; quindi
l’intero procedimento di soluzione del rilassamento continuo richiede un tempo polinomiale

**NB**: abbiamo notato che il rilassamento continuo dell'ATSP ha complessità polinomiale solamente in questa formulazione tramite problema di flusso, se ci fossimo fermati alla formulazione precedente come ILP non l'avremmo capito! (anche se nel caso medio anche il caso precedente ha complessità polinomiale)

### Modelli polinomiali per l'ATSP

Per raggiungere la potenza espressiva dei SEC, non ci serve per forza un numero esponenziale di vincoli. Ci bastano un numero polinomiale di variabili e un numero polinomiale di vincoli

**Esiste un modello polinomiale per il rilassamento continuo del ATSP**

- questo ci conferma che il rilassamento continuo del ATSP ha complessità polinomiale (risolviamo un problema di PL con un numero polinomiale di vincoli e variabili)

NB: questa formulazione, seppur polinomiale, non funziona con grafi molto grandi. Quindi non posso usarla con uno schema di branch and bound per risolvere il problema con anche i vincoli interi.

- per problemi piccoli può essere comoda per non dover risolvere il problema di separazione. Basta utilizzare un solver per la PL e riesco a risolvere il rilassamento continuo

### Formulazione Muller-Tucker-Zemelin (MTZ)

non mi sembra importante

...

i vincoli sembrano laschi ma in realtà sono per forza tight a causa del caso in cui xa=0, altrimenti non riesco a completare il tour
