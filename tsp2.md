# ripasso modello

per ogni ciclo, la somma degli archi deve essere <= |C| - 1

- devo avere un arco in meno rispetto al numero di vertici del ciclo

un vincolo più forte è considerare al posto di cicli sottoinsiemi di vertici

- più forte dato che consideriamo tutti gli archi (variabili) che ci possono essere tra s vertici, non solo quelli del circuito
- numero di vincoli è o(2^n), proporzionale al numero di sottoinsiemi di vertici

# Come gestiamo un numero esponenziale di vincoli?

## metodo con cutting plane

non so risolvere il problema e quindi ne considero un rilassamento

- all'inizio tolgo tutti i SECs e trovo la soluzione ottima x~

mi chiedo: x~ soddisfa i SECs?

- se si, a posto ho trovato una soluzione ottima anche per il problema originale
- se no, aggiungo il primo vincolo violato che trovo e itero
- conclusione: non risolvo considerando tutti i SEC, ma solo quelli che sono violati

Si osserva che nella pratica si converge con poche iterazioni

- il numero di SEC importanti sono pochi
- risolvo un problema con un numero esponenziale di vincoli, risolvendo tanti problemi piccoli risolvibili

In questo algoritmo abbiamo due manopole con cui giocare:

- il numero di SEC iniziali
- il numero di SEC che aggiungiamo ad ogni iterazione

### Come faccio a sapere se un SEC e violato? se si, come faccio a sapere quale SEC è violato?

tipicamente cerchiamo il vincolo più violato, quello che da più fastidio alla soluzione corrente

Cerchiamo il vincolo massimamente violato risolvendo un problma di programmazione lineare con funzione obiettivo = arg max i app. M : bi - ai^T x~

dobbiamo modellare questo problema (chiamato di separazione) con un ulteriore modello di ILP

le variabili decisionali modellano se un vertice appartiene o no ad un sottoinsieme di vertici

abbiamo poi bisogno di un ulteriore insieme di variabili decisionali che mi dicono se un arco tra i vertici nel sottoinsieme è preso o meno

- queste non mi servono a modellare la soluzione ma a descrivere il vincolo violato sotto forma di equazione

dobbiamo legare le variabili y alle variabili z, l'arco che collega due vertici deve collegare due vertici appartenenti al sottoinsieme

**NB**: invece di scandire tutti i vincoli (impossibile), risolvo un ILP che mi dice direttamente qual'è il vincolo più violato. Se il vincolo più violato non è violato allora la soluzione di partenza è ammissibile (e ottima) anche per il problema originale

## alternativa al risolvere un ILP

nel caso di x~ posso controllare gli uni dentro a x~ e vedere se torno al vertice 1 toccando tutti i vertici o meno

...

conviene esprimere i SEC in forma di archi uscenti

il vincolo di connessione lo posso modellare come un problema di flusso massimo

- la sorgente è il vertice 1
- la destinazione è un qualunque vertice k fuori dal mi sottoinsieme corrente
- devo avere un flusso >= 1 (almeno un arco uscente dal mio sottoinsieme)

risolvo un problema di flusso massimo per ogni vertice arbitrario k fuori dal mio sottoinsieme corrente

se trovo un flusso massimo < 1 trovo un vincolo violato (problema di separazione risolto)

se tutti i flussi sono >= 1 trovo la soluzione ottima del rilassamento continuo (problema di separazione risolto)

- ricordiamo che qua sto risolvendo il rilassamento continuo

la complessità di questo algoritmo di separazione è polinomiale dato che

- risolvere un problema di flusso massimo ha complessità o(n^3)
- potrebbe sembrare che nel caso peggiore devo aggiungere un vincolo alla volta (e ne ho un numero esponenziale)
  - è stato dimostrato che il numero di iterazioni di questo algoritmo (numero di vincoli che devo aggiungere) è polinomiale

...

Per raggiungere la potenza espressiva dei SEC, non ci serve per forza un numero esponenziale di vincoli. Ci bastano un numero polinomiale di variabili e un numero polinomiale di vincoli

**Esiste un modello polinomiale per il rilassamento continuo del ATSP**

- questo ci conferma che il rilassamento continuo del ATSP ha complessità polinomiale (risolviamo un problema di PL con un numero polinomiale di vincoli e variabili)

NB: questa formulazione, seppur polinomiale, non funziona con grafi molto grandi. Quindi non posso usarla con uno schema di branch and bound per risolvere il problema con anche i vincoli interi.

- per problemi piccoli può essere comoda per non dover risolvere il problema di separazione. Basta utilizzare un solver per la PL

## Formulazione Muller-Tucker-Zemelin (MTZ)

...

i vincoli sembrano laschi ma in realtà sono per forza tight a causa del caso in cui xa=0, altrimenti non riesco a completare il tour

# Come gestiamo i vincoli di interezza?

con Branch & Bound

consideriamo il TSP come caso di studio per gestire problemi con un numero esponenziale di vincoli

lo schema di branch and bound Depth-First visto con Martello non è lo schema più efficente per fare branch & bound.

In generale abbiamo 3 scelte da fare nello schema di branch & bound:

- quale problema scegliamo dalla lista?
  - con martello abbiamo visto DFS
- che rilassamento risolviamo per ottenere il lowerbound?
  - con martello abbiamo visto rilassamento continuo
- come determiniamo i due sottoinsiemi del branching?
  - con martello togliamo tutta la parte non intera in mezzo (partizioniamo lo spazio in base ad una variabile frazionaria in soluzione)
  - ma se ho più variabili frazionarie, quale scelgo per il branching?
  - una possibilità è fare strong-branching in cui si guarda un passo in avanti di un passo risolvendo con simplesso duale le coppie di rilassamenti continui e calcoliamo uno score
    - riduciamo il numero di nodi
    - tuttavia abbiamo un forte overhead nel calcolare gli score
  - per ridurre l'overhead possiamo calcolare delle approssimazioni dei rilassamenti continui
    - c'è un tradeoff tra tempo di calcolo e precisione dell'approssimazione (che mi riduce il numero di nodi)
  - oppure possiamo utilizzare pseudocosti in cui
    - si parte strong-branching
    - si va avanti per un po' in questo modo in maniera da imparare quali sono le variabili importanti su cui branchare
    - si procede con approssimazioni
