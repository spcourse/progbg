# Tentamen Inleiding Programmeren voor Bèta-gamma

Datum: 03-02-2023

Dit is een digitaal tentamen. Het tentamen bestaat uit 4 opdrachten waarin je een kort Pythonprogramma moet schrijven.

Je wordt alleen beoordeeld aan de hand van de correctheid van je code, niet op _design_. Je hoeft dus geen commentaar te schrijven of je zorgen te maken over de style guide.

Je kan je uitwerking verifiëren met checkpy. Download de checkpy voor de tentamens:

    checkpy -d /spcourse/exam-tests

Run checkpy:

    checkpy tentamen23_1

# Regels

- Maak alle opdrachten in een bestand genaamd `tentamen23_1.py` en lever deze file in.
- Je mag geen `numpy` of ander python module gebruiken. Dus geen `import`!
- Gedurende het tentamen mag je geen bronnen op internet raadplegen, afgezien van de progbg.mprog.nl website en de IDE.
- Je kan tijdens het tentamen geen hulp krijgen van de docenten en assistenten.
- Submit je oplossingen als je klaar bent. **Voor je de tentamenzaal verlaat, check met de surveillant dat je tentamen correct is ingeleverd!**

### 1: Optellen en delen

Schrijf een functie genaamd `sum_divisors(n)` die de som van alle delers van een gegeven getal teruggeeft. Bijvoorbeeld de `sum_divisors(6)` zou 12 moeten geven (namelijk $$1 + 2 + 3 + 6$$). Zoals je aan het voorbeeld ziet, `1` en `n` tellen zelf ook mee als delers.

Gebruiksvoorbeeld:

    print(sum_divisors(6))
    print(sum_divisors(12))

Verwachtte output:

    12
    28

### 2: Vowels

Schrijf een functie `count_vowels(text)`. De functie verwacht een string als input en returnt het aantal klinkers (a, e, i, o, u) in de string. Houd er rekening mee dat hoofdletters ook moeten worden meegerekend.

Gebruiksvoorbeeld 1:

    example_text = "Hello, world!"
    print(count_vowels(example_text))

Verwachtte output:

    3

Gebruiksvoorbeeld 2:

    example_text = "Exclent eggs!"
    print(count_vowels(example_text))

Verwachtte output:

    3

### 3: Gemeen

Schrijf een functie genaamd `gcd(a, b)` die de grootste gemene deler (Greates Common Divisor) van twee gegeven getallen teruggeeft.

> De grooste gemene deler van `a` en `b` is het grootste getal dat een deler is van zowel `a` als `b`. Bijvoorbeeld voor 24 en 60 zijn de gemene delers 1, 2, 3, 4, 6 en 12. De grooste gemene deler is dus 12.

Gebruiksvoorbeeld:

    print(gcd(24, 60))
    print(gcd(10, 25))

Verwachtte output:

    12
    5

### 4: Home again

Voor deze opdracht ga je het databestand [barca.txt](barca.txt) gebruiken. Dit bestand bevat de resultaten van het voetbalelftal van Barcelona (seizoenen 11/12 tot en met 13/14). De inhoud ziet er als volgt uit:

    29/08/11,Villarreal,won,5,0,home
    10/09/11,Sociedad,draw,2,2,away
    17/09/11,Osasuna,won,8,0,home
    ...
    03/05/14,Getafe,draw,2,2,home
    11/05/14,Elche,draw,0,0,away
    17/05/14,Ath Madrid,draw,1,1,home

Zoals je ziet zijn de velden gescheiden door komma’s en bevatten de volgende informatie:

0. de datum van de wedstrijd
1. de tegenstander
2. het resultaat: gewonnen/verloren/gelijkgespeeld (won/lost/draw)
3. het aantal goals voor Barcelona
4. het aantal goals voor de tegenstander
5. de locatie: uit/thuis (away/home)

Schrijf een functie `home_again(filename)`. Deze functie kijkt of er voor elke wedstrijd of er voor de tweede keer op een rij thuis wordt gespeeld. De functie returnt een lijst met alle data van wedstrijden waarvoor dit geldt. Bijvoorbeeld op 15/10/11 speelde Barcelona thuis en de volgende wedstrijd op 22/10/11 weer. Dus de output-lijst bevat de datum 22/10/11.

Gebruiksvoorbeeld:

    dates = home_again('barca.txt')
    print(dates)

Verwachtte output:

    ['22/10/11', '03/12/11', '05/05/12', '17/03/13', '18/08/13', '01/02/14']

Tips:

1. Je kan een bestand openen met `input_file = open(filename, 'r')`
2. Vergeet het bestand niet te sluiten met `input_file.close()`
