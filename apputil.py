import seaborn as sns
import pandas as pd


# update/add code below ...
# Exercise 1
def fib(n):
    """ 
    Calculate the nth Fibonacci number using recursion.

    Parameters
    --------
    n : int
        The position in the Fibonacci sequence (must be non-negative).

    Returns
    ------
    int
        The nth Fibonacci number.
    """
    # Base case: stop recursion when n is 0 or 1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    return fib(n - 1) + fib(n - 2)

# Test cases
print(fib(0))  # Expected 0
print(fib(1))  # Expected 1
print(fib(5))  # Expected 5
print(fib(9))  # Expected 34



# Exercise 2
def to_binary(n):
    """
    Convert a non-negative integer to its binary representation as a string.
    
    Parameters
    ----------
    n : int
        A non-negative integer (Must be >= 0).

    Returns
    ----------
    str
        The binary representation of the integer as a string.

    Raises
    ------
    ValueError
        If the input is not a non-negative integer.
    """
    #Input validation
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Base case: stop recursion when n is 0 or 1
    if n == 0:
        return '0'
    elif n == 1:
        return '1'

    # Recursive case: divide n by 2 and concatenate the remainder
    return to_binary(n // 2) + str(n % 2)



# Exercise 3
import pandas as pd

# Load the dataset
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

# clean up gender column
df_bellevue['gender'] = df_bellevue['gender'].str.strip().str.lower()
df_bellevue['gender'] = df_bellevue['gender'].replace({
    'm': 'male',
    'w': 'female'
})
df_bellevue['gender']  = df_bellevue['gender'].fillna('unknown')

def task_1():
    """ Task 1: Return a list of column names from the df_bellevue dataset,
    sorted by the number of missing values (least missing first)

    Returns
    -------
    list
        Column names ordered from least missing values to most missing values.
    """

    # Count missing values for each column
    missing_counts = df_bellevue.isnull().sum()

    # Sort columns by missing value counts
    sorted_columns = missing_counts.sort_values().index.tolist()
    return sorted_columns
print(task_1())  # Example usage

def task_2():
    """ 
    Task 2: Return a DataFrame with the year and the total number of admissions per year.
    
    Returns
    -------
    pd.DataFrame
        DataFrame with two columns: 'year' and 'total_admissions', sorted by year in ascending order.
    """
    # Extract year from 'date_in', handling invalid dates
    df_bellevue['year'] = pd.to_datetime(df_bellevue['date_in'], errors='coerce').dt.year

    # Check for missing years
    missing_years = df_bellevue['year'].isnull().sum()
    if missing_years > 0:
        print(f"Warning: {missing_years} records have invalid or missing 'date_in' values.")

    # Count total admissions per year
    admissions_per_year = df_bellevue.groupby('year').size()

    # Convert to DataFrame
    admissions_df = admissions_per_year.reset_index(name='total_admissions').sort_values(by='year')
    return admissions_df

# Example usage
print(task_2().head())


def task_3():
    """ 
    Task 3: Return a Pandas Series with gender as the index and the
    average age for each gender as the values.
    
    Returns
    -------
    pd.Series
        A Series where:
        - index = gender categories
        - values = average age for each gender
    """
    # Make a copy to avoid modifying the original dataset
    df_copy = df_bellevue.copy()

    #chack if 'age' column exists
    if 'age' not in df_copy.columns:
        print("Error: 'age' column is missing.")
        return None
    
    # Ensure 'age' is numeric
    df_copy['age'] = pd.to_numeric(df_copy['age'], errors='coerce')

    # Clean and replace or missing values with 'unknown'
    df_copy['gender'] = df_copy['gender'].str.strip().str.lower()
    df_copy['gender'] = df_copy['gender'].replace({
        'm': 'male',
        'w': 'female',
        '?': 'unknown'
    })
    df_copy['gender'] = df_copy['gender'].fillna('unknown')

    # Drop rows with missing 'age
    df_copy = df_copy.dropna(subset=['age'])
    
    # Filter out invalid gender values
    valid_genders = ['male', 'female', 'unknown']
    df_copy = df_copy[df_copy['gender'].isin(valid_genders)]

    # Check if the DataFrame is empty after cleaning
    if df_copy.empty:
        print("No valid data to calculate average age.")
        return None

    # Group by gender and calculate average age
    average_age = df_copy.groupby('gender')['age'].mean()

    # Ensure all genders appear in the index, even if missing
    average_age = average_age.reindex(valid_genders)

    return average_age

# Test the function
print(task_3())

import string

def task_4():
    """ 
    Task 4:Return a list of the 5 most common professions
    in order of prevalence (most common first).
    
    Returns
    -------
    list
        A list of the top 5 most frequent professions.
    """

    # Make a copy to avoid modifying the original dataset
    df_copy = df_bellevue.copy()

    # Check if 'profession' column exists
    if 'profession' not in df_copy.columns:
        print("Error: 'profession' column is missing.")
        return []
    
    # Clean profession column: lowercase, strip spaces, remove punctuation
    df_copy['profession'] = df_copy['profession'].str.lower().str.strip()
    df_copy['profession'] = df_copy['profession'].str.replace(f"[{string.punctuation}]", "", regex=True)

    # Drop missing values
    missing_professions = df_copy['profession'].isnull().sum()
    if missing_professions > 0:
        print(f"Warning: {missing_professions} records have missing 'profession' values.")
    df_copy = df_copy.dropna(subset=['profession'])

    # Count frequencies and get the top 5
    top_professions = df_copy['profession'].value_counts().head(5).index.tolist()

    return top_professions

# Test the function
print(task_4())  # Example usage

