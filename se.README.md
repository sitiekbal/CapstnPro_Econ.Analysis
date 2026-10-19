
**Capstone Project: Economic Analysis Global**
* Prepared By: Siti Ekbal
* Dataset Used: Global Economic Data
# Economic Data

Annual panel data (2000–2023) for six countries—USA, Russia, Canada, China, India, and Australia—documenting a broad set of indicators: national output (GDP and GDP per head), population dynamics, health and schooling metrics, energy and environmental variables, transport/infrastructure counts, and governance/social indices.

Raw CSV (source):
https://raw.githubusercontent.com/sitiekbal/CapstnPro_Econ.Analysis/refs/heads/main/Global%20Economic%20Data.csv

This dataset is well suited for cross-country panel analysis, exploratory data analysis (EDA), growth and sustainability modeling, and short-to-medium term forecasting and scenario analysis.

## Research objectives

1. Identify the main drivers of GDP and GDP per capita across countries and over time.
2. Quantify trade-offs between economic growth and environmental outcomes (CO2 emissions, renewable share).
3. Evaluate how human capital investments (education and healthcare) relate to growth and HDI.
4. Build and validate short-to-medium-term forecasts for GDP / GDP per capita to 2030 and run policy scenarios.
5. Cluster countries into development archetypes and compare policy implications.

 Link to Jupyter Notebook in Google Colab:
 (https://colab.research.google.com/drive/1EBd3SasNLBp9WaRmOErxjXsdkQPkPQlU#scrollTo=IGlvnoX-nfGh)
 
## Dataset overview

* **File name:** `Global Economic Data.csv`
* **Time horizon:** 2000 – 2023 (annual)
* **Countries:** USA, Russia, Canada, China, India, Australia
* **Themes:** Macroeconomics, demography, human capital, health, education, energy & emissions, infrastructure, governance, tourism, social outcomes

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

> **Notes:**
> * Percent-like columns are commonly in 0–100 format in the CSV; HDI/Gender index may be 0–1 or 0–100 — validate and rescale as needed.
> * GDP is in trillions and population in millions. Quick check: `computed_GDP_per_capita ≈ (GDP_in_Trillions_USD * 1_000_000) / Population_in_Millions`.

## Data quality & cleaning notes

* **Missingness:** run a full missingness audit — the pasted CSV shows few blank cells but validate programmatically.
* **Units:** confirm whether HDI and Gender Equality Index are 0–1 or 0–100 and rescale consistently.
* **Implausible values:** literacy slightly >100 in some rows; cap at 100 or verify source. Validate doctor-to-patient units and large counts (airports, road km).
* **Skew & outliers:** CO2 emissions & energy use are skewed — consider log transforms or per-capita normalization for modeling.
* **Structural events:** 2008 and 2020 affect many series — include event dummies or conduct breakpoint tests for forecasting.
* **Derived checks:** recompute GDP per capita from GDP and population to detect inconsistencies.
