from flask import Flask, render_template

from data_work.size_manager import initialize_data
from data_work.get_data_ready import get_data_ready
from visualizations.visualizations import get_all_vis

app = Flask(__name__)

try:
    initialize_data()
except FileExistsError:
    exit(1)

df = get_data_ready()
vis = get_all_vis(df)

@app.route("/")
def index():
    return render_template('index.html', vis=vis)

if __name__ == "__main__":
    app.run(debug=False)