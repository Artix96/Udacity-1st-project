# in order to use methods and class we need to import them first

import media
import fresh_tomatoes

# create a few movie objects using Movie init function.
ali_G = media.Movie(
    "Ali G",
    "A story about a rapper trying to save community center.",
    "https://d32qys9a6wm9no.cloudfront.net/images/movies/poster/12/12b668a1ada1828ba795332f419d4ef7_500x735.jpg",  # NOQA
    "https://www.youtube.com/watch?v=7YPru7A7woI"
                    )

borat = media.Movie(
    "Borat",
    "A documentary about kazahstan's reporter traveling to USA",
    "http://posterwire.com/wp-content/uploads/borat.jpg",
    "https://www.youtube.com/watch?v=WH2CABcffAo"
                     )

harry_potter = media.Movie(
    "Harry Potter Deathly Hallows 2",
    "A final chapter of the Harry Potter Series",
    "http://pre14.deviantart.net/efc8/th/pre/f/2013/308/d/4/harry_potter_and_the_deathly_hallows___poster_by_squiddytron-d6t1leg.png",  # NOQA
    "https://www.youtube.com/watch?v=mObK5XD8udk"
                            )

ratatoullie = media.Movie(
    "Ratatoulie",
    "A rat is a chef in paris",
    "http://1.bp.blogspot.com/-kuWu2HXlFdA/TlRTbrVQ5ZI/AAAAAAAAAUM/mRvdMdPQmTA/s1600/Ratatouille-Cartoon-Gallery.jpg",  # NOQA
    "https://www.youtube.com/watch?v=1yKqLNnxGZw"
                          )

pick_of_destiny = media.Movie(
    "Pick of Destiny",
    "Story of two musicians obtaining a mysterious guitar pick.",
    "http://www.movieposter.com/posters/archive/main/42/MPW-21227",
    "https://www.youtube.com/watch?v=TXxQFMG86HA"
                                )

hunger_games = media.Movie(
    "Hunger Games",
    "A distopian society ",
    "http://images5.fanpop.com/image/photos/27600000/The-Hunger-Games-the-hunger-games-27627297-1440-900.jpg",  # NOQA
    "https://www.youtube.com/watch?v=mfmrPu43DF8"
                            )
# create a list containing movie objects instantiated before
movies = [
        ali_G, borat,
        harry_potter, ratatoullie,
        pick_of_destiny, hunger_games
        ]

# pass the list to open_movies_page method from fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
