def saveSubdomains(subDomainsDict):
    f = open("Subdomain_List.txt","w")
    for subDomain in sorted(subDomainsDict.keys()):
        f.write(f"{subDomain}, {subDomainsDict[subDomain]}\n")
    f.close()
