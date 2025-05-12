from 讀取商家 import 讀取商家清單
from 抓評論 import 建立瀏覽器, 抓取評論
from 儲存 import 儲存評論
import os

# 修正路徑
csv_path = "Load/StoreList/去掉重複後的資料.csv"
儲存路徑 = "Load/Comment/全部評論.csv"

# 檢查檔案是否存在
if not os.path.exists(csv_path):
    print(f"找不到檔案：{csv_path}")
    exit()

if not os.path.exists(os.path.dirname(儲存路徑)):
    print(f"儲存路徑無效：{儲存路徑}")
    exit()

商家清單 = 讀取商家清單(csv_path)
driver = 建立瀏覽器()

for name, url in 商家清單[:5]:  # 先抓前 5 筆測試
    print(f"正在抓取：{name}")
    try:
        評論資料 = 抓取評論(driver, url)
        print(f"抓取到的評論資料：{評論資料}")
        print(f"共 {len(評論資料)} 筆")
        if not 評論資料:
            print(f"沒有抓取到任何評論：{url}")
            continue
        儲存評論(儲存路徑, 評論資料)
    except Exception as e:
        print(f"錯誤：{e}")
        import traceback
        traceback.print_exc()

driver.quit()
