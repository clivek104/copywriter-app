from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Direct Response Copywriter</title>
    <style>
        body { font-family: Arial; margin: 40px; background: #f7f7f7; }
        textarea { width: 100%; height: 120px; }
        select, button { padding: 10px; margin-top: 10px; }
        .box { background: white; padding: 20px; border-radius: 8px; }
        pre { background: #eee; padding: 15px; }
    </style>
</head>
<body>
    <div class="box">
        <h1>AI Direct Response Copywriter</h1>

        <form method="post">
            <label>Product / Offer Description</label><br>
            <textarea name="input_text">{{ input_text }}</textarea><br>

            <label>Framework</label><br>
            <select name="framework">
                <option>PAS</option>
                <option>AIDA</option>
            </select><br>

            <button type="submit">Generate Copy</button>
        </form>

        {% if output %}
            <h2>Generated Copy</h2>
            <pre>{{ output }}</pre>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    input_text = ""

    if request.method == "POST":
        input_text = request.form.get("input_text", "")
        framework = request.form.get("framework")

        if framework == "PAS":
            output = f"""PROBLEM:
{input_text}

AGITATION:
This problem is costing you time, money, and momentum.

SOLUTION:
Here is the solution that finally fixes it."""
        else:
            output = f"""ATTENTION:
{input_text}

INTEREST:
Imagine fixing this faster than you thought possible.

DESIRE:
Others already are — and they love it.

ACTION:
Start now."""

    return render_template_string(HTML, output=output, input_text=input_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


