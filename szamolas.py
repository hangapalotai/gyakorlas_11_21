
szam1=int(input('Kérem az első számot!'))
szam2=int(input('Kérem a második számot!'))
muvelet=str(input('Milyen műveletet végezzek el (+ / - *)?'))

if muvelet:str('+')

def osszead(szam1,szam2):
        print(szam1+szam2)
osszead(szam1,szam2)
    
if muvelet:str('-')

def kivon(szam1,szam2):
        print(szam1-szam2)
kivon(szam1,szam2)

if muvelet:str('*')

def szoroz(szam1,szam2):
        print(szam1*szam2)
szoroz(szam1,szam2)

if muvelet:str('/')

def oszt(szam1,szam2):
    if szam2==0:
        return(" Nullával nem lehet osztani")
    else:
        print(szam1/szam2)
oszt(szam1,szam2)