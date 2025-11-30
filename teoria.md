1. **Teorema di Prim**
    - dato un albero ricoprente parziale, l'MST ottimo contiene sicuramente il lato più corto di quelli appartenenti alla frontiera
    - dim: per assurdo, se si assume che l'MST ottimo non contiene quel lato, possiamo aggiungerlo e rimuoverne uno appartenente alla frontiera

2. **Teorema di Dijkstra**
    - data una arborescenza parziale, il prossimo arco da prendere è quello di costo cumulato minore tra quelli appartenenti alla frontiera

3. **Teorema di Floyd-Fulkerson**
    - il taglio minimo mi definisce il flusso massimo che riesco a mandare da s a t
        - trovare il flusso massimo equivale a trovare il taglio minimo
        - un taglio s-t è una partizione dei vertici in cui: s appartiene a V1, e t appartiene a V2
    - dim:
        - aumentiamo il flusso iterativamente trovando catene aumentanti (il flusso rimane ammissibile dato che continua a valere la conservazione del flusso)
        - quando non riesco più a raggiungere t, questo significa che per tutti gli archi tra V1 e V2:
            - il flusso è uguale alla loro capacità
            - oppure che il flusso all'indietro vale 0
        - il flusso che riesco a portare da s a t vale quanto il taglio che ho trovato

4. **Quando la matrice dei vincoli di un ILP è TUM, risolvere il rilassamento continuo trova comunque la soluzione ottima intera**
    - La matrice di incidenza di un digrafo è TUM, e quindi si può risolvere il problema del cammino modellandolo come un ILP di un flusso massimo e risolvendo il rilassamento continuo
    - Anche la matrice dei vincoli del problema dell'assegnamento è TUM, e quindi AP si può risolvere con LP del rilassamento continuo

5. **Rilassamento lagrangiano**
    - esempio motivante:
        - minimize x^2+y^2, subject to x+y=1
        - L(x,y,p) = x^2+y^2 + p(1-x-y).
        - vedendo dove la derivata si annulla otteniamo: x = y = p/2
        - ricordandoci del vincolo otteniamo: p = 1
    - l'idea principale del rilassamento lagrangiano è permettere che i vincoli siano violati ma pagare un prezzo quando questo accade
        - introduciamo un moltiplicatore per ogni vincolo
        - lambda' * (b -Ax)
    - quando i moltiplicatori vengono scelti correttamente la soluzione ottima del problema iniziale è uguale a quella ottima del problema rilassato
        - i vincoli non vengono imposti esplicitamente, ma i moltiplicatori giusti posizionano il minimo della funzione obiettivo in un punto in cui i vincoli sono rispettati
    - inoltre, si ha che la soluzione ottima del problema rilassato, anche con moltiplicatori scelti a caso, è sicuramente un lower bound per la soluzione ottima del problema vincolato
        - il problema rilassato è per definizione meno vincolato e i termini lagrangiani possono migliorare il valore della soluzione
        - ogni scelta di moltiplicatori produce un determinato lowerbound, alcuni peggiori altri migliori
    - Da qui nasce il problema lagrangiano duale, ovvero trovare quei moltiplicatori tali che massimizzano il lowerbound del rilassamento lagrangiano
        - trovare i moltiplicatori che massimizzano il lower bound, equivale a trovare i moltiplicatori che rendono la soluzione del rilassamento uguale a quella del vincolato
        - questo perchè il rilassamento è un lower bound -> il lower bound massimo vale tanto quanto la soluzione ottima -> la soluzione ottima si ha solo sei i moltiplicatori sono just right

6. **ATSP**
    - modello
        - x_a = x_(i,j) = 1 -> l'arco a (i, j) del grafo viene preso
        - minimizziamo sum(x_a * c_a) acrosso all a del grafo
        - vincoli di grado mi dicono che
            - somma degli archi su delta+ e delta- di tutti i vertici = 1
        - SEC mi dicono che
            - per qualsiasi sottoinsieme di vertici S, la somma degli archi al suo interno <= |S| - 1
            - equivalentemente, per qualsiasi sottoinsieme di vertici, la somma degli archi sul delta+(S) >= 1
        - infine abbiamo i vincoli binari delle variabili

