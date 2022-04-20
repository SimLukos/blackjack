import random


kalade = {'Sirdys': {'SA': 11, 'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10, 'SJ': 10, 'SQ': 10, 'SK': 10},
            'Bugnai': {'BA': 11, 'B2': 2, 'B3': 3, 'B4': 4, 'B5': 5, 'B6': 6, 'B7': 7, 'B8': 8, 'B9': 9, 'B10': 10, 'BJ': 10, 'BQ': 10, 'BK': 10},
            'Kryziai': {'KA': 11, 'K2': 2, 'K3': 3, 'K4': 4, 'K5': 5, 'K6': 6, 'K7': 7, 'K8': 8, 'K9': 9, 'K10': 10, 'KJ': 10, 'KQ': 10, 'KK': 10},
            'Lapai': {'LA': 11, 'L2': 2, 'L3': 3, 'L4': 4, 'L5': 5, 'L6': 6, 'L7': 7, 'L8': 8, 'L9': 9, 'L10': 10, 'LJ': 10, 'LQ': 10, 'LK': 10}
            }

def kalade_default():
    kalade_default = {'Sirdys': {'SA': 11, 'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10, 'SJ': 10, 'SQ': 10, 'SK': 10},
            'Bugnai': {'BA': 11, 'B2': 2, 'B3': 3, 'B4': 4, 'B5': 5, 'B6': 6, 'B7': 7, 'B8': 8, 'B9': 9, 'B10': 10, 'BJ': 10, 'BQ': 10, 'BK': 10},
            'Kryziai': {'KA': 11, 'K2': 2, 'K3': 3, 'K4': 4, 'K5': 5, 'K6': 6, 'K7': 7, 'K8': 8, 'K9': 9, 'K10': 10, 'KJ': 10, 'KQ': 10, 'KK': 10},
            'Lapai': {'LA': 11, 'L2': 2, 'L3': 3, 'L4': 4, 'L5': 5, 'L6': 6, 'L7': 7, 'L8': 8, 'L9': 9, 'L10': 10, 'LJ': 10, 'LQ': 10, 'LK': 10}
            }
    kalade.update(kalade_default)
    

def korta():
    rusis = random.choice(list(kalade.keys()))
    korta = random.choice(list(kalade[rusis].keys()))
    reiksme = kalade[rusis][korta]
    kalade[rusis].pop(korta)
    return rusis, korta, reiksme

def pradeti():
    #Dalintojas vvvvvvv
    korta1 = korta()
    istraukta_korta1 = korta1[1]
    reiksme1 = korta1[2]
    dalintojo_suma = reiksme1
    #Zaidejas vvvvvvv
    korta2 = korta()
    istraukta_korta2 = korta2[1]
    reiksme2 = korta2[2]
    #-------------------------
    korta3 = korta()
    istraukta_korta3 = korta3[1]
    reiksme3 = korta3[2]
    zaidejo_suma = reiksme2 + reiksme3
    if zaidejo_suma > 21 and (istraukta_korta3  == 'SA' or istraukta_korta3 =='BA' or istraukta_korta3 == 'KA' or istraukta_korta3 == 'LA'):
        zaidejo_suma = zaidejo_suma - 10
    return istraukta_korta1, reiksme1, istraukta_korta2, istraukta_korta3, zaidejo_suma


