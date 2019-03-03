import media
import fresh_tomatoes

planet_of_apes = media.Movie("Fight Club",
                             "Fight Club is a 1999 film based on the 1996 "
                             "novel by Chuck Palahniuk.",
                             "https://upload.wikimedia.org/wikipedia/pt/thumb/"
                             "2/2b/FightClubPoster.jpg/"
                             "230px-FightClubPoster.jpg",
                             "https://www.youtube.com/watch?v=xPMI3WZFMv0")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

captain_america = media.Movie("Captain America", "An enhanced soldier "
                                                 "fights off the nazis",
                              "https://s-media-cache-ak0.pinimg.com/736x/63"
                              "/35/b3/6335b33481b913f437b4e395cf71f9b6"
                              "--captain-america-movie-capt-america.jpg",
                              "https://www.youtube.com/watch?v=JerVrbLldXw")

thor = media.Movie("Thor", "A God gets Banished to earth",
                   "https://vignette2.wikia.nocookie.net/marvelcinematic"
                   "universe/images/5/5a/Thor_Official_Poster.jpg/revision/"
                   "latest?cb=20121220212004",
                   "https://www.youtube.com/watch?v=JOddp-nlNvQ")

iron_man = media.Movie("Iron Man", "A man builts a suit of amor "
                                   "with various abilities",
                       "http://cdn.collider.com/wp-content/uploads/2015/04/"
                       "iron-man-1-poster.jpg",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

hulk = media.Movie("Hulk", "Science experiment gone wrong, turns"
                           " a man into a monster",
                   "https://s-media-cache-ak0.pinimg.com/736x/2b/80/84/2b808"
                   "441369cc5304c1489179f2c9e78--bruce-banner-hulk-smash.jpg",
                   "https://www.youtube.com/watch?v=xbqNb2PFKKA")

ant_man = media.Movie("Ant Man", "A thief is given a second chance "
                                 "and becomes a tiny superhero",
                      "http://cdn.collider.com/wp-content/uploads/2015/"
                      "06/ant-man-poster-german.jpg",
                      "https://www.youtube.com/watch?v=pWdKf3MneyI")

black_panther = media.Movie("Black Panther", "A king must protect "
                                             "his homeland",
                            "http://cdn.collider.com/wp-content/uploads/2017"
                            "/06/black-panther-movie-poster-teaser.jpg",
                            "https://www.youtube.com/watch?v=dxWvtMOGAhw")

movies = [captain_america,
          thor,
          iron_man,
          hulk,
          ant_man,
          planet_of_apes,
          avatar]

fresh_tomatoes.open_movies_page(movies)
