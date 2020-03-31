from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY']='SuperSecretKey'

class GameDevForm(FlaskForm):
    game_name = StringField('Game Name:', validators=[DataRequired()])
    dev_name = StringField('Developer Name:', validators=[DataRequired()])

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Cullen\'s Games')

@app.route('/add_game', methods=['GET', 'POST'])
def add_game():
    form = GameDevForm()
    if form.validate_on_submit():
        return '<h2> My game name is {0} and its dev is {1}'.format(form.game_name.data, form.dev_name.data)

    return render_template('add_game.html', form=form, pageTitle='Add A New Game')

@app.route('/mike')
def mike():
    return render_template('mike.html', pageTitle='About Mike')

if __name__ == '__main__':
    app.run(debug=True)
