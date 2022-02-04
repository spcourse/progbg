# Tentamen Inleiding Programmeren voor Bèta-gamma

# Tentamen Inleiding Programmeren voor Bèta-gamma

Datum: 04-02-22

Dit is een digitaal tentamen. Het tentamen bestaat uit 4 opdrachten waarin je een kort Pythonprogramma moet schrijven.

Je wordt alleen beoordeeld aan de hand van de correctheid van je code, niet op _design_. Je hoeft dus geen commentaar te schrijven of je zorgen te maken over de style guide.

Je kan je uitwerking verifiëren met checkpy. Download de checkpy voor de tentamens:

    checkpy -d /spcourse/exam-tests

Run checkpy:

    checkpy tentamen22_2

# Regels

- Maak alle opdrachten in een bestand genaamd `tentamen22_2.py` en lever deze file in.
- Je mag geen `numpy` of ander python module gebruiken. Dus geen `import`!
- Gedurende het tentamen mag je geen bronnen op internet raadplegen, afgezien van de progbg.mprog.nl website en de IDE.
- Je kan tijdens het tentamen geen hulp krijgen van de docenten en assistenten.
- Submit je oplossingen als je klaar bent. **Voor je de tentamenzaal verlaat, check met de surveillant dat je tentamen correct is ingeleverd!**

### 1: Getallenlijst

Schrijf een functie `divisors(n)`. Deze functie berekent alle delers van `n` (inclusief `1` en `n` zelf). Return het resultaat als een lijst.

Gebruiksvoorbeeld:

    divisor_list = divisors(80)
    print(divisor_list)

Verwachte output:

    [1, 2, 4, 5, 8, 10, 16, 20, 40, 80]

<div style="page-break-after: always; break-after: page;"></div>

### 2: Perfect

Het getal $$6$$ is gelijk aan de som van z'n delers: De delers van $$6$$ zijn $$1$$, $$2$$ en $$3$$, en de som is $$1 + 2 + 3 = 6$$. Dit maakt $$6$$ een perfect getal. Een perfect getal is een getal dat gelijk is aan de som van z'n delers.

Schrijf een functie `perfect_list(n)` die een lijst genereert van alle perfecte getallen van $$1$$ tot $$n$$ ($$n$$ zelf niet inbegrepen).


Gebruiksvoorbeeld 1:

    perfect_numbers = perfect_list(29)
    print(perfect_numbers)

Verwachte output:

    [0, 6, 28]

Gebruiksvoorbeeld 2:

    perfect_numbers = perfect_list(497)
    print(perfect_numbers)

Verwachte output:

    [0, 6, 28, 496]

<div style="page-break-after: always; break-after: page;"></div>

### 3: Kort

Schrijf een functie `short(text)`. De functie verwacht een string als input en returnt het de lengte van het kortste woord in de string. Alle woorden die korter zijn dan twee letters moeten worden genegeerd. Houd er rekening mee dat punctuatie niet meetelt voor de lengte van een woord.

> Je mag voor deze opdracht géén gebruik maken van de ingebouwde python functies `min`, `sort` en `sorted`.

Gebruiksvoorbeeld 1:

    example_text = "Fuzzy Wuzzy was bear. Fuzzy Wuzzy had no hair. Fuzzy Wuzzy wasn’t fuzzy, was he?"
    print(short(example_text))

Verwachte output:

    2

Gebruiksvoorbeeld 2:

    example_text = "The best way to explain it is to do it."
    print(short(example_text))

Verwachte output:

    2

Gebruiksvoorbeeld 3:

    example_text = "They gave two! Great!"
    print(short(example_text))

Verwachte output:

    3

<div style="page-break-after: always; break-after: page;"></div>

### 4: Away goals

Voor deze opdracht ga je het databestand [barca.txt](barca.txt) gebruiken (download van https://progbg.mprog.nl/tentamens/tentamen). Dit bestand bevat de resultaten van het voetbalelftal van Barcelona (seizoenen 11/12 tot en met 13/14). De inhoud ziet er als volgt uit:

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

Schrijf een functie `total_away_goals(filename)`. Deze functie berekent het total aantal doelpunten dat Barcelona heeft gescoord in alle uitwedstrijden.

Gebruiksvoorbeeld:

    total = total_away_goals('barca.txt')
    print(total)

Verwachte output:

    200

Je kan ook het bestand [barca_short.txt](barca_short.txt) gebruiken om je code mee te testen. Deze bevat alleen de eerste 4 wedstrijden.

Gebruiksvoorbeeld:

    total = total_away_goals('barca_short.txt')
    print(total)

Verwachte output:

    13


Tips:

1. Je kan een bestand openen met `input_file = open(filename, 'r')`
2. Vergeet het bestand niet te sluiten met `input_file.close()`
