import pandas as pd

# Step 1: Create DataFrame
df = pd.DataFrame({
    'CustomerID': [101, 101, 102, 102, 103, 104, 104, 104],
    'OrderID': [1, 2, 3, 4, 5, 6, 7, 8],
    'OrderDate': [
        '2023-01-01', '2023-01-05', '2023-02-01', '2023-01-15',
        '2023-02-10', '2023-03-01', '2023-03-25', '2023-04-01'
    ],
    'Amount': [250, 300, 150, 200, 180, 500, 100, 120]
})

# Step 2: Convert OrderDate column to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Step 3: Sort data — most recent first, then highest amount
df = df.sort_values(by=['CustomerID', 'OrderDate', 'Amount'], ascending=[True, False, False])

# Step 4: Drop duplicate customers (keeping their most recent order)
latest_orders = df.drop_duplicates(subset='CustomerID', keep='first')
print("\nLatest Order per Customer:\n", latest_orders)

# Step 5: Find customers with >1 order and total amount >400
customer_totals = df.groupby('CustomerID')['Amount'].agg(['count', 'sum'])
eligible_customers = customer_totals[(customer_totals['count'] > 1) & (customer_totals['sum'] > 400)]
print("\nCustomers with >1 order and total amount >400:\n", eligible_customers)

# Step 6: Running total of Amount for each customer, sorted by OrderDate
df = df.sort_values(by=['CustomerID', 'OrderDate'])
df['RunningTotal'] = df.groupby('CustomerID')['Amount'].cumsum()
print("\nRunning Total per Customer:\n", df[['CustomerID', 'OrderDate', 'Amount', 'RunningTotal']])

# Step 7: Total revenue per month
df['Month'] = df['OrderDate'].dt.to_period('M')
revenue_by_month = df.groupby('Month')['Amount'].sum()
print("\nTotal Revenue per Month:\n", revenue_by_month)

# Step 8: Rank orders by Amount for each customer (descending)
df['AmountRank'] = df.groupby('CustomerID')['Amount'].rank(method='dense', ascending=False)
print("\nRank of Amount per Customer:\n", df[['CustomerID', 'Amount', 'AmountRank']])

# Step 9: Create Pivot Table — Rows: CustomerID, Columns: Month, Values: Sum of Amount
pivot_table = pd.pivot_table(df, index='CustomerID', columns='Month', values='Amount', aggfunc='sum')
print("\nPivot Table:\n", pivot_table)

# Step 10: Calculate days between consecutive orders
df['DaysSinceLastOrder'] = df.groupby('CustomerID')['OrderDate'].diff().dt.days
print("\nDays Since Last Order:\n", df[['CustomerID', 'OrderDate', 'DaysSinceLastOrder']])

# Step 11: Group by CustomerID — total orders, average amount, std deviation
stats = df.groupby('CustomerID')['Amount'].agg(
    TotalOrders='count',
    AvgOrder='mean',
    StdOrder='std'
).reset_index()
print("\nCustomer Order Statistics:\n", stats)

# Step 12: Find orders where Amount > average amount for that customer
df = df.merge(stats[['CustomerID', 'AvgOrder']], on='CustomerID', how='left')
above_avg_orders = df[df['Amount'] > df['AvgOrder']]
print("\nOrders where Amount > Average for that Customer:\n", above_avg_orders[['CustomerID', 'OrderID', 'Amount', 'AvgOrder']])
