Nato come colorazione di mappe geografiche

Questo lo posso vedere come un problema su grafo immaginando

- un vertice per ogni regione
- un lato per ogni confine tra due regioni
- assegnare un colore a tutti i vertici in modo che vertici collegati da lati abbiano colori diversi

## Teorema dei 4 colori

Qualunque **mappa** io voglia colorare, 4 colori sono sufficenti

- NB: posso pensare ad un grafo completo con 5 vertici per cui 4 colori non sono sufficenti
- tuttavia grafi di questi tipi non si traducono in mappe

## altri problemi motivanti

- scheduling di orari
- frequency assignment
- air traffic control
- register allocation

Tutti questi sono modellabili come VCP

In linea generale abbiamo degli utenti che vogliono accedere alla stessa risorsa; tuttavia, tra gli utenti ci sono delle incompatibilità che non mi permettono di assegnare la stessa copia della risorsa agli utenti affetti da una incompatibilità.

# Vertex Coloring Problem (VCP)

Datu un grafo non orientato, vogliamo assegnare un colore ad ogni vertice in maniera tale che vertici adiacenti abbiano colori diversi, e minimizzando il numero di colori

- numero cromatico del grafo = numero minimo di colori del grafo
- un insieme di vertici che ricevono lo stesso colore si chiama classe di colore

## Complessità

sempre NP-Hard come TSP ma anche più difficile per istanze del problema artificiali difficili

- nella pratica le istanze sono facili

# Approcci greedy

algoritmo sequenziale

- posso poi iterare su una permutazione diversa dei nodi
- tuttavia le permutazioni sono n! ...
- non è molto intelligente

algoritmo che considera il grado cromatico

- voglio prima risolvere i vertici più vincolati
- questo funziona meglio dell'algoritmo sequenziale

## Quanto sono buone queste soluzioni euristiche?

Dobbiamo capire quel'è il minimo numero di colori per un grafo

Notiamo che in un sottografo completo tutti i vertici devono ricevere colori diversi

- un sottografo completo viene chiamato **Clique**
- la cardinalità di una clique ci da un lower bound sul nuero di colori necessari per il grafo
- quindi vogliamo trovare la clique massima per avere il lower bound più grande possibile
- purtroppo anche questo è un problema NP-Hard
- tuttavia, costruire una clique massimale non è difficile
  - massimo = la più grande possibile
  - massimale = non più ulteriormente espandibile
  - per trovare la clique massimale posso utilizzare un algoritmo costruttivo che ad ogni iterazione aggiunge un nodo alla clique controllando che il nodo che si sta considerando sia adiacente a tutti quelli della clique

Ci sono dei casi in cui anche il lower bound denotate dalla clique massima è minore stretto del grado cromatico del grafo completo?

- si, in generale il lower bound della clique non è tight

**NB**: Quello che rende difficile il problema è che il rapporto chi/omega può essere arbitrarly bad

- questo però è il caso artificiale dei grafi costruiti apposta per essere difficili da colorare

# Approcci esatti

possiamo utilizzare un algoritmo branch & bound che lavora direttametne sul problema

qua il branching non è binario (non ho solo due figli)

il mio albero decisionale ha nodi che rappresentano una colorazione parziale del grafo

- al nodo radice nessuno vertice è colorato
- ai nodi foglia tutti i vertici sono colorati

il prossimo nodo da colorare è quello di massimo grado cromatico

ad ogni nodo posso avere al massimo k+1 figli

per costruzione non posso usare gli stessi colori che ho già usato, dato che sto usando quello di massimo grado cromatico

il procedimento mi permette di trovare anche una clique che mi definisce un LB

quando arrivo ad una foglia ottengo un un nuovo UB e quindi posso cominciare a tagliare

## Modello ILP

ho delle variabili binarie x_ih che valogno uno se il vertice i ha il colore h

i è l'indice dei vertici

...

Questo però è un modello debole. Due problemi:

- ottengo soluzioni che mi danno un lower bound ridicolo
- il modello è completamente simmetrico questo mi porta ad avere un sacco di soluzioni equivalenti il che mi porta a fare branching per molto tempo

La debolezza del modello viene da

- sto assegnando i colori ai vertici ... (?)
- i vincoli non sono scritti in modo intelligente
  - posso scrivere i vincoli per clique
  - questi mi elimina le soluzioni frazionarie del rilassamento continuo che valevano prima

slide 25

- max sta per maximal
- generare tutte le clique è infattibile dato che sono in numero esponenziale
  - (più che per ogni, è un alcune)
- posso generare alcune clique con delle euristiche e più ne metto nel modello, meglio è

rimane però l'altro problema (che non mi sono perso zio pera)

### Stable sets

complemento della clique

un insieme di vertici che non contiene nessuno lato

stable set e clique sono lo stesso problema uno sul grafo complementare dell'altro

osservazione fondamentale: una colorazione ammissibile mi definisce un partizionamento del grafo in stable sets

forse posso usare questo modello per scrivere un modello completamente diverso

## Modello per stable set

ipotizziamo di aver enumerato tutti gli insiemi stabili del grafo

- NB: sono esponenziali o(numero di sottoinsiemi di vertici del grafo), che abbiamo visto essere o(2^n)
- non tutti i sottoinsiemi saranno stabili ma l'upper bound è quello

variabili binarie ognuna associata agli stable set della famiglia

- sono quindi un numero esponenziale di variabili

i vincoli mi dicono che per tutti gli stable set che contengo il vertice i ne devo scegliere solo 1

il fatto che vertici adiacenti ricevano colori diversi non sta più nel modello ma sta nella definizione delle variabili

questo modello mi da un lower bound migliore

Oss: dire che ogni vertice deve ricevere esattamente un colore e dire che ogni vertice riceve almeno un colore sono due formulazioni dei vincoli diverse che però mi portano alla stessa soluzione ottima (non riesco ad usare dei colori in meno anche se uso la seconda formulazione)

- se un vertice è colorato due volte, tolgo il secondo colore

Questo è il modello migliore che abbiamo, ha però comunque un problema: abbiamo un numero esponenziale di variabili!

- passiamo dal duale che trasforma il numero esponenziale di variabili in un numero esponenziale di vincoli
- utilizziamo la procedura che risolve il TSP, che ha un numero esponenziale di vincoli
