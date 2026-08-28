#!/usr/bin/env python3
"""Overlay the corridor against the Tehuacán-Cuicatlán ANP boundary.

    python3 analysis/scripts/anp_overlay.py

WHAT THIS IS, AND IS NOT
This tests CORRIDOR WAYPOINTS against the reserve's *outer boundary*, obtained
from CONANP's own GIS (sig.conanp.gob.mx). It does NOT resolve subzones: the
subzonificación polygons are not published in the shapefiles CONANP distributes
(their zonas-nucleo layer contains no polygon for this reserve at all, which
independently confirms the management programme's statement that none exist).

The waypoints are AFORO STATIONS on route PUE-MEX-135, the highway that runs the
Cañada de Cuicatlán alongside the railway, plus the corridor endpoints. They are
a PROXY for the rail alignment, not the alignment itself. Treat the result as
"the corridor passes through the reserve, and roughly this much of it does",
not as a measured right-of-way overlap.

Geometry is lat/long ITRF2008, treated as WGS84 (the difference is far below
the precision of the proxy).
"""
from __future__ import annotations

import math
from pathlib import Path

import shapefile

ROOT = Path(__file__).resolve().parents[2]
SHP = ROOT / "sources" / "raw" / "_shp" / "232-ANP_ITRF08_19162026"

# Corridor waypoints, north -> south. Aforo stations on PUE-MEX-135 (the Cañada
# road paralleling the railway) plus the two endpoints.
WAYPOINTS = [
    ("Tehuacán (corridor entry)",        18.4871, -97.4562),
    ("Teotitlán del Camino",             18.1317, -97.0639),
    ("Teotitlán del Camino (2)",         18.1188, -97.0737),
    ("Santa María Tecomavaca",           17.9555, -97.0255),
    ("Santa María Tecomavaca (2)",       17.9495, -97.0222),
    ("San Juan Bautista Cuicatlán",      17.7939, -96.9600),
    ("Nacaltepec",                       17.5056, -96.9000),
    ("Nazareno Etla",                    17.1668, -96.7877),
    ("Oaxaca City (corridor terminus)",  17.0600, -96.7250),
]


def rings(shape):
    parts = list(shape.parts) + [len(shape.points)]
    return [shape.points[parts[i]:parts[i + 1]] for i in range(len(parts) - 1)]


def in_ring(x, y, ring):
    inside = False
    n = len(ring)
    for i in range(n):
        x1, y1 = ring[i]
        x2, y2 = ring[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            xin = x1 + (y - y1) / (y2 - y1) * (x2 - x1)
            if x < xin:
                inside = not inside
    return inside


def in_polygon(x, y, rs):
    """Even-odd across all rings: correctly handles holes."""
    return sum(in_ring(x, y, r) for r in rs) % 2 == 1


def haversine(a, b):
    (la1, lo1), (la2, lo2) = a, b
    R = 6371.0088
    p1, p2 = math.radians(la1), math.radians(la2)
    dp, dl = p2 - p1, math.radians(lo2 - lo1)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def main() -> None:
    r = shapefile.Reader(str(SHP))
    flds = [f[0] for f in r.fields[1:]]
    i_name = flds.index("NOMBRE")
    target = next(i for i, rec in enumerate(r.records()) if rec[i_name] == "Tehuacán-Cuicatlán")
    rec = r.records()[target]
    rs = rings(r.shape(target))
    print(f"ANP: {rec[i_name]} | {dict(zip(flds, rec))['CAT_MANEJO']} | "
          f"{dict(zip(flds, rec))['SUPERFICIE']:,.1f} ha | {len(rs)} ring(s)\n")

    print("WAYPOINT TEST (proxy: PUE-MEX-135 aforo stations + endpoints)")
    flags = []
    for name, lat, lon in WAYPOINTS:
        ins = in_polygon(lon, lat, rs)
        flags.append(ins)
        print(f"  {'INSIDE ' if ins else 'outside'}  {lat:8.4f} {lon:9.4f}  {name}")

    # Boundary geometry at each waypoint latitude: does the reserve leave a gap
    # along the valley floor, and how wide is it?
    print("\nBOUNDARY GEOMETRY AT EACH WAYPOINT LATITUDE")
    for name, lat, lon in WAYPOINTS:
        v = []
        for k in range(len(rs[0]) - 1):
            x1, y1 = rs[0][k]; x2, y2 = rs[0][k + 1]
            if (y1 > lat) != (y2 > lat):
                v.append(x1 + (lat - y1) / (y2 - y1) * (x2 - x1))
        v.sort()
        bands = list(zip(v[::2], v[1::2]))
        if not bands:
            print(f"  {name:32s} no reserve at this latitude")
            continue
        gap = ""
        for a, b in bands:
            if b < lon:
                gap = f"gap east of reserve edge {b:.4f} -> station {lon:.4f}: " \
                      f"{abs(lon - b) * 111 * 0.95:.1f} km"
        print(f"  {name:32s} reserve bands {[(round(a,3), round(b,3)) for a,b in bands]}")
        if gap:
            print(f"  {'':32s}   {gap}")

    # Densified traverse along the waypoint polyline
    STEP_KM = 1.0
    inside_km = total_km = 0.0
    for i in range(len(WAYPOINTS) - 1):
        (_, la1, lo1), (_, la2, lo2) = WAYPOINTS[i], WAYPOINTS[i + 1]
        seg = haversine((la1, lo1), (la2, lo2))
        n = max(1, int(seg / STEP_KM))
        for k in range(n):
            f0, f1 = k / n, (k + 1) / n
            mlat = la1 + (la2 - la1) * (f0 + f1) / 2
            mlon = lo1 + (lo2 - lo1) * (f0 + f1) / 2
            d = seg / n
            total_km += d
            if in_polygon(mlon, mlat, rs):
                inside_km += d
    print(f"\nDensified traverse ({STEP_KM} km steps) along the waypoint polyline:")
    print(f"  polyline length      : {total_km:7.1f} km  (straight-line chords, "
          f"so SHORTER than the 216.5 km route)")
    print(f"  inside the reserve   : {inside_km:7.1f} km")
    print(f"  share inside         : {100*inside_km/total_km:7.1f} %")
    print("""
DO NOT READ THAT PERCENTAGE AS A RIGHT-OF-WAY OVERLAP. It is an artefact.

The traverse chords straight between towns. The real alignment, like the
highway, follows the VALLEY FLOOR -- and every valley-floor waypoint tests
OUTSIDE the reserve. The reserve occupies the slopes on either side of the
Cañada, leaving the floor in a gap several km wide. A straight chord between two
excluded valley points cuts through the included slopes on the way; a railway
does not.

WHAT THIS OVERLAY ACTUALLY SHOWS
  - The Cañada valley floor, where both MEX-135 and the railway run, appears to
    be EXCLUDED from the reserve boundary.
  - South of roughly 17.53 N there is no reserve at any longitude.
  - So the alignment may run substantially, perhaps wholly, OUTSIDE the ANP.

WHAT IT DOES NOT SHOW
  - The rail centreline was never obtained; road stations are the proxy.
  - The excluded corridor is only a few km wide. Cuttings, borrow pits,
    structures, spoil and realignment could still enter reserve land even if
    the centreline does not.
  - The reserve's zone of influence is larger than the ANP polygon and may
    still trigger review.
  - Subzones are NOT resolved: CONANP does not publish subzonificación polygons,
    and its zonas-nucleo layer has no polygon for this reserve at all --
    independently confirming the management programme's statement that none
    was ever established.
""")


if __name__ == "__main__":
    main()
