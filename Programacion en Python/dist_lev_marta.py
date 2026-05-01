#:levenshtein
def dist_lev(s,t):
  d=dict()
  for i in range(len(s)+1):
     d[i]=dict()
     d[i][0]=i
  for i in range(len(t)+1):
     d[0][i] = i
  for i in range(1, len(s)+1):
     for j in range(1, len(t)+1):
        d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+(not s[i-1] == t[j-1]))
  return d[len(s)][len(t)]


print(dist_lev('abcde', 'acdfe')) #2
print(dist_lev('abcde', 'adfg')) #4
print(dist_lev('abcd', 'f')) #4
print(dist_lev('', 'abc')) #3