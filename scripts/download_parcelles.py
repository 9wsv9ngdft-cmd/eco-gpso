
#!/usr/bin/env python3
"""Télécharge les parcelles cadastrales d'Issy-les-Moulineaux."""
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

INSEE = "92040"
BASE = "https://apicarto.ign.fr/api/cadastre/parcelle"
LIMIT = 1000
OUT = Path(__file__).resolve().parents[1] / "data" / "parcelles_92040.geojson"


def fetch(start):
    params = {
        "code_insee": INSEE,
        "source_ign": "PCI",
        "_limit": LIMIT,
        "_start": start,
    }
    url = BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/geo+json, application/json"}
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=90) as response:
                return json.load(response)
        except (urllib.error.URLError, TimeoutError):
            if attempt == 3:
                raise
            time.sleep(2 ** (attempt + 1))


def main():
    features = []
    start = 0
    total = None

    while total is None or start < total:
        data = fetch(start)
        batch = data.get("features", [])

        if total is None:
            total = int(data.get(
                "totalFeatures",
                data.get("numberMatched", len(batch))
            ))
            print("Total annoncé :", total)

        if not batch:
            break

        features.extend(batch)
        start += len(batch)
        print(f"Reçues : {len(features)} / {total}")

        if len(batch) < LIMIT:
            break

        time.sleep(0.2)

    if not features:
        raise SystemExit("Aucune parcelle reçue.")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    collection = {
        "type": "FeatureCollection",
        "name": "parcelles_92040",
        "features": features,
    }
    OUT.write_text(
        json.dumps(collection, ensure_ascii=False),
        encoding="utf-8"
    )
    print("Export terminé :", OUT)


if __name__ == "__main__":
    main()
