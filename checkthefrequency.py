
test_dict = {

    "codingal" : 3,
    "is" : 2,
    "best" : 2,
    "for"  :2,
    "coding" :1,
}

print("the original dictinonary : " , test_dict)

k = int(input("Enter the frequency:"))
res = 0

for key in test_dict:
    if test_dict[key] == k:
        res = res + 1

print("frequency of k is :" , res)
