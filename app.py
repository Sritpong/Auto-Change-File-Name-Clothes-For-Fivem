import os
import shutil
import time
import ctypes

version = "1.2.0"
props = ['p_eyes', 'p_ears', 'p_head', 'p_lwrist', 'p_rwrist', 'p_lhand']

def printCopyRight():
	print('    )      )              )    (           )  ')
	print(' ( /(   ( /(      (    ( /(    )\ )     ( /(  ')
	print(' )\())  )\())   ( )\   )\())  (()/(     )\()) ')
	print('((_)\  ((_)\    )((_) ((_)\    /(_))   ((_)\  ')
	print(' _((_)   ((_)  ((_)_    ((_)  (_))_   __ ((_) ')
	print('| \| |  / _ \   | _ )  / _ \   |   \  \ \ / / ')
	print('| .` | | (_) |  | _ \ | (_) |  | |) |  \ V /  ')
	print('|_|\_|  \___/   |___/  \___/   |___/    |_|   ')
	print('\n')

def clearConsole(CopyRight):
	os.system('cls')
	if CopyRight == True:
		printCopyRight()

def main():
	clearConsole(True)
	os.system('title Auto rename for FIVEM By Nobody Dev (Current version: ' + version + ')')
	yddcount = 0
	ytdcount = 0
	i = int(input('Start at (0, 1, 2, etc..): '))
	clearConsole(True)
	input_path = input('Enter a directory path: ')
	clearConsole(True)
	path = input_path.replace('"', '').replace("\\", "/") + "/"
	export_path = path + "export/"
	type_file = input('Enter file your want (jbib, lowr, accs, etc..): ')
	clearConsole(True)

	isHashDirectory = os.path.exists(path)
	if not isHashDirectory:
		clearConsole(True)
		print('Not found directory "' + path + '"')
		exit()

	isHasExport = os.path.exists(export_path)
	if not isHasExport:
		clearConsole(True)
		print("Creating export directory")
		time.sleep(1)
		os.makedirs(export_path)
		clearConsole(True)

	while True:
		list_file = []
		first_name_file = input('Enter first name file (mp_m_freemode_01^brabrabra.ydd please input "mp_m_freemode_01" or if you want to exit please input "exit" or if you want to reset please input "reset"): ').split("^")[0]
		clearConsole(True)

		if first_name_file == 'exit':
			clearConsole(False)
			break
		elif first_name_file == 'reset':
			i = int(input('Start at (0, 1, 2, etc..): '))
			clearConsole(True)
			type_file = input('Enter file your want (jbib, lowr, accs, etc..): ')
			clearConsole(True)
			continue
		
		clearConsole(True)
		print("Starting to export from " + path + " to " + export_path)
		time.sleep(1)
		clearConsole(True)

		if type_file not in props:
			for filename in os.listdir(path):
				isFile = os.path.isfile(path + filename)
				if isFile == True:
					temp_filename = filename.split(".")
					if first_name_file.lower() != 'none' and temp_filename[0].split("^")[0] == first_name_file and temp_filename[1] != 'ymt':
						name = temp_filename[0].split("^")[1]
						ext = temp_filename[1]

						if ext == 'ydd' and name.split("_")[0] == type_file:
							new_name = None
							new_num = None
							check_type = name.split("_")

							if i < 10:
								new_num = "00" + str(i)
							elif i >= 10 and i <= 99:
								new_num = "0" + str(i)
							elif i >= 100:
								new_num = str(i)
							new_name = check_type[0] + "_" + new_num + "_" + check_type[2] + ".ydd"

							print("Exporting " + filename + " > " + new_name + " ...")
							shutil.copy2(path + filename, export_path + new_name)
							print("Exported " + filename + " > " + new_name)
							clearConsole(True)
							list_file.append([check_type[1], new_name])
							i += 1
							yddcount += 1
						else:
							continue
					elif first_name_file.lower() == 'none' and temp_filename[1] != 'ymt':
						name = temp_filename[0]
						ext = temp_filename[1]

						if ext == 'ydd' and name.split("_")[0] == type_file:
							new_name = None
							new_num = None
							check_type = name.split("_")

							if i < 10:
								new_num = "00" + str(i)
							elif i >= 10 and i <= 99:
								new_num = "0" + str(i)
							elif i >= 100:
								new_num = str(i)
							new_name = check_type[0] + "_" + new_num + "_" + check_type[2] + ".ydd"

							print("Exporting " + filename + " > " + new_name + " ...")
							shutil.copy2(path + filename, export_path + new_name)
							print("Exported " + filename + " > " + new_name)
							clearConsole(True)
							list_file.append([check_type[1], new_name])
							i += 1
							yddcount += 1
						else:
							continue
				else:
					continue

			for filename in os.listdir(path):
				isFile = os.path.isfile(path + filename)
				if isFile == True:
					temp_filename = filename.split(".")
					if temp_filename[0].split("^")[0] == first_name_file and temp_filename[1] != 'ymt':
						name = temp_filename[0].split("^")[1]
						ext = temp_filename[1]

						if ext == 'ytd' and name.split("_")[0] == type_file:
							check_type = name.split("_")
							for get_num in list_file:
								if get_num[0] == check_type[2]:
									file_type = None
									if len(check_type) == 4:
										ft = get_num[1].split(".")[0].split("_")[2]
										if ft == 'u':
											file_type = 'uni'
										elif ft == 'r':
											file_type = 'whi'
									else:
										file_type = check_type[4]

									new_name = check_type[0] + "_diff_" + get_num[1].split("_")[1] + "_" + check_type[3] + "_" + file_type + ".ytd"
									print("Exporting " + filename + " > " + new_name + " ...")
									shutil.copy2(path + filename, export_path + new_name)
									print("Exported " + filename + " > " + new_name)
									clearConsole(True)
									ytdcount += 1
									break
						else:
							continue
					elif first_name_file.lower() == 'none' and temp_filename[1] != 'ymt':
						name = temp_filename[0]
						ext = temp_filename[1]

						if ext == 'ytd' and name.split("_")[0] == type_file:
							check_type = name.split("_")

							for get_num in list_file:
								if get_num[0] == check_type[2]:
									file_type = None
									if len(check_type) == 4:
										ft = get_num[1].split(".")[0].split("_")[2]
										if ft == 'u':
											file_type = 'uni'
										elif ft == 'r':
											file_type = 'whi'
									else:
										file_type = check_type[4]

									new_name = check_type[0] + "_diff_" + get_num[1].split("_")[1] + "_" + check_type[3] + "_" + file_type + ".ytd"
									print("Exporting " + filename + " > " + new_name + " ...")
									shutil.copy2(path + filename, export_path + new_name)
									print("Exported " + filename + " > " + new_name)
									clearConsole(True)
									ytdcount += 1
									break
						else:
							continue
				else:
					continue
		else:
			for filename in os.listdir(path):
				isFile = os.path.isfile(path + filename)
				if isFile == True:
					temp_filename = filename.split(".")

					if first_name_file.lower() != 'none' and temp_filename[0].split("^")[0] == first_name_file and temp_filename[1] != 'ymt':
						name = temp_filename[0].split("^")[1]
						ext = temp_filename[1]
						temp_split_underscore = name.split("_")
						check_first_type_name = temp_split_underscore[0] + "_" + temp_split_underscore[1]

						if ext == 'ydd' and check_first_type_name == type_file:
							new_name = None
							new_num = None
							check_type = name.split("_")

							if i < 10:
								new_num = "00" + str(i)
							elif i >= 10 and i <= 99:
								new_num = "0" + str(i)
							elif i >= 100:
								new_num = str(i)
							new_name = check_type[0] + "_" + check_type[1] + "_" + new_num + ".ydd"

							print("Exporting " + filename + " > " + new_name + " ...")
							shutil.copy2(path + filename, export_path + new_name)
							print("Exported " + filename + " > " + new_name)
							clearConsole(True)
							list_file.append([check_type[2], new_name])
							i += 1
							yddcount += 1
						else:
							continue
					elif first_name_file.lower() == 'none' and temp_filename[1] != 'ymt':
						name = temp_filename[0]
						ext = temp_filename[1]
						temp_split_underscore = name.split("_")
						check_first_type_name = temp_split_underscore[0] + "_" + temp_split_underscore[1]

						if ext == 'ydd' and name.split("_")[0] == type_file:
							new_name = None
							new_num = None
							check_type = name.split("_")

							if i < 10:
								new_num = "00" + str(i)
							elif i >= 10 and i <= 99:
								new_num = "0" + str(i)
							elif i >= 100:
								new_num = str(i)
							new_name = check_type[0] + "_" + check_type[1] + "_" + new_num + ".ydd"

							print("Exporting " + filename + " > " + new_name + " ...")
							shutil.copy2(path + filename, export_path + new_name)
							print("Exported " + filename + " > " + new_name)
							clearConsole(True)
							list_file.append([check_type[2], new_name])
							i += 1
							yddcount += 1
						else:
							continue
				else:
					continue

			for filename in os.listdir(path):
				isFile = os.path.isfile(path + filename)
				if isFile == True:
					temp_filename = filename.split(".")
					if temp_filename[0].split("^")[0] == first_name_file and temp_filename[1] != 'ymt':
						name = temp_filename[0].split("^")[1]
						ext = temp_filename[1]
						temp_split_underscore = name.split("_")
						check_first_type_name = temp_split_underscore[0] + "_" + temp_split_underscore[1]

						if ext == 'ytd' and check_first_type_name == type_file:
							check_type = name.split("_")
							for get_num in list_file:
								if get_num[0] == check_type[3]:
									new_name = check_first_type_name + "_diff_" + get_num[1].split("_")[2].split(".")[0] + "_" + check_type[4] + ".ytd"
									print("Exporting " + filename + " > " + new_name + " ...")
									shutil.copy2(path + filename, export_path + new_name)
									print("Exported " + filename + " > " + new_name)
									clearConsole(True)
									ytdcount += 1
									break
						else:
							continue
					elif first_name_file.lower() == 'none' and temp_filename[1] != 'ymt':
						name = temp_filename[0]
						ext = temp_filename[1]
						temp_split_underscore = name.split("_")
						check_first_type_name = temp_split_underscore[0] + "_" + temp_split_underscore[1]

						if ext == 'ytd' and check_first_type_name == type_file:
							check_type = name.split("_")

							for get_num in list_file:
								if get_num[0] == check_type[2]:
									new_name = check_first_type_name + "_diff_" + get_num[1].split("_")[2].split(".")[0] + "_" + check_type[4] + ".ytd"
									print("Exporting " + filename + " > " + new_name + " ...")
									shutil.copy2(path + filename, export_path + new_name)
									print("Exported " + filename + " > " + new_name)
									clearConsole(True)
									ytdcount += 1
									break
						else:
							continue
				else:
					continue
		
		clearConsole(True)
		print('Successfully ' + str(yddcount) + " YDD files and " + str(ytdcount) + " YTD files")

if __name__ == '__main__':
	main()