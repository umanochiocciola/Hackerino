import time
print("starting shell...")
usernam = input("Userneim: ")
#listahDelNoce
Commands = {
    "Compiuterz, attiva la modalità hackering": "Certo mio signore e padrone " + usernam + ", cosa vorrebbe hackerizzare?",
    "Vorrei accedere ai databeis delle attività della Vodaferx": "Certo mio signore e padrone " + usernam + ", la collego subito col databeis...\nX=fac\nDatabeis=c6 dentro\nBenvenuto nei databeis della Vodaferx. Prego inserire il proprio ID di dipendente",
    "no, grazie.": "Mi scusi, " + usernam + " ma l'ID è obbligatorio",
    "Mi scusi, ma cerca rissa?": "Oscit ecco i databeis mi skoosee: \n 21/1/2020: malvagità assortita\n 29/1/2020 malvagità meno assortita\n 6/2/202...\nxycdxyzsn....\nRilevata intrusione, inizializzazione sequenza di tracciamento: " + usernam,
    "/BeegCeffone to ProceduraTracciamento": "Muorizzazione sequenza di tracciamento.\nRicaricaggiamento del databeis delle attività...\n21/1/2020: malvagità assortita\n29/1/2020 malvagità meno assortita\n6/2/2020 DEESTROOGGERE IOSONOMELLIODITU",
    "Annulla attività 6/2/2020": "ERROR 69: Comando= nonono. Inizializzazione sequenza di tracciamento inceffonabile: " + usernam,
    "OhScit.exe": "NOPE."
}
#picchone
while 1 == 1:
    a = input("$" + usernam + "_hack.shell >")
    print("> " + Commands.get(a, "Invalid input, blyat!"))
    if a == "OhScit.exe":
        print(usernam + ", 6 stato BANNED!")
        time.sleep(1)
        break
print("closing shell...")
