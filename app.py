from flask import Flask, render_template, request

app = Flask(__name__)


# Grade calculation function
def calculate_grade(mark):

    if mark >= 90:
        return "A"

    elif mark >= 75:
        return "B"

    elif mark >= 50:
        return "C"

    else:
        return "Fail"


@app.route("/", methods=["GET", "POST"])
def result():

    if request.method == "POST":

        # Get student name
        name = request.form["name"]

        # Get marks
        T = int(request.form["tamil"])
        E = int(request.form["english"])
        M = int(request.form["maths"])
        S = int(request.form["science"])
        SS = int(request.form["social"])

        # Total
        total = T + E + M + S + SS

        # Average
        average = total / 5

        # Percentage
        percentage = (total / 500) * 100

        # Subject grades
        tamil_grade = calculate_grade(T)
        english_grade = calculate_grade(E)
        maths_grade = calculate_grade(M)
        science_grade = calculate_grade(S)
        social_grade = calculate_grade(SS)

        # Overall grade
        overall_grade = calculate_grade(percentage)

        return render_template(
            "index.html",
            name=name,
            tamil=T,
            english=E,
            maths=M,
            science=S,
            social=SS,
            tamil_grade=tamil_grade,
            english_grade=english_grade,
            maths_grade=maths_grade,
            science_grade=science_grade,
            social_grade=social_grade,
            total=total,
            average=average,
            percentage=percentage,
            overall_grade=overall_grade
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)