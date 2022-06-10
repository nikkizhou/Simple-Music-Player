from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):

        fil = open(filnavn)

        for linje in fil:
            linje = linje.strip().split(';')    # ['Help', 'The Beatles']
            #oprett en sangObjekt basert paa data i linje i filen
            sangObjekt = Sang(linje[1], linje[0])
            #legg sang objektet inn i spillelisten
            self.leggTilSang(sangObjekt)

        fil.close()


    def leggTilSang(self, nySang):
        #Hvis sanget allerede er i spillelisten, skriv ut tilbakemelding.
        if self.sangetFinnes(nySang):
            print(f'Sanget [{nySang}] er allerede i spillelisten.')
        #ellers legg nySang i spillelisten og gi tilbakemelding.
        else:
            self._sanger.append(nySang)
            print(f'Sanget [{nySang}] er lagt til spillelisten!')


    def fjernSang(self, sang):
        #Hvis sanget finnes i spillelisten, remove det.
        if self.sangetFinnes(sang):
            self._sanger.remove(sang)
        #ellers skriv ut tilbakemelding.
        else:
            print(f'Sanget [{sang}] finnes ikke i spillelisten, kan ikke fjerne.')


    def spillSang(self, sang):
        #Hvis sanget finnes i spillelisten, spill det.
        if self.sangetFinnes(sang):
            sang.spill()
        #ellers skriv ut tilbakemelding.
        else:
            print(f'Sanget [{sang}] finnes ikke i spillelisten, kan ikke spille.')

    def spillAlle(self):
        #hvis spillelisten ikke er tom, spill alle sang
        if len(self._sanger) != 0:
            for sang in self._sanger:
                sang.spill()
        #ellers skriv ut tilbakemelding.
        else:
            print('Spillelisten er dessverre tom!')

    def finnSang(self, tittel):
        har_funnet = False
        teller =0
        
        #iter listen til har man har funnet tittelen og returnere det foerste sanget i spillelisten
        while not har_funnet and teller < len(self._sanger):
            if self._sanger[teller].sjekkTittel(tittel):
                har_funnet = True
                return self._sanger[teller]

            else:
                teller +=1

        #hvis man har iterert hele listen og finne ikke tittelen, retureres None
        return None


    #hjelpemetode. 
    #kontroll at sang objektet finnes eller ikke i spillelisten.
    def sangetFinnes(self,sanget):
        #hvis nysang er i spillelisten(har samme artist og tittel): returner True
        for sang in self._sanger:
            if sang == sanget:
                return True
        #ellers: returner False
        return False


    def hentArtistUtvalg(self, artistnavn):
        artistListe = []
    
        #iterer alle sang i spillelisten
        for sang in self._sanger:
            #hvis et sang i listen har samme artist som argumenten, legg det til den nye listen.
            if sang.sjekkArtist(artistnavn):
                artistListe.append(sang)
    
        #hvis artistnavn ikke finnes i spillelisten, skriv ut tilbakemelding og return.
        if len(artistListe)==0:
            print(f'Artisten [{artistnavn}] finnes ikke i spillelisten.')

        #hvis det er minst 1 sang med artistnavn, return artistListen
        return artistListe


    #hjelpemetode
    def toemeSpillelisten(self):
        self._sanger = []
        

    def __str__(self):
        return f'{self._navn}, {self._sanger}'
