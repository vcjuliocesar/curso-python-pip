import csv

def read_csv(path):
  with open(path,'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header,row)
      country_dict = {key:value for key,value in iterable}
      data.append(country_dict)
    return data

def transform_dict(dict):
  for key,value in dict:
    print(key)

if __name__ == '__main__':
 data = read_csv('./app/data.csv')
 transform_dict(data[1])
 #print(data[0])