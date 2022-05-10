import cv2
import os
# 獲取一個影片開啟cap 引數1 file name
#cap = cv2.VideoCapture("1.mp4")
#cv2.VideoCapture(0, cv2.CAP_DSHOW) # 攝像頭擷取
cap = cv2.VideoCapture('D:/b/aigo5.avi')
isOpened = cap.isOpened # 判斷是否開啟‘
print('isOpened')
# 獲取資訊 寬高
n_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('總幀數：',n_frame) # 整個影片的總幀數
fps = cap.get(cv2.CAP_PROP_FPS) # 幀率 每秒展示多少張圖片
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # w
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # h
print('幀數、寬度、高度分別為：',fps,width,height) # 幀率 寬 高
i = 0 # 記錄讀取多少幀
frameFrequency = 20 # 每frameFrequency儲存一張圖片
while(isOpened):
    # 結束標誌是否讀取到最後一幀
    if i == n_frame:
        break
    else:
        i = i+1
    (flag,frame) = cap.read() # read方法 讀取每一張 flag是否讀取成功 frame 讀取內容
    fileName = 'image'+str(i)+'.jpg' # 名字累加
    # True表示讀取成功 進行·寫入
    # if 判斷需要有冒號
    #if flag == True:
    outPutDirName = './d/' # 設定儲存路徑
    if not os.path.exists(outPutDirName):
        # 如果檔案目錄不存在則建立目錄
        os.makedirs(outPutDirName)
    if i % frameFrequency == 0:
        print(fileName)
        cv2.imwrite(outPutDirName+fileName,frame,[cv2.IMWRITE_JPEG_QUALITY,100])# 質量控制 100最高
print('end!')