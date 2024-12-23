import sys
import re
from tqdm import tqdm
import time

# List of URLs and patterns to search for (excluding numbers) (change it if needed)
parameters = [
    "?message=", 
]

# Function to search for specific parameters in a text file and show the full matching URL
def search_parameters(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()

            print("\n🔍 Searching for parameters in the file...\n")
            time.sleep(0.5)  # Pause to simulate animation start

            found_count = 0
            found_urls = {}

            # Adjusting tqdm parameters for better display
            for line in tqdm(content, desc="Scanning lines", unit="line", colour="cyan", ncols=100, mininterval=0.1):
                url = line.strip()
                for param in parameters:
                    if param in url:
                        # Extract URL up to the parameter to track uniqueness
                        base_url = url.split(param)[0]
                        param_url_combo = f"{base_url}{param}"

                        # Avoid printing the same URL and parameter combination more than once
                        if param_url_combo not in found_urls:
                            found_urls[param_url_combo] = True
                            time.sleep(0.05)  # Slight delay for each found parameter
                            found_count += 1
                            tqdm.write(f"👍 Found parameter: {url}")

            if found_count == 0:
                tqdm.write("\nNo parameters found in the file.")
            else:
                tqdm.write(f"\n🎉 Total parameters found: {found_count}")

    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python param.py <file_path>")
    else:
        search_parameters(sys.argv[1])
