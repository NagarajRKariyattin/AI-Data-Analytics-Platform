def generate_dataset_summary(df, dataset_info, business_kpis):
    """
    Generate a human-readable summary of the uploaded dataset.
    """

    summary = []

    summary.append(
        f"This dataset contains {dataset_info['rows']} rows and {dataset_info['columns']} columns."
    )

    summary.append(
        f"It has {dataset_info['numeric']} numeric columns and {dataset_info['categorical']} categorical columns."
    )

    summary.append(
        f"There are {dataset_info['missing']} missing values."
    )

    if business_kpis:

        summary.append("Key business metrics:")

        for key, value in business_kpis.items():

            if isinstance(value, float):
                value = f"{value:,.2f}"

            elif isinstance(value, int):
                value = f"{value:,}"

            summary.append(f"• {key}: {value}")

    return "\n".join(summary)