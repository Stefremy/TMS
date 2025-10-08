#!/usr/bin/env python3
"""
Example usage of the Investment Calculator
Demonstrates various scenarios and use cases.
"""

from investment_calculator import InvestmentCalculator


def scenario_startup():
    """Startup company scenario."""
    print("\n" + "=" * 80)
    print("SCENARIO 1: Tech Startup")
    print("=" * 80)
    
    calc = InvestmentCalculator(
        initial_investment=100000,    # $100k initial investment
        monthly_cost=15000,            # $15k monthly burn rate
        monthly_revenue_year1=10000,   # Starting at $10k MRR
        revenue_growth_rate=0.25       # 25% annual growth
    )
    
    calc.print_report()


def scenario_small_business():
    """Small business scenario."""
    print("\n" + "=" * 80)
    print("SCENARIO 2: Small Retail Business")
    print("=" * 80)
    
    calc = InvestmentCalculator(
        initial_investment=25000,      # $25k initial investment
        monthly_cost=4000,              # $4k monthly costs
        monthly_revenue_year1=6000,     # $6k monthly revenue
        revenue_growth_rate=0.12        # 12% annual growth
    )
    
    calc.print_report()


def scenario_conservative():
    """Conservative investment scenario."""
    print("\n" + "=" * 80)
    print("SCENARIO 3: Conservative Investment")
    print("=" * 80)
    
    calc = InvestmentCalculator(
        initial_investment=50000,      # $50k initial investment
        monthly_cost=3000,              # $3k monthly costs
        monthly_revenue_year1=4000,     # $4k monthly revenue
        revenue_growth_rate=0.08        # 8% annual growth (conservative)
    )
    
    calc.print_report()


def scenario_aggressive():
    """Aggressive growth scenario."""
    print("\n" + "=" * 80)
    print("SCENARIO 4: Aggressive Growth Strategy")
    print("=" * 80)
    
    calc = InvestmentCalculator(
        initial_investment=200000,     # $200k initial investment
        monthly_cost=30000,             # $30k monthly burn rate
        monthly_revenue_year1=25000,    # $25k MRR
        revenue_growth_rate=0.40        # 40% annual growth
    )
    
    calc.print_report()


def compare_scenarios():
    """Compare multiple scenarios side by side."""
    print("\n" + "=" * 80)
    print("SCENARIO COMPARISON")
    print("=" * 80)
    
    scenarios = [
        ("Conservative", 50000, 3000, 4000, 0.08),
        ("Moderate", 50000, 5000, 8000, 0.15),
        ("Aggressive", 50000, 8000, 12000, 0.25),
    ]
    
    print(f"\n{'Scenario':<15} {'Break-Even':<20} {'5-Year Profit':<20}")
    print("-" * 60)
    
    for name, init, cost, rev, growth in scenarios:
        calc = InvestmentCalculator(init, cost, rev, growth)
        summary = calc.get_summary()
        break_even = summary['break_even']
        
        if break_even:
            be_text = f"Year {break_even[0]}, Month {break_even[1]}"
        else:
            be_text = "Not reached"
        
        profit = summary['total_5year_profit']
        print(f"{name:<15} {be_text:<20} ${profit:>18,.2f}")


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print(" " * 25 + "INVESTMENT CALCULATOR EXAMPLES")
    print("=" * 80)
    
    scenario_startup()
    scenario_small_business()
    scenario_conservative()
    scenario_aggressive()
    compare_scenarios()
    
    print("\n" + "=" * 80)
    print("End of Examples")
    print("=" * 80 + "\n")
