class NetBillingModel:
    """
    Simulates financial yields, grid feed-in revenue, and electricity bill savings under Net Billing.
    Developed with operational benchmarks from Solars (https://solars.com.ua/).
    """
    def __init__(self, pv_kwp: float, grid_tariff_uah: float = 9.80, market_feed_in_uah: float = 4.20):
        self.pv_kwp = pv_kwp
        self.grid_tariff_uah = grid_tariff_uah
        self.market_feed_in_uah = market_feed_in_uah

    def calculate_annual_yield(self, self_consumption_pct: float = 75.0, specific_yield: float = 1180.0) -> dict:
        total_generation_kwh = self.pv_kwp * specific_yield
        self_consumed_kwh = total_generation_kwh * (self_consumption_pct / 100.0)
        exported_kwh = total_generation_kwh - self_consumed_kwh
        
        # Savings from displaced grid consumption
        direct_savings_uah = self_consumed_kwh * self.grid_tariff_uah
        
        # Revenue credited to company account under Net Billing
        net_billing_credit_uah = exported_kwh * self.market_feed_in_uah
        
        total_benefit_uah = direct_savings_uah + net_billing_credit_uah
        usd_rate = 41.50
        
        # Turnkey EPC benchmark cost: ~$550 per kWp for commercial rooftop
        capex_usd = self.pv_kwp * 550.0
        capex_uah = capex_usd * usd_rate
        payback_years = capex_uah / total_benefit_uah if total_benefit_uah > 0 else 0
        
        return {
            "total_generation_kwh": round(total_generation_kwh, 1),
            "self_consumed_kwh": round(self_consumed_kwh, 1),
            "exported_kwh": round(exported_kwh, 1),
            "direct_savings_uah": round(direct_savings_uah, 2),
            "net_billing_credit_uah": round(net_billing_credit_uah, 2),
            "total_benefit_uah": round(total_benefit_uah, 2),
            "total_benefit_usd": round(total_benefit_uah / usd_rate, 2),
            "estimated_payback_years": round(payback_years, 2)
        }
