import fresh_tomatoes
from media import movie

darkKnight = movie("The Dark Knight",
                   "https://images-na.ssl-images-amazon.com/images/M" + 
                   "/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@.5B" 
                   + "anBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_CR90,0,630" + 
                   ",1200_AL_.jpg",
                   "https://www.youtube.com/watch?v=EXeTwQWrcwY")

darkKnightRises = movie("The Dark Knight Rises",
                        "https://images-na.ssl-images-amazon.com/images/M/" 
                        + "MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0N" + 
                        "TM4Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=g8evyE9TuYk")

starWarsForceAwakens = movie("Star Wars: The Force Awakens",
                             "http://is3.mzstatic.com/image/thumb/Video69/v4/" 
                             + "c2/55/37/c25537af-f191-ef3a-e23e-11"
                             + "7621a98da2/source/1200x630bb.jpg",
                             'https://www.youtube.com/watch?v=sGbxmsDFVnE')

movies = []
movies.append(darkKnight)
movies.append(darkKnightRises)
movies.append(starWarsForceAwakens)

fresh_tomatoes.open_movies_page(movies)
