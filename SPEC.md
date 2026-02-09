HEADER
--------------------------------------------------
| MAGIC (4B) | VERSION (4B) |
| NUM_ROWS (4B) | NUM_COLS (4B) |
| SCHEMA_LEN (4B) | SCHEMA_JSON |
| COLUMN METADATA (per column) |

COLUMN METADATA (REPEATED)
--------------------------------------------------
| NAME_LEN (2B) | NAME |
| TYPE (1B) |
| OFFSET (8B) |
| COMPRESSED_SIZE (4B) |
| UNCOMPRESSED_SIZE (4B) |

DATA SECTION
--------------------------------------------------
| COMPRESSED COLUMN 1 |
| COMPRESSED COLUMN 2 |
| ... |
