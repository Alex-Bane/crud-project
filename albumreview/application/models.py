from application import db



class Albums(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    album = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    review = db.relationship('Review', backref='albums')


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'))
