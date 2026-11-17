from tools import clear_data, add_item, sell_item, find_item, list_items

while True:
    try:
        perintah = input().strip()
    except EOFError:
        break

    if perintah == "EXIT":
        break
    elif perintah == "CLEAR":
        clear_data()
        print("Data dikosongkan.")
    elif perintah.startswith("ADD|"):
        bagian = perintah.split("|")
        if len(bagian) != 4:
            print("Error: format tidak valid.")
            continue
        _, nama, stok, harga = bagian
        try:
            add_item(nama, stok, harga)
            print("Barang ditambahkan.")
        except ValueError as e:
            print(f"Error: {e}")
    elif perintah.startswith("SELL|"):
        bagian = perintah.split("|")
        if len(bagian) != 3:
            print("Error: format tidak valid.")
            continue
        _, nama, qty = bagian
        try:
            sell_item(nama, qty)
            print("Penjualan berhasil.")
        except ValueError as e:
            print(f"Error: {e}")
    elif perintah.startswith("FIND|"):
        print(find_item(perintah.split("|", 1)[1]))
    elif perintah == "LIST":
        print(list_items())
    else:
        print("Error: perintah tidak dikenal.")