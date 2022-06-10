class Sang:
    def __init__(self, artist, tittel):
        self._artist = artist    #"The Rolling Stones"
        self._tittel = tittel

    def spill(self):
        print(f"Spiller '{self._tittel}' fra artist '{self._artist}'")


    def sjekkArtist(self,navn):
        #konvert baade self._artist og argumenten til lister, og tilordner dem til nye variabler.
        artist_list = self._artist.lower().split() #['the', 'rolling', 'stones']
        navn_list = navn.lower().split()   #[ 'rolling', 'stones']

        riktig_artist = False

        #iter ord i listen av argumenten, hvis ett av ordene i listen er i artist_list, blir True.
        for ord in navn_list:
            if ord in artist_list:
                riktig_artist = True

        return riktig_artist


    def sjekkTittel(self, tittel):
        return tittel.lower() == self._tittel.lower()


    def sjekkArtistOgTittel(self, artist, tittel):
        return self.sjekkArtist(artist) and self.sjekkTittel(tittel)


    def __str__(self):
        return f'{self._tittel}, {self._artist}'

    #Hvis to sang objekter har akurrat samme artist navn og tittel, defineres dem som samme
    def __eq__(self,annen):
        return self._artist==annen._artist and self._tittel==annen._tittel
