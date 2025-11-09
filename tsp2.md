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
