import os
from collections import defaultdict
from datasets import load_dataset

OUT_DIR = "datasets/ICEWS14"
os.makedirs(OUT_DIR, exist_ok=True)

def guess_keys(example):
    candidates = [
        ("head", "relation", "tail", "time"),
        ("h", "r", "t", "time"),
        ("subject", "predicate", "object", "timestamp"),
        ("head", "relation", "tail", "timestamp"),
    ]
    for h, r, t, tm in candidates:
        if h in example and r in example and t in example and tm in example:
            return h, r, t, tm
    raise KeyError(f"Could not find (h,r,t,time) keys in example keys={list(example.keys())}")

def write_split(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        for h, r, t, tm in rows:
            f.write(f"{h}\t{r}\t{t}\t{tm}\n")

def main():
    ds = load_dataset("linxy/ICEWS14")  

    all_rows = []
    for split_name in ds.keys():
        for ex in ds[split_name]:
            if not all_rows:
                hk, rk, tk, tmk = guess_keys(ex)
            all_rows.append((str(ex[hk]), str(ex[rk]), str(ex[tk]), str(ex[tmk])))

    by_time = defaultdict(list)
    for row in all_rows:
        by_time[row[3]].append(row)

    times_sorted = sorted(by_time.keys())

    n = len(times_sorted)
    n_train = int(0.8 * n)
    n_valid = int(0.1 * n)
    train_times = set(times_sorted[:n_train])
    valid_times = set(times_sorted[n_train:n_train + n_valid])
    test_times  = set(times_sorted[n_train + n_valid:])

    train_rows = []
    valid_rows = []
    test_rows  = []
    for tm, rows in by_time.items():
        if tm in train_times:
            train_rows.extend(rows)
        elif tm in valid_times:
            valid_rows.extend(rows)
        else:
            test_rows.extend(rows)

    write_split(os.path.join(OUT_DIR, "train.txt"), train_rows)
    write_split(os.path.join(OUT_DIR, "valid.txt"), valid_rows)
    write_split(os.path.join(OUT_DIR, "test.txt"),  test_rows)

    print("Wrote:")
    print("  train:", len(train_rows))
    print("  valid:", len(valid_rows))
    print("  test :", len(test_rows))
    print("Distinct timestamps:", n)

if __name__ == "__main__":
    main()
