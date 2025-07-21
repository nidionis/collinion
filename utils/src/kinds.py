# src/kinds.py
from utils import get_config
import numpy as np
import random

class Kind:
    def __init__(self, name, color, hotness=1, weight=1):
        self.name = name
        self.color = color
        self.hotness = hotness
        self.weight = weight

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Kinds:
    config = get_config("config")
    kinds = None
    colors = None
    hotness_total = 0
    # Cache for random selection
    kind_names = None
    hotness_ratio = None

    colors = config["colors"]
    try:
        kinds = config["kinds"]
    except KeyError:
        kinds = {}

    def __init__(self, *args, **kwargs):
        self.add(*args, **kwargs)
        self.add("DFLT", "black", hotness=0)
        self._update_random_cache()

    def _update_random_cache(self):
        self.kind_names = np.array(list(self.kinds.keys()))
        self.hotness_ratio = np.array([self.kinds[k]["hotness"] for k in self.kind_names])
        if self.hotness_total > 0:
            self.hotness_ratio = self.hotness_ratio / self.hotness_total

    def add(self, name=None, color="pink", hotness=1, weight=1):
        if name is None:
            name = "DFLT"
            hotness = 0
            weight = 0

        self.kinds[name] = {
            "color": color,
            "hotness": hotness,
            "weight": weight
        }
        self.hotness_total += hotness
        self._update_random_cache()

    def kind(self, name):
        if name not in self.kinds:
            raise ValueError(f"kind {name} not found")
        return Kind(name, self.color(name), self.hotness(name), self.weight(name))

    def weight(self, kind):
        return self.kinds[str(kind)]["weight"]

    def color(self, kind):
        return self.kinds[str(kind)]["color"]

    def hotness(self, kind):
        return self.kinds[kind]["hotness"]

    def rgb(self, kind):
        return self.colors[kind.color()]

    def rand(self):
        if self.hotness_total <= 0:
            return self.kind("DFLT")
            
        if len(self.kind_names) > 0:
            selected = np.random.choice(self.kind_names, p=self.hotness_ratio)
            return self.kind(selected)
        else:
            r = random.randint(1, self.hotness_total)
            for k, v in self.kinds.items():
                r -= v["hotness"]
                if r <= 0:
                    break
            return self.kind(k)
