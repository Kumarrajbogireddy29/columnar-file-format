from writer import write_columnar_file
from reader import read_selective_columns

write_columnar_file("sample_data/sample.csv", "output.col")
print("✔ Columnar file created")

data = read_selective_columns("output.col", ["id", "name"])
print("\n✔ Selective read output:")
for col, values in data.items():
    print(col, "->", values)
