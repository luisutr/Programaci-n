lis = [(1,'a'), (3,'c'), (4,'e'), (-1,'z')]
print(max(lis))
#(4, 'e')
print(max(lis, key = lambda x: x[1]))
#(-1, 'z')

lis = ['1','100','111','2']
print(max(lis))  # works in Python 2
#'2'
print(max(lis, key=lambda x: int(x)))  # compare integer version of each item
#'111'

print(min("c", "b", "a", "Y", "Z"))
#'Y'
print(min("c", "b", "a", "Y", "Z", key=str.lower))
#'a'

print(min(("java", "python", "z++")))
#'java'
print(min(("java", "python", "z++"), key=len))
#'z++'