7. **Rilassamento continuo ATSP**
    - il rilassamento continuo dell'ATSP ha troppi vincoli e quindi dobbiamo rilassarlo ulteriormente rimuovendo i SEC
    - dopo aver risolto il modello doppiamente rilassato, ottenendo come soluzione ottima x*, dobbiamo separare i SEC violati da x* da quelli non violati
    - trovati i SEC violati, quest'ultimi vengono aggiunti al modello e si itera fino a quando il problema di separazione non trova più alcun SEC violato
    - a questo punto la soluzione x* è la soluzione ottima del rilassamento continuo
    - the algorithm works very well in practice in the sense that the final number of constraints is generally much smaller than the total number.
    - risolvere il problema di separazione significa definire un un secondo problema di ottimizzazione e risolvere quest'ultimo con ILP

8. **Modello rilassamento continuo ATSP**
    - si parte con solo i degree constraints
    - separazione
        - data una soluzione corrente x*, vogliamo trovare un sottoinsieme di vertici S* tale che il corrispondente SEC risulti violato (sum(x_a*) > |S| - 1)
        - introduciamo un ILP per il problema di separazione
            - dico solo che abbiamo come variabili decisionali (se consideriamo i SEC nella prima formulazione vista)
                - y_i = {1 se vertice i appartiene a S*, 0 altrimenti}
                - z_a = {1 se l'arco a appartiene ad S*, 0 altrimenti}
            - l'obiettivo è quindi controllare se ho più si |S| - 1 archi
        - dopo aver risolto il problema, se la soluzione ottima ha valore >= 1 (corrisponde a <= |S| - 1) allora tutti i SEC sono soddisfatti
        - altrimenti, le variabili decisionali dell'ILP specificano l'insieme S* che definisce il SEC più violato. Questo sarà il prossimo vincolo da aggiungere

9. **Modello rilassamento continuo ATSP flusso massimo**
    - i SEC nella formulazione di vincoli di connessione impongono che la soluzione corrente x~ induca un sottografo (tutti i vertici ma sottoinsieme degli archi) connesso
        - ossia tale da contenere un cammino dal vertice 1 ad ogni vertice k ∈ V \ {1}
    - Immaginiamo di aver fissato il vertice k ∈ V \ {1}; e che il sottografo definito da x~ abbia come capacità degli archi i valori delle componenti
    - la condizione di connessione equivale a richiedere che il valore di qualunque taglio della forma (S_k, V \ S_k) con 1 ∈ S_k e k !∈ S_k sia almeno 1
    - Quindi, se il vertice 1 non è connesso al vertice k -> esiste un insieme Sk tale che 1 ∈ Sk, k /∈ Sk ed il valore del taglio (Sk, V \ Sk) è minore di 1.
        - questo è il tipo di taglio che stiamo cercando per separare i vincoli violati
    - Per trovare un taglio con queste caratteristiche cerchiamo il taglio di valore minimo dal vertice 1 al vertice k e verifichiamo se questo valore è maggiore o minore di 1.
    - Il problema del taglio minimo è equivalente al problema del flusso massimo che riusciamo a mandare da 1 a k
        - se questo flusso è < 1, allora abbiamo trovato un SEC violato e l'insime S* è composto dai vertici in S_k
        - se il flusso è >= 1 per tutti i k, allora tutti i SEC sono rispettati e la separazione termina
    - Conclusione:
        - per l'ATSP possiamo risolvere la separazione, con n-1 problemi di flusso massimo (uno per ogni k), invece che risolvere un ILP
        - Ad ogni iterazione almeno un vincolo violato (se esiste) viene aggiunto alla formulazione corrente e si riparte con un'altra separazione.
        - Il numero di iterazioni necessarie per risolvere esattamente il rilassamento continuo potrebbe sembrare esponenziale in n dato che ci sono altrettanti SEC da controllare.
        - E stato però dimostrato che la soluzione del rilassamento continuo del modello richiede un numero polinomiale di iterazioni di separazione
            - ciascuna delle quali richiede un tempo polinomiale (n-1 volte n^3);
            - quindi l’intero procedimento di soluzione del rilassamento continuo richiede un tempo polinomiale.
        - Infatti, esistono anche formulazioni alternative di ILP per l'ATSP nella quale il numero di variabili e vincoli è polinomiale.
            - il rilassamento continuo di questi modelli si risolve quindi in tempo polinomiale
            - e questo ci convince empiricamente che la complessità del rilassamento continuo dell'ATSP sia effettivamente polinomiale

10. **Schemi di Row generation**
    - consistono nel risolvere un LP, nel nostro caso il rilassamento continuo di un ILP, con un numero enorme di vincoli aggiungendo iterativamente vincoli violati trovati mediante la risoluzione di un secondo ILP per il problema di separazione
    - questi schemi hanno la particolarità di poter essere interrotti anche prima di aver trovato la soluzione ottima del rilassamento continuo (Full LP), ed avere comunque in mano un lower bound valido (seppur peggiore) dell'ILP
        - il fatto di avere sempre un LB è chiaro, ho risolto un rilassamento con meno vincoli
    - questo è molto buono per schemi di branch and bound in cui si hanno dei timeout, mancanza di vincoli violati dovuti a tolleranze numeriche, risoluzione del problema di separazione in maniera euristica

11. **Schemi di Column generation**
    - questi schemi vengono utilizzati per risolvere LP con un numero di variabili enorme (vedi rilassamento continuo di VCP con stable set)
    - On the contrary of the case of considering a subset of the constraints that requires to test the feasibility of the solution of the reduced LP, if one considers only a subset of the variables one has to test the optimality of the solution of the reduced LP
        - chiaro, qua i vincoli possono essere controllati tutti quindi la soluzione trovata sarà sicuramente ammissibile
        - non possiamo però considerare tutte le variabili (quelle non considerate vengono messe a zero) e quindi dobbiamo controllarei in qualche modo che la soluzione trovata sia ottima
    - The optimality test is possible by exploiting the dual problem of the LP, questo avrà un numero enorme di vincoli
    - Per trovare la soluzione ottima del primale:
        - selezioniamo un sottoinsieme di variabili, e quindi un sottinsieme di A e di c
        - risolviamo l'LP e otteniamo le soluzioni x\* e y\* del primale e del duale
        - se y* non viola alcun vincolo del duale, abbiamo trovato la soluzione ottima primale
        - altrimenti, dobbiamo risolvere il problema di separazione per trovare un vincolo violato nel duale (row generation nel duale)
            - al vincolo violato duale corrisponde una variabile con costo ridotto negativo primale
        - una volta trovata (grazie al duale) la variabile da aggiungere, questa viene aggiunta al LP e si reitera il procedimento
    - Stavolta però, se lo schema di column generation viene interrotto prematuramente, non abbiamo più un LB in mano
        - Risolvere un LP considerando solo una porzione delle variabili mi darà probabilmente una soluzione non ottima per l'intero LP
        - Thus we do not know if it is bigger or smaller than the optimal value of the ILP of which the full LP is the continuous relaxation of
        - Abbiamo un LB per l'ILP solamente se troviamo la soluzione ottima del full LP, in altre parole se completiamo lo schema di column generation
        - Questo complica gli schemi di branch and bound per l'ILP
            - if the column generation is stopped prematurely because of a time limit or because the separation problem of the dual is solved heuristically and no more violated constraints are found, no lower bound is available

12. **branch and bound**
    - In generale abbiamo 3 scelte da fare nello schema di branch & bound:
        - che rilassamento risolviamo per ottenere il lowerbound?
        - data una soluzione del rilassamento non ammissibile, su che variabile facciamo branching?
            - con martello quella che ci pareva
            - un'altra strategia è lo strong branching
                - si guarda un passo in avanti e si risolvono i problemi figli generati da una scelta di variabile di branching
                - per ognuno dei due rami calcoliamo uno score che si basa su quanto la scelta di quella variabile di branching **migliora il bound**
                    - in un problema di minimo, un LB buono è un LB alto dato che più vicino al valore della soluzione ottima intera e quindi **più facilmente potabile**
                    - con strong branching scegliamo come variabile di branching quella che porta ad avere dei bound più alti nei rami figli
                - in questo modo riduciamo il numero di nodi da esplorare, tuttavia abbiamo un forte overhead nel calcolare gli score
                - per ridurre l'overhead possiamo calcolare delle approssimazioni dei rilassamenti continui
                - oppure possiamo utilizzare pseudocosti in cui
                    - si parte strong-branching
                    - si va avanti per un po' con questa strategia in maniera da imparare quali sono le variabili importanti su cui branchare
                        - è importante capire quali sono le variabili importanti nei primi livelli del branch and bound
                    - si procede con approssimazioni
        - quale problema scegliamo dalla lista?
            - con martello facevamo DFS
                - con questa strategia troviamo in fretta una soluzione incumbent
                - tuttavia il lowerbound definito dalla soluzione incumbent rimane basso
            - un altra strategia è best bound
                - si sceglie il nodo con lower bound minore dato che è uno che andrebbe comunque esplorato
                - questa strategia migliora il lower bound dato che elimina quello più basso
                - ma non migliora facilmente la soluzione incumbent dato che non scende in profondità
