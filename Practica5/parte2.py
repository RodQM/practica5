from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Función para ingresar los valores de y_true y y_pred
def ingresar_valores():
    y_true = list(map(int, input("Ingresa los valores de y_true (separados por comas): ").split(',')))
    y_pred = list(map(int, input("Ingresa los valores de y_pred (separados por comas): ").split(',')))
    return y_true, y_pred

# Función para utilizar los valores de ejemplo
def usar_valores_ejemplo():
    y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]
    return y_true, y_pred

# Menú interactivo
def menu():
    print("\nSelecciona una opción:")
    print("1. Ingresar nuevos valores de ejemplo")
    print("2. Usar valores de ejemplo predeterminados")
    print("3. Calcular Accuracy")
    print("4. Calcular Precision")
    print("5. Calcular Recall")
    print("6. Calcular F1-Score")
    print("7. Mostrar la matriz de confusión y sus componentes")
    print("8. Salir")
    return input("Elige una opción (1-8): ")

# Inicializar valores con los predeterminados
y_true, y_pred = usar_valores_ejemplo()

while True:
    choice = menu()
    
    if choice == "1":
        y_true, y_pred = ingresar_valores()
    
    elif choice == "2":
        y_true, y_pred = usar_valores_ejemplo()
        print("Usando valores de ejemplo predeterminados.")
    
    elif choice == "3":
        acc = accuracy_score(y_true, y_pred)
        print(f"Accuracy: {acc}")
    
    elif choice == "4":
        precision = precision_score(y_true, y_pred)
        print(f"Precision: {precision}")
    
    elif choice == "5":
        recall = recall_score(y_true, y_pred)
        print(f"Recall: {recall}")
    
    elif choice == "6":
        f1 = f1_score(y_true, y_pred)
        print(f"F1-Score: {f1}")
    
    elif choice == "7":
        cm = confusion_matrix(y_true, y_pred)
        TP = cm[1, 1]
        TN = cm[0, 0]
        FP = cm[0, 1]
        FN = cm[1, 0]
        print(f"Matriz de confusión:\n{cm}")
        print(f"True Positives (TP): {TP}")
        print(f"True Negatives (TN): {TN}")
        print(f"False Positives (FP): {FP}")
        print(f"False Negatives (FN): {FN}")
    
    elif choice == "8":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida, por favor intenta de nuevo.")