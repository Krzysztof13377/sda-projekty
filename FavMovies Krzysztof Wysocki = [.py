FavMovies = [
    {
        "title": "Władca Pierścieni Powrót Króla",
        "year": 2003,
        "rating": 8.4,
        "opis": "Zwienczenie filmowej trylogii wg powieści Tolkiena. Aragorn jednoczy siły Śródziemia, szykując się do bitwy, która ma odwrócić uwagę Saurona od podążających w kierunku Góry Przeznaczenia hobbitów.",
        "directors": ["Peter Jackson"],
        "autorzy": ["J R R Tolkien"],
        "gwiazdy": ["Orlando Bloom"],
        "gatunki": ["Fantasy"]
    },
    {
        "title": "Harry Potter i Insygnia Śmierci: Część I",
        "year": 2010,
        "rating": 7.5,
        "opis": "Harry, Ron i Hermiona wyruszają odnaleźć horkruksy, dzięki którym Voldemort zapewnił sobie nieśmiertelność. Muszą je wszystkie zniszczyć, by go pokonać.",
        "directors": ["David Yates"],
        "autorzy": ["J K Rowling"],
        "gwiazdy": ["Emma Watson"],
        "gatunki": ["Fantasy"]
    },
    {
        "title": "Jak zostałem gangsterem. Historia prawdziwa",
        "year": 2019,
        "rating": 7.4,
        "opis": "Historia najniebezpieczniejszego gangstera w Polsce, dla którego władza, bycie ponad stan i pieniądze stanowią priorytet.",
        "directors": ["Maciej Kawulski"],
        "autorzy": ["Krzysztof Gureczny"],
        "gwiazdy": ["Natalia Szroeder"],
        "gatunki": ["Sensacyjny"]
    },
    {
        "title": "Piraci z Karaibów: Na nieznanych wodach",
        "year": 2011,
        "rating": 7.4,
        "opis": "Legendarny pirat Czarnobrody planuje zdobyć żywą syrenę i dwa kielichy, by się odmłodzić. Sprytny kapitan Jack Sparrow chce mu pokrzyżować plany.",
        "directors": ["Rob Marshall"],
        "autorzy": ["Tery Rossio"],
        "gwiazdy": ["Johny Depp"],
        "gatunki": ["Fantasy", "przygodowy"]
    }
]

print("Tytuł pierwszego filmu to: " + FavMovies[0]["title"])
print("Rok premiery drugiego filmu to: " + str(FavMovies[1]["year"]))
print("Ocena IMDB trzeciego filmu to: " + str(FavMovies[2]["rating"]))
print("Krótki opis czwartego filmu to: " + FavMovies[3]["opis"])

print("Główny reżyser pierwszego filmu to: " + FavMovies[0]["directors"][0])
print("Głównym scenarzystą drugiego filmu jest: " + FavMovies[1]["autorzy"][0])
print("Główną gwiazdą trzeciego filmu jest: " + FavMovies[2]["gwiazdy"][0])
print("Główny gatunek czwartego filmu to: " + FavMovies[3]["gatunki"][0])
{
        "title": "Władca Pierścieni Powrót Króla"
        # Inne szczegóły...
        "directors": ["Peter Jackson"],
        "autorzy": ["J R R Tolkien"],
        "gwiazdy": ["Orlando Bloom"],
        "gatunki": ["Fantasy"].
    },
{
        "title": "Harry Potter i Insygnia Śmierci: Część I"
        # Inne szczegóły...
        "directors": ["David Yates"],
        "autorzy": [" J K Rowling"],
        "gwiazdy": [" Emma Watson"],
        "gatunki": ["Fantasy"].
    },
{
        "title": "Jak zostałem gangsterem. Historia prawdziwa"
        # Inne szczegóły...
        "directors": ["Maciej Kawulski"],
        "autorzy": ["Krzysztof Gureczny"],
        "gwiazdy": ["Natalia Szroeder"],
        "gatunki": ["Sensacyjny"].
    },
{
        "title": "Piraci z Karaibów: Na nieznanych wodach "
        # Inne szczegóły...
        "directors": ["Rob Marshall"],
        "autorzy": ["Tery Rossio"],
        "gwiazdy": ["Johny Depp"],
        "gatunki": ["Fantasy" , "przygodowy"].
    },

averageRating = (FavMovies[0]["rating"] + FavMovies[1]["rating"] + FavMovies[2]["rating"] + FavMovies[3]["rating"]) / 4
print("Średnia ocena wynosi: " + str(averageRating))

averageAge = ((2024 - FavMovies[0]["year"]) + (2024 - FavMovies[1]["year"]) + (2024 - FavMovies[2]["year"]) + (2024 - FavMovies[3]["year"])) / 4
print("Średni wiek to: " + str(averageAge))