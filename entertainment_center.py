import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", "http://www.youtube.com/watch?v=-9ceBgWV8io")

minority_report = media.Movie("Minority Report", "In 2054, where police utilize a psychic technology to arrest and convict murderers before they commit their crime", "http://www.gstatic.com/tv/thumb/movieposters/29122/p29122_p_v8_aq.jpg", "https://www.youtube.com/watch?v=wkBNuScDLtA")

jumper = media.Movie("Jumper", "Aimless David Rice (Hayden Christensen) has the ability to instantly transport himself to any place he can imagine.", "http://www.gstatic.com/tv/thumb/movieposters/173063/p173063_p_v8_ab.jpg", "https://www.youtube.com/watch?v=X5ZNG3Oveh4")

transformer = media.Movie("Transformers: Age of Extinction", "Autobots must escape sight from a bounty hunter who has taken control of the human", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwNTg1MTA5Nl5BMl5BanBnXkFtZTgwOTg2OTM4MTE@._V1_SY1000_CR0,0,640,1000_AL_.jpg", "https://www.youtube.com/watch?v=dYDGqmxMZFI")

star_trek = media.Movie("Star Trek (2009)", "The brash James T. Kirk tries to live up to his father's legacy with Commander Spock keeping him in check as a vengeful, time-traveling Romulan creates black holes to destroy the Federation one planet at a time.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE5NDQ5OTE4Ml5BMl5BanBnXkFtZTcwOTE3NDIzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg", "https://www.youtube.com/watch?v=3PM1pvOzn_w")

movies = [toy_story, avatar, minority_report, jumper, transformer, star_trek]
fresh_tomatoes.open_movies_page(movies)
