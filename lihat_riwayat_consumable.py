from csv_stuffs import readCSV
from tgl import sort_data_date

def lihat_riwayat_consumable(): # Melihat riwayat pengambilan consumable
    datas_consumable_history = readCSV("consumable_history.csv")

    sort_data_date(datas_consumable_history[1]) # mengurutkan data terbaru berdasarkan tanggal

    if len(datas_consumable_history[1]) <= 5: # saat data <= 5
        for i in range(len(datas_consumable_history[1])):
            print("ID Pengambilan      : " + str(datas_consumable_history[1][i][0]))
            print("Nama Pengambil      : " + str(datas_consumable_history[1][i][1]))
            print("Nama Consumable     : " + str(datas_consumable_history[1][i][2]))
            print("Tanggal Pengambilan : " + str(datas_consumable_history[1][i][3]))
            print("Jumlah              : " + str(datas_consumable_history[1][i][4]))
            print("")
    else: # saat data > 5
        idx = 0
        while idx < 5:
            print("ID Pengambilan      : " + str(datas_consumable_history[1][idx][0]))
            print("Nama Pengambil      : " + str(datas_consumable_history[1][idx][1]))
            print("Nama Consumable     : " + str(datas_consumable_history[1][idx][2]))
            print("Tanggal Pengambilan : " + str(datas_consumable_history[1][idx][3]))
            print("Jumlah              : " + str(datas_consumable_history[1][idx][4]))
            print("")
            idx += 1