import numpy as np

# Данные из таблицы
xi = np.array([1, 2, 3, 4, 5, 6, 7, 8])
F1 = np.array([2, 2, 2, 3, 3, 4, 5, 5])
F2 = np.array([6, 4, 7, 2, 4, 4, 6, 5])

# А) Линейная свертка критериев
alpha = 0.5
beta = 0.5
linear_convolution = alpha * F1 + beta * F2
min_linear_solution_index = np.argmin(linear_convolution)
min_linear_solution = xi[min_linear_solution_index]
print("Минимальное решение по линейной свертке критериев:", min_linear_solution)

# Б) Находим множество Парето
pareto_front = []
for i in range(len(xi)):
    is_pareto = True
    for j in range(len(xi)):
        if i != j and F1[j] <= F1[i] and F2[j] <= F2[i]:
            is_pareto = False
            break
    if is_pareto:
        pareto_front.append(xi[i])

print("Множество Парето:", pareto_front)
