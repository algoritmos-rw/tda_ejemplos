import json
from typing import Any, Callable
from itertools import chain
from dataclasses import dataclass
import pathlib

import requests
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.widgets import Slider
from mpl_toolkits.basemap import Basemap  # type: ignore

POLYGONS_PATH = pathlib.Path(__file__).parent / "country_polygons.json"

countries_map = {
    "Argentina": "Argentina",
    "Bolivia": "Bolivia",
    "Brazil": "Brasil",
    "Chile": "Chile",
    "Colombia": "Colombia",
    "Ecuador": "Ecuador",
    "Guyana": "Guyana",
    "France": "Guyana Francesa",
    "Paraguay": "Paraguay",
    "Peru": "Perú",
    "Suriname": "Surinam",
    "Uruguay": "Uruguay",
    "Venezuela": "Venezuela",
}

colors_list = ["red", "blue", "green", "purple", "orange"]


def get_polygons() -> dict[str, list[Any]]:
    if POLYGONS_PATH.exists():
        with open(POLYGONS_PATH, "r") as f:
            return json.load(f)

    # get country shapefiles with request
    url = "https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson"
    response = requests.get(url)
    response.raise_for_status()
    polygons_gen = (
        (x["properties"]["ADMIN"], x["geometry"]["coordinates"])
        for x in response.json()["features"]
    )
    countries_filter = set(
        chain(
            countries_map,
            ("Falkland Islands", "South Georgia and South Sandwich Islands"),
        )
    )
    country_polygons = {x: y for x, y in polygons_gen if x in countries_filter}
    country_polygons["Argentina"] += country_polygons["Falkland Islands"]
    country_polygons["Argentina"] += country_polygons[
        "South Georgia and South Sandwich Islands"
    ]
    with open(POLYGONS_PATH, "w") as f:
        json.dump(country_polygons, f)
    return country_polygons


def get_lines(
    ax: Axes, m: Basemap, polygons: dict[str, list[Any]]
) -> dict[str, LineCollection]:
    country_lines = {}
    for country in countries_map:
        segments = []
        if country not in polygons:
            print(f"Country {country} not found on geo data")
            continue
        for polygon in polygons[country]:
            for coords in polygon:
                lon, lat = zip(*coords)
                x, y = m(lon, lat)
                segments.append(list(zip(x, y)))
        lines = LineCollection(segments, antialiaseds=(1,))
        lines.set_facecolor("white")
        lines.set_edgecolor("k")
        lines.set_linewidth(0.3)
        ax.add_collection(lines)
        country_lines[country] = lines
    return country_lines


@dataclass
class MapController:
    update: Callable[[dict[str, int], str, str], None] = lambda *_: None
    wait_for_close: Callable[[], None] = lambda: None
    __delay_slider: Slider | None = None


def show_map(initial_delay: float | None = None) -> MapController:
    if initial_delay is None:
        return MapController()
    fig = plt.figure()
    m = Basemap(
        projection="merc", llcrnrlat=-60, urcrnrlat=20, llcrnrlon=-90, urcrnrlon=-30
    )
    width = 5
    fig.set_size_inches(width, width * m.aspect)
    m.drawcountries(linewidth=0)
    ax = plt.subplot()
    polygons = get_polygons()
    lines = get_lines(ax, m, polygons)
    fig.tight_layout()
    plt.show(block=False)

    title = plt.title("")
    label = plt.text(0.01, 0.025, "", fontsize=12, transform=ax.transAxes)
    closed = False
    delay: float = initial_delay

    def update(colors: dict[str, int], title_txt: str, label_txt: str) -> None:
        if closed:
            return
        for country, line in lines.items():
            mapped = countries_map[country]
            color = colors_list[colors[mapped]] if mapped in colors else "white"
            line.set_facecolor(color)
        title.set_text(title_txt)
        label.set_text(label_txt)
        plt.pause(delay)

    def wait_for_close() -> None:
        if closed:
            return
        plt.show()

    def on_close(_: Any) -> None:
        nonlocal closed
        closed = True
        plt.close()

    def on_slider_change(val: float) -> None:
        nonlocal delay
        delay = val

    ax_slider = fig.add_axes((0.3, 0.9, 0.4, 0.05))
    delay_slider = Slider(
        ax=ax_slider,
        label="Step delay",
        valmin=0.001,
        valmax=5,
        valinit=delay,
        orientation="horizontal",
        valfmt="%1.2fs",
    )

    delay_slider.on_changed(on_slider_change)
    fig.canvas.mpl_connect("close_event", on_close)
    return MapController(update, wait_for_close, delay_slider)
