# 2) Importez la bibliothèque numpy
import numpy as np

# Créer le tableau « grades »
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

# 3) Calculer la moyenne
mean_grade = np.mean(grades)
print(f"Moyenne des notes : {mean_grade}")

# Calculer la médiane
median_grade = np.median(grades)
print(f"Médiane des notes : {median_grade}")

# Calculer l'écart type
std_dev_grade = np.std(grades)
print(f"Écart type des notes : {std_dev_grade}")

# 4) Trouver le maximum 
max_grade = np.max(grades)
print(f"Note maximale : {max_grade}")

# Trouver le minimum
min_grade = np.min(grades)
print(f"Note minimale : {min_grade}")

# 5) Trier les notes par ordre croissant
sorted_grades = np.sort(grades)
print(f"Notes triées : {sorted_grades}")

# 6) Trouver l'index de la note la plus élevée
index_max_grade = np.argmax(grades)
print(f"Index de la note la plus élevée : {index_max_grade}")

# 7) Compter le nombre d'élèves ayant un score supérieur à 90
count_above_90 = np.sum(grades > 90)
print(f"Nombre d'élèves avec une note supérieure à 90 : {count_above_90}")

# 8) Calculer le pourcentage d'élèves ayant un score supérieur à 90
percentage_above_90 = np.mean(grades > 90) * 100
print(f"Pourcentage d'élèves avec une note supérieure à 90 : {percentage_above_90:.2f}%")

# 9) Calculer le pourcentage d'élèves ayant un score inférieur à 75
percentage_below_75 = np.mean(grades < 75) * 100
print(f"Pourcentage d'élèves avec une note inférieure à 75 : {percentage_below_75:.2f}%")

# 10) Extraire les notes supérieures à 90
high_performers = grades[grades > 90]
print(f"Notes supérieures à 90 : {high_performers}")

# 11) Créer un tableau avec toutes les notes supérieures à 75
passing_grades = grades[grades > 75]
print(f"Notes supérieures à 75 : {passing_grades}")
