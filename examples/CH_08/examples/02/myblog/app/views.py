from app import app

from flask import render_template
from datetime import datetime
from random import sample
import json



class PageVisit:
    COUNT = 0

    def counts(self):
        PageVisit.COUNT += 1
        return PageVisit.COUNT


class BannerColors:
    COLORS = [
        "lightcoral", "salmon", "red", "firebrick", "pink",
        "gold", "yellow", "khaki", "darkkhaki", "violet",
        "blue", "purple", "indigo", "greenyellow", "lime",
        "green", "olive", "darkcyan", "aqua", "skyblue",
        "tan", "sienna", "gray", "silver"
    ]

    def get_colors(self):
        return sample(BannerColors.COLORS, 5)


@app.route("/")
def home():
    banner_colors = BannerColors().get_colors()
    return render_template("index.html", data={
        "now": datetime.now(),
        "page_visit": PageVisit(),
        "banner_colors": {
            "display": banner_colors,
            "js": json.dumps(banner_colors)
        }
    })