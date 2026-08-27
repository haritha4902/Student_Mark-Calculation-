from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def result():

    if request.method == "POST":

        T = int(request.form["tamil"])
        E = int(request.form["english"])
        M = int(request.form["maths"])
        S = int(request.form["science"])
        SS = int(request.form["social"])

        total = T + E + M + S + SS

        average = total / 5

        percentage = (total / 500) * 100

        if average >= 90:
            grade = "Grade A"

        elif average >= 75:
            grade = "Grade B"

        elif average >= 50:
            grade = "Grade C"

        else:
            grade = "Grade Fail"


        # Store student result in Python dictionary

        student = {
            "tamil": T,
            "english": E,
            "maths": M,
            "science": S,
            "social": SS,
            "total": total,
            "average": average,
            "percentage": percentage,
            "grade": grade
        }


        # Store dictionary in JSON file

        with open("students.json", "w") as file:
            json.dump(student, file, indent=4)


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

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)