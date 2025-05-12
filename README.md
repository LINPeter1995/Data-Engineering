# Tibame-Project 

Tibame 專案：士林夜市商家評論收集與分析

專案簡介

本專案聚焦於資料工程技能實作，透過 Python Selenium 爬取 Google Maps 上士林夜市商家的評論資訊，並整合多種資料平台與工具，建構完整的資料流管線（Data Pipeline），最終以商業智慧工具呈現分析結果。

技術架構與流程

 1.	資料擷取層（Data Collection）

  使用 Python + Selenium 自動化爬取商家評論
	 評論內容儲存為 CSV 檔

 2.	資料儲存與轉換（ETL）

 將 CSV 匯入：
	MongoDB（做為暫存與結構化資料存取）
	MySQL（結構化儲存，利於關聯查詢）
	使用 Apache Airflow 調度 ETL 任務
	將資料同步至：
	Hadoop HDFS + Hive（處理大量資料）
	Google BigQuery（進行雲端資料分析）

 3.	資料視覺化（Visualization）

 使用 Power BI 或 Tableau 對評論進行關鍵字統計、星級分佈、評論數熱區等分析與圖表呈現

 預期成果

 建立士林夜市各商家評論的資料集
 完成自動化資料管線建置
 以可視化方式洞察顧客評論趨勢

 未來延伸方向
 建立 FastAPI 接口提供資料查詢服務
 加入 NLP 模型分析評論情緒與主題
