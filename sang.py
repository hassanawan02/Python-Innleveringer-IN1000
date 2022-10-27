class Sang:
    def __init__(self, artist, tittel): #Lager konstruktøren
        self._tittel = tittel
        self._artist = artist
    def __str__(self):
        return '{self._tittel} {self._artist}'.format(self=self)    
    def spill(self):        #Lager metoden spill der vi printer ut tittel og artist.
        print("Spiller av " + self._tittel + " av " + self._artist)
    def sjekkArtist(self, navn):
        for x in navn.split(" "):       #For-løkke som går gjennom navn og splitter på mellomrom
            if x in self._artist.split(" "): #if-sjekk for å sjekke om noen av navnene er lik artistene.
                return True                 #Returnerer True om det stemmer.
        return False                    #Ellers False.
    def sjekkTittel(self, tittel):
        if tittel.lower() == self._tittel.lower():  #if-sjekk og vi bruker lower for å sjekke med kun små bokstaver
            return True                             #Returnerer True om det stemmer.
        else:
            return False                            #Ellers False.
    def sjekkArtistOgTittel(self, artist, tittel):  #Siste metode og sjekk.
        if self.sjekkArtist(artist) == True and self.sjekkTittel(tittel) == True:   #if-sjekk som sjekker om sjekkArtist og sjekkTittel stemmer. 
            return True         #Returnerer True hvis det stemmer.
        else:
            return False        #Ellers False.
