def ContinSubSeq(lst):
  size=len(lst)
  for start in range(size):
    for end in range(start+1,size+1):
      yield (start,end)

def getsubmat(mat,start_row,end_row,start_col,end_col):
  return [i[start_col:end_col] for i in mat[start_row:end_row] ]

def get_all_sub_mat(mat):
  rows = len(mat)
  cols = len(mat[0])
  for start_row,end_row in ContinSubSeq(list(range(rows))):
    for start_col,end_col in ContinSubSeq(list(range(cols))):
      yield getsubmat(mat,start_row,end_row,start_col,end_col)

for i in get_all_sub_mat([[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1]]):
  print (i)

