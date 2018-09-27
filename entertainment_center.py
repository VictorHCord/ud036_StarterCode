from media import Movie
import fresh_tomatoes

matrix = Movie(
    "Matrix",
    "A computer hacker learns from mysterious rebels about the true nature "
    "of his reality and his role in the war against its controllers.",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

_300 = Movie(
    "300",
    "King Leonidas of Sparta and a force of 300 men fight the Persians at "
    "Thermopylae in 480 B.C.",
    "https://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg",
    "https://www.youtube.com/watch?v=UrIbxk7idYA")

vendetta = Movie(
    "V for Vendetta",
    "In a future British tyranny, a shadowy freedom fighter, known only by "
    "the alias of \"V\", plots to overthrow it with the help of a "
    "young woman.",
    "https://upload.wikimedia.org/wikipedia/pt/9/9f/Vforvendettamov.jpg",
    "https://www.youtube.com/watch?v=lSA7mAHolAw")

avatar = Movie(
    "Avatar",
    "A paraplegic marine dispatched to the moon Pandora on a unique mission "
    "becomes torn between following his orders and protecting the world he "
    "feels is his home.",
    "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

lord = Movie(
    "The Lord of the Rings",
    "A meek Hobbit from the Shire and eight companions set out on a journey "
    "to destroy the powerful One Ring and save Middle-earth from the Dark "
    "Lord Sauron.",
    "https://upload.wikimedia.org/wikipedia/pt/thumb/0/0c/The_Fellowship_Of_"
    "The_Ring.jpg/250px-The_Fellowship_Of_The_Ring.jpg",
    "https://www.youtube.com/watch?v=V75dMMIW2B4")

predator = Movie(
    "Predator",
    "A team of commandos on a mission in a Central American jungle find "
    "themselves hunted by an extraterrestrial warrior.",
    "https://upload.wikimedia.org/wikipedia/pt/9/95/Predator_Movie.jpg",
    "https://www.youtube.com/watch?v=X2hBYGwKh3I")

terminator = Movie(
    "The Terminator",
    "A seemingly indestructible android is sent from 2029 to 1984 to "
    "assassinate a waitress, whose unborn son will lead humanity in a war "
    "against the machines, while a soldier from that war is sent to protect "
    "her at all costs.",
    "https://upload.wikimedia.org/wikipedia/pt/5/5a/Terminator1984.jpg",
    "https://www.youtube.com/watch?v=k64P4l2Wmeg")

alien3 = Movie(
    "Alien 3",
    "After her last encounter, Ellen Ripley crash-lands on Fiorina 161, "
    "a maximum security prison. When a series of strange and deadly "
    "events occur shortly after her arrival, Ripley realizes that she "
    "has brought along an unwelcome visitor.",
    "https://upload.wikimedia.org/wikipedia/pt/b/ba/Alien_3.jpg",
    "https://www.youtube.com/watch?v=KUTaNMJJBa8")

warz = Movie(
    "World War Z",
    "Former United Nations employee Gerry Lane traverses the world in a "
    "race against time to stop the Zombie pandemic that is toppling armies "
    "and governments, and threatening to destroy humanity itself.",
    "https://upload.wikimedia.org/wikipedia/pt/f/fa/World_War_Z.jpg",
    "https://www.youtube.com/watch?v=Md6Dvxdr0AQ")


films_list = [matrix, _300, vendetta, avatar, lord,
              predator, terminator, alien3, warz]

fresh_tomatoes.open_movies_page(films_list)

# matrix.show_info()
