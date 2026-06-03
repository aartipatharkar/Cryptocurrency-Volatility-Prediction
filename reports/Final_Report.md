Exploratory Data Analysis (EDA) Report

Cryptocurrency Volatility Prediction
1. Introduction
Cryptocurrency markets are known for extreme volatility. Understanding historical behavior is critical before building a predictive model. This EDA aims to:
- Understand distribution of prices and volatility
- Identify correlations among variables
- Detect anomalies and outliers
- Study volatility clustering behavior
- Support feature engineering decisions


2. Dataset Description
The dataset contains daily historical data for multiple cryptocurrencies.

Features Included:
- Open Price
- High Price
- Low Price
- Close Price
- Trading Volume
- Market Capitalization
- Date
- Timestamp
- Cryptocurrency Name

Dataset Size:
- 70,452 records
- 20 engineered features after preprocessing
Each row represents one day of trading data.

3. Data Cleaning Process
Steps performed:
1. Converted all column names to lowercase.
2. Renamed `marketCap` to `market_cap`.
3. Converted date column to datetime format.
4. Forward-filled missing values.
5. Removed NaN values caused by rolling calculations.
6. Removed infinite values caused by division operations.
Final dataset contains no missing or infinite values.

4. Summary Statistics
Key findings:
- Prices vary significantly across cryptocurrencies.
- Volume shows heavy fluctuations.
- Market cap spans several orders of magnitude.
- Volatility distribution is right-skewed.
Mean and standard deviation indicate high dispersion in market activity.

5. Price Trend Analysis
Observed patterns:
- Long bullish and bearish cycles.
- Sharp spikes during rallies.
- Large drops during crashes.
- Trend persistence in price movements.
These confirm the non-linear nature of crypto markets.

6. Correlation Analysis
Key relationships:
- Strong correlation between Open, High, Low, and Close.
- Moderate correlation between Volume and Volatility.
- Larger market cap coins tend to show lower volatility.
- Liquidity ratio increases during high volatility periods.
Tree-based models are suitable due to correlated features.

7. Volatility Distribution
- Majority of days show moderate volatility.
- Extreme volatility events are rare but impactful.
- Volatility clustering observed (high volatility follows high volatility).
This supports using rolling-window features.

8. Key Insights from EDA
- Crypto markets exhibit non-stationary behavior.
- Volatility is clustered over time.
- Liquidity spikes often precede volatility increases.
- Rolling indicators smooth noisy price signals.

9. Conclusion
EDA confirms that:
- Volatility prediction is feasible.
- Feature engineering is necessary.
- Ensemble models are appropriate.
- Time-aware splitting is required.
EDA guided the design of the machine learning pipeline.

PIPELINE ARCHITECTURE
		
			
Raw Data
↓
Preprocessing
↓
Feature Engineering
↓
Model Training
↓
Evaluation
↓
Model Save (.pkl)
↓
Streamlit Deployment
 
# Final Project Report

 1. Problem Statement
Cryptocurrency markets are highly volatile. Predicting volatility enables better risk management and trading decisions.

 2. Solution Approach
- Data preprocessing
- Feature engineering
- Random Forest model
- Hyperparameter tuning
- Streamlit deployment

3. Model Performance
Metrics used:
- RMSE
- MAE
- R² Score
Model trained on 70,000+ records.

4. Business Value
Risk Management
Helps traders hedge against sudden price movements.

Portfolio Optimization
Improves asset allocation decisions.
Trading Strategy
Supports volatility-aware trading.
 Institutional Use
Useful for quantitative trading desks.

 5. Limitations
- Uses historical data only
- No sentiment analysis
- No macroeconomic indicators
 6. Future Improvements
- LSTM deep learning model
- Real-time data integration
- Sentiment-based features
- Walk-forward validation
