import csv
import struct
import json

def write_columnar_file(csv_file, output_file):
    with open(csv_file, "r", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        columns = reader.fieldnames

    num_rows = len(rows)

    # Prepare column-wise data
    column_data = {col: [] for col in columns}
    for row in rows:
        for col in columns:
            column_data[col].append(row[col])

    with open(output_file, "wb") as f:
        # 1. Write magic header
        f.write(b"COLM")

        # 2. Write number of rows
        f.write(struct.pack("<I", num_rows))

        # 3. Write schema as JSON
        schema = {"columns": columns}
        schema_bytes = json.dumps(schema).encode("utf-8")

        f.write(struct.pack("<I", len(schema_bytes)))
        f.write(schema_bytes)

        # 4. Write column data
        for col in columns:
            values = column_data[col]

            # column name
            col_name_bytes = col.encode("utf-8")
            f.write(struct.pack("<H", len(col_name_bytes)))
            f.write(col_name_bytes)

            # values
            for value in values:
                val_bytes = value.encode("utf-8")
                f.write(struct.pack("<H", len(val_bytes)))
                f.write(val_bytes)
