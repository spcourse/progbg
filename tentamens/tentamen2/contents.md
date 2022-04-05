# Hertentamen Inleiding Programmeren voor Bèta-gamma

Datum: 05-04-22

Dit is een digitaal tentamen. Het tentamen bestaat uit 4 opdrachten waarin je een kort Pythonprogramma moet schrijven.

Je wordt alleen beoordeeld aan de hand van de correctheid van je code, niet op _design_. Je hoeft dus geen commentaar te schrijven of je zorgen te maken over de style guide.

Je kan je uitwerking verifiëren met checkpy. Download de checkpy voor de tentamens:

    checkpy -d /spcourse/exam-tests

Run checkpy:

    checkpy tentamen22_3

# Regels

- Maak alle opdrachten in een bestand genaamd `tentamen22_3.py` en lever deze file in.
- Je mag geen `numpy` of ander python module gebruiken. Dus geen `import`!
- Gedurende het tentamen mag je geen bronnen op internet raadplegen, afgezien van de progbg.mprog.nl website en de IDE.
- Je kan tijdens het tentamen geen hulp krijgen van de docenten en assistenten.
- Submit je oplossingen als je klaar bent. **Voor je de tentamenzaal verlaat, check met de surveillant dat je tentamen correct is ingeleverd!**

### 1: Grootste deler

Schrijf een functie `biggest_divisor(n)`. Deze functie returnt de grootste deler van `n` (exclusief `n` zelf).

Gebruiksvoorbeeld:

    print(biggest_divisor(80))
    print(biggest_divisor(11))
    print(biggest_divisor(15))

Verwachte output:

    40
    1
    5

<div style="page-break-after: always; break-after: page;"></div>

### 2: Meeste delers

Het getal $$12$$ heeft 6 delers: $$1$$, $$2$$, $$3$$, $$4$$, $$6$$ en $$12$$. Dat is meer dan bijvoorbeeld $$13$$ die heeft maar 2 delers: $$1$$ en $$13$$ (het is een priemgetal).

Schrijf een functie `most_divisors(n)` die berekent welk getal, kleiner dan $$n$$, het meeste aantal delers heeft.

Gebruiksvoorbeeld 1:

    number_with_most_divisors = most_divisors(29)
    print(number_with_most_divisors)

Verwachte output:

    24

Gebruiksvoorbeeld 2:

    number_with_most_divisors = most_divisors(20)
    print(number_with_most_divisors)

Verwachte output:

    12

<div style="page-break-after: always; break-after: page;"></div>

### 3: Herhaling

De tekst "a aa aa b" heeft een woord dat één keer wordt herhaald: ("aa"). De tekst "aa bb aa y" heeft geen herhaalde woorden (de twee "aa" staan niet direct achter elkaar). De tekst "x aa aa aa y bb bb" heeft in totaal drie herhaalde woorden ("aa" wordt twee keer herhaald en "bb" wordt één keer herhaald).

Schrijf een functie `repetition_count(text)`. De functie verwacht een string als input en returnt het aantal herhaalde woorden dat in de string voorkomt.

Gebruiksvoorbeeld 1:

    example_text = "x aa aa aa y bb bb"
    print(repetition_count(example_text))

Verwachte output:

    3

Gebruiksvoorbeeld 2:

    example_text = "x aa l aa aa y bb bb"
    print(repetition_count(example_text))

Verwachte output:

    2

<div style="page-break-after: always; break-after: page;"></div>

### 4: Doelsaldo
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

Het doelverschil in een wedstrijd is het verschil tussen het aantal goals voor en het aantal goals tegen. Als Barcelona 3 doelpunten heeft gescoord tegen Valencia en Valencia er maar 2 heeft gemaakt, dan is het doelverschil voor Barcelona 1 doelpunt.

Schrijf een functie `average_goal_difference(filename)`. Deze functie berekent het _gemiddelde_ doelverschil over alle wedstrijden uit de dataset.

Gebruiksvoorbeeld:

    total = average_goal_difference('barca.txt')
    print(f'{total:.3f}')

Verwachte output:

    1.991

Je kan ook het bestand [barca_short.txt](barca_short.txt) gebruiken om je code mee te testen. Deze bevat alleen de eerste 4 wedstrijden.

Gebruiksvoorbeeld:

    total = average_goal_difference('barca_short.txt')
    print(f'{total:.3f}')

Verwachte output:

    3.250

Tips:

1. Je kan een bestand openen met `input_file = open(filename, 'r')`
2. Vergeet het bestand niet te sluiten met `input_file.close()`
