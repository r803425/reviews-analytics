data = []
count = 0 #計數次數
with open('reviews.txt', 'r') as f:
    #print(f)
    for line in f:
        data.append(line.strip())
        count += 1
        #print(len(data))  #每回loop結束前，印出清單長度
        if count % 100000 == 0: #當迴圈次數為100000的倍數時，才印出清單長度
            print(len(data))  #每回loop結束前，印出清單長度
print('檔案讀取完了，總共有', len(data), '筆資料') #印出清單長度

#計算全部留言平均長度
sum_len = 0
for d in data: #把data資料，一筆一筆字串拿出來，命名為d
    #print(len(d)) #印出每筆d字串的長度
    sum_len = sum_len + len(d) #累加長度，就是全部總長度
print('留言平均長度為，', sum_len/len(data))


#篩選留言長度
new = []
for d in data:
    if len(d) < 100: #當留言長度<100，新增加到new清單裡
        new.append(d)
print('一共有', len(new), '筆留言長度小於100') #如果寫在for loop裡面，每次loop就印一次
#print(new[0]) #印出第一筆留言長度<100
#print(new[1]) #印出第二筆留言長度<100


#篩選留言包含good
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言包含good')
#print(good[0]) #印出第一筆留言包含good
#print(good[1]) #印出第二筆留言包含good


# 單字記數 # print(data[0])
wc = {} # 先創造出一個空字典 word_count
for d in data:
    words = d.split() # split(' ')不寫空白鍵，預設值就是空白鍵，就不會切割成空字串
    for word in words:
        if word in wc:
            wc[word] += 1 # 目前次數累加1
        else:
            wc[word] = 1 # 未出現過的字，新增加次數1進字典
# wc[word]為出現次數的意思
for word in wc: # 將字典中的每個key一個一個拿出來
    if wc[word] > 1000000:
        print(word, wc[word])

# print(len(wc)) # 印出wc字典key的長度，就是總共有幾個不同的單字
# print(wc['Ryan'])

while True:
    word = input('請輸入你要查找次數的單字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為', wc[word])
    else:
        print('這個字沒有出現過哦!!!')

print('感謝使用查詢功能')
