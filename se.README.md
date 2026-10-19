
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



## Executive Summary: Global Economic & Environmental Analysis Report (2000–2023)

This report synthesizes the empirical findings, model estimations, and projections completed across five critical analytical research areas for the selected panel of major global economies (**USA, Canada, Australia, Russia, China, and India**).

---

## 1. Drivers of GDP & GDP per Capita (Objective 1)
To control for unobserved, country-specific historical, cultural, and institutional characteristics, we fitted an **Entity Fixed Effects Panel Regression** on GDP per capita.
* **Key Finding:** **Healthcare Expenditure per Capita** is the single most statistically significant and powerful driver of economic prosperity ($p = 0.0003$). Every additional dollar invested in healthcare per capita corresponds to a **$0.993** increase in GDP per capita. 
* **Other Drivers:** Lower baseline corruption (higher Corruption Perception Index scores, $+54.50$) and steady urbanization trends are positively associated with long-term wealth, while higher baseline inflation rates correlate negatively with sustained per-capita GDP growth ($r = -0.73$).

## 2. Economic Growth vs. Environmental Trade-offs (Objective 2)
We investigated whether economic development is tied to higher carbon emissions by regressing year-over-year (YoY) $CO_2$ emissions growth on YoY GDP growth.
* **Key Finding:** The emission elasticity of GDP growth is **$-0.0913$** and is statistically insignificant ($p = 0.4327$). 
* **Implication:** The lack of a strong, positive, statistically significant link between GDP growth and emission increases suggests that these nations are successfully undergoing **structural decoupling**, where economic expansion no longer guarantees a proportional rise in greenhouse gas emissions.

## 3. Human Capital & HDI Dynamics (Objective 3)
We modeled the short-to-medium-term relationship between health/education expenditures and the **Human Development Index (HDI)** using Panel OLS.
* **Key Finding:** Traditional annual fluctuations in education budgets (% of GDP) or healthcare spending do not show short-term statistically significant impacts on annual HDI score changes.
* **Implication:** HDI is a deeply structural, slow-moving metric. Human capital investments require a **lagged, decadal perspective** before translating into measurable improvements in national education indexes or overall human development scores.

## 4. Medium-Term Projections to 2030 (Objective 4)
Using a **Vector Autoregressive (VAR)** model taking historical trends (2000–2023) into account, we generated forecasts up to **2030**:
* **High-Wealth Nations:** The USA, Canada, and Australia are projected to maintain stable, incremental growth trajectories.
* **Emerging Markets:** China and India are expected to continue narrowing the absolute GDP gap, though their GDP per capita figures remain structurally distinct from the developed cohort.

## 5. Development Archetypes & Policy Implications (Objective 5)
Using unsupervised **K-Means clustering** ($K=3$) on multi-dimensional performance metrics, we identified three clear global development archetypes:
1. **Archetype 0 (High-Wealth, Fossil-leaning Urban Centers):** Highly urbanized (~84%), extremely clean institutions, very high wealth, but heavily reliant on fossil energy (renewables make up only ~19.9% of the mix).
2. **Archetype 1 (Developing / Transitional States):** Rapidly industrializing economies with high population growth, lower per-capita GDP, and lower urbanization (~56.1%).
3. **Archetype 2 (High-Wealth, Green Innovators):** High-wealth economies with very clean institutions and an exceptionally high share of renewable/clean energy (~67.3%), demonstrating that absolute wealth and transition grids can coexist.
