# Task-1_ShrivedPatade
Shrived Umesh Patade
shrivedpatade@gmail.com

## Project Overview

This project is part of an AI internship task. It invlolves Developing an Agentic Tool to perform various analysis operations on the data which are specified by the user in the prompt. It uses Google's Gemini for handeling the inputs and yfinance api to fetch the realtime data from Yahoo finance.

## File Structure

- `/Task-1_ShrivedPatade/Task-1/`
    - `README.md`: Project documentation.
    - `lgWorkflow.py`: Creates the Work Flow Graph with LangGraph.
    - `model.py`: Gets User Prompt, Parses the input and uses the necessary tools specified by the user.
    - `fecthData.py`: Contains function to fetch data from the yfinance api.
    - `analyzeData.py`: Contains functions to apply different analysis methods over the data.
    - `plotData.py`: Contains the function that plots the data with the specified analysis.

## How to Run

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the `model.py` script or import it's `getResponse()` function, the project is kept modular therefor no need to import all files in the implementatino or using the Agentic Tool.

## Dependencies

- Python 3.x
- pandas
- numpy
- matplotlib
- requests
- google-generativeai
- langgraph
- yfinance

## Contact

For any questions or issues, please contact Shrived Umesh Patade at shrivedpatade@gmail.com.