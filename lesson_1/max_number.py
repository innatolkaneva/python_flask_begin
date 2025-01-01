from flask import Flask

app = Flask(__name__)

@app.route("/max_number/<path:nums>")
def max_num(nums: str):
    num_as_int = (int(item) for item in nums.split('/'))
    return f"Максимальное переданное число <b>{max(num_as_int)}</b>"

if __name__ == "__main__":
    app.run(debug=True)