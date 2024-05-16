import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def calculate_metrics(data, metrics_list):
    temperatures = data['F2019']
    sma = temperatures.rolling(window=5).mean().dropna()

    metrics = {}

    if 'mean' in metrics_list:
        metrics["mean_temperature"] = temperatures.mean()
    if 'std_dev' in metrics_list:
        metrics["std_dev_temperature"] = temperatures.std()
    if 'min' in metrics_list:
        metrics["min_temperature"] = temperatures.min()
    if 'max' in metrics_list:
        metrics["max_temperature"] = temperatures.max()
    if 'mse' in metrics_list:
        metrics["mse"] = mean_squared_error(temperatures[:len(sma)], sma)
    if 'mae' in metrics_list:
        metrics["mae"] = mean_absolute_error(temperatures[:len(sma)], sma)

    if 'r2' in metrics_list:
        metrics["r2"] = r2_score(temperatures[:len(sma)], sma)
    if 'sma' in metrics_list:
        metrics["sma"] = sma

    return metrics

def main():
    data = pd.read_csv("C:/Users/ionel/Downloads/dataset.csv")
    data_cleaned = data.dropna()

    print("\nSelectați metricile pe care doriți să le calculați (separate prin virgulă):")
    print("mean, std_dev, min, max, mse, mae, rmse, r2, sma")
    selected_metrics = input("Metrici: ").strip().split(',')

    metrics = calculate_metrics(data_cleaned, selected_metrics)

    print("\nRezultatele analizei:")
    for metric_name, value in metrics.items():
        print(f"{metric_name}: {value}")

    save_plot = input("\nDoriți să salvați graficul într-un fișier de imagine? (da/nu): ").lower()
    if save_plot == 'da':
        file_name = input("Introduceți numele fișierului (fără extensie): ")
        plt.figure(figsize=(10, 6))
        plt.plot(data_cleaned.index, data_cleaned['F2019'], label='Temperaturi 2019')
        if 'sma' in selected_metrics:
            plt.plot(data_cleaned.index[:len(metrics.get("sma", []))], metrics.get("sma", []), label='SMA (Fereastră 5)')
        plt.xlabel('Indexul Datelor')
        plt.ylabel('Temperaturi')
        plt.title('Temperaturi 2019 și SMA')
        plt.legend()
        plt.savefig(f"{file_name}.png")
        print(f"Graficul a fost salvat ca '{file_name}.png'.")
    else:
        plt.figure(figsize=(10, 6))
        plt.plot(data_cleaned.index, data_cleaned['F2019'], label='Temperaturi 2019')
        if 'sma' in selected_metrics:
            plt.plot(data_cleaned.index[:len(metrics.get("sma", []))], metrics.get("sma", []), label='SMA (Fereastră 5)')
        plt.xlabel('Indexul Datelor')
        plt.ylabel('Temperaturi')
        plt.title('Temperaturi 2019 și SMA')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    main()
