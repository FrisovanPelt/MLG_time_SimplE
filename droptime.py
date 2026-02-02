from pathlib import Path

def strip_time(in_path: str, out_path: str, dedup: bool = True):
    triples = set() if dedup else None
    out_lines = []

    with open(in_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 3:
                continue
            h, r, t = parts[0], parts[1], parts[2]

            if dedup:
                key = (h, r, t)
                if key in triples:
                    continue
                triples.add(key)

            out_lines.append(f"{h}\t{r}\t{t}\n")

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.writelines(out_lines)

strip_time("datasets/ICEWS14/train.txt", "datasets/ICEWS14_static/train.txt", dedup=True)
strip_time("datasets/ICEWS14/valid.txt", "datasets/ICEWS14_static/valid.txt", dedup=True)
strip_time("datasets/ICEWS14/test.txt",  "datasets/ICEWS14_static/test.txt",  dedup=True)
