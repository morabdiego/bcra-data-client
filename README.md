# BCRA Data Client (coming soon)


A Python client for accessing monetary statistics and foreign exchange data published by the Central Bank of Argentina (BCRA). Designed for economists, analysts, and developers working with macroeconomic data.

---

## 📦 Installation

Clone this repository and start exploring:

```bash
git clone https://github.com/morabdiego/bcra-data-client.git
cd bcra-data-client
```

Or (coming soon):
```bash
pip install bcra-data-client
```

---

## ✨ What you can do with it:

- Discover all official currencies and their codes.
- Fetch the latest exchange rates in one line of code.
- Check historical exchange rate trends for any currency.
- Get clean pandas DataFrames ready for analysis or visualization.
- Soon: integrate easily with Reflex apps for web-based dashboards.

---

## 🚀 Quick Start Examples

### List all official currencies:
```python
from bcra_data_client import maestros_divisas

currencies = maestros_divisas()
currencies.head()
```

### Get today’s exchange rates:
```python
from bcra_data_client import cotizaciones

latest_rates = cotizaciones()
latest_rates
```

### Get rates on a specific date:
```python
rates = cotizaciones(fecha="2024-03-15")
rates
```

### Explore historical trends (e.g., USD):
```python
from bcra_data_client import cotizaciones_moneda

usd_history = cotizaciones_moneda(
    moneda="USD",
    fecha_desde="2023-01-01",
    fecha_hasta="2024-01-01",
    limit=500
)
usd_history.head()
```

---

## 📊 Data Source

All data is retrieved from the official [BCRA Public API](https://www.bcra.gob.ar/BCRAyVos/estadisticas_cambiarias_api.asp).

---

## 🛠️ Coming Soon
- Reflex app examples to build interactive dashboards using this data.
- More convenience functions and visualizations.

---

## 👋 About Me

Hi! I’m Diego Mora — Economist, data analyst, and Python enthusiast.  
I build tools that make data exploration simpler and more enjoyable.

👉 [LinkedIn](https://www.linkedin.com/in/morabdiego) | [GitHub](https://github.com/morabdiego)

---

## 📜 License

This project is licensed under the [CC BY-NC 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/).  
Use it freely for non-commercial purposes — just don’t forget to give credit!

