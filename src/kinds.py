# src/kinds.py
import json
import os

def get_config(name="config"):
    config_dir = os.path.join(os.path.dirname(__file__), f"../{name}")
    config_file = os.path.join(config_dir, f"{name}.json")
    os.makedirs(config_dir, exist_ok=True)
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

class Kind:
    def __init__(self, name, color, hotness):
        self.name = name
        self.color = color
        self.hotness = hotness

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.color

class Kinds:
    config = get_config("config")
    kinds = None
    colors = None
    hotness_total = 0

    colors = config["colors"]
    try:
        kinds = config["kinds"]
    except KeyError:
        kinds = {}

    def __init__(self, *args, **kwargs):
        self.add(*args, **kwargs)

    def add(self, name=None, color="pink", hotness=1):
        if name is None:
            name = "null"
            hotness = 0

        self.kinds[name] = {
            "color": color,
            "hotness": hotness
        }
        self.hotness_total += hotness

    def kind(self, name):
        if name not in self.kinds:
            raise ValueError(f"kind {name} not found")
        return Kind(name, self.color(name), self.hotness(name))

    def color(self, kind):
        return self.kinds[kind]["color"]

    def hotness(self, kind):
        return self.kinds[kind]["hotness"]

    def rgb(self, kind):
        return self.colors[kind.color()]

    def rand(self):
        import random
        r = random.randint(1, self.hotness_total)
        #print("r= ", r)
        for k, v in self.kinds.items():
            r -= v["hotness"]
            if r <= 0:
                break
        return self.kind(k)
