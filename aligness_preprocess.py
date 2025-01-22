import pandas as pd
import sys

def process_ec_data(input_filepath, output_filepath):
    """
    Processes EC data from a TSV file and writes the results to a text file.

    Args:
        input_filepath (str): Path to the input TSV file.
        output_filepath (str): Path to the output text file.
    """

    # Read and prepare output of picrust
    function_per_species_df = pd.read_csv(input_filepath, sep="\t")
    d = function_per_species_df.drop("sequence", axis=1)
    d = d.to_numpy()

    # Get strings in the format aligness takes it - at depth of 3 EC numbers eg 2.1.3
    function_per_species_dict = {}
    for i in range(len(function_per_species_df)):
        func_str_list = []
        for j in range(len(function_per_species_df.columns[1:])):
            if d[i][j] > 0:
                s = function_per_species_df.columns[1:][j]
                l0, l1, l2, l3 = s.split(".")
                func_str = l0[-1] + "." + l1 + "." + l2
                func_str_list.append(func_str)

        all_func_str = ""
        for funcs in list(set(func_str_list)):
            all_func_str += funcs
            all_func_str += ":"
        function_per_species_dict[function_per_species_df["sequence"][i]] = all_func_str

    # Combine into a single string
    ec_strings = []
    for s in list(function_per_species_dict.values()):
        s = s[:-1]
        ec_strings.append(s)

    # Write strings into txt file with strings of each species in a new line
    with open(output_filepath, mode="w", encoding="utf-8") as myfile:
        for i in range(len(ec_strings)):
            item = ec_strings[i]
            sp_id = function_per_species_df["sequence"][i]
            myfile.write(f"{sp_id}\t{item}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_filepath> <output_filepath>")
        sys.exit(1)

    input_filepath = sys.argv[1]
    output_filepath = sys.argv[2]
    process_ec_data(input_filepath, output_filepath)
