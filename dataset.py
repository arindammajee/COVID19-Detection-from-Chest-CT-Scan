import csv
import os

#field names
field = ['Image', 'Label']

#data rows of csv file
rows = []
#def rows_item(n):

filename = 'data.csv'


# This Python code is for creating a csv file. In this CSV file one column is for the location of the image and other column is for
# the 'label'. 

# create two blank array. One for image_names and other for image_labels.
image_name = []
image_label = []

for folder in os.listdir('Dataset/covid_ctscan/New_Data_CoV2'):
    data_folder = 'Dataset/covid_ctscan/New_Data_CoV2/' + folder
    for subfolder in os.listdir(data_folder):
        sub_folder = data_folder + '/' + subfolder
        for files in os.listdir(sub_folder):
            filename, fileextension = os.path.splitext(files)
            if(fileextension == '.png'):
                file_path = sub_folder + '/' + files
                image_name.append(file_path)
                image_label.append(folder)



for i in range(len(image_name)):
    
    rows_element = [image_name[i], image_label[i]]
    rows.append(rows_element)


#print(rows)
with open('data.csv', 'w', newline='') as csvfile:
        # creating a csv writer object
    csvwriter = csv.writer(csvfile,delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)

    # writing the fields
    csvwriter.writerow(['Image', 'label'])

    #writing the data rows
    csvwriter.writerows(rows)
    

