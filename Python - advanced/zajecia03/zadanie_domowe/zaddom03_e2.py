# Bartłomiej Janiszewski


def unikalne_adresy_ip():
    plik = open('apache_logs', mode='r')
    ip_log =[]
    for element in plik.readlines():
        element = element.split()
        element = element[0]
        ip_log.append(element)

    new_ip_log = list(set(ip_log))
    return new_ip_log


if __name__ == '__main__':
    print(unikalne_adresy_ip())
