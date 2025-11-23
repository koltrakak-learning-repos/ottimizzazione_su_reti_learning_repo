# Come gestiamo i vincoli di interezza?

con Branch & Bound

consideriamo il TSP come caso di studio per gestire problemi con un numero esponenziale di vincoli

Fare B&B con TSP è simile a fare B&B con qualsiasi altro TSP

- ad ogni risolvo il rilassamento continuo del TSP
- **NB**: stavolta per risolvere il rilassamento continuo devo risolvere il problema di separazione il che consiste nel risolvere diversi ILP iterando
- ottenuta la soluzione del rilassamento continuo continuo il branch and bound come prima
- se la soluzione del rilassamento è intera ho ottenuto una incumbent solution, altrimenti branch producendo due sottoproblemi con una disuguaglianza in più su una variabile frazionaria
- applico il bounding come sempre quando ci sono nodo con un lowerbound > della incumbent solution

# Considerazioni su branch and bound in generale

lo schema di branch and bound Depth-First visto con Martello non è lo schema più efficente per fare branch & bound.

## Come faccio branching?

In generale abbiamo 3 scelte da fare nello schema di branch & bound:

- quale problema scegliamo dalla lista?
  - con martello abbiamo visto DFS
- che rilassamento risolviamo per ottenere il lowerbound?
  - con martello abbiamo visto rilassamento continuo
- come determiniamo i due sottoinsiemi del branching?

Concentriamoci su come si fa il branching:

- con martello togliamo tutta la parte non intera in mezzo (partizioniamo lo spazio in base ad una variabile frazionaria in soluzione)
- **ma se ho più variabili frazionarie, quale scelgo per il branching?**
- una possibilità è fare strong-branching in cui si guarda un passo in avanti risolvendo con simplesso duale le coppie di rilassamenti continui
  - per ognuno dei due rami calcoliamo uno score che si basa su quanto la scelta di quella variabile di branching **migliora il bound**
    - in un problema di minimo, un LB buono è un LB alto dato che più vicino al valore della soluzione ottima intera e quindi **più facilmente potabile**
    - con stron branching scegliamo come variabile di branching quella che porta ad avere dei bound più alti nei rami figli
  - riduciamo il numero di nodi da esplorare
  - tuttavia abbiamo un forte overhead nel calcolare gli score
- per ridurre l'overhead possiamo calcolare delle approssimazioni dei rilassamenti continui
  - c'è un tradeoff tra tempo di calcolo e precisione dell'approssimazione (che mi riduce il numero di nodi)
- oppure possiamo utilizzare pseudocosti in cui
  - si parte strong-branching
  - si va avanti per un po' con questa strategia in maniera da imparare quali sono le variabili importanti su cui branchare
    - è importante capire quali sono le variabili importanti nei primi livelli del branch and bound
  - si procede con approssimazioni

## Come scelgo il prossimo nodo da esplorare?

**Strategia best bound**

- ho tanti nodi aperti
- scelgo quello con il lower bound più basso
  - tanto lo dovrei esplorare lo stesso dato che esplorando altri nodi (che hanno un bound maggiore) otterei alla meglio delle incumbent solution comunque maggiori di questo bestbound
- consente di esplorare un numero di nodi ridotto, però richiede tanta memoria dato che salto a destra e a sinistra nell'albero e quindi non posso riutilizzare il tableau del padre aggiungendo/togliendo orlature
- questo schema ad ogni iterazione migliora anche il lower bound (lo fa crescere) dato che toglie il minimo
- questo schema però non scende molto in profondità dato che i lower bound bassi sono in alto nel mio albero
  - tende quindi a non migliorare z_best

**Strategia depth-first**

- quella vista in ricrca operativa
- migliora velocemente z_best
  - comodo se non vogliamo trovare l'ottimo ma ci interessa una soluzione intera buona
- il lower bound non cresce facilmente

esistono anche schemi ibridi che combinano i pregi di entrambe le strategie

- partiamo con depth-first e raggiungo una certa profondità
- continuo con best bound per dimostrare che la soluzione ammissibile trovata è effettivamente ottima

## Come calcolo i lower bound?

vorremmo i lower bound più forte possibile (più grande)

magari il rilassamento continuo classico non ci dà il lower bound migliore possibile

digressione su branch and cut per TSP:

- nel caso del rilassamento continuo del TSP abbiamo visto che per trovare l'ottimo dobbiamo iterare e risolvere vari problemi di separazione
- lo schema che abbiamo visto ha la desiderabile proprietà che anche se non troviamo l'ottimo del rilassamento continuo (non separiamo tutti i SEC violati) abbiamo comunque un LB valido, seppur peggiore

**Per ottenere dei lower bound migliori possiamo ad ogni nodo non solo risolvere il rilassamento continuo ma anche applicare dei tagli (che è quello che facciamo con il problema di separazione)**

- uno schema di branch and bound in cui per trovare i LB applichiamo tagli (non strettamente di gomory?) oltre a fare rilassamenti si chiama branch and cut

curiosità: abbiamo visto che per il TSP per migliorare il LB possiamo aggiungere dei vincoli opzionali che troviamo risolvendo un ulteriore problema di separazione (gli aggiungiamo solo se sono violati)
