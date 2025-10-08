# Investment Calculator - Quick Start Guide

## What This Calculator Does

This calculator helps you plan and simulate a 5-year investment strategy by providing:

1. **Cost Analysis**: Total costs including initial investment and ongoing operational expenses
2. **Break-Even Point**: Exact timing when your investment becomes profitable
3. **Scalable Income**: Revenue projections showing growth potential over time

## Quick Start

### 1. Run the Basic Calculator

```bash
python3 investment_calculator.py
```

This will:
- Show an example scenario
- Prompt you to enter your own numbers

### 2. View Multiple Scenarios

```bash
python3 examples.py
```

See pre-configured scenarios:
- Tech Startup
- Small Retail Business  
- Conservative Investment
- Aggressive Growth Strategy

### 3. Run Tests

```bash
python3 test_calculator.py
```

Verify all calculations are working correctly.

## Key Inputs Needed

1. **Initial Investment** - One-time upfront cost (e.g., $50,000)
2. **Monthly Operational Cost** - Recurring monthly expenses (e.g., $5,000)
3. **First Year Monthly Revenue** - Expected monthly revenue in year 1 (e.g., $8,000)
4. **Annual Growth Rate** - Expected yearly revenue increase (e.g., 0.15 for 15%)

## Understanding the Output

### Year-by-Year Breakdown
- **Costs**: Total expenses for the year (Year 1 includes initial investment)
- **Revenue**: Total income for the year
- **Profit**: Revenue minus costs
- **Cumulative**: Running total of profit/loss

### Break-Even Point
- Shows when cumulative profit turns positive
- Format: Year X, Month Y
- If "Not reached" - investment doesn't pay off in 5 years

### Scalable Income Projection
- Shows Years 6-10 if growth continues
- Helps evaluate long-term potential
- Useful for understanding exit value

## Example Interpretation

If the calculator shows:
- Break-even: Year 2, Month 4
- 5-Year Profit: $297,268.60
- Year 5 Monthly Revenue: $13,992.05

This means:
- ✓ You'll recover your investment in ~16 months
- ✓ After 5 years, you'll have ~$297k in profit
- ✓ By year 5, you're making ~$14k/month in revenue

## Tips for Best Results

1. **Be Realistic**: Use conservative estimates for revenue
2. **Include All Costs**: Don't forget hidden operational expenses
3. **Research Growth**: Look at industry benchmarks for growth rates
4. **Run Scenarios**: Try optimistic, realistic, and pessimistic cases
5. **Update Regularly**: Revise projections as you get real data

## Common Use Cases

- **Startup Planning**: Determine runway and fundraising needs
- **Business Expansion**: Evaluate ROI of opening new locations
- **Product Launch**: Calculate profitability timeline for new products
- **Investment Analysis**: Compare different business opportunities

## Custom Usage in Your Code

```python
from investment_calculator import InvestmentCalculator

# Create calculator
calc = InvestmentCalculator(
    initial_investment=50000,
    monthly_cost=5000,
    monthly_revenue_year1=8000,
    revenue_growth_rate=0.15
)

# Get formatted report
calc.print_report()

# Or get raw data
summary = calc.get_summary()
break_even = calc.find_break_even()
profits = calc.calculate_yearly_profit()
```

## Support

For questions or issues, refer to:
- README.md for detailed documentation
- examples.py for various scenarios
- test_calculator.py for implementation details
