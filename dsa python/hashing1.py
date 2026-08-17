#brute force
n=[1,3,2,4,4,2,3,1,3,3,4,5,6,7,7,8,9]
m=[1,2,3,4,5,6,7,8,9]

for i in m:
    count=0
    for x in n:
        if i==x:
            count+=1
    print(count)
#time complexity is O(n^2) (not optimal)
#will give TLE error for large inputs (if >10^8)
#method 2: using dictionary (optimal if number of inputs is low) 
#frequency distribution in dictionary
n=[1,3,2,4,4,2,3,1,3,3,4,5,6,7,7,8,9]
m=[1,2,3,4,5,6,7,8,9]
freq_dict={}
for i in range(0,len(n)):
    if n[i] in freq_dict:
        freq_dict[n[i]]+=1
    else:
        freq_dict[n[i]]=1
print("Dictionary:",freq_dict)
for j in range(0,len(m)):
    if m[j] in freq_dict:
        if m[j]<0 or m[j]>10:
            print("out of bounds")
        else:    
            print(freq_dict[m[j]])
#method 3: using hashing (optimal)    
      #hashing
hash_list=[0]*11
for num in n:
    hash_list[num]+=1 #prestoring the frequency of each number in the hash_list
    
for num in m:
    if num<0 or num>10:
        print(0)
    else:print(hash_list[num])
'''