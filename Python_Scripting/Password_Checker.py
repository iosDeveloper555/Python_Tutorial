import requests
import hashlib


def request_api_data(query_data):
    url = "https://api.pwnedpasswords.com/range/" + query_data
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f" Error while fetching data {res.status_code} please try again.")

    return res


def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        # print(h, count)
        if h == hash_to_check:
            return count

    return 0


def password_check_api(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leak_count(response, tail)


def main(password):
    print("password: ", password)
    # for password in args:
    count = password_check_api(password)
    if count:
        print(f"{password} was found {count} times... you should change it.")
    else:
        print(f"{password} not found {count}. Go for it.")
    return "done!"


password = input("Inter your password to check = ")
main(password)
