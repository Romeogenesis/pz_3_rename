import matplotlib.pyplot as plt
import numpy as np

electric_scooters_detailed = {
    "Kugoo Kirin M5": {
        "Максимальная скорость (км/ч)": 55,
        "Запас хода (км)": 60,
        "Мощность мотора (Вт)": 1000,
        "Ёмкость батареи (Ач)": 21,
        "Вес (кг)": 35,
        "Максимальная нагрузка (кг)": 150
    },
    "Ninebot Max G30": {
        "Максимальная скорость (км/ч)": 30,
        "Запас хода (км)": 65,
        "Мощность мотора (Вт)": 350,
        "Ёмкость батареи (Ач)": 15,
        "Вес (кг)": 19.2,
        "Максимальная нагрузка (кг)": 100
    },
    "Xiaomi Mi Electric Scooter Pro 2": {
        "Максимальная скорость (км/ч)": 25,
        "Запас хода (км)": 45,
        "Мощность мотора (Вт)": 300,
        "Ёмкость батареи (Ач)": 12.8,
        "Вес (кг)": 14.2,
        "Максимальная нагрузка (кг)": 100
    },
    "Halten RS-02": {
        "Максимальная скорость (км/ч)": 40,
        "Запас хода (км)": 50,
        "Мощность мотора (Вт)": 800,
        "Ёмкость батареи (Ач)": 18,
        "Вес (кг)": 28,
        "Максимальная нагрузка (кг)": 130
    }
}

models = list(electric_scooters_detailed.keys())
characteristics = list(list(electric_scooters_detailed.values())[0].keys())

inverse_chars = ["Вес (кг)"]

def get_normalized_data():
    base_model = list(electric_scooters_detailed.values())[0]
    normalized = []
    
    for model_name in models:
        model_data = electric_scooters_detailed[model_name]
        norm_values = []
        
        for char in characteristics:
            if char in inverse_chars:
                norm_value = base_model[char] / model_data[char]
            else:
                norm_value = model_data[char] / base_model[char]
            norm_values.append(norm_value)
        
        normalized.append(norm_values)
    
    return normalized

def get_technical_level(normalized):
    result = []
    for item in normalized:
        result.append(round(sum(item) / len(item), 2))
    return result

def create_bar(models, values):
    plt.figure(figsize=(10, 6))
    plt.bar(models, values, color="skyblue", edgecolor="black")
    plt.xlabel("Модель")
    plt.ylabel("Kту")
    plt.title("Сравнение моделей по качеству", pad=15)
    plt.xticks(rotation=15, ha="right")
    plt.tight_layout()
    plt.show()

def create_radial(models, characteristics, values):
    num_vars = len(characteristics)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection="polar"))
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    
    for i in range(len(values)):
        values_closed = values[i] + values[i][:1]
        ax.plot(angles, values_closed, 'o-', linewidth=2.5, label=models[i], 
                color=colors[i % len(colors)], markersize=8, alpha=0.8)
        ax.fill(angles, values_closed, alpha=0.1, color=colors[i % len(colors)])
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(characteristics, size=10, weight='bold')
    ax.tick_params(pad=20)
    
    max_value = max(max(item) for item in values)
    ax.set_ylim(0, max_value * 1.15)
    
    num_circles = 5
    y_ticks = np.linspace(0, max_value * 1.15, num_circles + 1)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels([f'{i:.1f}' for i in y_ticks], size=8)
    
    ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.0), fontsize=9)
    plt.title("Сравнение относительных характеристик", pad=40, size=13, weight='bold')
    plt.tight_layout()
    plt.show()

normalized_data = get_normalized_data()
technical_levels = get_technical_level(normalized_data)
create_bar(models, technical_levels)
create_radial(models, characteristics, normalized_data)