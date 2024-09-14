# url-parameter-scanner
A lightweight Python tool that scans a list of URLs and detects specific query parameters, designed for web scraping and cybersecurity purposes. This script searches through a provided text file containing URLs and identifies occurrences of predefined parameters, displaying the full URL when a match is found.

# Features:
    Efficient Scanning: Uses tqdm for real-time progress display while scanning through thousands of URLs.
    Duplicate Filtering: Avoids displaying the same URL with identical parameters multiple times, but allows different parameters for the same base URL.
    Customizable Parameter List: Easily extend the list of query parameters to search for by modifying the parameters list in the script.
    Clear Output: Displays matching URLs with simple, elegant notifications and keeps track of progress.
    
# Example:
    $ python3 param.py endpoints.txt
    
    🔍 Searching for parameters in the file...
  
    👍 Found parameter: https://crossfeed.cyber.dhs.gov/saved-searches/?page=
    👍 Found parameter: https://esta.cbp.dhs.gov/?lang=da
    👍 Found parameter: https://tripwire.dhs.gov/?q=user/login/
    👍 Found parameter: https://studyinthestates.dhs.gov/?p=8370
    👍 Found parameter: https://studyinthestates.dhs.gov/?q=conference+circuit
    
    Scanning lines: 100%|███████████████████████████████▉ | 500000/500000 [00:12<00:00, 40000.00line/s]
    
    🎉 Total parameters found: 5

# Usage:

Clone the repository:

    git clone https://github.com/your-username/url-parameter-scanner.git
    cd url-parameter-scanner
    
Install the required Python libraries:

    pip install tqdm
    
Prepare a text file (endpoints.txt) with the list of URLs to scan.

Run the script:

    python3 param.py endpoints.txt
    
# Customization:

You can modify the parameters list inside the script to add or remove query parameters based on your specific use case.

# Contributions:
Feel free to submit issues or pull requests if you would like to improve the tool or report any bugs.
