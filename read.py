data = []
count = 0 #計數次數
with open('reviews.txt', 'r') as f:
    #print(f)
    for line in f:
        data.append(line.strip())
        count += 1
        #print(len(data))  #每回loop結束前，印出清單長度
        if count % 1000 == 0: #當迴圈次數為1000的倍數時，才印出清單長度
            print(len(data))  #每回loop結束前，印出清單長度

print(len(data)) #印出清單長度

print(data[0]) #印出清單的第0個位置，第一筆
print('-----------------------------------------------------------------------------------------------------------------')
print(data[1]) #印出清單的第1個位置，第二筆