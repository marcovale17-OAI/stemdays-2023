import streamlit as st
import os
from PIL import Image

st.set_page_config(layout="wide")


#root_images_path = os.path.join(
#    os.path.dirname(os.path.dirname(__file__)), "STEMDays_test", "images"
#)

#st.write = os.path.join(root_images_path, 'stemdays_photo.jpg')
#image = Image.open(os.path.join(root_images_path, 'stemdays_photo.jpg'))


st.title("HYDRA.it")

st.subheader("Steam Days 2023")

tab1, tab2 = st.tabs(["Introduzione", "Chi siamo"])

with tab1:
    st.subheader("Gusti musicali in rapporto ai disturbi mentali")
    st.markdown("""
    ★ANSIA
    ★DEPRESSIONE
    ★INSONNIA
    ★OCD

    ANSIA\n
    I disturbi d’ansia sono un insieme di disturbi psichiatrici che condividono tra loro una caratteristica comune. In tutti infatti è presente una eccessiva paura o ansia che determina una serie di problematiche comportamentali associate come l’evitamento o l’eccessiva richiesta di rassicurazioni.
    I disturbi d’ansia sono un insieme di patologie psichiatriche che sono particolarmente comuni nella società occidentale rappresentando la patologia psichiatrica più diffusa nella popolazione generale. Questi disturbi  possono variare di intensità e gravità, portando anche a disabilità nelle forme più severe. Se non adeguatamente curati tendono a cronicizzare, con periodi di manifestazioni sintomatologiche alternate a periodi di parziale remissione.
    I disturbi d’ansia classificati dal DSM-5 sono:
    •Disturbo d’ansia da separazione
    •Mutismo selettivo
    •Fobia specifica
    •Disturbo d’ansia sociale
    •Disturbo di panico
    •Agorafobia
    •Disturbo d’ansia generalizzata

    DEPRESSIONE\n
    Dopo l’ ansia, la depressione è il disturbo mentale più comune. Circa il 30% delle persone che ricorre al medico di base presenta sintomi di depressione, ma meno del 10% di esse ha una depressione grave. In genere, la depressione si sviluppa negli adolescenti, nei ventenni o nei trentenni, sebbene possa comparire a qualsiasi età, compresa l’infanzia.I disturbi depressivi sono caratterizzati da tristezza tanto grave o persistente da interferire con il funzionamento e, frequentemente, da diminuzione d'interesse o di piacere nelle attività. La causa precisa è sconosciuta ma probabilmente include una componente ereditaria, modificazioni nei livelli neurotrasmettitoriali, alterazioni della funzione neuroendocrina e fattori psicosociali. 

    INSONNIA\n
    Per insonnia s’intende la difficoltà ad addormentarsi o a restare addormentati ed una scarsa qualità del sonno. Quando la qualità del sonno è scarsa, al mattino non ci si sente riposati o freschi.
    L’insonnia può evolversi in EDS, per sonnolenza diurna eccessiva (excessive daytime sleepiness, EDS) s’intende avere molta difficoltà a restare svegli durante il giorno.
    Chi soffre di queste patologie può:
     Essere irritabile e avere difficoltà di concentrazione
    Addormentarsi al lavoro o a scuola
    Correre un maggior rischio di avere un incidente d’auto

    OCD\n
    l disturbo ossessivo-compulsivo è caratterizzato da pensieri ricorrenti, persistenti, non voluti e intrusivi o da immagini (ossessioni) e/o comportamenti ripetitivi o azioni mentali che i pazienti si sentono spinti a compiere (compulsioni) per cercare di diminuire o evitare l'ansia che provocano tali ossessioni. 
    Il disturbo ossessivo-compulsivo si manifesta più comunemente nelle donne rispetto agli uomini e colpisce circa il 1-2% della popolazione. L'età media di insorgenza del disturbo ossessivo-compulsivo è tra i 19 e i 20 anni, ma circa il 25% dei casi comincia entro i 14 anni. 

    Molte persone con disturbo ossessivo-compulsivo presentano coesistenti disturbi psicologici, tra cui
    Disturbi d'ansia (76%)
    Un disturbo depressivo o un disturbo bipolare (63%)
    Disturbo di personalità ossessivo-compulsivo (dal 23 al 32%)
    Da più di un quarto a circa due terzi delle persone con disturbo ossessivo compulsivo a un certo punto ha pensieri suicidi, e dal 10 al 13% tenta il suicidio.

    La misurazione delle preferenze musicali
    Le prime ricerche sui gusti musicali in psicologia della personalità sono basate sulla misura delle preferenze per brevi estratti di brani musicali somministrati ai soggetti (Cattell e Saunders, 1954; Keston e Pinto, 1955), secondo un approccio che presentava alcuni limiti posti dalla scelta dei brani da parte dello sperimentatore e dall’uso quasi esclusivo di musica classica.
    Più di recente, negli anni ’80, si è ricorso ad un altro metodo: le preferenze venivano misurate con una scala di tipo Likert rispetto a un elenco di generi musicali contenente degli esempi di autori rappresentativi (Christenson e Peterson, 1988; Litle e Zuckerman, 1985; Dollinger, 1993; Rawlings e Ciancarelli, 1997).

    La Musical Preference Scale di Litle e Zuckerman
    La scala di preferenze musicali costruita da Litle e Zuckerman (1985) è stata utilizzata negli Stati Uniti e in Australia, in diverse ricerche sulle preferenze musicali.
    Questa scala è costituita da una prima parte in cui sono presenti alcune domande sugli interessi musicali, sul tempo di ascolto e sul tipo di conoscenze e competenze in campo musicale, e da una seconda in cui viene chiesto di dare un giudizio di preferenza su una scala Likert a 5 punti per una serie di generi musicali divisi in ulteriori categorie rappresentative dei diversi tipi di musica presenti sul mercato. La selezione è stata infatti ottenuta sulla base delle indicazioni del mercato discografico, prendendo a riferimento le classificazioni dei principali distributori di dischi (i generi vanno dal rock, al jazz, al pop, alle colonne sonore, alla musica elettronica ed alla musica classica).

    Le teorie della personalità confrontate con i gusti musicali
    Gli studi sul rapporto tra le preferenze musicali e le caratteristiche di personalità hanno fatto riferimento principalmente a quattro modelli teorici:
    la teoria dei tratti di Cattell,
    la teoria di Eysenck,
    la teoria della “ricerca di sensazioni” di Zuckerman,
    il modello dei 5 fattori (Big Five).

    La ricerca di Cattell
    Il suo modello è basato su una serie di tratti, intesi come strutture mentali per osservare il comportamento di determinati soggetti in specifiche situazioni(1982). Rispetto alle preferenze musicali Cattell ha cercato di individuare i tratti collegati ai diversi gusti musicali per distinguere e definire quali tipi di musica sarebbero potuti risultare “terapeutici” per particolari tipi di personalità. A tale scopo ha creato un apposito strumento di misura, il Music Preference Test Personality IPAT, per valutare le preferenze e confrontarle con gli aspetti della personalità.

    Il modello della personalità di Eysenck
    La prima elaborazione di questo modello (Eysenck, 1960) è basata su due superfattori l’estroversione–introversione ed il nevroticismo, è successiva l’aggiunta di un terzo fattore, lo psicoticismo.    
    Eysenck analizza l’estroversione e l’introversione in rapporto con il livello di eccitazione dell’individuo. Così, per effetto di un elevato livello di eccitazione interna gli introversi tendono ad evitare la stimolazione esterna per evitare un eccesso di stimolazione, mentre gli estroversi, avendo un basso livello di eccitazione, sono inclini a più intense stimolazioni esterne per raggiungere e mantenere un livello di stimolazione per loro ottimale. 
    Studi più dettagliati sulla dimensione di psicoticismo sono stati condotti da Rawlings, Hodge, Sherr e Dempsey (1995), su diverse sfaccettature delle preferenze musicali, da cui sono emerse delle correlazioni con le scelte per l’hard rock rispetto alla musica più semplice da ascoltare ricorrendo a due metodi diversi, cioè misurando i gusti musicali sia con l’ascolto diretto di brani rappresentativi di quattro generi differenti, sia con la Scala di preferenze musicali di Litle e Zuckerman, da cui sono emersi risultati concordanti; inoltre è stato messo in risalto che i soggetti con alto livello di psicoticismo preferivano di più accordi di tipo dissonante, rispetto a quelli con un livello minore che invece preferivano accordi consonanti, il che potrebbe spiegare le preferenze per l’hard rock, come preferenze per i suoni duri, rumorosi, tipici di questo tipo di musica. Sono state anche confrontate le preferenze per i brani musicali ascoltati e gli accordi di diverso tipo su uno stesso gruppo di soggetti, dando conferma dei risultati precedenti ottenuti separatamente.

    Il Big Five e il NEO Personality Inventory
    Le ricerche più recenti fanno riferimento al modello dei 5 fattori di personalità (Dollinger, 1993; Rawlings e Ciancarelli, 1997) e al NEO-PI (Costa e McCrae, 1992).
    I cinque fattori sono stati cosi indicati:
    1) “estroversione/introversione”
    2) ”gradevolezza/ostilità”
    3) ”coscienziosità”
    4) ”stabilità/instabilità emotiva o nevroticismo”
    5) “apertura all’esperienza” 

    Dall’analisi effettuate su 3 fattori musicali, le 5 scale di personalità del NEO-PI e le variabili demografiche sono risultate 3 variabili canoniche che hanno spiegato il 100% della varianza. La prima variabile legava le preferenze per la popular music, un basso livello di “apertura all’esperienza“, “estroversione” e scarso interesse per la musica; la seconda univa le preferenze per il rock e una tendenza a non preferire le altre musiche con poca competenza musicale, l’essere maschi e l’incoscienza; la terza variabile univa tutti i tipi di musica con la tendenza ad essere aperti all’esperienza ed estroversi.""")


with tab2:
    st.subheader("Presentazione Lavoro")
    if st.button("Festeggia con noi", help="Prova a vedere cosa succede"):
        st.balloons()
    st.markdown("""Questo sito è stato pensato e creato da un team di 10 ragazze tra i 16 e i 18 anni di Torino. L’idea è nata durante la partecipazione agli STEMDAYS, un campo di sole ragazze che ha l’obiettivo di abbattere i pregiudizi legati al ruolo femminile nel mondo della scienza e della tecnologia. Questa non è solo una pagina sul web che affronta il tema della musica in relazione ai disturbi mentali, ma il prodotto del lavoro di due settimane vissute insieme unite dal principio della collaborazione e dell’impegno al fine di portare al termine un progetto che possa essere utile e interessante per chi lo legge.""")
    #st.image(image, caption='Il Team')
    st.divider()


