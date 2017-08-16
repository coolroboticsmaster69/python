import fresh_tomatoes
import media
toy_story=media.Movie("toy story","a story of a boy and his toys that come to life","http://www.impawards.com/1995/posters/toy_story_ver1.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc","released on 1955","http://www.imdb.com/title/tt0114709/?ref_=nv_sr_1")
#print(toy_story.storyline)
avatar=media.Movie("avatar","a marine on an alien planet ","http://www.impawards.com/2009/posters/avatar.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY","released on 2009","http://www.imdb.com/title/tt0499549/?ref_=nv_sr_1")
#print(avatar.storyline)
#avatar.show_trailer()
lego=media.Movie("lego","a story of nobody who saved everybody ","https://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg","https://www.youtube.com/watch?v=fZ_JOBCLF-I","released on 2014","http://www.imdb.com/title/tt1490017/?ref_=nv_sr_2")
#lego.show_trailer()
school_of_rock=media.Movie("school_of_rock","using rock music to learn","https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg","https://www.youtube.com/watch?v=3PsUJFEBC74","released on 2003","http://www.imdb.com/title/tt0332379/?ref_=nv_sr_3")
surfupwavemanie=media.Movie("surfupwavemani","starring your faviourite WWE superstars","http://images4.static-bluray.com/movies/covers/532_front.jpg","https://www.youtube.com/watch?v=zJarcJEmwgQ","released on 2017","http://www.imdb.com/title/tt5513260/?ref_=nv_sr_1")

movies=[toy_story,avatar,lego,school_of_rock,surfupwavemanie]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
