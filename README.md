# TMS - Investment Calculator

A comprehensive 5-year investment plan calculator that simulates costs, break-even points, and scalable income projections.

## Features

- **Cost Analysis**: Calculate total costs including initial investment and monthly operational expenses
- **Break-Even Point**: Determine when your investment will become profitable
- **Revenue Projections**: Model revenue growth over 5 years with customizable growth rates
- **Scalable Income**: Project future income potential beyond the 5-year plan
- **Detailed Reports**: Get year-by-year breakdowns of costs, revenue, and cumulative profit

## Usage

### Run the Calculator

```bash
python3 investment_calculator.py
```

The script will:
1. Show an example scenario with predefined values
2. Prompt you to enter your own investment parameters for a custom calculation

### Example Output

The calculator provides:
- Initial investment summary
- Year-by-year financial breakdown
- Break-even analysis
- 5-year total profit
- Extended income projections (Years 6-10)

### Using as a Module

```python
from investment_calculator import InvestmentCalculator

# Create a calculator instance
calc = InvestmentCalculator(
    initial_investment=50000,      # Initial one-time investment
    monthly_cost=5000,              # Monthly operational costs
    monthly_revenue_year1=8000,     # Expected monthly revenue in year 1
    revenue_growth_rate=0.15        # 15% annual growth rate
)

# Print detailed report
calc.print_report()

# Or get data programmatically
summary = calc.get_summary()
break_even = calc.find_break_even()
```

## Parameters

- **initial_investment**: One-time upfront investment cost
- **monthly_cost**: Fixed monthly operational expenses
- **monthly_revenue_year1**: Expected monthly revenue in the first year
- **revenue_growth_rate**: Annual revenue growth rate (e.g., 0.1 for 10% growth)

## Requirements

- Python 3.6 or higher
- No external dependencies required

## License

MIT
