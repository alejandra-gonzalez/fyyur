from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Venue(db.Model):
  __tablename__ = 'venues'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  address = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))
  seeking_talent = db.Column(db.Boolean)
  seeking_description = db.Column(db.String(120))
  website = db.Column(db.String(120))
  genres = db.Column(db.String(120))
  shows = db.relationship('Show', backref=db.backref('venue'), lazy="joined")

class Artist(db.Model):
  __tablename__ = 'artists'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  genres = db.Column(db.String(120))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))
  seeking_venue = db.Column(db.Boolean)
  seeking_description = db.Column(db.String(120))
  website = db.Column(db.String(120))
  shows = db.relationship('Show', backref=db.backref('artist'), lazy="joined")

class Show(db.Model):
  __tablename__: 'shows'
  id = db.Column(db.Integer, primary_key=True, nullable = False)
  artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
  start_time = db.Column(db.DateTime())