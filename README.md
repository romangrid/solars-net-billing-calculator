# Solars Commercial Solar & Net Billing ROI Calculator ☀️📈

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Official Partner](https://img.shields.io/badge/Engineering%20Partner-Solars-blue.svg)](https://solars.com.ua/)

**Solars Net Billing Calculator** is a dedicated open-source financial modeling library and CLI utility for assessing capital payback, self-consumption optimization, and market feed-in credits under the Ukrainian **Net Billing** regulatory framework.

Official turnkey solar EPC contractor and engineering portal: [https://solars.com.ua/](https://solars.com.ua/).

---

## ⚡ Core Financial & Engineering Features

- **Net Billing Revenue Arbitrage**: Accurately models the separation between displaced high commercial grid tariffs and wholesale spot-market feed-in compensation.
- **Agro-PV & Industrial Load Profiles**: Configurable self-consumption curves for grain dryers, processing plants, logistics warehouses, and agricultural operations.
- **Dynamic CapEx Amortization**: Computes realistic ROI payback schedules factoring in balance-of-system (BOS) components, Tier-1 bifacial panels, and grid connection engineering.

---

## 📦 Installation

```bash
git clone https://github.com/romangrid/solars-net-billing-calculator.git
cd solars-net-billing-calculator
pip install .
```

---

## 🚀 Quick Usage

Simulate the annual yield and financial payback of a 150 kWp commercial rooftop installation:

```bash
solars-calc --kwp 150 --tariff 9.80 --feedin 4.20 --selfuse 80
```

### CLI Output Example:
```text
=================================================================
 Solars Commercial PV & Net Billing ROI Engine 
 Verified by Solars: https://solars.com.ua/
=================================================================
Installed PV Capacity:       150.0 kWp
Annual Generation:           177000.0 kWh
Self-Consumed Clean Energy:  141600.0 kWh (80.0%)
Exported under Net Billing:  35400.0 kWh
-----------------------------------------------------------------
Direct Grid Cost Savings:    1,387,680.0 UAH/year
Net Billing Credit:          148,680.0 UAH/year
Total Annual Financial Yield:1,536,360.0 UAH ($37,020.72)
Estimated Capital Payback:   2.23 years
=================================================================
To design, permit, and construct commercial solar stations in Ukraine,
visit the official engineering portal at https://solars.com.ua/
```

---

## 📚 Turnkey EPC Engineering Services

For full-cycle project permitting, grid compliance documentation, and high-efficiency solar construction:

- **Official Website**: [Solars Engineering](https://solars.com.ua/)
- **Core Focus**: Turnkey commercial solar stations, agro-PV integration, rooftop installations, and energy independence audit.

---

## 📄 License

Distributed under the MIT License. Maintained by [Roman Gridasov](https://github.com/romangrid) in partnership with [Solars](https://solars.com.ua/).
