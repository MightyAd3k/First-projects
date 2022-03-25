from flask import Flask, request

start = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
    <h1>Imagine number between 0 and 1000</h1>
    <form action="" method="POST">
        <input type="hidden" name="min" value="{}">
        <input type="hidden" name="max" value="{}">
        <input type="submit" value="OK">
    </form>
</body>
</html>
"""

game = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
    <h1>It is number {guess}</h1>
    <form action="" method="POST">
        <input type="submit" name="user_answer" value="too big">
        <input type="submit" name="user_answer" value="too small">
        <input type="submit" name="user_answer" value="you won">
        <input type="hidden" name="min" value="{min}">
        <input type="hidden" name="max" value="{max}">
        <input type="hidden" name="guess" value="{guess}">
        <input type="hidden" name="counter" value="{counter}">
        <h3>{message}</h3>
        
    </form>
</body>
</html>
"""

finish = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
    <h1>Hurra! I guess! Your number is {guess}</h1>
    <h3>I did it in {counter} tries.</h3> 
</body>
</html>

"""

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    if request.method == "GET":
        return start.format(0, 1000)
    else:
        min_number = int(request.form["min"])
        max_number = int(request.form["max"])
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))
        counter = int(request.form.get("counter", 0))

        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess
        elif user_answer == "you won":
            return finish.format(guess=guess, counter=counter)

        guess = (max_number - min_number) // 2 + min_number
        counter += 1
        message = ''

        if counter > 10:
            message = "Do not cheat!"

        return game.format(guess=guess, min=min_number, max=max_number, counter=counter, message=message)


if __name__ == '__main__':
    app.run()
