# 地點1 地點2 方位 里程 書籍 原文文句
classified_data = [[],[],[],[]]
country_set = [set(),set(),set(),set()]
# para=0 dis_dir, para=1 dis, para=2 dir, para=3 other
def addin(row,index) :
  classified_data[index].append(row)
  country_set[index].add(row[0])
  country_set[index].add(row[1])
def data_clean_and_classify(data) :
    # data.replace('\uf0be','筹')
    p1 = 0 ; p2 = 1 ; rp = 2 ; dp = 3
    # point 1 , point 2 , direction , distance parameter position
    for row in data :
      # let the same country or town to be same name ('溫宿國'->'溫宿')
      if row[p1][-1] == '國' or row[p1][-1] == '城' or row[p1][-1] == '王':
        row[p1] = row[p1][:-1]
      if row[p2][-1] == '國' or row[p2][-1] == '城' or row[p2][-1] == '王':
        row[p2] = row[p2][:-1]
    for row in data :
      # classify the data
      if row[dp] == '--' : # data without distance
        addin(row,2)
      else :
        tmp = row[dp][:-1] # eliminate '里'
        # *warning* isnumeric() fuction also avai when num = '3/4' or '二' or '\u..'
        if tmp.isnumeric() : # correct data
          row[dp] = tmp
          if row[rp] == '--' : # data without direction
            addin(row,1)
          else :
            addin(row,0)
        else : # other kinds of data (e.g. 二千餘里)
          addin(row,3)
    # print the number of nodes and edges
    '''
    for element in classified_data : # 147 77 69 29 edges
      print(len(element),end=' ')
    print()
    '''
    country_set.append(country_set[0].union(country_set[1]))
    '''
    for element in country_set : # 87 70 62 37 , 105 vertices
      print(len(element),end=' ')
    '''
    return classified_data , country_set[4]

def data_process(pre_data) :
  c_data , disset = data_clean_and_classify(pre_data)
  return c_data,disset
