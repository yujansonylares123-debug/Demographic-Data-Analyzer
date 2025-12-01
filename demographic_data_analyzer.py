import pandas as pd


def calculate_demographic_data(print_data=True):
    # 1. Carga de datos
    df = pd.read_csv(
                        "adult.data",           # ruta al archivo de datos
                        header=None,            # sin fila de encabezado
                        names=[
                            "age",
                            "workclass",
                            "fnlwgt",
                            "education",
                            "education-num",
                            "marital-status",
                            "occupation",
                            "relationship",
                            "race",
                            "sex",
                            "capital-gain",
                            "capital-loss",
                            "hours-per-week",
                            "native-country",
                            "salary"
                        ],
                        skipinitialspace=True   # elimina espacios iniciales
                    )

    # 2. Conteo de cada raza
    race_count = df["race"].value_counts()

    # 3. Edad promedio de los hombres
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 4. % con título de Bachelors
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    # 5. % con educación avanzada (Bachelors, Masters, Doctorate) que gana >50K
    higher_education_mask = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )
    higher_education = df[higher_education_mask]
    lower_education = df[~higher_education_mask]

    # 6. % con educación avanzada que gana >50K
    higher_education_rich = round(
        (higher_education[higher_education["salary"] == ">50K"].shape[0]
         / higher_education.shape[0]) * 100,
        1,
    )

    # 7. % sin educación avanzada que gana >50K
    lower_education_rich = round(
        (lower_education[lower_education["salary"] == ">50K"].shape[0]
         / lower_education.shape[0]) * 100,
        1,
    )

    # 8. Horas mínimas de trabajo por semana
    min_work_hours = df["hours-per-week"].min()

    # 9. % de personas que ganan >50K entre los que trabajan las horas mínimas
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_min_workers = min_workers[min_workers["salary"] == ">50K"].shape[0]
    rich_percentage = round(
        (rich_min_workers / min_workers.shape[0]) * 100,
        1,
    )

    # 10. País con el mayor % de personas que ganan >50K
    # número de personas que ganan >50K por país
    rich_by_country = df[df["salary"] == ">50K"]["native-country"].value_counts()
    # número total de personas por país
    total_by_country = df["native-country"].value_counts()

    # % de personas que ganan >50K por país
    rich_country_percent = (rich_by_country / total_by_country * 100).sort_values(
        ascending=False
    )

    highest_earning_country = rich_country_percent.index[0]
    highest_earning_country_percentage = round(
        rich_country_percent.iloc[0],
        1,
    )

    # 11. Ocupación más común entre los que ganan >50K en India
    top_IN_occupation = (
        df[
            (df["native-country"] == "India")
            & (df["salary"] == ">50K")
        ]["occupation"]
        .value_counts()
        .idxmax()
    )

    # Impresión de los resultados
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            "Highest percentage of rich people in country:",
            highest_earning_country_percentage,
            "%",
        )
        print("Top occupation in India:", top_IN_occupation)

    # Retorno de los resultados en un diccionario
    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
