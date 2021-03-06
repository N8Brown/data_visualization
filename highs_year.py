import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Get high temperatures from file
filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates = []
    highs = []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        high = int(row[1])

        dates.append(current_date)
        highs.append(high)

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red")

# Format plot
plt.title("Daily high temperatures, 2014", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
