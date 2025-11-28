1. Teorema di Prim
    - dato un albero ricoprente parziale, l'MST ottimo contiene sicuramente il lato più corto di quelli appartenenti alla frontiera
    - dim: per assurdo, se si assume che l'MST ottimo non contiene quel lato, possiamo aggiungerlo e rimuoverne uno appartenente alla frontiera

2. Teorema di Dijkstra
    - data una arborescenza parziale, il prossimo arco da prendere è quello di costo cumulato minore tra quelli appartenenti alla frontiera

3. Teorema di Floyd-Fulkerson
    - il taglio minimo mi definisce il flusso massimo che riesco a mandare da s a t
        - trovare il flusso massimo equivale a trovare il taglio minimo
        - un taglio s-t è una partizione dei vertici in cui: s appartiene a V1, e t appartiene a V2
    - dim:
        - aumentiamo il flusso iterativamente trovando catene aumentanti (il flusso rimane ammissibile dato che continua a valere la conservazione del flusso)
        - quando non riesco più a raggiungere t, questo significa che per tutti gli archi tra V1 e V2:
            - il flusso è uguale alla loro capacità
            - oppure che il flusso all'indietro vale 0
        - il flusso che riesco a portare da s a t vale quanto il taglio che ho trovato

4. Quando la matrice dei vincoli di un ILP è TUM, risolvere il rilassamento continuo trova comunque la soluzione ottima intera
    - La matrice di incidenza di un digrafo è TUM, e quindi si può risolvere il problema del cammino modellandolo come un ILP di un flusso massimo e risolvendo il rilassamento continuo
    - Anche la matrice dei vincoli del problema dell'assegnamento è TUM, e quindi AP si può risolvere con LP del rilassamento continuo

5. Rilassamento lagrangiano
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
