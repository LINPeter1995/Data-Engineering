# Tibame-Project 

專案：士林夜市商家評論收集與分析

⸻⸻⸻⸻⸻⸻⸻

專案簡介

本專案聚焦於資料工程技能實作，透過 Python Selenium 爬取 Google Maps 上士林夜市商家的評論資訊，並整合 Kafka、Airflow、MongoDB、Hadoop、BigQuery 等資料平台與工具，建構完整的資料流管線（Data Pipeline），最終以商業智慧工具呈現分析結果，並支援後續 NLP 模型分析與 API 服務開發。

⸻⸻⸻⸻⸻⸻⸻

技術架構與資料流程

1. 資料擷取層（Data Collection）
	•	使用 Python + Selenium 自動化爬取 Google Maps 商家評論。
	•	每筆評論以 CSV 結構 即時送入 Apache Kafka Producer。
	•	Kafka 將資料發送至指定 Topic（如 shilin-reviews），實現評論資料串流處理。

⸻⸻⸻⸻⸻⸻⸻

2. 資料接收與儲存（Data Ingestion & Storage）
	•	Kafka Consumers 接收資料並處理：
	•	Consumer A：儲存至 MongoDB（彈性結構，利於全文搜尋）
	•	Consumer B：同步寫入 MySQL（做結構化查詢與商家分類）
	•	Consumer C：傳送至 Hadoop HDFS + Hive，支援大數據分析
	•	Consumer D：將資料轉存至 Google BigQuery 進行雲端分析

⸻⸻⸻⸻⸻⸻⸻

3. 資料處理與排程（ETL & Workflow Orchestration）
	•	使用 Apache Airflow 作為工作流程調度工具：
	•	排程資料清洗、結構轉換與同步任務
	•	控制 Kafka 資料轉存、統整與資料管線流動

⸻⸻⸻⸻⸻⸻⸻

4. 資料分析與視覺化（Analytics & Visualization）
	•	使用 Power BI / Tableau：
	•	關鍵字雲、評論星等分佈圖、熱門評論時段
	•	商家評論趨勢與分類統計
	•	地理視覺化（哪幾區評論最多）

⸻⸻⸻⸻⸻⸻⸻

預期成果
	•	建立結構化與非結構化的士林夜市商家評論資料集
	•	實作一條具備 Kafka 串流處理 + Airflow 自動排程 的資料管線
	•	透過互動式報表與圖表分析，洞察顧客評論行為與商家表現

⸻⸻⸻⸻⸻⸻⸻

未來延伸方向
	•	FastAPI 查詢接口：提供評論查詢、商家資料搜尋 API，支援前端串接或平台整合
	•	加入 NLP 模型：
	•	情緒分析（Sentiment Analysis）：標記正評、中評、負評
	•	主題模型（Topic Modeling）：分類評論重點（如：價格、服務、環境）
	•	NLP 結果可透過 Kafka 發布 / 儲存 / 回寫，並與報表整合
	•	串接警示系統：當負評激增，觸發告警或自動通知商家平台
