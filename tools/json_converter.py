import pandas as pd
import json
import argparse
import os # Import os module for path manipulation

def json_to_csv(input_json_file, output_csv_file):
    """
    Converts a simple JSON file (no nesting) into a CSV file
    with 'Keys' and 'Values' columns.

    Args:
        input_json_file (str): The path to the input JSON file.
        output_csv_file (str): The path to the output CSV file.
    """
    try:
        with open(input_json_file, 'r') as f:
            data = json.load(f)

        if not isinstance(data, dict):
            raise TypeError("The JSON file does not contain a simple key-value structure.")

        rows = [{'Keys': key, 'Values': value} for key, value in data.items()]
        df = pd.DataFrame(rows)

        # Ensure the output directory exists
        output_dir = os.path.dirname(output_csv_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        df.to_csv(output_csv_file, index=False)
        print(f"✅ Successfully converted '{input_json_file}' to '{output_csv_file}'")

    except FileNotFoundError:
        print(f"❌ Error: The input file '{input_json_file}' was not found.")
    except json.JSONDecodeError:
        print(f"❌ Error: Could not decode JSON from '{input_json_file}'. Please ensure it's valid JSON.")
    except TypeError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert a simple JSON file to a two-column CSV (Keys, Values)."
    )

    parser.add_argument(
        "-i", "--input",
        type=str,
        required=True,
        help="Path to the input JSON file."
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        default="output.csv", # Default output file
        help="Path for the output CSV file. Defaults to 'output.csv'."
    )

    args = parser.parse_args()

    # Call the conversion function with arguments from the command line
    json_to_csv(args.input, args.output)
