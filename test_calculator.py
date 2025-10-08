#!/usr/bin/env python3
"""
Tests for the Investment Calculator
"""

import sys
from investment_calculator import InvestmentCalculator


def test_basic_calculations():
    """Test basic calculation functionality."""
    print("Testing basic calculations...")
    
    calc = InvestmentCalculator(
        initial_investment=10000,
        monthly_cost=1000,
        monthly_revenue_year1=1500,
        revenue_growth_rate=0.1
    )
    
    # Test yearly costs
    costs = calc.calculate_yearly_costs()
    assert len(costs) == 5, "Should have 5 years of costs"
    assert costs[0] == 22000, f"Year 1 should include initial investment: expected 22000, got {costs[0]}"
    assert costs[1] == 12000, f"Year 2 should be monthly costs only: expected 12000, got {costs[1]}"
    
    # Test yearly revenue
    revenues = calc.calculate_yearly_revenue()
    assert len(revenues) == 5, "Should have 5 years of revenue"
    assert revenues[0] == 18000, f"Year 1 revenue: expected 18000, got {revenues[0]}"
    # Year 2 should be 10% more
    assert abs(revenues[1] - 19800) < 1, f"Year 2 revenue: expected ~19800, got {revenues[1]}"
    
    print("✓ Basic calculations passed")


def test_break_even():
    """Test break-even calculation."""
    print("Testing break-even calculation...")
    
    # Scenario that breaks even quickly
    calc1 = InvestmentCalculator(
        initial_investment=5000,
        monthly_cost=1000,
        monthly_revenue_year1=2000,
        revenue_growth_rate=0.1
    )
    
    break_even = calc1.find_break_even()
    assert break_even is not None, "Should find break-even point"
    year, month = break_even
    assert year == 1, f"Should break even in year 1, got year {year}"
    assert month == 5, f"Should break even at month 5, got month {month}"
    
    # Scenario that doesn't break even
    calc2 = InvestmentCalculator(
        initial_investment=100000,
        monthly_cost=5000,
        monthly_revenue_year1=1000,
        revenue_growth_rate=0.05
    )
    
    break_even2 = calc2.find_break_even()
    assert break_even2 is None, "Should not break even in 5 years with poor revenue"
    
    print("✓ Break-even calculations passed")


def test_profit_calculations():
    """Test profit and cumulative profit calculations."""
    print("Testing profit calculations...")
    
    calc = InvestmentCalculator(
        initial_investment=10000,
        monthly_cost=2000,
        monthly_revenue_year1=3000,
        revenue_growth_rate=0.2
    )
    
    profits = calc.calculate_yearly_profit()
    assert len(profits) == 5, "Should have 5 years of profit"
    
    # Year 1: Revenue (3000 * 12 = 36000) - Costs (10000 + 2000 * 12 = 34000) = 2000
    assert profits[0] == 2000, f"Year 1 profit: expected 2000, got {profits[0]}"
    
    cumulative = calc.calculate_cumulative_profit()
    assert len(cumulative) == 5, "Should have 5 years of cumulative profit"
    assert cumulative[0] == profits[0], "First cumulative should equal first profit"
    assert cumulative[4] == sum(profits), "Last cumulative should equal sum of all profits"
    
    print("✓ Profit calculations passed")


def test_summary():
    """Test summary generation."""
    print("Testing summary generation...")
    
    calc = InvestmentCalculator(
        initial_investment=20000,
        monthly_cost=3000,
        monthly_revenue_year1=5000,
        revenue_growth_rate=0.15
    )
    
    summary = calc.get_summary()
    
    assert 'initial_investment' in summary
    assert 'yearly_data' in summary
    assert 'break_even' in summary
    assert 'total_5year_profit' in summary
    
    assert len(summary['yearly_data']) == 5
    assert summary['initial_investment'] == 20000
    
    for year_data in summary['yearly_data']:
        assert 'year' in year_data
        assert 'costs' in year_data
        assert 'revenue' in year_data
        assert 'profit' in year_data
        assert 'cumulative_profit' in year_data
    
    print("✓ Summary generation passed")


def test_scalable_income():
    """Test that revenue scales correctly over time."""
    print("Testing scalable income...")
    
    calc = InvestmentCalculator(
        initial_investment=0,
        monthly_cost=1000,
        monthly_revenue_year1=2000,
        revenue_growth_rate=0.5  # 50% growth for easy testing
    )
    
    revenues = calc.calculate_yearly_revenue()
    
    # Year 1: 2000 * 12 = 24000
    assert revenues[0] == 24000, f"Year 1: expected 24000, got {revenues[0]}"
    
    # Year 2: 2000 * 1.5 * 12 = 36000
    assert revenues[1] == 36000, f"Year 2: expected 36000, got {revenues[1]}"
    
    # Year 3: 2000 * 1.5^2 * 12 = 54000
    assert revenues[2] == 54000, f"Year 3: expected 54000, got {revenues[2]}"
    
    print("✓ Scalable income passed")


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("Running Investment Calculator Tests")
    print("=" * 60 + "\n")
    
    try:
        test_basic_calculations()
        test_break_even()
        test_profit_calculations()
        test_summary()
        test_scalable_income()
        
        print("\n" + "=" * 60)
        print("✓ ALL TESTS PASSED")
        print("=" * 60 + "\n")
        return 0
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}\n")
        return 1
    except Exception as e:
        print(f"\n✗ ERROR: {e}\n")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
