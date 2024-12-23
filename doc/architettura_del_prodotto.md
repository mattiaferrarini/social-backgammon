Panoramica di alto livello e componenti principali
--------------------------------------------------

Ad alto livello, andiamo a considerare grossolanamente la descrizione del progetto scelto: si tratta di una **web application** che permetta
di giocare a backgammon online **tra due persone** o **tra persona e un ”agente intelligente”**; deve permettere di organizzare tornei fino a 4 giocatori e anche di tenere una **leaderboard** basata sui rating personali. I giocatori dovranno avere modo di trovarsi e sfidarsi, concordare la modalità e i tempi di gioco, giocare la partita e salvarla, vedere i propri risultati in una classifica generale (leaderboard). Il prodotto dovrà inoltre essere **collegato ad uno o più social network** per poter commentare e cercare partner.

L'architettura del prodotto sarà fedele al modello di architettura three-tier, ovvero avremo i seguenti 3 livelli concettuali:

1. **Presentation Tier / Front-End**: interfaccia tramite cui l'utente interagisce col prodotto.
2. **Logic Tier / Back-End**: logica applicativa sottostante che gestisce il gameplay, l’AI e il multiplayer; dovrà inoltre implementare l'integrazione con i servizi di autenticazione e social network.
3. **Data Tier / Database**: si occupa della memorizzazione dei dati quali i profili utente, le partite salvate, i punteggi e la leaderboard.

Andiamo dunque a considerare nel dettaglio ciascuno dei 3 livelli.

### Front-End

Dovrà essere accessibile da desktop e dispositivi mobili, dunque essere reattivo. Tramite questo livello, l'utente dovrà poter:

* **Accedere e gestire l'account**: login e registrazione, gestione dei profili, con integrazione con social network.
* **Avviare partite**: con amici, giocatori casuali o con l'AI.
* **Giocare**: visualizzare ed interagire con il tavolo da gioco.
* **Visualizzare la leaderboard:** classifiche globali o per amici, con la possibilità di condividere i risultati sui social network.

A questi scopi, prevediamo di utilizzare tecnologie quali **HTML+CSS** per lo stile, **Vue.js** come framework JavaScript per creare una Single-Page Application, **WebSocket** per la comunicazione in tempo reale con il backend, in particolare per il multiplayer.

### Back-End

Si occupa della logica applicativa sottostante alle funzionalità del prodotto. In particolare, saranno qui implementati:

* **Gestore delle partite**: sincronizza gli eventi di gioco, monitora lo stato delle partite e aggiorna ciascun giocatore in tempo reale.
* **Avversario AI**: modulo dedicato all’AI che si interfaccia con il motore di gioco per selezionare le mosse contro il giocatore umano. Potrebbe basarsi su algoritmi di minimax oppure su modelli AI pre-addestrati.
* **Leaderboard e gestione punteggi**: memorizzazione e recupero delle classifiche globali e degli amici, consentendo agli utenti di confrontare i propri punteggi con quelli degli altri giocatori.
* **Autenticazione**: gestisce l'accesso degli utenti, le registrazioni e l'integrazione con i social network.
* **Gestore delle sessioni di gioco**: Questo componente si occupa di tenere traccia delle sessioni attive, salvare i progressi delle partite in caso di disconnessione e permettere agli utenti di riprendere le partite salvate.

A questi scopi, prevediamo di utilizzare a questo livello tecnologie per la costruzione dei microservizi, per la gestione della comunicazione in tempo reale tra i giocatori, per lo sviluppo di API RESTful per comunicare con il Front-End e con servizi esterni, per l'autenticazione degli utenti tramite servizi esterni (es. Facebook), ed infine eventuali tecnologie per l'AI.

### Database

Utilizzato per la memorizzazione e gestione dei dati persistenti necessari al corretto funzionamento persistente del prodotto, ovvero:

* **Utenti**: memorizzazione dei profili utente, inclusi i dati personali, le impostazioni di gioco e le preferenze.
* **Partite**: salvataggio delle sessioni di gioco, inclusa la modalità, lo stato delle partite (in corso, completate), il punteggio finale e la cronologia delle mosse.
* **Leaderboard**: registrazione e aggiornamento continuo dei punteggi dei giocatori e delle classifiche.

Si baserà su una tecnologia per gestione di database.

Interazione tra componenti
--------------------------

**Frontend ↔ Backend**: tramite WebSocket per il multiplayer, tramite API RESTful per tutto il resto.

**Backend ↔ Database**: tramite la tecnologia per gestione di database scelta.

**Backend ↔ API Social**: tramite un'apposita tecnologia.

Deployment e diagramma UML di deployment
----------

Il deployment si baserà sui servizi per i tre livelli descritti sopra: frontend, backend, database.

![Diagramma UML di deployment](uml/sprint0_uml_deployment.png)


Diagramma UML per use cases
----------

![Diagramma UML per use cases](uml/sprint0_uml_use_cases.png)