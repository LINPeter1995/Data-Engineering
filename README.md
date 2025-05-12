# Tibame-Project 

專案：士林夜市商家評論收集與分析

⸻⸻⸻⸻⸻⸻⸻

專案簡介

本專案聚焦於資料工程技能實作，透過 Python Selenium 爬取 Google Maps 上士林夜市商家的評論資訊，並整合多種資料平台與工具，建構完整的資料流管線（Data Pipeline），最終以商業智慧工具呈現分析結果。

⸻⸻⸻⸻⸻⸻⸻

技術架構與流程

1. 資料擷取層（Data Collection）
	•	使用 Python + Selenium 自動化爬取 Google Maps 上的商家評論
	•	每筆評論即時送入 Apache Kafka Producer
	•	Kafka 將評論資料送入指定的 Topic（例如 shilin-reviews）

2. 資料串流與暫存（Streaming & Buffer）
	•	Kafka 中的資料由多個 Consumer 接收與處理：
	•	Consumer A：儲存資料至 MongoDB（非結構化暫存）
	•	Consumer B：同步儲存至 MySQL（結構化資料查詢用）
	•	Consumer C：寫入 Hadoop HDFS / Hive 進行後續大數據處理
	•	Consumer D：送入 Google BigQuery 進行雲端查詢與分析

3. 資料轉換與排程（ETL Pipeline）
	•	使用 Apache Airflow 排程資料清理、轉換與搬移任務
	•	定時處理 Kafka 累積的評論資料，進行格式轉換與彙整

4. 資料視覺化（Visualization）
	•	使用 Power BI / Tableau 視覺化評論資料，包括：
	•	關鍵字統計
	•	星等分佈
	•	評論數熱區
	•	商家評論變化趨勢

⸻⸻⸻⸻⸻⸻⸻

預期成果
	•	建立結構化與非結構化的士林夜市商家評論資料集
	•	完成具有 Kafka 串流處理的自動化資料管線建置
	•	透過視覺化介面洞察顧客評論行為與商家表現

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

未來延伸方向
	•	建立 FastAPI 查詢接口，提供前端或使用者即時查詢評論資訊
	•	整合 NLP 模型分析評論：
	•	情緒分析（正面／中立／負面）
	•	主題分類（如：食物、服務、價格、環境等）
	•	模型結果可透過 Kafka 發佈，實現即時評論分類與預測
	•	串接告警或推播系統：如負面評論暴增時自動通知店家或平台
