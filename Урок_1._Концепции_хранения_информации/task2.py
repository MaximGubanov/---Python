bytes_list = [b"class", b"function", b"method"]

for row in bytes_list:
    print(f'{type(row)} - {row.decode()} - {len(row)}')