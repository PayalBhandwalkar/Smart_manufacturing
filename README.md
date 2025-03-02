Smart Manufacturing Process Optimization with AWS IoT & Power BI 🚀

📌 Project Overview

This project implements a real-time IoT-enabled smart manufacturing system that detects equipment anomalies and predicts failures using AWS IoT Core, Amazon S3, Athena, and Power BI. The system collects sensor data, performs anomaly detection, and visualizes insights through an interactive Power BI dashboard.

⚙️ Tech Stack

IoT & Cloud: AWS IoT Core, Amazon S3, AWS Lambda, Amazon Athena
Data Processing: Python, MQTT, Paho-MQTT, Pandas
Machine Learning: Anomaly Detection, Predictive Analytics
Visualization: Power BI, Real-time Dashboards
📊 Features

✅ IoT Sensor Data Streaming: Publish & subscribe sensor data using AWS IoT Core
✅ Anomaly Detection: Identify potential equipment failures using real-time monitoring
✅ Predictive Maintenance: Forecast failures using ML models in Python
✅ Data Storage & Querying: Store and query sensor data in Amazon S3 & Athena
✅ Real-Time Power BI Dashboard: Interactive visualization for factory insights

🛠️ Setup & Deployment

1️⃣ Set up AWS IoT Core → Create Thing, Attach Policy, Subscribe to Topic
2️⃣ Run MQTT Publisher → Send real-time sensor data using Python
3️⃣ Store Data in Amazon S3 → Configure AWS IoT Rule to store data
4️⃣ Query with Amazon Athena → Process data for Power BI
5️⃣ Create Power BI Dashboard → Connect Athena via ODBC & build visualizations

📌 How It Works

Sensors stream real-time data to AWS IoT Core
Data is stored in Amazon S3 and queried with Athena
Anomaly detection algorithms analyze equipment health
Insights are visualized in Power BI dashboards
