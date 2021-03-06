from flask import render_template, redirect, url_for, request
from application import db, app
from application.models import Review, Albums
from application.forms import ReviewForm

@app.route('/')
def index():
    albums = Albums.query.all()
    reviews =  Review.query.all()
    return render_template('index.html', reviews= reviews, albums=albums)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = ReviewForm()
    albums = Albums.query.all()
    album_choices = []
    for album in albums:
        album_choices.append((str(album.id), album.album))
    form.albumid.choices = album_choices
    if form.validate_on_submit():
        new_review = Review(review=form.review.data, album_id=form.albumid.data,rating=form.rating.data)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/update/<int:review_id>', methods=['GET', 'POST'])
def update(review_id):
    form = ReviewForm()
    albums = Albums.query.all()
    album_choices = []
    for album in albums:
        album_choices.append((str(album.id), album.album))
    form.albumid.choices = album_choices
    review_to_update = Review.query.get(review_id)
    if form.validate_on_submit():
        review_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.review.data = review_to_update.review
    return render_template('update.html', form=form)

@app.route('/delete/<int:review_id>')
def delete(review_id):
    review_to_delete = Review.query.get(review_id)
    db.session.delete(review_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

