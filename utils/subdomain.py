# check if it's a subdomain of ics.uci.edu domain
def saveSubdomains(subDomainsDict):
    f = open("subdomain_list.txt","w")
    for subDomain in sorted(subDomainsDict.keys()):
        f.write(f"{subDomain}, {subDomainsDict[subDomain]}\n")
    f.close()
