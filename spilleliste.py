from sang import Sang           #Importerer fra klassen Sang fra filen sang.py

class Spilleliste:
    def __init__(self, listenavn):  #Lager konstruktøren
        self._sanger = []
        self._navn = listenavn
    def __str__(self):
        return '{self._sanger} {self._listenavn}'.format(self=self)    
    def lesFraFil(self, filnavn):   #Opretter metoden lesFraFil som leser hver linje fra musikk.txt og splitter på
        for linje in open(filnavn):  # ";". Vi bruker videre index på artist og tittel
            alleData = linje.strip().split(";")
            artist = alleData[0]
            tittel = alleData[1]
            self._sanger.append(Sang(artist, tittel))  #Vi bruker append til å legge til artist og tittel til
    def leggTilSang(self, nySang):   #Ny metode leggTilSang                   #listen vår
        self._sanger.append(nySang)   #Bruker append igjen til å legge til nySang til listen.
    def fjernSang(self, sang):
        self._sanger.remove(sang)       #Bruker remove til å fjerne sang. 
    def spillSang(self, sang):
        sang.spill()                    #Bruker spill til å spille sang.
    def spillAlle(self):
        for x in self._sanger:      #Vi lager en for-løkke til å gå gjennom listen og spille hver enkelt sang.
            x.spill()
    def finnSang(self, tittel):     
        for x in self._sanger:      #Vi lager en til før-løkke til å gå gjennom listen og printer hver sang.
            print(x)
            if x.sjekkTittel(tittel) == True:   #if-sjekk som bruekr metoden sjekkTittel for å se om det stemmer
                return x                         #Returnerer x hvis det stemmer.
        return None                             #Ellers None
    def hentArtistUtvalg(self, artistnavn):     
        artistUtvalg = []                       #Lager listen artistUtvalg.
        for x in self._sanger:              #For-løkke som går gjennom listen igjen.
            if x.sjekkArtist(artistnavn):   #if-sjekk som bruker sjekkArtist.
                artistUtvalg.append(x)      #Legger til artistene i listen vi lagde. 
        return artistUtvalg                 #Returnerer artistUtvalg listen.
                                    

