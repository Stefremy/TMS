#!/usr/bin/env python3
"""
5-Year Investment Plan Calculator
Calculates costs, break-even point, and scalable income for a business investment.
"""

class InvestmentCalculator:
    def __init__(self, initial_investment, monthly_cost, monthly_revenue_year1, 
                 revenue_growth_rate=0.1):
        """
        Initialize the investment calculator.
        
        Args:
            initial_investment: One-time initial investment cost
            monthly_cost: Monthly operational costs
            monthly_revenue_year1: Monthly revenue in the first year
            revenue_growth_rate: Annual revenue growth rate (default 10%)
        """
        self.initial_investment = initial_investment
        self.monthly_cost = monthly_cost
        self.monthly_revenue_year1 = monthly_revenue_year1
        self.revenue_growth_rate = revenue_growth_rate
        self.years = 5
    
    def calculate_yearly_costs(self):
        """Calculate total costs for each year."""
        yearly_costs = []
        for year in range(1, self.years + 1):
            # Year 1 includes initial investment
            if year == 1:
                total_cost = self.initial_investment + (self.monthly_cost * 12)
            else:
                total_cost = self.monthly_cost * 12
            yearly_costs.append(total_cost)
        return yearly_costs
    
    def calculate_yearly_revenue(self):
        """Calculate projected revenue for each year with growth."""
        yearly_revenue = []
        for year in range(1, self.years + 1):
            # Apply growth rate for each subsequent year
            annual_revenue = self.monthly_revenue_year1 * 12 * (1 + self.revenue_growth_rate) ** (year - 1)
            yearly_revenue.append(annual_revenue)
        return yearly_revenue
    
    def calculate_yearly_profit(self):
        """Calculate profit/loss for each year."""
        costs = self.calculate_yearly_costs()
        revenues = self.calculate_yearly_revenue()
        return [revenues[i] - costs[i] for i in range(self.years)]
    
    def calculate_cumulative_profit(self):
        """Calculate cumulative profit over time."""
        profits = self.calculate_yearly_profit()
        cumulative = []
        total = 0
        for profit in profits:
            total += profit
            cumulative.append(total)
        return cumulative
    
    def find_break_even(self):
        """
        Find the break-even point (when cumulative profit becomes positive).
        Returns tuple: (year, month) or None if never breaks even in 5 years.
        """
        monthly_costs = self.monthly_cost
        cumulative_profit = -self.initial_investment
        
        for year in range(1, self.years + 1):
            monthly_revenue = self.monthly_revenue_year1 * (1 + self.revenue_growth_rate) ** (year - 1)
            
            for month in range(1, 13):
                cumulative_profit += monthly_revenue - monthly_costs
                
                if cumulative_profit >= 0:
                    return (year, month)
        
        return None
    
    def get_summary(self):
        """Generate a complete investment summary."""
        costs = self.calculate_yearly_costs()
        revenues = self.calculate_yearly_revenue()
        profits = self.calculate_yearly_profit()
        cumulative = self.calculate_cumulative_profit()
        break_even = self.find_break_even()
        
        summary = {
            'initial_investment': self.initial_investment,
            'monthly_operational_cost': self.monthly_cost,
            'starting_monthly_revenue': self.monthly_revenue_year1,
            'revenue_growth_rate': self.revenue_growth_rate,
            'yearly_data': [],
            'break_even': break_even,
            'total_5year_profit': cumulative[-1] if cumulative else 0
        }
        
        for year in range(self.years):
            summary['yearly_data'].append({
                'year': year + 1,
                'costs': costs[year],
                'revenue': revenues[year],
                'profit': profits[year],
                'cumulative_profit': cumulative[year]
            })
        
        return summary
    
    def print_report(self):
        """Print a formatted report of the investment plan."""
        summary = self.get_summary()
        
        print("=" * 80)
        print(" " * 20 + "5-YEAR INVESTMENT PLAN CALCULATOR")
        print("=" * 80)
        print()
        print(f"Initial Investment:        ${summary['initial_investment']:,.2f}")
        print(f"Monthly Operational Cost:  ${summary['monthly_operational_cost']:,.2f}")
        print(f"Starting Monthly Revenue:  ${summary['starting_monthly_revenue']:,.2f}")
        print(f"Annual Revenue Growth:     {summary['revenue_growth_rate'] * 100:.1f}%")
        print()
        print("-" * 80)
        print(f"{'Year':<6} {'Costs':>15} {'Revenue':>15} {'Profit':>15} {'Cumulative':>15}")
        print("-" * 80)
        
        for data in summary['yearly_data']:
            print(f"{data['year']:<6} "
                  f"${data['costs']:>14,.2f} "
                  f"${data['revenue']:>14,.2f} "
                  f"${data['profit']:>14,.2f} "
                  f"${data['cumulative_profit']:>14,.2f}")
        
        print("-" * 80)
        print()
        
        if summary['break_even']:
            year, month = summary['break_even']
            print(f"✓ BREAK-EVEN POINT: Year {year}, Month {month}")
        else:
            print("✗ NO BREAK-EVEN within 5 years")
        
        print()
        print(f"Total 5-Year Profit: ${summary['total_5year_profit']:,.2f}")
        print()
        
        # Scalable income projection
        print("=" * 80)
        print(" " * 25 + "SCALABLE INCOME PROJECTION")
        print("=" * 80)
        print()
        final_year_monthly = summary['yearly_data'][-1]['revenue'] / 12
        print(f"Year 5 Monthly Revenue:    ${final_year_monthly:,.2f}")
        print(f"Year 5 Monthly Profit:     ${final_year_monthly - summary['monthly_operational_cost']:,.2f}")
        print()
        print("If growth continues at the same rate:")
        for extra_year in [6, 7, 8, 9, 10]:
            projected_monthly = self.monthly_revenue_year1 * (1 + self.revenue_growth_rate) ** (extra_year - 1)
            projected_annual = projected_monthly * 12
            projected_profit = projected_annual - (self.monthly_cost * 12)
            print(f"  Year {extra_year:2d}: ${projected_annual:>12,.2f} revenue, ${projected_profit:>12,.2f} profit")
        print()
        print("=" * 80)


def main():
    """Main function to run example calculations."""
    print("\n" + "=" * 80)
    print(" " * 30 + "EXAMPLE SCENARIO")
    print("=" * 80 + "\n")
    
    # Example scenario
    calculator = InvestmentCalculator(
        initial_investment=50000,      # $50,000 initial investment
        monthly_cost=5000,              # $5,000 monthly operational costs
        monthly_revenue_year1=8000,     # $8,000 monthly revenue in year 1
        revenue_growth_rate=0.15        # 15% annual growth
    )
    
    calculator.print_report()
    
    print("\n" + "=" * 80)
    print(" " * 28 + "CUSTOM CALCULATION")
    print("=" * 80 + "\n")
    
    # Interactive mode
    try:
        initial = float(input("Enter initial investment ($): "))
        monthly_cost = float(input("Enter monthly operational costs ($): "))
        monthly_revenue = float(input("Enter expected monthly revenue in year 1 ($): "))
        growth = float(input("Enter annual revenue growth rate (e.g., 0.1 for 10%): "))
        
        custom_calc = InvestmentCalculator(initial, monthly_cost, monthly_revenue, growth)
        print()
        custom_calc.print_report()
    except (ValueError, KeyboardInterrupt):
        print("\n\nSkipping custom calculation.\n")


if __name__ == "__main__":
    main()
