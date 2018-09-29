from media import Movie
import fresh_tomatoes

matrix = Movie(
    1,
    "Matrix",
    "A computer hacker learns from mysterious rebels about the true nature "
    "of his reality and his role in the war against its controllers.",
    "https://image.ibb.co/daHQte/matrix.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

_300 = Movie(
    2,
    "300",
    "King Leonidas of Sparta and a force of 300 men fight the Persians at "
    "Thermopylae in 480 B.C.",
    "https://image.ibb.co/gchmzK/300poster_1.jpg",
    "https://www.youtube.com/watch?v=UrIbxk7idYA")

vendetta = Movie(
    3,
    "V for Vendetta",
    "In a future British tyranny, a shadowy freedom fighter, known only by "
    "the alias of \"V\", plots to overthrow it with the help of a "
    "young woman.",
    "https://image.ibb.co/m2Jqte/vforvendettamov_1.jpg",
    "https://www.youtube.com/watch?v=lSA7mAHolAw")

avatar = Movie(
    4,
    "Avatar",
    "A paraplegic marine dispatched to the moon Pandora on a unique mission "
    "becomes torn between following his orders and protecting the world he "
    "feels is his home.",
    "https://image.ibb.co/jRJemz/avatar_teaser_poster_1.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

lord = Movie(
    5,
    "The Lord of the Rings",
    "A meek Hobbit from the Shire and eight companions set out on a journey "
    "to destroy the powerful One Ring and save Middle-earth from the Dark "
    "Lord Sauron.",
    "https://image.ibb.co/govs6z/250px_the_fellowship_of_the_ri.jpg",
    "https://www.youtube.com/watch?v=V75dMMIW2B4")

predator = Movie(
    6,
    "Predator",
    "A team of commandos on a mission in a Central American jungle find "
    "themselves hunted by an extraterrestrial warrior.",
    "https://image.ibb.co/bVNVRz/predator_movie_1.jpg",
    "https://www.youtube.com/watch?v=X2hBYGwKh3I")

terminator = Movie(
    7,
    "The Terminator",
    "A seemingly indestructible android is sent from 2029 to 1984 to "
    "assassinate a waitress, whose unborn son will lead humanity in a war "
    "against the machines, while a soldier from that war is sent to protect "
    "her at all costs.",
    "https://image.ibb.co/hdt1zK/terminator1984_1.jpg",
    "https://www.youtube.com/watch?v=k64P4l2Wmeg")

alien3 = Movie(
    8,
    "Alien 3",
    "After her last encounter, Ellen Ripley crash-lands on Fiorina 161, "
    "a maximum security prison. When a series of strange and deadly "
    "events occur shortly after her arrival, Ripley realizes that she "
    "has brought along an unwelcome visitor.",
    "https://image.ibb.co/cTfWzK/alien_3_1.jpg",
    "https://www.youtube.com/watch?v=KUTaNMJJBa8")

warz = Movie(
    9,
    "World War Z",
    "Former United Nations employee Gerry Lane traverses the world in a "
    "race against time to stop the Zombie pandemic that is toppling armies "
    "and governments, and threatening to destroy humanity itself.",
    "https://image.ibb.co/d3m4KK/world_war_z_1.jpg",
    "https://www.youtube.com/watch?v=Md6Dvxdr0AQ")


films_list = [matrix, _300, vendetta, avatar, lord,
              predator, terminator, alien3, warz]

fresh_tomatoes.open_movies_page(films_list)

# matrix.show_info()
