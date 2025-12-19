import pandas as pd
from io import StringIO

data = """Date\tRegion\tProduct\tQuantity\tUnit_Price\tSales_Person
9/27/2024\tWest\tGadget\t11\t38.74\tBob
2/24/2024\tNorth\tWidget\t16\t81.99\tAlice
8/6/2024\tSouth\tThingamajig\t10\t23\tDiana
12/22/2024\tSouth\tWidget\t16\t60.85\tCharlie
12/13/2024\tWest\tGadget\t17\t39.9\tFrank
4/17/2024\tNorth\tDoohickey\t11\t81.11\tDiana
8/13/2024\tNorth\tThingamajig\t14\t17.05\tDiana
10/27/2024\tWest\tDoohickey\t13\t29.53\tBob
8/11/2024\tEast\tGadget\t1\t79.44\tFrank
10/14/2024\tEast\tThingamajig\t13\t60.14\tFrank
4/22/2024\tSouth\tDoohickey\t16\t73.63\tCharlie
1/5/2024\tEast\tDoohickey\t3\t40.73\tFrank
1/7/2024\tNorth\tThingamajig\t18\t67.1\tBob
12/23/2024\tSouth\tThingamajig\t17\t99.26\tFrank
10/25/2024\tEast\tGadget\t20\t92.85\tCharlie
7/26/2024\tEast\tWidget\t20\t39.89\tBob
11/21/2024\tSouth\tGadget\t9\t48.23\tCharlie
7/18/2024\tNorth\tWidget\t12\t48.46\tEve
11/20/2024\tWest\tDoohickey\t17\t31.31\tFrank
7/9/2024\tNorth\tThingamajig\t16\t74.67\tFrank
3/21/2024\tNorth\tGadget\t5\t24.44\tFrank
7/31/2024\tNorth\tThingamajig\t11\t91.91\tCharlie
8/27/2024\tWest\tGadget\t10\t97.21\tBob
8/30/2024\tSouth\tDoohickey\t3\t79.26\tCharlie
8/25/2024\tSouth\tGadget\t15\t74.31\tEve
8/22/2024\tSouth\tGadget\t6\t83.05\tBob
9/27/2024\tSouth\tDoohickey\t14\t18.93\tEve
4/15/2024\tSouth\tWidget\t17\t70.31\tCharlie
10/20/2024\tNorth\tThingamajig\t14\t19.42\tAlice
5/13/2024\tSouth\tDoohickey\t15\t66.97\tFrank
11/16/2024\tNorth\tThingamajig\t18\t26.25\tAlice
9/5/2024\tNorth\tWidget\t10\t19.95\tCharlie
6/30/2024\tWest\tThingamajig\t5\t87.48\tDiana
4/18/2024\tSouth\tDoohickey\t20\t17.92\tEve
9/29/2024\tEast\tThingamajig\t19\t24.83\tEve
8/2/2024\tSouth\tDoohickey\t13\t81.86\tFrank
4/6/2024\tSouth\tDoohickey\t11\t74.65\tEve
12/13/2024\tNorth\tThingamajig\t7\t97.05\tBob
8/1/2024\tSouth\tWidget\t9\t24.74\tDiana
3/24/2024\tNorth\tThingamajig\t15\t71.67\tFrank
8/10/2024\tNorth\tThingamajig\t13\t38.52\tDiana
11/30/2024\tNorth\tWidget\t11\t45.61\tCharlie
1/10/2024\tSouth\tThingamajig\t5\t81.78\tAlice
7/16/2024\tNorth\tWidget\t15\t88.89\tDiana
11/16/2024\tNorth\tThingamajig\t7\t15.56\tFrank
10/15/2024\tNorth\tThingamajig\t3\t66.41\tFrank
7/5/2024\tNorth\tDoohickey\t11\t96.4\tDiana
2/15/2024\tEast\tGadget\t17\t96.6\tCharlie
10/25/2024\tNorth\tDoohickey\t7\t45.63\tDiana
5/26/2024\tSouth\tDoohickey\t4\t25.15\tDiana"""

# Load into DataFrame
df = pd.read_csv(StringIO(data), sep='\t', parse_dates=['Date'])

# Display the first few rows
print(df.head())

df["Date"] = pd.to_datetime(df["Date"])

df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

sales_2024 = df[df["Date"].dt.year == 2024]
print("\nData_of_2024:")
print(sales_2024)

group = sales_2024.groupby(["Region", "Product"]).agg({"Total_Sales": "sum", "Quantity": "sum"}).reset_index()
print(group)

sales_by_per_person = df.groupby("Sales_Person")["Total_Sales"].sum().reset_index()
top_salesperson = sales_by_per_person.sort_values(by="Total_Sales", ascending=False).head(1)
print("Top Salesperson:")
print(top_salesperson)