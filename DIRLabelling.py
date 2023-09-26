import csv

file_name = "labelsCalculated.csv"

# change number when diff set
image_labels = [0.0] * 3539
screenshot_labels = [0.0] * 3539
i = 0

# change to training_data.csv
with open('/home/ama9tk/Desktop/Regression/Data/labels.csv', 'r') as csv_file:
        
        csv_reader = csv.reader(csv_file)
        previous = 0

        for row in csv_reader:  
            # print(row)
            csv_arr = row[0].split(" : ")
            
            if int(csv_arr[1]) >= 5:
                if int(csv_arr[1]) == 5:
                    image_labels[i] = csv_arr[2] + "_" + csv_arr[1]
                    screenshot_labels[i] = [0]
                    previous = float(csv_arr[4]) 
                else:
                    image_labels[i] = csv_arr[2] + "_" + csv_arr[1]
                    screenshot_labels[i] = [float(csv_arr[4]) - float(previous)]
                    previous = csv_arr[4]
            
            i += 1

for i in range(len(screenshot_labels)):
    print(image_labels[i])
    print(screenshot_labels[i])

with open("all_screenshot_labels.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    i = 0
    for row in screenshot_labels:
        writer.writerow([row, str(image_labels[i])])
        i += 1

    


