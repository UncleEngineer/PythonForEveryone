import csv

def writecsv(data):
    # data = ['john',14,500]
    with open('knowledge.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # FW = File Writer
        fw.writerow(data)

    # ถ้า error 
    # filename = 'C:\\Users\\Uncle Engineer\\Desktop\\Python for Everyone\\knowledge.csv'
    # with open(filename,'a',newline='',encoding='utf-8') as file:

def readcsv():
    with open('knowledge.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
        print(data)

readcsv()

# d = ['lisa',16,500]
# writecsv(d)
