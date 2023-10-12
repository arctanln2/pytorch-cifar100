import csv
import sys
import time
# #python2可以用file替代open
# with open("test.csv","w") as csvfile: 
#     writer = csv.writer(csvfile)

#     #先写入columns_name
#     writer.writerow(["index","a_name","b_name"])
#     #写入多行用writerows
#     writer.writerows([[0,1,3],[1,2,3],[2,3,4]])
#     while 1:
#         c = input()
#         if c=='c':
#             writer.writerow([0,1,4])
#         else:
#             break

sys.stdout = open('hello.txt', 'a')
# with open('out.txt', 'w+') as f:
    # sys.stdout = f 
for i in range(10):
    print(1,flush=True)
    time.sleep(1)