from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def guessing_game():
    if request.method == 'POST':
        to_small = request.form['to_small']
        to_big = request.form['to_big']
        guessed = request.form['guessed']

        min = 0
        max = 1000

        return render_template('game.html')

    else:
        return render_template('start.html')


if __name__ == '__main__':
    app.run(debug=True)
