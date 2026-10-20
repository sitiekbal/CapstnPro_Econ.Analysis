**Capstone Project: Economic Analysis Global**
* Prepared By: Siti Ekbal
* Dataset Used: Global Economic Data

<img width="1147" height="396" alt="image" src="https://github.com/user-attachments/assets/73848cf2-7747-4b59-820b-3ea20d1c14e2" />


# Economic Data

Annual panel data (2000–2023) for six countries—USA, Russia, Canada, China, India, and Australia—documenting a broad set of indicators: national output (GDP and GDP per head), population dynamics, health and schooling metrics, energy and environmental variables, transport/infrastructure counts, and governance/social indices.

Raw CSV (source):
https://raw.githubusercontent.com/sitiekbal/CapstnPro_Econ.Analysis/refs/heads/main/Global%20Economic%20Data.csv

This dataset is well suited for cross-country panel analysis, exploratory data analysis (EDA), growth and sustainability modeling, and short-to-medium term forecasting and scenario analysis. Report outlines a structured approach to analyzing global macro-economic indicators (GDP, Inflation, and Unemployment) spanning from **2000 to 2023**. The analysis reveals critical long-term growth shifts, structural shocks from major global events (such as the 2008 Financial Crisis and the 2020 COVID-19 Pandemic), and cyclical macroeconomic variations.


---

# Research Objectives

Based on the variables present in the dataset, the following five core research objectives have been established to guide the exploratory and advanced analysis of global economic trends from 2000 to 2023.

---

### 📊 Descriptive Objectives (Exploration & Trend Assessment)

*   **Objective 1 (GDP & Shock Velocity):** To chart and profile the long-term trends and structural variance in **GDP (in Trillions USD)** across all monitored countries between **2000 and 2023**, explicitly diagnosing how quickly each economy recovered from external shocks like the **2008 Financial Crisis** and the **2020 Pandemic**.
*   **Objective 2 (Labor & Price Stability Dynamics):** To evaluate and contrast the distribution, spread, and volatility profiles of the **Unemployment Rate (%)** and **Inflation Rate (%)** across different nations to test the real-world application of traditional economic trade-off models (such as the Phillips Curve).
*   **Objective 3 (Sustainability & Human Progress Links):** To cross-examine the statistical correlation structures between industrial progress metrics—specifically **CO2 Emissions** and **Energy Consumption**—against societal benchmarks like the **Human Development Index (HDI)** and the **Renewable Energy Share (%)**.

---

### 🔮 Predictive Objectives (Modeling & Forecasting)

*   **Objective 4 (Quality of Life Forecasting):** To construct a multivariate regression framework to model and estimate future movements in the **Human Development Index (HDI)**, testing the relative impact strength of infrastructure spending (like **Healthcare** and **Education Expenditures**) versus technological shifts like **Internet Penetration (%)**.
*   **Objective 5 (Environmental Impact Projections):** To build a predictive time-series simulation evaluating how upcoming changes in economic output (**GDP**) and clean energy transitions (**Renewable Energy Share (%)**) will dynamically influence long-term national **CO2 Emissions** profiles.


Link to Jupyter Notebook in Google Colab:
(https://colab.research.google.com/drive/1EBd3SasNLBp9WaRmOErxjXsdkQPkPQlU#scrollTo=IGlvnoX-nfGh)


## Dataset Overview & Data Cleaning
Before running statistical evaluations, a comprehensive sanity check was conducted on `Global Economic Data.csv`:
* **Shape:** Balanced panel data covering multiple countries across 24 consecutive years.
* **Missing Value Treatment:** Imputation/removal steps implemented for missing values to maintain data continuity.
* **Outlier Verification:** Hyperinflation instances and abnormal spikes in unemployment were validated against historic historical economic narratives rather than treated purely as mechanical noise.
* **Missingness:** run a full missingness audit — the pasted CSV shows few blank cells but validate programmatically.
* **Units:** confirm whether HDI and Gender Equality Index are 0–1 or 0–100 and rescale consistently.
* **GDP:** is in trillions and population in millions. Quick check: `computed_GDP_per_capita ≈ (GDP_in_Trillions_USD * 1_000_000) / Population_in_Millions`.
* **Implausible values:** literacy slightly >100 in some rows; cap at 100 or verify source.
* **Skew & outliers:** CO2 emissions & energy use are skewed — consider log transforms or per-capita normalization for modeling.
* **Derived checks:** recompute GDP per capita from GDP and population to detect inconsistencies.
* **Implication:** The lack of a strong, positive, statistically significant link between GDP growth and emission increases suggests that these nations are successfully undergoing **structural decoupling**, where economic expansion no longer guarantees a proportional rise in greenhouse gas emissions.



## Data dictionary

| Column | Type | Description |
| :--- | :--- | :--- |
| Country | String | Country name (USA, Russia, Canada, China, India, Australia) |
| Year | Integer | Year (2000–2023) |
| GDP (in Trillions USD) | Float | Nominal GDP in trillions of USD |
| GDP per Capita (in USD) | Float | GDP per person in USD |
| Population (in Millions) | Float | Total population (millions) |
| CO2 Emissions (Million Metric Tons) | Float | Annual CO2 emissions (million metric tons) |
| Human Development Index (HDI) | Float | HDI index (0–1 or 0–100 — validate units) |
| Renewable Energy Share (%) | Float | Share of energy from renewables (percent) |
| Internet Penetration (%) | Float | Share of population using the internet (percent) |
| Healthcare Expenditure per Capita (USD) | Float | Annual healthcare spending per person (USD) |


---

## Core Insights & Trends Explored

### 📊 Metric A: Long-Term Growth Shifts (GDP Trends)
* **Emerging vs Developed Liftoff:** Dynamic divergence between established markets (e.g., US, Germany) maintaining steady, linear growth versus developing powerhouses (e.g., China, India) experiencing exponential upward curves.
* **Macro Shocks:** Visually evident disruptions during the **2008 Global Financial Crisis** and the **2020 COVID-19 pandemic**, where sudden drop-offs hit aggregate production across almost all monitored territories.

### 📈 Metric B: Inflationary Environments (Price Stability)
* **Volatility Distributions:** Distinct distributions between highly stable inflation blocks (e.g., Eurozone, Japan) vs volatile price fluctuations in emerging South American or African economies.
* **Post-Pandemic Surge:** Visible uptick across multiple clusters during the 2021–2023 cycle reflecting global supply-side crunches and quantitative easing pullbacks.

### 💼 Metric C: Labor Markets & Structural Unemployment
* **Economic Buffers:** Evaluation of how resilient domestic labor markets were when confronted by systemic global growth contractions. 
