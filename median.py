import csv

with open('F:\python\class\C 104\SOCR-HeightWeight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

new_data=[]

for i in range(len(file_data)):
    n_num=file_data[i][2]
    new_data.append(float(n_num))

n=len(new_data)
new_data.sort()

if n %2 ==0:
    #getting the first middle number
    print(n)
    median1=float(new_data[n//2])

    #getting the second middle number

    median2=float(new_data[n//2-1])

    #getting mean of these numbers

    median=(median1+median2)/2

else:
    median=new_data(n//2)
    print(n)

print('median = '+str(median))