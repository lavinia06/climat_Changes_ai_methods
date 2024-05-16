import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/ionel/Downloads/dataset.csv")
data_cleaned = data.dropna()
temperatures = data['F2019']
sma = temperatures.rolling(window=3).mean()

# Calculul metricilor suplimentare
mean_temperature = temperatures.mean()  # Media temperaturilor
std_dev_temperature = temperatures.std()  # Deviația standard a temperaturilor
min_temperature = temperatures.min()  # Temperatura minimă
max_temperature = temperatures.max()  # Temperatura maximă
mse = ((temperatures - sma)**2).mean()  # Eroarea Medie Pătratică (MSE)

# Afisarea valorilor metrice calculate
print("Media temperaturilor:", mean_temperature)
print("Deviația standard a temperaturilor:", std_dev_temperature)
print("Temperatura minimă:", min_temperature)
print("Temperatura maximă:", max_temperature)
print("Eroarea Medie Pătratică (MSE):", mse)

# Afișarea graficului
plt.figure(figsize=(10, 6))
plt.plot(data.index, temperatures, label='Temperaturi 2019')
plt.plot(data.index, sma, label='SMA (Fereastră 3)')
plt.xlabel('Indexul Datelor')
plt.ylabel('Temperaturi')
plt.title('Temperaturi 2019 și SMA')
plt.legend()
plt.show()



