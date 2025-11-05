# benvenuti nel nostro progetto(gruppo2) .
#Per cominciare il nostro codice ,per evitare di scrivere a mano in un dizionario tutta la tavola periodica,
#andremo ad usare dal dizionario la voce periodictable ,
#ciò renderà molto piu facile e semplice il lavoro

import periodictable

#la persona prima di andare ad analizzare i composti semplici,
#dovra sapere le informazioni su qualche elemeto della tavola 

#inanzitutto chiedamo alla persona che dovrà usare il codice
#lelemento che andremo ad analizzare 

simbolo=input("inserisci l'elemento sui cui vuoi informazioni(es:Fe,Na,H ....):")

#ora bisognerà fare un passaggio molto importante , andremo a considerare la tavola periodica come
#un grande dizionario con tutti gli elementi esistenti all interno ,quindi:

tavola_periodica={}

#questo dizionario contiene informazioni su tutti gli elementi.
#le informazioni che avremo bisogno per creare i composti sono:
#-massa atomica(M)
#-numero atmico(Z)

for elemento in periodictable.elements:
    tavola_periodica[elemento.symbol]={
        "numero_atomico": elemento.number,
        "massa_atomica": elemento.mass
    }       

#la libreria periodctable fornisce un oggetto chiamato elements,ovvero una lista
#che contiene tutti gli elementi conosciuti.
#Ogni elemento in quella lista è un oggetto con le proprietà fondamentali.  
#Quindi questo ciclo serve per scorrere gli elementi dalla libreria al dizionario, rendendo
#facile l'organizzazione dei dati ,cosi si puo accedere in modo facile
    
#puo capitare che l'utente che usa il codice può sbagliare a scrivere il simbolo dell'elemento,
#allora con questo if qui sotto se l'utente sbaglia il codice glielo fa sapere.

#se invece l'utente scrive correttamente l'elemento da analizzare allora il codice procede a dargli
#le informazioni grazie alla variabile "info"

if simbolo in tavola_periodica:
    info = tavola_periodica[simbolo]
    print("Elemento:", simbolo)
    print("Numero atomico:", info["numero_atomico"])
    print("Massa atomica:", info["massa_atomica"])
else:
    print("Elemento non trovato nella tavola periodica.")
    
#ora che abbiamo permesso all'utente di avere informazioni sugli elementi ,bisognerà creare un codice che
#lo aiuta ad analizzare composti semplici.La libreria periodictable ha una funzione utilissima
#periodictable.formula(formula), che riconosce automaticamente una formula
#chimica e può calcolare la massa molecolare totale.
#però dato che dobbiamo fare il confronto di più composti,chiederemo all'utente di inserire piu composti, delineati da spazi
#il nostro compito attraverso un codice particolare sarà di dividere la stringa in formule da mettere a confronto,quindi:

formule_utente= input("Inserisci una o più formule chimiche separate da spazi (ES:H2O CO2, CH4): ")
formule = formule_utente.replace(",", " ").split()

#ora che abbiamo tutti i composti pronti da esaminare useremo un dizionario per
#salvare il nome di ogni composto e la sua massa molecolare totale.

masse_composti = {}
#Quando Python incontra un errore (ad esempio una formula sbagliata), normalmente il codice non prosegue e ti mostra dove si trova l'errore 
#In questo caso noi non vogliamo che se l'utente scrive un composto che non esiste il codice si ferma ,
#ma che continui con i composti rimanenti avvisando l'utente dell'errore
#ecco che entrano in gioco dei nuovi comandi:try e exept
for f in formule:
    try:
        composto = periodictable.formula(f)
        massa = composto.mass
        masse_composti[f] = massa
        print(f"{f}: massa molecolare = {massa:.3f} u")
    except Exception as e:
        print(f" Errore: la formula '{f}' non è valida ({e})")

#con questo codice si inizierà un ciclo che passerà uno per uno  tutti i composti che l’utente ha scritto.
#Il codice a riga 72  serve per analizzare tutti i composti inseriti dall'utente e quindi serve per analizzare le proprietà di ognuna.
#nella riga successiva il codice  calcola la massa molecolare totale del composto e
#e somma le masse atomiche di tutti gli atomi presenti.

#il codice nella riga 73 aggiunge un elemento nel dizionario masse_composti.
#La chiave è la formula  e il valore è la massa calcolata
#la riga 74 è la piu importante:il codice stampa il risultato sullo schermo con 3 cifre decimali.

if len(masse_composti) > 0:
    primo = list(masse_composti.keys())[0]
    più_leggero = primo
    più_pesante = primo

# dato che il codiche ha bisogno di sapere se cè almeno un composto scritto correttamente ,useremo l'iteratore LEN che conta
#tutti gli elementi scritti correttamente 

    for composto in masse_composti:
        massa = masse_composti[composto]
#attraverso questo ciclo for scorreremo tutti i composti ,permettendoci di fare il confronto 
        
        if massa < masse_composti[più_leggero]:
            più_leggero = composto
#con questo if il codice verificherà se il composto che sta analizzando è minore della massa del composto precedente ,
#e se la condizione è vera il codice aggiornerà il valore della variabile 
        
        if massa > masse_composti[più_pesante]:
            più_pesante = composto

#la stessa cosa succede per il piu pesante
#non rimane che stampare i risultati,quindi se l'utente non ha scritto correttamente nessuno dei composti il codice lo avviserà
    print("Confronto tra composti:")
    print(f"- Il composto più leggero è {più_leggero} ({masse_composti[più_leggero]:.3f} u)")
    print(f"- Il composto più pesante è {più_pesante} ({masse_composti[più_pesante]:.3f} u)")
else:
    print("Nessuna formula valida inserita.")

#spero che il nostro modo di lavorare vi sia piaciuto ,un saluto
