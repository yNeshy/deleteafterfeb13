import requests

def create_loan(params):
    # fetching from this API takes some time.
    google_json = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=GOOG&apikey=X1AN6OR1Y3WI51E3").json()
    print()
    print(google_json)
    print("\n")
    return google_json

def delete_loan(params):
    print("boo")
    return {
        "result": 200,
        "boo": "boo"}

def loan_submission_failure(params):

    # pretend to send an email.
    print("Sending an email...")
    return {"result": 200}
