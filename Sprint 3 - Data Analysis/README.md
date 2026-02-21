# Engineering Graduate Salary Analysis

This project is a data analysis program. It uses an Engineering Graduate Salary dataset found on Kaggle.com.
This dataset includes valuable information about college specializations, personality traits, and gender, all
of which are used in this program. Using Python and the Pandas library, we can analyze the data to answer 
critical questions, filter, sort, and aggregate the data, and visualize some of the findings. 

The three questions I asked are:
1. Which engineering specializations yield the highest average starting salaries?
	- Aggregate & Sort

2. Does high "Conscientiousness" and "Extraversion" correlate with a higher average salary compared to introverted/less conscientious graduates?
	- Filter, then Aggregate

3. How does the average salary compare between male and female graduates specifically within the top 3 most popular engineering specializations?
	- Filter, Group, then Sort

I listed beneath each the requirements they fulfill from the module. You will see the findings answered in the video linked below.

## Instructions for Build and Use

[Software Demo](https://youtu.be/ulqfIUYgtEQ)

Steps to build and/or run the software:

1. Ensure you have Python 3 installed on your machine.
2. Install the required external libraries by running the following command in your terminal: `pip install pandas matplotlib`.
3. Ensure the dataset `Engineering_graduate_salary.csv` is downloaded and placed in the same directory as the Python script.

Instructions for using the software:

1. Open your terminal or command prompt.
2. Open the folder containing the script and dataset.
3. Run the script using the command: `python <name_of_your_script>.py`. 
4. Review the data summaries printed in the terminal, and view the pop-up bar chart visualization. 

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python 3
* Pandas (for data manipulation and analysis)
* Matplotlib (for data visualization)
* IDE

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Pandas 10 Minute Tutorial](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
* [Matplotlib Pyplot Tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
* [Kaggle Datasets](https://www.kaggle.com/datasets)
* [Gemini](https://gemini.google.com)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Add more complex visualizations using libraries like Seaborn or Plotly.
* [ ] Build a simple regression model to predict salaries based on a graduate's specialization and personality test scores.