# Custom Columnar File Format (Python)

## Project Overview

This project implements a custom binary **columnar file format** using Python.  
It converts row-based CSV files into a column-oriented binary format and supports **selective column reads**, improving read efficiency compared to traditional row-based storage.

The project includes:
- A writer to convert CSV → custom columnar format
- A reader to selectively read required columns
- Command-line tools for conversion and testing
- A formal specification of the binary file format

---

## Features

- Custom binary file format
- Column-oriented storage
- Selective column reads
- Command-line interface (CLI)
- Lossless round-trip conversion (CSV → columnar → CSV)
- No external dependencies (pure Python)

---

## Repository Structure

columnar-file-format/
├── reader.py # Columnar file reader
├── writer.py # Columnar file writer
├── cli.py # Command-line tools
├── test_run.py # Test script
├── sample_data/
│ └── test.csv # Sample CSV file
├── README.md
├── SPEC.md # File format specification
└── requirements.txt



---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher

### Install Dependencies
This project uses only Python standard libraries.

```bash
#pip install -r requirements.txt


