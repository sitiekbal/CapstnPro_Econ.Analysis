**Capstone Project: Global Economic Analysis **
* Prepared By: Siti Ekbal
* Dataset Used: Global Economic Data

<img width="1147" height="396" alt="image" src="https://github.com/user-attachments/assets/73848cf2-7747-4b59-820b-3ea20d1c14e2" />


# 🌍 Global Economic Data & Green Transition Analysis (2000–2023)

## 📌 Project Overview
This project investigates the macro-level relationships between **economic growth (GDP)**, **energy consumption**, **renewable energy adoption**, and **CO2 emissions** across 6 major global economies (**USA, Russia, Canada, China, India, Australia**) from **2000 to 2023**. 

The goal of this repository is to provide a clean exploratory data analysis (EDA) pipeline and blueprint for an interactive dashboard that visualizes how major powers are balancing economic expansion with environmental sustainability.

---

Raw CSV (source):
https://raw.githubusercontent.com/sitiekbal/CapstnPro_Econ.Analysis/refs/heads/main/Global%20Economic%20Data.csv

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
| Renewable Energy Share (%) | Float | Share of energy from renewables (percent) |


## 🎯 Problem Statement

* **What is the problem?** As major global economies grow, their adoption of clean energy is not keeping pace with their industrial energy demands.
* **Why is it a problem?** Economic growth remains heavily reliant on fossil fuels, keeping CO2 emissions persistently high across top powers.
* **What happens if we don't fix it?** Failing to decouple GDP from carbon emissions will worsen climate risks, increase regulatory costs, and undermine future economic resilience.
---

## ❓ Core Research Questions
1. **Decoupling Analysis:** Are major economies successfully decoupling economic growth (GDP) from total CO2 emissions over time?
2. **Energy Mix Evolution:** How has the share of renewable energy evolved relative to total energy consumption across developed vs. developing economies?
3. **Environmental Footprint:** What is the relationship between industrial activity and resource consumption across nations?

---

## 📊 Dashboard Architecture & Layout Plan

---

## 🐍 Python EDA & Visualization Script

Run (https://colab.research.google.com/drive/1EBd3SasNLBp9WaRmOErxjXsdkQPkPQlU#scrollTo=IGlvnoX-nfGh) script inside a **Google Colab** notebook to automatically load dataset, perform exploratory data analysis, and export the analysis charts.



## 🎯 Research Objectives

### Descriptive Objectives
1. **Macro-Trend Analysis:** Evaluate historical trends in GDP, energy consumption, and CO2 emissions across major global economies (2000–2023).
2. **Energy Mix Comparison:** Contrast renewable energy adoption rates and structural energy dependencies between developed and emerging economies.
3. **Resource Impact Mapping:** Examine how industrial activity and economic expansion correlate with land use and environmental footprints.

### Predictive Objectives
4. **EKC & Decoupling Modeling:** Apply polynomial regression to model the Environmental Kuznets Curve (EKC), predicting carbon intensity thresholds relative to GDP per capita growth.
5. **Clean Energy Forecasting:** Utilize historical trend analysis and linear regression modeling to forecast future renewable energy share trajectories up to 2030.
