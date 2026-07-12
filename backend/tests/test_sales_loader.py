from app.tools.sales_loader import load_sales

sales = load_sales()

print(len(sales))
print(sales[0])