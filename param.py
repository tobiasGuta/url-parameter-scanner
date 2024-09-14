import sys
import re
from tqdm import tqdm
import time

# List of URLs and patterns to search for (excluding numbers)
parameters = [
    "/2wayvideochat/index.php?r=", "/elms/subscribe.php?course_id=", "/gen_confirm.php?errmsg=", 
    "/hexjector.php?site=", "/index.php?option=com_easygb&Itemid=", "/index.php?view=help&amp;faq=1&amp;ref=",
    "/index.php?view=help&faq=1&ref=", "/info.asp?page=fullstory&amp;key=1&amp;news_type=news&amp;onvan=",
    "/info.asp?page=fullstory&key=1&news_type=news&onvan=", "/main.php?sid=", "/news.php?id=",
    "/notice.php?msg=", "/preaspjobboard//Employee/emp_login.asp?msg1=", "/Property-Cpanel.html?pid=",
    "/schoolmv2/html/studentmain.php?session=", "/search.php?search_keywords=", "/ser/parohija.php?id=", 
    "/showproperty.php?id=", "/site_search.php?sfunction=", "/strane/pas.php?id=", "/vehicle/buy_do_search/?order_direction=",
    "/view.php?PID=", "/winners.php?year=2008&amp;type=", "/winners.php?year=2008&type=",
    "index.php?option=com_reservations&amp;task=askope&amp;nidser=2&amp;namser=", 
    "index.php?option=com_reservations&task=askope&nidser=2&namser=", "intext:”Website by Mile High Creative”",
    "inurl:”.php?author=”", "inurl:”.php?cat=”", "inurl:”.php?cmd=”", "inurl:”.php?feedback=”",
    "inurl:”.php?file=”", "inurl:”.php?from=”", "inurl:”.php?keyword=”", "inurl:”.php?mail=”",
    "inurl:”.php?max=”", "inurl:”.php?pass=”", "inurl:”.php?q=”", "inurl:”.php?query=”", 
    "inurl:”.php?search=”", "inurl:”.php?searchstring=”", "inurl:”.php?searchst­ring=”", "inurl:”.php?tag=”",
    "inurl:”.php?txt=”", "inurl:”.php?vote=”", "inurl:”.php?years=”", "inurl:”.php?z=”", 
    "inurl:”contentPage.php?id=”", "inurl:”displayResource.php?id=”", "inurl:.com/search.asp", 
    "inurl:/poll/default.asp?catid=", "inurl:/products/classified/headersearch.php?sid=",
    "inurl:/products/orkutclone/scrapbook.php?id=", "inurl:/search_results.php?search=", 
    "inurl:/­search_results.php?se­arch=", "inurl:/search_results.php?search=Search&amp;k=",
    "inurl:/search_results.php?search=Search&k=", "inurl:”contentPage.php?id=”", "inurl:”displayResource.php?id=”", 
    "inurl:com_feedpostold/feedpost.php?url=", "inurl:headersearch.php?sid=", "inurl:scrapbook.php?id=", 
    "inurl:search.php?q=", "pages/match_report.php?mid=", "/?s=", "/search?q=", "/index.php?lang=", 
    "/pplay/info_prenotazioni.asp?immagine=", "/shared/lgflsearch.php?terms=", "/index.php?page=", 
    "/search?query=", "/en/Telefon-Cam?search=", "/index.php?bukva=", "/pro/events_print_setup.cfm?list_type=", 
    "/pro/events_print_setup.cfm?categoryid=", "/pro/events_print_setup.cfm?categoryid2=", "/?eventSearch=", 
    "/?startTime=", "/pro/events_ical.cfm?categoryids=", "/pro/events_ical.cfm?categoryids2=", 
    "/pro/events_print_setup.cfm?month=", "/pro/events_print_setup.cfm?year=", "/pro/events_print_setup.cfm?begindate=", 
    "/pro/events_print_setup.cfm?enddate=", "/search?keyword=", "/?q=", "/search/?q=", "/index.php?pn=", 
    "/?lang=", "/property/search?uid=", "/index.php?id=", "/search?orgId=", "/products?handler=", 
    "/pro/events_print_setup.cfm?view=", "/pro/events_print_setup.cfm?keywords=", "/?p=", 
    "/search.php?q=", "/?search=", "/pro/minicalendar_detail.cfm?list_type=", "/index.php?produkti_po_cena=", 
    "/index.php?produkti_po_ime=", "/servlet/com.jsbsoft.jtf.core.SG?CODE=", "/login?redirect_uri=", 
    "/connexion?redirect_uri=", "/index.php?action=", "/plugins/actu/listing_actus-front.php?id_site=", 
    "/index.php?mebel_id=", "/search/?search=", "/news/class/index.php?myshownums=", "/news/class/index.php?myord=", 
    "/search.html?searchScope=", "/search?field%5B%5D=", "/videos?tag=", "/videos?place=", "/videos?search=", 
    "/?email=", "/?cat=", "/content.php?expand=", "/?page=", "/search/?s=", "/?keywords=", "/search/?keyword=", 
    "/apps/email/index.jsp?n=", "/?name=", "/?sort=", "/search?search=", "/pro/minicalendar_print_setup.cfm?begindate=", 
    "/pro/minicalendar_print_setup.cfm?enddate=", "/pro/minicalendar_print_setup.cfm?keywords=", "/search-results?q=", 
    "/?listingtypeid=", "/search?s=", "/pro/minicalendar_print_setup.cfm?categoryid2=", "/?bathrooms=", 
    "/?listingagent=", "/?featuredsearchseourl=", "/?squarefeet=", "/?siteid=", "/?bedrooms=", 
    "/?featuredsearch=", "/?price=", "/?maxbuilt=", "/?lsid=", "/?listingtypes=", "/?garages=", 
    "/?maxprice=", "/?minprice=", "/?keywordsany=", "/?yearbuilt=", "/?minbuilt=", "/?subdivision=", 
    "/?lotsizeval=", "/?listingstatusid=", "/?mls=", "/firms/?text=", "/servlet/com.jsbsoft.jtf.core.SG?OBJET=", 
    "/plan_du_site.php?lang=", "/index.php?Itemid=", "/?view=", "/?t=", "/?selat=", "/?selong=", "/?nwlat=", "/?geo="
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
