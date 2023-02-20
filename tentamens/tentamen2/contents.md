# Tentamen Inleiding Programmeren voor Bèta-gamma

Datum: 20-02-23

Dit is een digitaal tentamen. Het tentamen bestaat uit 4 opdrachten waarin je een kort Pythonprogramma moet schrijven.

Je wordt alleen beoordeeld aan de hand van de correctheid van je code, niet op _design_. Je hoeft dus geen commentaar te schrijven of je zorgen te maken over de style guide.

Je kan je uitwerking verifiëren met checkpy. Download de checkpy voor de tentamens:

    checkpy -d /spcourse/exam-tests

Run checkpy:

    checkpy tentamen23_2

# Regels

- Maak alle opdrachten in een bestand genaamd `tentamen23_2.py` en lever deze file in.
- Je mag geen `numpy` of ander python module gebruiken. Dus geen `import`!
- Gedurende het tentamen mag je geen bronnen op internet raadplegen, afgezien van de progbg.mprog.nl website en de IDE.
- Je kan tijdens het tentamen geen hulp krijgen van de docenten en assistenten.
- Submit je oplossingen als je klaar bent. **Voor je de tentamenzaal verlaat, check met de surveillant dat je tentamen correct is ingeleverd!**

### 1: Triangular

*Triangular numbers* x zijn getallen die de het resultaat zijn van de som $1 + 2 + \ldots + i$ voor een gegeven waarde $i$. Het eerste *triangular number* is $1$, het volgende is $1 + 2 = 3$, het volgende $1 + 2 + 3 = 6$, het *triangular number** erna is $10$, etc.

Schrijf een functie genaamd `triangular(n)` dat een lijst van alle triangular numbers kleiner dan $n$ produceert.

Gebruiksvoorbeeld:

    print(triangular(6))
    print(triangular(15))
    print(triangular(16))

Verwachtte output:

    [1, 3]
    [1, 3, 6, 10]
    [1, 3, 6, 10, 15]

### 2: Classified

Schrijf een functie `classified(text, censor_word)`. De functie verwacht een `text` en een `censor_word` als input en vervangt alle woorden uit `text` die overeenkomen met `censor_word` voor hekjes (`####`). Het aantal hekjes moet overeenkomen met de lengte van het woord.

Gebruiksvoorbeeld:

    print(classified("We're all mad here.", "mad"))
    print(classified("Why, sometimes I've believed as many as six impossible things before breakfast.", "AS"))

Verwachtte output:

    We're all ### here.
    Why, sometimes I've believed ## many ## six impossible things before breakfast.

### 3: Collatz

Een *Collatz*-reeks is een reeks getallen. Je begint bij een gegeven nummer $n$.  Gegeven het laatste nummer in de reeks $x$ kan je het volgende nummer bereken als volgt: als $x$ even is, is het volgende nummer $x/2$ als $x$ oneven is wordt het volgende nummer $x*3+1$. Je blijft dit proces herhalen tot het laatste nummer $1$ is.

Schrijf een functie `collatz(n)` die de *Collatz*-reeks berekent met $n$ als startwaarde.

Gebruiksvoorbeeld:

    print(collatz(12))
    print(collatz(3))

Verwachtte output:

    [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
    [3, 10, 5, 16, 8, 4, 2, 1]

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

1. de datum van de wedstrijd
2. de tegenstander
3. het resultaat: gewonnen/verloren/gelijkgespeeld (won/lost/draw)
4. het aantal goals voor Barcelona
5. het aantal goals voor de tegenstander
6. de locatie: uit/thuis (away/home)

Schrijf een functie `average_goals_per_game(filename)`. Deze functie berekent het gemiddelde aantal goals dat Barcelona per wedstrijd heeft gescoord.

Gebruiksvoorbeeld:

    avg = average_goals_per_game('barca.txt')
    print(avg)

Verwachtte output:

    2.8859649122807016

Je kan ook het bestand [barca_short.txt](barca_short.txt) gebruiken om je code mee te testen. Deze bevat alleen de eerste 4 wedstrijden.

Gebruiksvoorbeeld:

    avg = average_goals_per_game('barca_short.txt')
    print(avg)

Verwachtte output:

    4.25

1. Je kan een bestand openen met `input_file = open(filename, 'r')`
2. Vergeet het bestand niet te sluiten met `input_file.close()`
