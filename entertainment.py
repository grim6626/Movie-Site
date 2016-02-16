
import fresh_tomatoes
import movie

john_wick = movie.Movie("John Wick", "Ex-hitman takes revenge for being attacked.", "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg", "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")

horns = movie.Movie("Horns", "A man accused of murder and rape wakes up with horns after a night of drinking", "https://upload.wikimedia.org/wikipedia/en/0/09/Horns_Official_Movie_Poster.jpg", "https://www.youtube.com/watch?v=B8s_1UcdoNI")

maltese_falcon = movie.Movie("The Maltese Falcon", "A private investigator takes a case involving criminals and a valuable statue", "https://upload.wikimedia.org/wikipedia/en/9/99/Falconm.JPG", "https://www.youtube.com/watch?v=phUxnXGhEiI")

constantine = movie.Movie("Constantine", "An exorcist is involved in the battle between heaven and hell.", "https://upload.wikimedia.org/wikipedia/en/2/2b/Constantine_poster.jpg", "https://www.youtube.com/watch?v=oU4moy3Wz4c")

v = movie.Movie("V is for Vendetta", "A man rebels against an oppressive government", "https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg", "https://www.youtube.com/watch?v=k_13fFIrhPk")

john_dies = movie.Movie("John Dies at the End", "A man is wrapped up in a battle against evil forces", "https://upload.wikimedia.org/wikipedia/en/8/8e/John_dies_at_the_end_poster.jpg", "https://www.youtube.com/watch?v=IfJp417dyig")

movies = [john_wick, horns, maltese_falcon, constantine, v, john_dies]
fresh_tomatoes.open_movies_page(movies)
