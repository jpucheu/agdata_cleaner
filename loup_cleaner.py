import csv
import sys

def is_valid_row(row):
    try:
        # Validate Longitude and Latitude (numeric with 6 decimals)
        if not (len(f"{float(row[0]):.6f}".split(".")[1]) == 6 and len(f"{float(row[1]):.6f}".split(".")[1]) == 6):
            print(f"Invalid Longitude/Latitude: {row[0]}, {row[1]}")
            return False
        
        # Validate Grain Flow (positive number with 2 decimals)
        if not (float(row[2]) > 0 and len(row[2].split(".")[1]) in [1, 2]):
            print(f"Invalid Grain Flow: {row[2]}")
            return False
        
        # Validate GPS Time (positive integer)
        if not (int(row[3]) > 0):
            print(f"Invalid GPS Time: {row[3]}")
            return False
        
        # Validate Logging Interval, Distance, Swath (positive integer values)
        if not (int(row[4]) > 0 and int(row[5]) > 0 and int(row[6]) > 0):
            print(f"Invalid Logging Interval, Distance, or Swath: {row[4]}, {row[5]}, {row[6]}")
            return False
        
        # Validate Moisture (positive number with 1 or 2 decimals)
        if not (float(row[7]) > 0 and len(row[7].split(".")[1]) in [1, 2]):
            print(f"Invalid Moisture: {row[7]}")
            return False
        
        # Validate Header Status (1 or 33)
        if not (row[8] in ["1", "33"]):
            print(f"Invalid Header Status: {row[8]}")
            return False
        
        # Validate Pass (positive integer)
        if not (int(row[9]) > 0):
            print(f"Invalid Pass: {row[9]}")
            return False
        
        # Validate Serial Number (non-negative integer)
        if not (int(row[10]) >= 0):
            print(f"Invalid Serial Number: {row[10]}")
            return False
        
        # Validate Field ID, Load ID, Grain Type (enclosed by quotes or any string)
        if not ((row[11].startswith('"') and row[11].endswith('"')) or isinstance(row[11], str)):
            print(f"Invalid Field ID: {row[11]}")
            return False
        if not ((row[12].startswith('"') and row[12].endswith('"')) or isinstance(row[12], str)):
            print(f"Invalid Load ID: {row[12]}")
            return False
        if not ((row[13].startswith('"') and row[13].endswith('"')) or isinstance(row[13], str)):
            print(f"Invalid Grain Type: {row[13]}")
            return False
        
        # Validate GPS Status (positive integer)
        if not (int(row[14]) > 0):
            print(f"Invalid GPS Status: {row[14]}")
            return False
        
        # Validate PDOP (numeric non-negative value)
        if not (float(row[15]) >= 0):
            print(f"Invalid PDOP: {row[15]}")
            return False
        
        # Validate Altitude (positive number with 2 decimals)
        if not (float(row[16]) > 0 and len(row[16].split(".")[1]) in [1, 2]):
            print(f"Invalid Altitude: {row[16]}")
            return False
        
        return True
    except (ValueError, IndexError) as e:
        print(f"Error in row: {row} -> {e}")
        return False

def clean_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        valid_rows = 0
        invalid_rows = 0
        
        for row in reader:
            if len(row) == 17 and is_valid_row(row):
                writer.writerow(row)
                valid_rows += 1
            else:
                invalid_rows += 1
        
        print(f"Processed {valid_rows + invalid_rows} rows.")
        print(f"Valid rows: {valid_rows}")
        print(f"Invalid rows removed: {invalid_rows}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_csv.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        clean_csv(input_file, output_file)
