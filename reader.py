import struct
import json

def read_selective_columns(file_path, selected_columns):
    result = {}

    with open(file_path, "rb") as f:
        # 1. Check magic
        magic = f.read(4)
        if magic != b"COLM":
            raise ValueError("Invalid file format")

        # 2. Read row count
        num_rows = struct.unpack("<I", f.read(4))[0]

        # 3. Read schema
        schema_len = struct.unpack("<I", f.read(4))[0]
        schema = json.loads(f.read(schema_len).decode("utf-8"))
        columns = schema["columns"]

        # 4. Read columns
        for col in columns:
            name_len = struct.unpack("<H", f.read(2))[0]
            col_name = f.read(name_len).decode("utf-8")

            values = []
            for _ in range(num_rows):
                val_len = struct.unpack("<H", f.read(2))[0]
                value = f.read(val_len).decode("utf-8")
                values.append(value)

            if col_name in selected_columns:
                result[col_name] = values

    return result
