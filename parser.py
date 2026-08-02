import pandas as pd


def load_bom(uploaded_file) -> pd.DataFrame:
    """Reads the uploaded CSV file and cleans column names."""
    df = pd.read_csv(uploaded_file)

    # Clean whitespace from string columns
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    return df


def calculate_bom_summary(df: pd.DataFrame) -> dict:
    """Calculates high-level metrics for the uploaded BOM."""
    total_line_items = len(df)

    # Check for common variations of quantity column name
    qty_col = next(
        (col for col in df.columns if col.lower() in ["qty", "quantity"]), None
    )

    total_components = int(df[qty_col].sum()) if qty_col else total_line_items

    return {
        "total_line_items": total_line_items,
        "total_components": total_components,
        "has_quantity_col": qty_col is not None,
    }