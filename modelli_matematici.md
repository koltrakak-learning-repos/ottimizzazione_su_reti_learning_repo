# Modelli matematici

possiamo usare un modello o un algoritmo per risolvere un problema

che vantaggi ha un algoritmo rispetto ad un modello?

- l'algoritmo sfrutta la conoscenza che io ho sul problema e quindi può avere una complessità minore rispetto al modello

Il modello per contro è più flessibile dato che riesce a risolvere qualunque problema modellabile in un'istanza del modello

il modello è più flessibile

l'algoritmo è più efficente

### Consideriamo il problema del cammino minimo

```
matrice di incidenza
- definita per digrafi
- una riga per vertice
- una colonna per arco
- ogni colonna mi dica dove l'arco esce e dove entra
```

riformuliamo il problema come un problema di flusso di costo minimo

- flusso di valore 1
- costo per unità di flusso == costo di attraversamento dell'arco
- mandare un'unità di flusso con costo minimo si traduce nel trovare il cammino minimo

**NB**: il prodotto per la matrice con il vettore delle variabili di flusso degli archi, ci da il risultato dell'espressione di conservazione del flusso

- otteniamo un problema di programmazione lineare!
- le variabili decisionali sono il flusso che devo mandare in ogni arco

**Attenzione**:
non ho imposto il vincolo di interezza delle variabili.

- il flusso potrebbe quindi anche essere frazionario
- Chi mi assicura che quando vado a risolvere con il simplesso la mia soluzione sia intera?
- è necessario imporre l'interezza delle variabili?

In generale no, ma **se la matrice A è TUM allora il simplesso mi da una soluzione intera**

**Si può dimostrare (tramite la sufficient unimodularity condition) che A è proprio TUM**

Conseguenze:
**-> la matrice di incidenza di un digrafo è TUM**
**-> the shortest path problem can be solved through LP**

Ma allora Dijkstra non serve a niente? NO!

- Dijkstra (che è più specializzato) è più efficente rispetto a risolvere tramite simplesso
- Se devo risolvere un solo cammino minimo cambia poco, ma se il cammino minimo è un problema intermedio, e ne devo risolvere tanti, allora Dijkstra diventa necessario per avere efficenza

Ma la complessità del simplesso, IN PRATICA, non è o(log n), mentre Dijkstra non è o(n^2)? Come fa Dijkstra ad essere più efficente di Dijkstra?

- non bisogna confondere caso medio con caso peggiore
- qua stai confrontando caso medio del simplesso con caso peggiore di Dijkstra
- anche Dijkstra nel caso medio non è o(n^2)

Altra conseguenza che abbiamo data la sufficient unimodularity condition riguarda il **problema dell'assegnamento**

- matriche (quadrata) degli assegnamenti in cui ogni riga è una persona e ogni colonna è un lavoro
- ogni persona ha un solo lavoro
- uso delle variabili binarie xij = { i se assegno riga i a colonna j; 0 altrimenti}
- vincoli che mi dicono:
  - le variabili sono binarie
  - la somma sulla riga = 1
  - la somma sulla colonna = 1

By replacing constraints xij ∈ {0, 1} with xij ≥ 0 (rilassamento continuo) posso risolvere con simplesso dato che diventa un normale PL

- se elimino il vincolo di interezza e risolvo con il simplesso, ottengo una soluzione intera?
- Anche qua Si dato che si dimostra che anche in questo problema la matrice è TUM

**Oss**: notare che nell'eliminare il vincolo di interezza non devo specificare che le x <= 1 dato che le somme pari a 1 impongono già questa condizione

**anche il problema dell'assegnamento si può risolvere tramite LP del suo rilassamento continuo**

Tuttavia, stesso discorso di prima, se risolvo con un modello sono flessibile, ma Hungarian algorythm lo risolve con molta più efficenza

```
A quanto pare ci fermiamo a slide 22
```
