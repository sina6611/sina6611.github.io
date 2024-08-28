from flask import Flask, render_template
import random
from datetime import datetime
app=Flask(__name__)


@app.route("/")
def home():
    current_year=datetime.now().year
    randn=random.randint(1,100)
    return render_template('index.html',rnd=randn,cry=current_year)
