"""
                         Count IP Addresses

Implement a function that receives two IPv4 addresses, and returns the
number of addresses between them (including the first one, excluding the last one).
All inputs will be valid IPv4 addresses in the form of strings.
The last address will always be greater than the first one.

Examples

ips_between("10.0.0.0", "10.0.0.50")  ==   50
ips_between("10.0.0.0", "10.0.1.0")   ==  256
ips_between("20.0.0.10", "20.0.1.0")  ==  246
"""

ip2 = []

def minus_pos(pos):
    global ip2
    if not ip2[pos]:
        if not ip2[pos - 1]:
            ip2[pos - 2] -= 1
            ip2[pos - 1] = 254
            ip2[pos] = 254
        else:
            ip2[pos - 1] -= 1
            ip2[pos] = 254
    else:
        ip2[pos] -= 1


def ips_between(start, end):
    global ip2
    ip1 = list(map(lambda x: int(x), start.split(".")))
    ip2 = list(map(lambda x: int(x), end.split(".")))
    digit = 0
    raznost = 0
    pos = 0
    for i in range(3, -1, -1):
        if ip1[i] != ip2[i]:
            if ip1[i] > ip2[i]:
                raznost += ((256 + ip2[i]) - ip1[i]) * 256 ** (3 - i)
                minus_pos(i - 1)
            elif ip1[i] < ip2[i]:
                raznost += (ip2[i] - ip1[i]) * 256 ** (3 - i)
    return raznost


def print_count_ip_adresses():
    print("\n", "-" * 40)
    print("\t\tTask2: Count IP Addresses - 5kuy")
    print("35.185.28.197 and 39.63.49.42, Expecting:{}".format(
          ips_between("35.185.28.197", "39.63.49.42")))
    print("66.193.248.193 and 71.175.252.40, Expecting:{}".format(
          ips_between("66.193.248.193", "71.175.252.40")))
    print("80.90.112.30 and 255.255.255.255, Expecting:{}".format(
          ips_between("80.90.112.30", "255.255.255.255")))
    print("107.155.161.19 and 107.155.161.112, Expecting:{}".format(
        ips_between("107.155.161.19", "107.155.161.112")))
    print("61.124.191.224 and 61.124.191.229, Expecting:{}".format(
        ips_between("61.124.191.224", "61.124.191.229")))
    print("-" * 40)



























