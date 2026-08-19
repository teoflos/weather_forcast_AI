# Weather Forecasting Predictive AI System

Welcome to the **Weather Forecasting Predictive AI System** workspace. This repository contains a modular Python application built to train, evaluate, and forecast time-series climate variables (Maximum Temperature, Minimum Temperature, Precipitation, Relative Humidity, and Sunshine Duration) using statistical **SARIMAX** architecture.

---

## 📁 Repository Structure

```text
├── .vscode/                     # Editor-specific workspace settings
├── backend/                     # Backend application root
│   ├── data/                    # App-level backend data directory
│   └── app.py                   # Flask API entry point for serving metrics and charts
├── data/                        # Project data directory
│   ├── monthly_timeseries.csv   # Aggregated historical climate features
│   └── raw_data.csv             # Raw historical climate input observations
├── Documentation/               # Comprehensive project documentation
│   ├── Weather_forcast_predictive_AI_model_document.pdf
│   └── Weather_forcast_predictive_AI_model_document.docx
├── frontend/                    # Interactive dashboard frontend source code
├── outputs/                     # Persistent model artifact generation output folder
│   ├── forecast_24months.csv     # 24-month horizon target predictions
│   ├── forecast_charts.png       # Generated data visualizations with 80% CI
│   └── model_accuracy_summary.csv# Evaluation metrics summary (MAE, MSE)
├── 01_prepare_data.py           # Data ingestion and historical cleansing pipeline
├── 02_train_forecast.py          # SARIMAX model optimization, training, and testing pipeline
├── LEUL D.xls                   # Legacy data source spreadsheet
├── Readme.md                    # Core project introduction and instructions
└── requirements.txt             # Consolidated project library dependencies
```

---

## 🛠️ Modules Breakdown

### 1. Data Ingestion & Preprocessing
* **`01_prepare_data.py`**: Reads raw data assets (`data/raw_data.csv` or `LEUL D.xls`), performs transformations, handles missing records, and aggregates timelines into the structured `data/monthly_timeseries.csv` file.

### 2. Machine Learning Core
* **`02_train_forecast.py`**: Consumes preprocessed monthly histories, tunes optimal hyper-parameters for Seasonal Autoregressive Integrated Moving Average with Exogenous Regressors (SARIMAX), exports 2-year forecast sequences to `outputs/forecast_24months.csv`, and validates operational models against mean metrics.
* **Outputs Generated**:
  * `forecast_charts.png`: Visual tracking histories alongside 80% confidence interval bands.
  * `model_accuracy_summary.csv`: Explicit tracking of performance margins via **MAE** and **MSE**.

### 3. Application Programming Interface (Backend)
* **`backend/app.py`**: A **Flask** engine setup configured with custom **CORS** routes to transmit calculated evaluation summaries, predictions, and asset plots directly onto frontend interfaces.

### 4. Interactive Dashboard (Frontend)
* **`frontend/`**: The presentation layout environment configured to render statistical time-series forecasts interactively for targeted public consumption.

---

## 🚀 Getting Started

### Prerequisites
Ensure your local environment runs Python 3.8+.

### Installation
1. Clone your workspace repository directory.
2. Initialize a secure virtual python workspace environment.
3. Install package distributions straight from your generated lock configurations file:
   ```bash
   pip install -r requirements.txt
   ```

### Operational Workflow Executions
1. Run data sanitization pipelines:
   ```bash
   python 01_prepare_data.py
   ```
2. Trigger analytics modeling and graph builds:
   ```bash
   python 02_train_forecast.py
   ```
3. Boot up the API service engine:
   ```bash
   python backend/app.py
   ```

---

## 📄 References & Governance
* **Documentation**: Find structured implementation details under the `Documentation/` node.
* **Section References**: Corresponds tightly with dashboard integrations outlined across structural LaTeX document templates (`Section \ref{sec:frontend}`).
