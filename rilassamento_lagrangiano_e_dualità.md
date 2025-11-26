I rilassamenti servono and ottenere upper/lower bound per problemi che non si riescono a risolvere direttamente e per cui bisogna utilizzare approcci tipo branch and bound

Possiamo avere varie tipologie di rilassamento

- constraint elimination
- rilassamento continuo

Ci interessa particolarmente il **rilassamento Lagrangiano**

# Rilassamento Lagrangiano

l'idea è spostare dei vincoli in funzione obiettivo, e penalizzare quest'ultima quando i vincoli vengono violati, a questo punto possiamo eliminare i vincoli e risolvere il problema rilassato

I moltiplicatori sono i pesi che do alla violazione del vincolo

- quali moltiplicatori usiamo?

Il problema rilassato mi da un lower bound valido

- possiamo pensare al fatto che la soluzione ottima del problema non rilassato viene sicuramente migliorata (non peggiorata) dai moltiplicatori e quindi il problema rilassato può solo fare meglio

**NB**: La soluzione del rilassamento non è detta che sia ammissibile, ma se lo è, non è detto che sia ottima anche per il problema originale se il lagrangiano ha rilassato delle disuguaglianze

- è ottima anche per il problema originale solo se le due funzioni obiettivo hanno lo stesso valore (i moltiplicatori non hanno migliorato il valore della soluzione)
- guardando la formula, questo succede: o quando il moltiplicatore vale 0, o quando il vincolo è tight, in tutti i vincoli rilassati

**NMB**: Il problema allora diventa capire quali moltiplicatori usare per ottenere il lower bound maggiore (migliore) possibile (quello in cui i termini lagrangiani non mi hanno aiutato)

- ottenere lower bound grandi mi permette di tagliare via molti rami in uno schema branch and bound
  - se ho una soluzione incumbent di valore già abbastanza basso, avere lower bound alti mi rende più probabile tagliare, altrimenti dovrei esplorare
- in questa maniera la soluzione del rilassamento si avvicina il più possibile alla soluzione ottima per il non rilassato (che ricordiamo essere lower bounded dal rilassamento)
- inoltre, è facile che la soluzione del rilassamento diventi anche ammissibile

Cercare i moltiplicatori che mi massimizzano il valore del rilassamento mi definiscono un altro LP -> problema lagrangiano duale

**NMB**: il rilassamento lagrangiano permette di trovare l'ottimo del problema non rilassato se riusciamo a trovare quei valori dei moltiplicatori the presence or absence of the constraints does not affect the optimal cost e garantisce che i vincoli rilassati siano rispettati

```It turns out that the right prices can be found by solving a new linear programming problem, called the dual of the original.```

## Rilassamento lagrangiano di equazioni

il procedimento è praticamente identico a prima

stavolta però se i vincoli rispettati il termine lagrangiano diventa nullo

in altre parole **se la soluzione del rilassamento è ammissibile**, allora i valori delle due funzioni obiettivo sono identici, e quindi **la soluzione ottima del rilassamento è ottima anche per il problema originale!**

Il problema diventa quindi trovare il valore dei moltiplicatori tali che i vincoli non siano violati

- "**When the price is properly chosen** (p = 1, in example), the optimal solution to the constrained problem is also optimal for the unconstrained problem."
- anche qui si passa per il problema (di massimizzazione) del lagrangiano duale

# Rilassamento lagrangiano e dualità

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

```
In summary, the construction of the dual of a primal minirnization problem can be viewed as follows.

We have a vector of parameters (dual variables) p, and for every p we have a method for obtaining a lower bound on the optimal primal cost (troviamo il minimo del problema non vincolato studiando la derivata della funzione obiettivo con i termini lagrangiani).

The dual problem is a maximization problem that looks for the tightest such lower bound with p as the vector of decision variables.

Il dual problem sembra quindi non essere soggetto a vincoli, tuttavia, for some vectors p, the corresponding lower bound is equal to -inf, e nel contesto di un problema di massimizzazione does not carry any useful information. Thus, we only need to maximize over those p that lead to nontrivial lower bounds, and this is what gives rise to the dual constraints.
```
