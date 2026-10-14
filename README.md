# RetailPulse: Sales & Customer Intelligence

## Project Overview
RetailPulse is a data analysis project that explores retail sales and profitability using Python. It analyzes product categories, sub-categories, regional performance, and discount levels to identify useful business insights.

## Business Problem
Retail businesses need to understand which products and regions perform well, where losses occur, and how discount levels relate to profitability. RetailPulse uses historical sales data to explore these questions.

## Tools Used
- Python
- Pandas
- Matplotlib
- CSV dataset

## Dataset
The project uses the Sample Superstore dataset, containing sales records and information about shipping modes, customer segments, locations, product categories, sales, quantities, discounts, and profits.

## Project Workflow
1. Load and explore the dataset.
2. Check data quality and remove duplicate records.
3. Verify missing values.
4. Perform exploratory data analysis.
5. Calculate descriptive statistics and examine relationships between numerical variables.
6. Create visualizations.
7. Summarize business insights and recommendations.

## Key Findings
- Technology generated the highest total sales and profit among the three product categories.
- Furniture generated substantial sales but comparatively low profit.
- The West region recorded the highest total sales and profit among the four regions.
- Tables showed the largest total loss among the product sub-categories.
- Higher discount levels were associated with lower profitability in parts of the dataset; this does not establish that discounts alone caused the losses.
- The cleaned dataset contains 9,977 records after duplicate removal.

## Visualizations
The `charts` folder contains four charts:
- Sales and Profit by Product Category
- Profit by Product Sub-Category
- Sales and Profit by Region
- Average Profit by Discount Level

## Recommendations
- Review the profitability of Furniture and loss-making sub-categories.
- Investigate pricing and discount policies.
- Study the practices associated with strong Technology and West-region performance.
- Continue checking data quality before analysis.

## Limitations
This project uses historical data. The observed relationships do not prove causation, and the findings should be validated against additional business information before making operational decisions.

## Project Status
Version 1: Data cleaning, exploratory analysis, statistical analysis, visualizations, and business recommendations.
