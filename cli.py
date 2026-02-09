import sys
import csv
from writer import write_columnar_file
from reader import read_selective_columns, read_all_columns


def columnar_to_csv(columnar_file, output_csv):
    data = read_all_columns(columnar_file)
    headers = list(data.keys())
    rows = zip(*data.values())

    with open(output_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


if __name__ == "__main__":
    cmd = sys.argv[1]

    if cmd == "write":
        write_columnar_file(sys.argv[2], sys.argv[3])
        print("✔ Columnar file created")

    elif cmd == "read":
        data = read_selective_columns(sys.argv[2], sys.argv[3:])
        for k, v in data.items():
            print(k, "->", v)

    elif cmd == "to_csv":
        columnar_to_csv(sys.argv[2], sys.argv[3])
        print("✔ CSV recreated")
