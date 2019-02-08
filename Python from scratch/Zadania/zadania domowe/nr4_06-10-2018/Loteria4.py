from Loteria2 import moj_zaklad
from Loteria3 import wszystkie_zaklady

def czy_jest_zwyciezca(zwycieskie_liczby):
    #for zwycieskie_liczby in zwycieskie_liczby:
    if zwycieskie_liczby in wszystkie_zaklady:
        print('Mamy zwycięzcę I stopnia, który poprawnie skreślił liczby: ',zwycieskie_liczby)
    else:
        print('Tym razem nie ma zwycięzcy')


czy_jest_zwyciezca(moj_zaklad)
