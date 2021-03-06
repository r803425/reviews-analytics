data = []
count = 0 #計數次數
with open('reviews.txt', 'r') as f:
    #print(f)
    for line in f:
        data.append(line.strip())
        count += 1
        #print(len(data))  #每回loop結束前，印出清單長度
        if count % 100000 == 0: #當迴圈次數為1000的倍數時，才印出清單長度
            print(len(data))  #每回loop結束前，印出清單長度
print('檔案讀取完了，總共有', len(data), '筆資料') #印出清單長度
#print(data)


#計算全部留言平均長度
sum_len = 0
for d in data: #把data資料，一筆一筆字串拿出來，命名為D
    #print(len(d)) #印出每筆d字串的長度
    sum_len = sum_len + len(d) #累加長度，就是全部總長度
print('留言平均長度為，', sum_len/len(data))


#篩選留言長度
new = []
for d in data:
    if len(d) < 100: #當留言長度<100，新增加到new清單裡
        new.append(d)
print('一共有', len(new), '筆留言長度小於100') #如果寫再for loop裡面，每次loop就印一次
print(new[0]) #印出第一筆留言長度<100
print(new[1]) #印出第二筆留言長度<100


good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言包含good')
print(new[0]) #印出第一筆留言包含good
print(new[1]) #印出第二筆留言包含good
