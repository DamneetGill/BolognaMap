import pickle
import csv


with open("graph (8).pkl", "rb") as f:
    G = pickle.load(f)

print("Grafo caricato")



with open("nodes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "id",
        "label",
        "x",
        "y",
        "elev",
        "mode",
        "subtype",
        "slope_pct", 
        "delta_h",
        "length",
        "key",
        "value"    
    ])

    for node_id, data in G.nodes(data=True):
        lon = data.get("lon") or data.get("x")
        lat = data.get("lat") or data.get("y")
        writer.writerow([
            node_id,
            data.get("type"),
            lon,
            lat,
            data.get("elev"),
            ",".join(data.get("mode", [])) if isinstance(data.get("mode"), list) else data.get("mode"),
            data.get("subtype"),
            data.get("slope_pct"),
            data.get("delta_h"),
            data.get("length"),
            data.get("key"),
            data.get("value")
        ])

print("nodes.csv esportato")

with open("edges.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "source",
        "target",
        "type"
    ])

    for u, v, data in G.edges(data=True):
        writer.writerow([
            u,
            v,
            data.get("type")
        ])

print("edges.csv esportato")
