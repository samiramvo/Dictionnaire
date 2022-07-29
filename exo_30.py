article={
    'item1':45.50,
    'item2':35,
    'item3':41.30,
    'item4':55,
    'item5':24
}
from heapq import nlargest
from operator import itemgetter
for name,value in nlargest(3,article.items(),key=itemgetter(1)):
    print(name,value)