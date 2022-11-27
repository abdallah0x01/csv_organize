import csv
import time
from datetime import date

start = time.perf_counter()
order_number_list = []
check_in_list = []
check_out_list = []

with open('Tent and Bed Orders.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        if  line:
            if line[0] != 'Order Number':
                order_number_list.append(line[0])  # order number
            if line[8] != 'Check In':
                check_in_list.append(line[8])  # check in
            if line[9] != 'Check Out':
                check_out_list.append(line[9])  # check out

with open('tents.csv', 'a') as tents_file:
    csv_writer = csv.writer(tents_file)
    csv_writer.writerow(['Order Number', 'Check In', 'Check Out', 'No.Reserved Days'])

    for order_number, ckeck_in, check_out in zip(order_number_list, check_in_list, check_out_list):
        splited_check_in_date = ckeck_in.split('/')
        check_in_date = date(int(splited_check_in_date[2]), int(splited_check_in_date[0]),int(splited_check_in_date[1]))
        splited_check_out_date = check_out.split('/')
        check_out_date = date(int(splited_check_out_date[2]), int(splited_check_out_date[0]), int(splited_check_out_date[1]))
        no_reseved_days = (check_out_date - check_in_date).days

        csv_writer.writerow([order_number, ckeck_in, check_out, no_reseved_days])

end = time.perf_counter()

print(f'Finished in {round(end- start, 3)} sec')
