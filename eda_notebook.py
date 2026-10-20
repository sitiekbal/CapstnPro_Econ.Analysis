# Jupyter-friendly EDA script for "Global Economic Data.csv"
# Save as eda_notebook.py and open with Jupyter (or run in VSCode/Colab)
#
# Cells are marked with '# %%' so the file can be executed as a notebook.
#
# Outputs (saved to outputs/):
# - missing_summary.csv, missingness_heatmap.png
# - summary_stats_by_country.csv, summary_stats_global.csv
# - corr_matrix_global.csv, corr_matrix_global.png
# - trend_<var>.png, facet_GDP_per_Capita.png
# - outliers_impossible.csv, outliers_zscore.csv
# - pca_biplot.png, clusters.csv, cluster_summary.csv
#
# Requirements: pandas, numpy, matplotlib, seaborn, scikit-learn, scipy
# Install in notebook: pip install pandas numpy matplotlib seaborn scikit-learn scipy

# %% [markdown]
# ## Setup & imports

# %%
import os
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy import stats
from IPython.display import display

sns.set(style="whitegrid", context="notebook")
OUTDIR = Path("outputs")
OUTDIR.mkdir(exist_ok=True)

# %% [markdown]
# ## Utility functions

# %%
def tidy_columns(df):
    df = df.copy()
    cols = {}
    for c in df.columns:
        nc = c.strip()
        nc = nc.replace("\n", " ").replace("\r", " ")
        nc = nc.replace("%", "percent").replace("/", "_").replace("(", "").replace(")", "")
        nc = nc.replace(" ", "_")
        nc = nc.replace("__", "_")
        cols[c] = nc
    return df.rename(columns=cols)

def safe_numeric_coerce(df, exclude_cols=('Country','Year')):
    df2 = df.copy()
    for col in df2.columns:
        if col in exclude_cols:
            continue
        if df2[col].dtype == object:
            df2[col] = df2[col].str.replace(",", "").str.strip()
        df2[col] = pd.to_numeric(df2[col], errors='coerce')
    return df2

def summarize_missing(df):
    counts = df.isna().sum()
    pct = (counts / len(df) * 100).round(2)
    summary = pd.concat([counts, pct], axis=1)
    summary.columns = ['missing_count', 'missing_pct']
    return summary

# %% [markdown]
# ## Load and prepare data
# Place "Global Economic Data.csv" in the same folder as this script.

# %%
INPUT_CSV = "Global Economic Data.csv"
if not Path(INPUT_CSV).exists():
    raise FileNotFoundError(f"{INPUT_CSV} not found. Put the file in the notebook folder.")

raw = pd.read_csv(INPUT_CSV, dtype=str)
raw = tidy_columns(raw)
# Ensure Country and Year columns exist and types
if 'Country' not in raw.columns and 'country' in raw.columns:
    raw.rename(columns={'country':'Country'}, inplace=True)
if 'Year' in raw.columns:
    raw['Year'] = pd.to_numeric(raw['Year'], errors='coerce').astype('Int64')

# quick preview
print("Preview of loaded data:")
display(raw.head(3))

# Convert numeric columns where possible
df = safe_numeric_coerce(raw, exclude_cols=('Country','Year'))
print("\nAfter coercion: dtypes (sample):")
display(df.dtypes.head(10))

# %% [markdown]
# ## 1) Missingness summary (table + heatmap)

# %%
missing_before = summarize_missing(df)
missing_before.to_csv(OUTDIR / "missing_summary.csv")
print("Missingness summary (top rows):")
display(missing_before[missing_before['missing_count']>0].sort_values('missing_count', ascending=False).head(30))

plt.figure(figsize=(14,6))
sns.heatmap(df.isna().T, cbar=False, cmap="Greys", yticklabels=True)
plt.title("Missingness heatmap (columns x rows)")
plt.xlabel("Row index")
plt.ylabel("Columns")
plt.tight_layout()
plt.savefig(OUTDIR / "missingness_heatmap.png", dpi=150)
plt.show()

# %% [markdown]
# ## 2) Descriptive statistics by country & global

