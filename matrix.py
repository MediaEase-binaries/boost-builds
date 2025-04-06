#!/usr/bin/env python3
import yaml
from collections import defaultdict

all_versions = [
    "1.69.0","1.70.0","1.71.0","1.72.0","1.73.0","1.74.0",
    "1.75.0","1.76.0","1.77.0","1.78.0","1.79.0","1.80.0",
    "1.81.0","1.82.0","1.83.0","1.84.0","1.85.0","1.86.0",
    "1.87.0","1.88.0_rc1"
]
rc_version = "1.88.0_rc1"

rules = [
    ("1.69.0", "1.75.0", ["ubuntu-20.04"]),
    ("1.75.0", "1.82.0", ["ubuntu-22.04"]),
    ("1.82.0", None,     ["ubuntu-24.04"]),

    ("1.72.0", "1.82.0", ["debian-11"]),
    ("1.82.0", None,     ["debian-12"]),
]

def parse(v):
    core = v.split("_")[0]
    return tuple(int(x) for x in core.split("."))

def ge(v1, v2):
    return parse(v1) >= parse(v2)

def le(v1, v2):
    return parse(v1) <= parse(v2)

support_map = defaultdict(list)
for vmin, vmax, oses in rules:
    for v in all_versions:
        if v == rc_version:
            continue
        if ge(v, vmin) and (vmax is None or le(v, vmax)):
            support_map[oses[0]] if False else None
            for os in oses:
                support_map[os].append(v)

matrix = []
for os, vers in support_map.items():
    sorted_vers = sorted(set(vers), key=parse)
    for v in sorted_vers[:-1]:
        matrix.append({"boost_version": v, "os": os, "stability": "oldstable"})
    matrix.append({"boost_version": sorted_vers[-1], "os": os, "stability": "stable"})

for vmin, vmax, oses in rules:
    if ge(rc_version, vmin) and (vmax is None or le(rc_version, vmax)):
        for os in oses:
            matrix.append({"boost_version": rc_version, "os": os, "stability": "next"})

print(yaml.safe_dump({"include": matrix}, sort_keys=False))
