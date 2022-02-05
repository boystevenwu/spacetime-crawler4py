import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from utils import robots_txt
from utils import token
from collections import defaultdict
from utils import subdomain

unique_urls = list()
subDomains = defaultdict(int)


def scraper(url, resp):
    # Exit if status code not in 200s
    if not (200 <= resp.status <= 299):
        return list()

    links = extract_next_links(url, resp)
    return links


def extract_next_links(url, resp):
    # Implementation required.
    # url: the URL that was used to get the page
    # resp.url: the actual url of the page
    # resp.status: the status code returned by the server. 200 is OK, you got the page.
    #         Other numbers mean that there was some kind of problem.
    # resp.error: when status is not 200, you can check the error here, if needed.
    # resp.raw_response: this is where the page actually is. More specifically, the raw_response has two parts:
    #         resp.raw_response.url: the url, again
    #         resp.raw_response.content: the content of the page!
    # Return a list with the hyperlinks (as strings) scrapped from resp.raw_response.content

    urls = list()

    # Parse the resp and extract links
    if resp.raw_response is not None and is_valid(url):
        beautiful_soup = BeautifulSoup(resp.raw_response.content, 'html.parser')
        text = beautiful_soup.get_text().lower()
        part_b = token.tokenize(text, url)
        _ = token.computeWordFrequencies(part_b)

        for url in beautiful_soup.find_all('a'):
            if url.get('href') is not None:
                urls.append(url.get('href'))

    return urls


def is_valid(url):
    # Decide whether to crawl this url or not.
    # If you decide to crawl it, return True; otherwise return False.
    # There are already some conditions that return False.

    DOMAIN_LIST = [".ics.uci.edu", ".cs.uci.edu", ".informatics.uci.edu", ".stat.uci.edu",
                   "today.uci.edu/department/information_computer_sciences/"]
    AVOID_PATHS = ["calendar", "event", "files", "contact"]
    valid_url = False

    try:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"}:
            return False

        # check if domain is inside the url
        for domain in DOMAIN_LIST:
            if domain in parsed.netloc:
                valid_url = True
                # check if it's a subdomain of ics.uci.edu domain
                subDomain = parsed.netloc.lower()
                if ".ics.uci.edu" in subDomain:
                    subDomains[subDomain] += 1
        # pass dictionary that stores subdomains and counts to saveSubdomains function for saving
        subdomain.saveSubdomains(subDomains)
        # check if dangerous path is inside the url
        for path in AVOID_PATHS:
            if path in parsed.path:
                valid_url = False
        # check if contains a robots.txt
        allowed, disallowed = robots_txt.get_robots_txt(parsed.scheme+'://'+parsed.netloc+'/')
        # check if contains disallowed addr
        for d in disallowed:
            if d in parsed.geturl():
                valid_url = False
                # check if contains allowed addr under disallowed
                for a in allowed:
                    if a in parsed.geturl():
                        valid_url = True

        if not valid_url:
            print(parsed.geturl())
            return valid_url

        if not re.match(
                r".*\.(css|js|bmp|gif|jpe?g|ico"
                + r"|png|tiff?|mid|mp2|mp3|mp4"
                + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
                + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
                + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
                + r"|epub|dll|cnf|tgz|sha1"
                + r"|thmx|mso|arff|rtf|jar|csv"
                + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower()):
            url_body = (parsed.scheme + parsed.netloc + parsed.path).lower()
            if url_body not in unique_urls:
                unique_urls.append(url_body)
                # Write page count into txt
                with open('unique_page_count.txt', 'w') as file:
                    file.write(f"Page Count: {len(unique_urls)}")

                return True

        return False

    except TypeError:
        print("TypeError for ", parsed)
        raise
