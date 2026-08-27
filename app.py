from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def result():

    if request.method == "POST":

        T = int(request.form["tamil"])
        E = int(request.form["english"])
        M = int(request.form["maths"])
        S = int(request.form["science"])
        SS = int(request.form["social"])

        # Calculate total
        total = T + E + M + S + SS

        # Calculate average
        average = total / 5

        # Calculate percentage
        percentage = (total / 500) * 100

        # Calculate grade
        if average >= 90:
            grade = "Grade A"

        elif average >= 75:
            grade = "Grade B"

        elif average >= 50:
            grade = "Grade C"

        else:
            grade = "Grade Fail"

        # Display result
        return render_template(
            "index.html",
            tamil=T,
            english=E,
            maths=M,
            science=S,
            social=SS,
            total=total,
            average=average,
            percentage=percentage,
            grade=grade
        )

    # GET request
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)