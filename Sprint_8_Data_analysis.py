import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Load data
df_companies = pd.read_csv('moved_project_sql_result_01.csv')
df_locations = pd.read_csv('moved_project_sql_result_04.csv')

print('Companies shape:', df_companies.shape)
print('Locations shape:', df_locations.shape)
print(df_companies.head())
print(df_locations.head())

# --- Top 10 Taxi Companies by Number of Trips ---
top_companies = df_companies.nlargest(10, 'trips_amount')

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.barh(top_companies['company_name'], top_companies['trips_amount'], color='steelblue')
ax.invert_yaxis()
ax.set_xlabel('Number of Trips')
ax.set_title('Top 10 Taxi Companies by Number of Trips')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))

for bar in bars:
    width = bar.get_width()
    ax.text(width + 100, bar.get_y() + bar.get_height() / 2,
            f'{int(width):,}', va='center', fontsize=9)

plt.tight_layout()
plt.savefig('top_companies.png', dpi=150)
plt.show()

# --- Top 15 Dropoff Locations by Average Trips ---
top_locations = df_locations.nlargest(15, 'average_trips')

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.barh(top_locations['dropoff_location_name'], top_locations['average_trips'], color='coral')
ax.invert_yaxis()
ax.set_xlabel('Average Trips')
ax.set_title('Top 15 Dropoff Locations by Average Trips')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))

for bar in bars:
    width = bar.get_width()
    ax.text(width + 50, bar.get_y() + bar.get_height() / 2,
            f'{width:,.1f}', va='center', fontsize=9)

plt.tight_layout()
plt.savefig('top_locations.png', dpi=150)
plt.show()

# --- Summary Statistics ---
print('\n=== Taxi Companies ===')
print(df_companies['trips_amount'].describe().round(0))

print('\n=== Dropoff Locations ===')
print(df_locations['average_trips'].describe().round(2))
