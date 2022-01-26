# Oefententamen Inleiding Programmeren voor Bèta-gamma

Datum: 31-01-2022

Dit is een digitaal tentamen. Het tentamen bestaat uit 4 opdrachten waarin je een kort python programma moet schrijven.

Je wordt alleen beoordeeld aan de hand van de correctheid van je code, niet op _design_. You hoeft does geen commentaar te schrijven of je zorgen te maken over de style guide.

Je kan je uitwerking checken met checkpy. Download de checkpy voor de tentamens:

    checkpy -d /spcourse/exam-tests

Run checkpy:

    checkpy tentamen22_1

# Regels

- Maak alle opdrachten in een bestand genaamt `tentamen22_1.py` en lever deze file in.
- Je mag geen `numpy` of ander python module gebruiken.
- Gedurende het tentamen mag je geen bronnen op internet raadplegen, afgezien van de progbg.mprog.nl website en de IDE.
- Je kan tijdens het tentamen geen hulp krijgen van de docenten en assistenten.
- Submit je oplossingen als je klaar bent. **Voor je de tentamenzaal verlaat, check met de surveillant dat je tentamen correct is ingeleverd!**

### 1: Fizzy

Schrijf een functie `fizzy(n)`. Maakt returnt lijst met alle fizzy getallen van `1` tot `n` (exclusief `n` zelf). Een fizzy getal is een getal dat deelbaar is door 3 en 5 of 3 en 7 (of beide).

Gebruiksvoorbeeld:

    fizzy_list = fizzy(100)
    print(fizzy_list)

Verwachtte output:

    [15, 21, 30, 42, 45, 60, 63, 75, 84, 90]

### 2: Decompose

> Er is geen checkpy voor deze opdracht

Sommige getallen $$n$$ kan je schrijven in de vorm $$n = 2 \cdot a + b$$ waarbij $$a$$ en $$b$$ allebei delers van $$n$$ zijn.
Schrijf een functie `print_decomposition(n)`. Deze functie print alle decomposities die aan de bovenstaande
regel voldoen.

Gebruiksvoorbeeld 1:

    print_decomposition(12)

Verwachte output:

    12 = 2 * 3 + 6
    12 = 2 * 4 + 4

Gebruiksvoorbeeld 2:

    print_decomposition(32)

Verwachte output:

    32 = 2 * 8 + 16  

### 3: Starting letter

Schrijf een functie `filter_words_starting_with(text, letter)`. Deze functie krijgt als input twee strings: text en
letter. De functie zoekt alle woorden uit text die beginnen met de letter letter. Je mag er van uitgaan dat
de parameter letter altijd een enkele letter is.

Gebruiksvoorbeeld:

    example_text = "David Donald Doo dreamed a dozen doughnuts and a duck-dog, too."
    print(filter_words_starting_with(example_text, "d"))

Verwachte output:

    ['David', 'Donald', 'Doo', 'dreamed', 'dozen', 'doughnuts', 'duck-dog']


### 4: Winning streak

Voor deze opdracht ga je het databestand [barca.txt](barca.txt) gebruiken. Dit bestand bevat de resultaten van het voetbalelftal van Barcelona (seizoenen 11/12 tot en met 13/14). De inhoud ziet er als volgt uit:

    29/08/11,Villarreal,won,5,0,home
    10/09/11,Sociedad,draw,2,2,away
    17/09/11,Osasuna,won,8,0,home
    ...
    03/05/14,Getafe,draw,2,2,home
    11/05/14,Elche,draw,0,0,away
    17/05/14,Ath Madrid,draw,1,1,home

Zoals je ziet zijn de velden gescheiden door komma’s en bevatten de volgende informatie:
1. de datum van de wedstrijd
2. de tegenstander
3. het resultaat: gewonnen/verloren/gelijkgespeeld (won/lost/draw)
4. het aantal goals voor Barcelona
5. het aantal goals voor de tegenstander
6. de locatie: uit/thuis (away/home)

Schrijf een functie `longest_streak(filename)`. Deze functie betekent de lengte van langste winning streak.
Een winning streak is een aaneengesloten periode met alleen maar gewonnen wedstrijden (dus niet onderbroken
door een verlieswedstrijd of gelijkspel).

Gebruiksvoorbeeld 1:

    streak = longest_streak('barca.txt')
    print(streak)

Verwachte output:

    13

Je kan ook het bestand [barca_short.txt](barca_short.txt) gebruiken om je code mee te testen. Deze bevat alleen de eerste 4 wedstrijden.


Gebruiksvoorbeeld 2:

    streak = longest_streak('barca_short.txt')
    print(streak)

Verwachte output:

    1

Tips:

1. Je kan een bestand openen met `input_file = open(filename, 'r')`
2. Vergeet het bestand niet te sluiten met `input_file.close()`
