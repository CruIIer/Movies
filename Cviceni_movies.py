oddelovac = "=" * 62
from pprint import pprint

sluzby = ("dostupne filmy", "detaily filmu", 'reziseri', "doporuc film")

uzivatele = {
    "tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
    "petr": {"The Godfather", "The Dark Knight"},
    "marek": {"The Dark Knight", "The Prestige"}
}

film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
     )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
}

#spojíme všechny filmy dohromady

filmy = [
    film_1.get("JMENO"),
    film_2.get("JMENO"),
    film_3.get("JMENO"),
    film_4.get("JMENO"),
]

# uvítání a výpis nabídky

jmeno = input("Zadej jméno: ")
if jmeno in uzivatele:
    print("V pořádku")

else:
    print("Je mi líto, zadané jméno v systému neexistuje.")
    exit()

print(oddelovac)
uvitani = "Vítejte v našem filmovém slovníku"
uvitani_1 = uvitani.center(62)
print(uvitani_1)
print(oddelovac)
print(" | ".join(sluzby), end=" |\n") 
print(oddelovac)

# vyber služby

vyber_sluzby = input("Vyber sluzbu: ")


# dostupné filmy
if vyber_sluzby == sluzby[0]:
    print("Naše filmy: ", ", ".join(filmy))

# detaily filmu    
elif vyber_sluzby == sluzby[1]:
    film = input("Vyber film ")
    
    if film() == filmy[0]:
        pprint(film_1)
    elif film == filmy[1]:
        pprint(film_2)
    elif film == filmy[2]:
        pprint(film_3)
    elif film == filmy[3]:
        pprint(film_4)
    else:
        print("Zadaný název není v databázi.")

# reziseri
elif vyber_sluzby == sluzby[2]:
    reziseri = set([film_1["REZISER"], film_2["REZISER"],
                    film_3["REZISER"], film_4["REZISER"]])
    print(", ".join(reziseri), sep="\n")

# doporučení filmu podle ostatních uživatelů
elif vyber_sluzby == sluzby[3]:
    if jmeno == "tomas":
        tomas_marek = uzivatele["tomas"].symmetric_difference(uzivatele["marek"])
        tomas_petr = uzivatele["tomas"].symmetric_difference(uzivatele["petr"])
        print(tomas_petr | tomas_marek)
    elif jmeno == "petr":
        petr_marek = uzivatele["petr"].symmetric_difference(uzivatele["marek"])
        petr_tomas = uzivatele["petr"].symmetric_difference(uzivatele["tomas"])
        print(petr_marek | petr_tomas)
    elif jmeno == "marek":
        marek_petr = uzivatele["marek"].symmetric_difference(uzivatele["petr"])
        marek_tomas = uzivatele["marek"].symmetric_difference(uzivatele["tomas"])
        print(marek_petr | marek_tomas)
        

print(oddelovac)

