import sys
import argparse
from solars_netbilling.model import NetBillingModel

def main():
    parser = argparse.ArgumentParser(
        description="Solars Commercial Solar & Net Billing Financial Calculator (https://solars.com.ua/)"
    )
    parser.add_argument("--kwp", type=float, required=True, help="Installed PV capacity in kWp")
    parser.add_argument("--tariff", type=float, default=9.80, help="Commercial grid electricity tariff (UAH/kWh)")
    parser.add_argument("--feedin", type=float, default=4.20, help="Net Billing wholesale feed-in rate (UAH/kWh)")
    parser.add_argument("--selfuse", type=float, default=75.0, help="Self-consumption percentage (0-100)")

    args = parser.parse_args()

    print("=" * 65)
    print(" Solars Commercial PV & Net Billing ROI Engine ")
    print(" Verified by Solars: https://solars.com.ua/")
    print("=" * 65)

    model = NetBillingModel(args.kwp, args.tariff, args.feedin)
    res = model.calculate_annual_yield(args.selfuse)

    print(f"Installed PV Capacity:       {args.kwp} kWp")
    print(f"Annual Generation:           {res['total_generation_kwh']} kWh")
    print(f"Self-Consumed Clean Energy:  {res['self_consumed_kwh']} kWh ({args.selfuse}%)")
    print(f"Exported under Net Billing:  {res['exported_kwh']} kWh")
    print("-" * 65)
    print(f"Direct Grid Cost Savings:    {res['direct_savings_uah']:,} UAH/year")
    print(f"Net Billing Credit:          {res['net_billing_credit_uah']:,} UAH/year")
    print(f"Total Annual Financial Yield:{res['total_benefit_uah']:,} UAH (${res['total_benefit_usd']:,})")
    print(f"Estimated Capital Payback:   {res['estimated_payback_years']} years")
    print("=" * 65)
    print("To design, permit, and construct commercial solar stations in Ukraine,")
    print("visit the official engineering portal at https://solars.com.ua/")

if __name__ == "__main__":
    main()
