def read_csvfile( datanum ): # datanum is the collection of dataname
    import csv
    data = [] # pouring all data into "data" without distinct book_class
    for i in range( len(datanum) ):
        with open( datanum[i] , newline='', encoding='utf-8' ) as csvfile :
            data_tmp = []
            rows = csv.reader(csvfile)
            for row in rows :
                data_tmp.append(row)
            data_tmp.pop(0) # remove column name
            data = data + data_tmp
    return data
