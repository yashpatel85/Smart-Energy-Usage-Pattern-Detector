⚡ Smart Energy Usage Pattern Detector
A Machine Learning-powered Streamlit web app to analyze energy consumption patterns and detect anomalies using the Isolation Forest algorithm. This tool helps identify irregularities in usage that may indicate device faults, inefficiencies, or unusual behavior in residential or industrial energy data.

🔧 Features
📤 Upload energy usage CSV data

🧠 Run anomaly detection using Isolation Forest

📊 Visual display of normal vs anomalous energy usage

📈 Automatically shows anomaly scores

✅ Clean, intuitive Streamlit interface

⚙️ Scalable and ready for future models (LSTM, time series, etc.)

💡 How It Works
Input: Upload a CSV file containing energy consumption data. Required column: usage (float/integer type).

Anomaly Detection:

The app uses an Isolation Forest algorithm to detect outliers in usage patterns.

The model outputs:

usage: Energy consumption value.

anomaly: -1 (anomaly) or 1 (normal).

anomaly_score: A score indicating how isolated the data point is.

Output:

A table of results.

Metrics on total records, normal usage points, and detected anomalies.

📈 Sample Visualization
The app highlights anomalies in red when plotted against time (if timestamp is available). If timestamp is split into features like hour, day, etc., visualization may be skipped or adapted.

🧪 Model Details
Algorithm: Isolation Forest (Unsupervised)

Library: scikit-learn

Preprocessing:

Features were scaled before training.

Date-time was broken into features: hour, day, weekday, month, year.

🖥️ How to Run
🔧 Setup Environment:

# 1. Clone the repository
git clone https://github.com/your-username/smart-energy-usage-pattern-detector.git
cd smart-energy-usage-pattern-detector

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch streamlit app
streamlit run app.py

🧠 Future Improvements (Optional)
Integrate LSTM-based time series model for temporal pattern prediction

Live streaming sensor input via MQTT or APIs

Dashboard with trend graphs and anomaly heatmaps

Cloud deployment via AWS EC2 & Streamlit Sharing

Extract the 'data_compressed.zip' to access the raw and the processed csv files.

👨‍💻 Author
Yash Patel
