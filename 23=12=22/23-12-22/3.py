sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# def slice_chunks(l, n):
#     for i in range(0, len(l),n):
#         yield l[i:i +n]
# n=3
# x= list(slice_chunks(sample_list,n))  
# print(x)      
l = len(sample_list)
chunk = int(l/3)
start = 0
end = chunk

for i in range(3):
    ind = slice(start, end)
    list_chunk = sample_list[ind]
    print("Chunk ", i, list_chunk)
    print("After reversing it ",list(reversed(list_chunk)))

    start=end
    end += chunk
