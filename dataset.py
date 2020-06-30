import csv

#field names
field = ['Image', 'Label']

#data rows of csv file
rows = []
#def rows_item(n):

filename = 'data.csv'


# This Python code is for creating a csv file. In this CSV file one column is for the location of the image and other column is for
# the 'label'. To create the CSV file one need change as the inputs every time. This process is quite time taking that's why I have 
# 'os' library of python to get the location of the images instead of CSV file and pandas library.


a = ['Captura de Tela 2020-06-01 às 23.38.58.png',
'Captura de Tela 2020-06-01 às 23.39.05.png',
'Captura de Tela 2020-06-01 às 23.39.13.png',
'Captura de Tela 2020-06-01 às 23.39.19.png' ,
'Captura de Tela 2020-06-01 às 23.39.26.png' ,
'Captura de Tela 2020-06-01 às 23.39.38.png',
'Captura de Tela 2020-06-01 às 23.39.49.png',
'Captura de Tela 2020-06-01 às 23.39.58.png',
'Captura de Tela 2020-06-01 às 23.40.07.png',
'Captura de Tela 2020-06-01 às 23.40.15.png',
'Captura de Tela 2020-06-01 às 23.40.25.png',
'Captura de Tela 2020-06-01 às 23.40.38.png',
'Captura de Tela 2020-06-01 às 23.40.49.png',
'Captura de Tela 2020-06-01 às 23.40.58.png',
'Captura de Tela 2020-06-01 às 23.41.06.png',
'Captura de Tela 2020-06-01 às 23.41.17.png',
'Captura de Tela 2020-06-01 às 23.41.30.png'

]


for i in range(1,len(a)):
    f = 'Covid/Patient/' + a[i] 
    #f = 'Healthy/Patient/' + a[i] 
    #f = 'Others/Patient/' + a[i] 

    l = 'covid' 
   # l = 'healthy'
    #l = 'others'
    rows_element = [f, l]
    rows.append(rows_element)



#print(rows)
with open('data.csv', 'a', newline='') as csvfile:
        # creating a csv writer object
    csvwriter = csv.writer(csvfile,delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)

    # writing the fields
   # csvwriter.writerow(['Image', 'label'])

    #writing the data rows
    csvwriter.writerows(rows)
    

