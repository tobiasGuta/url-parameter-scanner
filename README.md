# url-parameter-scanner
A lightweight Python tool that scans a list of URLs and detects specific query parameters, designed for web scraping and cybersecurity purposes. This script searches through a provided text file containing URLs and identifies occurrences of predefined parameters, displaying the full URL when a match is found.

# Value for Bug Hunting:
In cybersecurity, URL parameters can often reveal vulnerabilities or interesting attack vectors, especially in scenarios like:

Insecure Direct Object References (IDOR): Parameters like id, uid, or pid could expose sensitive data or allow unauthorized access to certain resources.
SQL Injection Points: Parameters like search, q, s, page, and similar can be exploited for SQL injection vulnerabilities.
Cross-Site Scripting (XSS): Parameters such as search, q, and view are often passed directly into web pages, which makes them possible vectors for XSS attacks.
Parameter Tampering: Changing or adding certain parameters can allow a bug hunter to bypass security controls, access unauthorized resources, or modify application behavior.
This tool helps bug hunters easily identify URLs with these parameters, making it easier to assess the security posture of a web application. By filtering duplicate URLs with the same parameter, it also allows for focused testing.

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

    git clone https://github.com/tobiasGuta/url-parameter-scanner.git
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
if you want me to add more paramater let me know.
