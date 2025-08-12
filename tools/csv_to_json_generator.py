import csv
import json
import argparse
import os

def csv_to_json(input_csv_path, en_output_json_path="en.json", de_output_json_path="de.json"):
    """
    Converts a 3-column CSV file into two JSON files.

    The first column of the CSV is used as the key for both JSON files.
    The second column is used as the value for the English JSON file (en.json).
    The third column is used as the value for the German JSON file (de.json).

    Args:
        input_csv_path (str): The path to the input CSV file.
        en_output_json_path (str): The desired path for the English JSON output file.
                                   Defaults to "en.json".
        de_output_json_path (str): The desired path for the German JSON output file.
                                   Defaults to "de.json".
    """
    en_data = {}
    de_data = {}

    try:
        with open(input_csv_path, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Skip header row if it exists (assuming the first row might be headers)
            # You might want to add a check here if headers are always present or not.
            # next(csv_reader, None) # Uncomment this line if you have a header row and want to skip it

            for i, row in enumerate(csv_reader):
                if len(row) < 3:
                    print(f"Skipping row {i+1} due to insufficient columns: {row}")
                    continue
                key = row[0]
                en_value = row[1]
                de_value = row[2]

                en_data[key] = en_value
                de_data[key] = de_value

        # Ensure output directories exist
        os.makedirs(os.path.dirname(en_output_json_path) or '.', exist_ok=True)
        os.makedirs(os.path.dirname(de_output_json_path) or '.', exist_ok=True)

        with open(en_output_json_path, mode='w', encoding='utf-8') as en_json_file:
            json.dump(en_data, en_json_file, indent=4, ensure_ascii=False)
        print(f"Successfully created English JSON file: {en_output_json_path}")

        with open(de_output_json_path, mode='w', encoding='utf-8') as de_json_file:
            json.dump(de_data, de_json_file, indent=4, ensure_ascii=False)
        print(f"Successfully created German JSON file: {de_output_json_path}")

    except FileNotFoundError:
        print(f"Error: The input CSV file '{input_csv_path}' was not found. Please check the path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert a 3-column CSV file into two JSON files (English and German)."
    )
    parser.add_argument(
        "input_csv",
        type=str,
        help="Path to the input CSV file."
    )
    parser.add_argument(
        "--en_output",
        type=str,
        default="en.json",
        help="Path for the English JSON output file (default: en.json)."
    )
    parser.add_argument(
        "--de_output",
        type=str,
        default="de.json",
        help="Path for the German JSON output file (default: de.json)."
    )

    args = parser.parse_args()

    csv_to_json(args.input_csv, args.en_output, args.de_output)
