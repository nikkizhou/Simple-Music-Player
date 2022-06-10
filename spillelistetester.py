from pydoc import allmethods
from sang import Sang
from spilleliste import Spilleliste

def hovedprogram():

    allMusikk = Spilleliste('Hele musikkbiblioteket')
    allMusikk.lesFraFil('musikk.txt')
    
    print("\nTester spillAlle: Spiller alle sanger i listen:")
    allMusikk.spillAlle()
    print()
    
    nySang = Sang("Jahn Teigen", "Mil etter mil")
    print("Spiller ny sang:")
    allMusikk.spillSang(nySang)
    print()   
	 
    allMusikk.leggTilSang(nySang)
    print("Spiller alle sanger i listen inkl ny sang:")
    allMusikk.spillAlle()
    print()
    
    funnetSang = allMusikk.finnSang("Mil etter mil")
    if funnetSang is not None:
        print("Fant sangen:")
        allMusikk.spillSang(funnetSang)
    else:
        print("Fant ikke sangen\n")
    assert(funnetSang in allMusikk.hentArtistUtvalg("Jahn"))
    print()
    
    # Tester om flere sanger returneres for samme artist
    queenListe = allMusikk.hentArtistUtvalg("Queen")
    print("Spiller sanger med Queen hentet fra listen: ")
    for queenSang in queenListe:
        queenSang.spill()
    
    allMusikk.fjernSang(funnetSang)
    assert(not (funnetSang in allMusikk.hentArtistUtvalg("Jahn")))
    
    #test Legg til et sang som allerede finnes i listen
    print('\n(NY) Legg til et sang som allerede finnes i listen:')
    allMusikk.leggTilSang(Sang("The Beatles", 'Help'))

    #test hentArtistUtvalg med et artistnavn som ikke finnes i spillelisten
    print('\n(NY)Test hentArtistUtvalg med et artistnavn som ikke finnes i spillelisten: ')
    noneListe = allMusikk.hentArtistUtvalg("abc")

    #test fjernSang og spillSang med et sang som ikke finnes i spillelisten
    print('\n(NY)Test fjernSang og spillSang med et sang som ikke finnes i spillelisten: ')
    allMusikk.fjernSang(Sang("en artiskt", 'et sang'))
    allMusikk.spillSang(Sang("en artiskt", 'et sang'))

    #test spillAlle med en tom spillelist
    print('\n(NY)Test spillAlle med en tom spillelist: ')
    allMusikk.toemeSpillelisten()
    allMusikk.spillAlle()


hovedprogram()
