from application import db
from application.models import Albums 


db.drop_all()
db.create_all()

new_album = Albums(album = "IGOR", artist= "Tyler, The Creator", genre = "Hip-Hop")
db.session.add(new_album)
new_album = Albums(album = "thank u, next", artist= "Ariana Grande", genre = "Pop")
db.session.add(new_album)
new_album = Albums(album = "Soy Pablo", artist = "Boy Pablo", genre = "Indie")
db.session.add(new_album)
new_album = Albums(album = "Kids See Ghosts", artist = "Kids See Ghosts", genre = "Hip-Hop")
db.session.add(new_album)
new_album = Albums(album = "Hold Your Colour", artist = "Pendulum", genre = "Drum and Bass")
db.session.add(new_album)
db.session.commit()
