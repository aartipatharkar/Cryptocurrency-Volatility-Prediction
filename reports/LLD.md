# Low-Level Design (LLD)
## Cryptocurrency Volatility Prediction System

---

## 1. Function-Level Design

### 1.1 load_and_clean()

**Purpose:** Load and preprocess raw dataset.

**Steps:**

- Read CSV
- Convert date column
- Sort chronologically
- Forward-fill missing values

---

### 1.2 scale_features()

**Purpose:** Normalize numerical features.

**Method:** StandardScaler

**Features scaled:**

- open
- high
- low
- close
- volume
- market_cap

---

### 1.3 create_features()

**Purpose:** Generate volatility-related features.

---

## 2. Feature Formulas

### 2.1 Returns

\[
return_t = \frac{close_t - close_{t-1}}{close_{t-1}}
\]

---

### 2.2 Rolling Volatility (Target)

\[
volatility_t = std(return_{t-6:t})
\]

(window = 7 days)

---

### 2.3 Moving Averages

\[
MA7 = rolling\ mean(close, 7)
\]

\[
MA21 = rolling\ mean(close, 21)
\]

---

### 2.4 Liquidity Ratio

\[
Liquidity = \frac{Volume}{MarketCap}
\]

---

### 2.5 Bollinger Bands

\[
BB_{upper} = MA_{20} + 2\sigma
\]

\[
BB_{lower} = MA_{20} - 2\sigma
\]

---

### 2.6 ATR (Average True Range proxy)

\[
ATR = rolling\ mean(high - low, 14)
\]

---

## 3. Hyperparameters

### Random Forest

- n_estimators: [100, 200]
- max_depth: [5, 10, None]
- random_state: 42
- CV folds: 3

---

## 4. Model Choice Justification

Random Forest was selected because:

- Handles nonlinear relationships
- Robust to noise
- Works well with tabular financial data
- Low preprocessing requirements
- Good baseline performance

---

## 5. Evaluation Metrics

### RMSE

Measures magnitude of prediction error.

### MAE

Measures average absolute deviation.

### R² Score

Measures explained variance.

---

## 6. Time-Series Consideration

- Chronological split used
- No data leakage
- Future data never used in training

---

**End of LLD**