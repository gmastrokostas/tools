import sys
#Compare two files instead of using excel spreadsheet
file1 = input("Enter name of first file:  ")
file2 = input("Enter name of second file: ")

print(file1, file2)

if not file1.endswith('.csv') or not file2.endswith('.csv'):
    sys.exit("Exiting")

try:
    with open(file1) as f1, open(file2) as f2:
        for f in (f1,f2):
            for line in f:
                line=line.rstrip("\n")  
                if len(line.split()) > 1:
                    print("Exiting. Script is designed for one column comparison. Format cannot be processed")
                    raise SystemExit
                else:
                    set_f1=(set(f1))
                    set_f2=(set(f2))
                    result_common=set_f1.intersection(set_f2)
                    result_different=set_f1.difference(set_f2)
                    print("Common Elements between the two files")
                    print(result_common)
                    print("--------------------------")
                    print("Difference between the two files")
                    print(result_different)

            

except Exception as e:
    print(f"Error: {e}")
