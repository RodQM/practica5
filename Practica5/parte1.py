# Funciones de desempeño
def accuracy(y_true, y_pred):
    correct_predictions = sum([1 for true, pred in zip(y_true, y_pred) if true == pred])
    return correct_predictions / len(y_true)

def error_rate(y_true, y_pred):
    incorrect_predictions = sum([1 for true, pred in zip(y_true, y_pred) if true != pred])
    return incorrect_predictions / len(y_true)

def confusion_matrix(y_true, y_pred):
    TP = sum([1 for true, pred in zip(y_true, y_pred) if true == 1 and pred == 1])
    TN = sum([1 for true, pred in zip(y_true, y_pred) if true == 0 and pred == 0])
    FP = sum([1 for true, pred in zip(y_true, y_pred) if true == 0 and pred == 1])
    FN = sum([1 for true, pred in zip(y_true, y_pred) if true == 1 and pred == 0])
    return TP, TN, FP, FN

def precision(TP, FP):
    return TP / (TP + FP) if (TP + FP) > 0 else 0

def recall(TP, FN):
    return TP / (TP + FN) if (TP + FN) > 0 else 0

def true_negative_rate(TN, FP):
    return TN / (TN + FP) if (TN + FP) > 0 else 0

def false_positive_rate(FP, TN):
    return FP / (FP + TN) if (FP + TN) > 0 else 0

def false_negative_rate(FN, TP):
    return FN / (FN + TP) if (FN + TP) > 0 else 0

def f1_score(precision, recall):
    return 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

# Función para ingresar los valores de y_true y y_pred
def ingresar_valores():
    y_true = list(map(int, input("Ingresa los valores de y_true (separados por comas): ").split(',')))
    y_pred = list(map(int, input("Ingresa los valores de y_pred (separados por comas): ").split(',')))
    return y_true, y_pred

# Menú interactivo
def menu():
    print("\nSelecciona una opción:")
    print("1. Ingresar nuevos valores de ejemplo")
    print("2. Calcular Accuracy")
    print("3. Calcular Error Rate")
    print("4. Calcular Precision, Recall, y F1-Score")
    print("5. Calcular True Negative Rate y False Positive Rate")
    print("6. Calcular False Negative Rate y F1-Score")
    print("7. Salir")
    return input("Elige una opción (1-7): ")

# Valores de ejemplo iniciales
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]

while True:
    choice = menu()
    
    if choice == "1":
        y_true, y_pred = ingresar_valores()
    
    elif choice == "2":
        acc = accuracy(y_true, y_pred)
        print(f"Accuracy: {acc}")
    
    elif choice == "3":
        error = error_rate(y_true, y_pred)
        print(f"Error Rate: {error}")
    
    elif choice == "4":
        TP, TN, FP, FN = confusion_matrix(y_true, y_pred)
        precision_value = precision(TP, FP)
        recall_value = recall(TP, FN)
        f1 = f1_score(precision_value, recall_value)
        print(f"Precision: {precision_value}")
        print(f"Recall: {recall_value}")
        print(f"F1-Score: {f1}")
    
    elif choice == "5":
        TP, TN, FP, FN = confusion_matrix(y_true, y_pred)
        tnr_value = true_negative_rate(TN, FP)
        fpr_value = false_positive_rate(FP, TN)
        print(f"True Negative Rate: {tnr_value}")
        print(f"False Positive Rate: {fpr_value}")
    
    elif choice == "6":
        TP, TN, FP, FN = confusion_matrix(y_true, y_pred)
        fnr_value = false_negative_rate(FN, TP)
        precision_value = precision(TP, FP)
        recall_value = recall(TP, FN)
        f1 = f1_score(precision_value, recall_value)
        print(f"False Negative Rate: {fnr_value}")
        print(f"F1-Score: {f1}")
    
    elif choice == "7":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida, por favor intenta de nuevo.")