# %%
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
summary_by_country = df.groupby('Country')[numeric_cols].agg(['count','mean','median','std','min','max']).round(3)
# flatten multiindex columns
summary_by_country.columns = ["_".join(col).strip() for col in summary_by_country.columns.values]
summary_by_country.to_csv(OUTDIR / "summary_stats_by_country.csv")
print("Summary (by country) saved to outputs/summary_stats_by_country.csv")
display(summary_by_country.head())

summary_global = df[numeric_cols].agg(['count','mean','median','std','min','max']).round(3).T
summary_global.to_csv(OUTDIR / "summary_stats_global.csv")
print("Global numeric summary saved to outputs/summary_stats_global.csv")
display(summary_global.head())

# %% [markdown]
# ## 3) Correlation matrix (pooled) + heatmap

# %%
corr = df[numeric_cols].corr(method='pearson')
corr.to_csv(OUTDIR / "corr_matrix_global.csv")

plt.figure(figsize=(14,12))
sns.heatmap(corr, cmap="vlag", center=0)
plt.title("Pearson correlation matrix (pooled)")
plt.tight_layout()
plt.savefig(OUTDIR / "corr_matrix_global.png", dpi=150)
plt.show()

# %% [markdown]
# ## 4) Time-series plots (selected vars) and faceted GDP per capita

# %%
# Choose variables if present (using tidied names)
vars_to_plot = [
    'GDP_in_Trillions_USD','GDP_per_Capita_in_USD',
    'CO2_Emissions_Million_Metric_Tons','Renewable_Energy_Share_percent',
    'Human_Development_Index_HDI','Life_Expectancy_Years'
]
avail = [v for v in vars_to_plot if v in df.columns]
countries = df['Country'].dropna().unique()

for var in avail:
    plt.figure(figsize=(10,6))
    for c in countries:
        sub = df[df['Country']==c].sort_values('Year')
        if var in sub.columns:
            plt.plot(sub['Year'], sub[var], marker='o', label=c)
    plt.title(f"{var} by Country (2000-2023)")
    plt.xlabel("Year")
    plt.ylabel(var)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTDIR / f"trend_{var}.png", dpi=150)
    plt.show()

# Faceted GDP per Capita
if 'GDP_per_Capita_in_USD' in df.columns:
    g = sns.FacetGrid(df, col="Country", col_wrap=3, height=3.5, sharey=False)
    g.map_dataframe(sns.lineplot, x="Year", y="GDP_per_Capita_in_USD", marker="o")
    g.set_axis_labels("Year", "GDP per Capita (USD)")
    plt.tight_layout()
    plt.savefig(OUTDIR / "facet_GDP_per_Capita.png", dpi=150)
    plt.show()

# %% [markdown]
# ## 5) Outlier checks
# - Impossible values (e.g., literacy > 100)
# - Z-score based outliers for key vars

# %%
# Detect columns likely related to literacy
literacy_cols = [c for c in df.columns if 'literacy' in c.lower()]
impossible_rows = pd.DataFrame()
for col in literacy_cols:
    bad = df[df[col] > 100][['Country','Year',col]]
    if not bad.empty:
        bad = bad.assign(issue='literacy_gt_100', column=col)
        impossible_rows = pd.concat([impossible_rows, bad], ignore_index=True)

# negative checks for population/GDP/CO2
for col in ['Population_in_Millions','GDP_in_Trillions_USD','GDP_per_Capita_in_USD']:
    if col in df.columns:
        neg = df[df[col] < 0][['Country','Year',col]]
        if not neg.empty:
            neg = neg.assign(issue='negative_value', column=col)
            impossible_rows = pd.concat([impossible_rows, neg], ignore_index=True)

impossible_rows.to_csv(OUTDIR / "outliers_impossible.csv", index=False)
print("Impossible-value outliers (if any) written to outputs/outliers_impossible.csv")
display(impossible_rows.head())

# Z-score multivariate outliers for selected key variables
key_vars = [v for v in ['GDP_per_Capita_in_USD','GDP_in_Trillions_USD','CO2_Emissions_Million_Metric_Tons',
                'Renewable_Energy_Share_percent','Human_Development_Index_HDI'] if v in df.columns]
