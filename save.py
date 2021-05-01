import os
import time
from csv_stuffs import getListCSV
from load import copas
from load import setupFile

def nosave():
	# nosave, dipakai ketika tidak dilakukan penyimpanan di CWD pada saat exit
	# semua file baru dihapus (bisa jadi disave di folder lain sebelumnya)
	RemoveList = getListCSV("no_temp")
	for i in range(len(RemoveList)):	
		os.remove(RemoveList[i]) 
	
	# file lama (temp_) diubah kembali namanya
	RenameList = getListCSV("only_temp")
	for i in range(len(RenameList)):	
		os.rename(RenameList[i], RemoveList[i]) 
	
	return None

def upToDate():
	# ngecek apakah file up to date (perlu disave atau engga)
	CSV = getListCSV("no_temp")
	Temp_CSV = getListCSV("only_temp")
	for i in range(len(CSV)): # ukurannya sama
		f = open(CSV[i], 'r')
		g = open(Temp_CSV[i], 'r')
		if (f.read() != g.read()):
			f.close()
			g.close()
			return False # ada yg ga up to date
		f.close()
		g.close()
	return True # semua file up to date

def save(exit = False):
	# fungsi save, untuk ditengah program ataupun pada saat exit (jika dipilih yes)
	if upToDate():
		# kalau gada perubahan yang perlu disimpan
		print("Tidak ada perubahan yang perlu disimpan!")
		return None
	
	ans = str(input("Apakah anda ingin menyimpan data di folder saat ini? (y/n): "))
	ansValid = False
	while (not(ansValid)): 
		if (ans == "y") or (ans == "Y") : # penyimpanan di current working directory (cwd)
			print("Saving...")
			time.sleep(3) # efek saving...
			# file lama (_temp) dihapus, file baru menggantikan
			RemoveList = getListCSV("only_temp")
			for i in range(len(RemoveList)):	
				os.remove(RemoveList[i]) 	
				
			if (not(exit)):
				# Kasus penyimpanan di tengah program (bukan saat exit)
				# Dilakukan setupFile seperti pada load, karena ada kemungkinan program masih digunakan setelah save
				setupFile()
				print("Data telah disimpan pada folder saat ini!")
			else: # saat exit
				print("Perubahan file telah disimpan di folder saat ini, Terima Kasih!")
			
			ansValid = True
		elif (ans == "n") or (ans == "N") : # penyimpanan di folder/direktori lain
			
			# file lama tidak perlu dihapus, file baru dicopy ke folder baru kemudian dihapus pada cwd, nama file lama diganti kembali 
			# file baru tidak dihapus karena mungkin masih digunakan pada program (jika tidak disave lagi, akan dihapus pada saat exit)
			folder_name = input("Masukkan nama folder penyimpanan: ")
			dir_save = os.path.dirname(os.path.abspath(__file__)) + "\\" + folder_name # direktori tujuan
			
			print("Saving...")
			time.sleep(3)
			
			if not(os.path.exists(dir_save)):
				# Jika foldernya belum ada, dibuat dulu foldernya
				print("Folder belum ada, akan dibuat folder baru")
				os.mkdir(dir_save) # foldernya dibuat
				
			# path file tujuan = dir_save + "\\" + CopasList[i]
			# copas ke path tujuan
			CopasList = getListCSV("no_temp")
			for i in range(len(CopasList)):	
				copas(CopasList[i], dir_save + "\\" + CopasList[i]) 
			
			
			if (exit):
				# Dalam kasus ketika exit, file baru (sudah disimpan di folder lain) dihapus dan file lama (_temp) diganti kembali namanya
				nosave() # -dilakukan di nosave
				print("Perubahan file telah disimpan pada folder " + folder_name + ", terima kasih!")
			else: # not exit
				print("Perubahan file telah disimpan pada folder " + folder_name + "!")
				
			ansValid = True	
		else: # jawaban tidak valid
			ans = str(input("Jawab dengan y(ya) atau n(tidak) !: "))	
	
	return None

