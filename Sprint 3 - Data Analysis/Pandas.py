import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """Attempt to load dataset."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None


def run_eda(df):
    """Data checks and currency conversion."""
    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Missing values found: {df.isnull().sum().sum()}\n")


    # Convert INR to USD (approximate rate)
    df['Salary_USD'] = df['Salary'] * 0.011
    return df


def calc_salary_extremes(df):
    """Find the highest and lowest paying specializations."""
    avg_salaries = df.groupby('Specialization')['Salary_USD'].mean().sort_values(ascending=False)

    top_3 = avg_salaries.head(3)
    bottom_3 = avg_salaries.tail(3)

    print("--- Top 3 Average Salaries ---")
    print(top_3.apply(lambda x: f"${x:,.2f}").to_string())

    print("\n--- Bottom 3 Average Salaries ---")
    print(bottom_3.apply(lambda x: f"${x:,.2f}").to_string())
    print()

    return top_3, bottom_3


def check_personality_trends(df):
    """Compare salaries based on extreme personality traits."""
    high_traits = df[(df['extraversion'] > 0) & (df['conscientiousness'] > 0)]
    low_traits = df[(df['extraversion'] < 0) & (df['conscientiousness'] < 0)]

    print("--- Salary by Personality Traits ---")
    print(f"High extraversion/conscientiousness: ${high_traits['Salary_USD'].mean():,.2f}")
    print(f"Low extraversion/conscientiousness:  ${low_traits['Salary_USD'].mean():,.2f}")
    print()


def gender_breakdown(df):
    """Salary comparison by gender."""
    top_specs = df['Specialization'].value_counts().head(3).index.tolist()
    filtered_data = df[df['Specialization'].isin(top_specs)]

    comp = filtered_data.groupby(['Specialization', 'Gender'])['Salary_USD'].mean()

    print("--- Gender Salary Comparison (Top 3 Specializations) ---")
    print(comp.apply(lambda x: f"${x:,.2f}").to_string())
    print()


def plot_data(top_3, bottom_3):
    """Bar chart for salary extremes."""
    combined = pd.concat([top_3, bottom_3])

    plt.figure(figsize=(10, 6))

    # Differentiate top and bottom with colors
    bar_colors = ['#2ca02c', '#2ca02c', '#2ca02c', '#d62728', '#d62728', '#d62728']
    combined.plot(kind='bar', color=bar_colors, edgecolor='black')

    plt.title('Average Salaries by Specialization (Top 3 vs Bottom 3)')
    plt.ylabel('Salary (USD)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def main():
    df = load_data('Engineering_graduate_salary.csv')

    if df is not None:
        df = run_eda(df)
        top_3, bottom_3 = calc_salary_extremes(df)
        check_personality_trends(df)
        gender_breakdown(df)
        plot_data(top_3, bottom_3)


if __name__ == "__main__":
    main()