z_outliers = pd.DataFrame()
if key_vars:
    sub = df[['Country','Year'] + key_vars].dropna()
    zscores = np.abs(stats.zscore(sub[key_vars], nan_policy='omit'))
    z_df = pd.DataFrame(zscores, columns=key_vars, index=sub.index)
    mask = (z_df > 3).any(axis=1)
    if mask.any():
        z_outliers = sub.loc[mask]
    z_outliers.to_csv(OUTDIR / "outliers_zscore.csv", index=False)
    print("Z-score outliers (|z|>3) saved to outputs/outliers_zscore.csv")
    display(z_outliers.head())

# %% [markdown]
# ## 6) Country clustering summary (PCA + KMeans)
# Aggregate per country (mean across years), standardize, run PCA and KMeans (k=2..4), pick best silhouette.

# %%
# Candidate profile features (fall back to first numeric columns)
candidate_features = [
    'GDP_per_Capita_in_USD','Human_Development_Index_HDI','Renewable_Energy_Share_percent',
    'CO2_Emissions_Million_Metric_Tons','Internet_Penetration_percent',
    'Healthcare_Expenditure_per_Capita_USD'
]
available = [c for c in candidate_features if c in df.columns]
if len(available) < 3:
    numeric = df.select_dtypes(include=[np.number]).columns.tolist()
    available = numeric[:6]

profile = df.groupby('Country')[available].mean().dropna(axis=1, how='all').fillna(df[available].mean())
profile.to_csv(OUTDIR / "clusters_input_profile.csv")

# Standardize
scaler = StandardScaler()
X = scaler.fit_transform(profile.values)

# PCA projection (2D)
pca = PCA(n_components=2, random_state=42)
pcs = pca.fit_transform(X)
pca_df = pd.DataFrame(pcs, columns=['PC1','PC2'], index=profile.index)

# KMeans best k
best_k = None
best_score = -1
best_labels = None
for k in range(2, min(5, len(profile))):  # up to 4 or n-1
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X)
    score = silhouette_score(X, labels) if len(profile) > k else -1
    if score > best_score:
        best_score = score
        best_k = k
        best_labels = labels.copy()

profile['cluster'] = best_labels
profile.to_csv(OUTDIR / "clusters.csv")
cluster_summary = profile.groupby('cluster').agg(['count','mean','std']).round(3)
cluster_summary.to_csv(OUTDIR / "cluster_summary.csv")

# Plot PCA scatter with labels
plt.figure(figsize=(8,6))
palette = sns.color_palette("tab10", n_colors=len(np.unique(best_labels)))
for c in profile['cluster'].unique():
    mask = profile['cluster']==c
    plt.scatter(pca_df.loc[mask,'PC1'], pca_df.loc[mask,'PC2'], label=f'cluster {c}', s=140)
    for idx in pca_df[mask].index:
        plt.text(pca_df.loc[idx,'PC1']+0.02, pca_df.loc[idx,'PC2']+0.02, idx, fontsize=9)
plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% var)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% var)")
plt.title("Country clusters (PCA 2D projection)")
plt.legend()
plt.tight_layout()
plt.savefig(OUTDIR / "pca_biplot.png", dpi=150)
plt.show()

print(f"Best k selected: {best_k} (silhouette {best_score:.3f})")
display(cluster_summary)

# %% [markdown]
# ## Wrap-up: print saved outputs and short notes

# %%
print("Saved outputs to:", OUTDIR.resolve())
print("- missing_summary.csv, missingness_heatmap.png")
print("- summary_stats_by_country.csv, summary_stats_global.csv")
print("- corr_matrix_global.csv, corr_matrix_global.png")
print("- trend_*.png, facet_GDP_per_Capita.png")
print("- outliers_impossible.csv, outliers_zscore.csv")
print("- clusters.csv, cluster_summary.csv, pca_biplot.png")

# Short notes for next steps
notes = """
Notes:
- Review outputs/outliers_impossible.csv for domain errors (e.g., literacy > 100). Decide on correction or removal.
- Check corr_matrix_global.png for multicollinearity before modeling.
- For forecasting, consider stationarity checks (ADF/KPSS) and panel/dynamic approaches.
- Clustering used mean over years; use 'latest year' if you want current-profile clusters instead.
"""
print(notes)