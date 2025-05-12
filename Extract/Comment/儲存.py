import csv
import os

def 儲存評論(output_path, data):
    try:
        # 檢查檔案是否存在
        file_exists = os.path.exists(output_path)

        # 開啟檔案，使用 "a" 模式追加寫入
        with open(output_path, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["author", "rating", "text"])
            if not file_exists:  # 如果檔案不存在，寫入表頭
                writer.writeheader()
            writer.writerows(data)
        print(f"成功儲存 {len(data)} 筆評論到 {output_path}")
    except Exception as e:
        print(f"錯誤：{e}")
        import traceback
        traceback.print_exc()
