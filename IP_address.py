import csv

def region(csv_file_path, ip):

	csvFile = open(path, "r")
	reader = csv.reader(csvFile)


	ip_list = ip.split(sep=".")
	for i in range(len(ip_list)):
		ip_list[i] = int(ip_list[i])
		if ip_list[i] < 0 or ip_list[i] >255:
			return('INPUT IP ADDRESS INVALID')


	next(reader)

	for item in reader:
		data = item[0].split(sep=",")

		start = data[1].split(sep=".")
		end = data[2].split(sep=".")

		i = 0
		flag = True

		while flag and i < 4:
			if ip_list[i] < int(start[i]):
				flag = False
			elif ip_list[i] > int(start[i]):
				break
			else:
				i += 1

		i = 0

		while flag and i < 4:
			if ip_list[i] > int(end[i]):
				flag = False
			elif ip_list[i] < int(end[i]):
				break
			else:
				i += 1

		if flag:
			return data[0]

	return('NO FOUND')


				
path = 'test_ip_address.csv'
ip = '192.168.0.1'

print(region(path, ip))

