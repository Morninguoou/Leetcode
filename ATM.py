myInput = int(input())
t = 0
f_h = 0
h = 0
while myInput != 0:
    if myInput >= 1000:
        t = myInput // 1000
        myInput = myInput % 1000
    elif myInput >= 500:
        f_h = myInput // 500
        myInput = myInput % 500
    else: 
        h = myInput // 100
        myInput = myInput % 100
#Output of Input Example
print("1000 * ", t)
print("500 * ", f_h)
print("100 * ", h)

#Tips:  Run for check input format