from demographic_data_analyzer import calculate_demographic_data

if __name__ == "__main__":
    results = calculate_demographic_data(print_data=True)

    print("\n--- Diccionario devuelto ---")
    for key, value in results.items():
        print(f"{key}:")
        print(value)
        print("-" * 40)
