#syntax  [start : end (it is always -1)] or [start : end (it is always -1): skeep word]

Name = "Nilesh, Kiran"
# print(Name[11])
# print(Name[12])
print(len(Name)) # it use to print length of string Name
# for i, j in enumerate(Name):
#     print(f"Word={j}  at Index={i}") #To print particular word on index location  here i for index and j for word
'''
Word=N  at Index=0
Word=i  at Index=1
Word=l  at Index=2
Word=e  at Index=3
Word=s  at Index=4
Word=h  at Index=5
Word=,  at Index=6
Word=   at Index=7
Word=K  at Index=8
Word=i  at Index=9
Word=r  at Index=10
Word=a  at Index=11
Word=n  at Index=12
'''

# print(Name[0:3]) # Nil start with index [0] and at index [2]
# print(Name[:3]) # Nil start with index [0] and at index [2] by default start with index "0"
# print(Name[:]) # it is by default start with index [0] and end with index[12] i.e end of index
# print(Name[1:]) # it is by default start with index [1] and end with index[12] i.e end of index
# print(Name[-2:-1]) # a
# print(Name[-3:-1]) # ra
# # print(Name[1:10]) # ilesh, Ki -->start with index[1] and  end at index [9]
# print(Name[0:6:2]) # Nls --> it start with index [0] and end at index[5] also skeep 2 word
# print(Name[0::2]) # Nls,Krn--> it start with index [0] and end at index[12] also skeep 2 word

