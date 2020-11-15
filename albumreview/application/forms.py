from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Review, Albums

class ReviewCheck:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        all_reviews = Review.query.all()
        for review in all_reviews:
            if review.review == field.data:
                raise ValidationError(self.message)

class ReviewForm(FlaskForm):
    albumid = SelectField('Album',
            choices=[]
            )

    review = StringField('Review',
            validators=[
                DataRequired(),
                ReviewCheck(message='That Review already exists')
            ]
         )

    rating = SelectField('Rating',
                         choices=['1','2','3','4','5'],
                         validators=[
                             DataRequired(),
                             ReviewCheck(message='You must include a rating')
                        ]
                    )

    submit = SubmitField('Add Review')
    
