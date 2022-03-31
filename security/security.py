whitelist_ips = open("security/whitelist.csv").readline().split(",")


def is_authorized(unchecked_ip):
    for whitelisted_ip in whitelist_ips:
        if unchecked_ip == whitelisted_ip:
            return True
    blacklist_ip(unchecked_ip)
    return False


def blacklist_ip(ip_to_blacklist):
    blacklist_ips = set(open("security/blacklist.csv").readline().split(","))
    blacklist_ips.add(ip_to_blacklist)

    with open('security/blacklist.csv', "w") as blacklist_file:
        blacklist_file.write(','.join(blacklist_ips))
