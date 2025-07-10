import pandas as pd

data = {
    "Name": ["Vibhor", "Ankit", "Rishabh"],
    "Age": ["29", "16", "12"],
    "City": ["Varanasi", "Dehradun", "Pune"]
}

df = pd.DataFrame(data)

print(df)

#df.to_csv("csv_output.csv", index=False)
#df.to_excel("xlsx_output.xlsx", index=False)
#df.to_json("json_output.json", index=False)
