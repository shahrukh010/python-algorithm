import pandas as pd;

file_path = "./file.xlsx"
data = pd.ExcelFile("file.xlsx")

for sheet_name in data.sheet_names:
  print(sheet_name)
  df = pd.read_excel(file_path,sheet_name=sheet_name);
  duplicate = df[df.duplicated()]
  if not  duplicate.empty:
    print("No duplicate found");
    print(duplicate)
  else:
    print("No duplicate found");
  break;
    
