import requests

def create_loan(params):
    google_json = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=GOOG&apikey=X1AN6OR1Y3WI51E3").json()
    print(google_json)
    return google_json

def delete_loan(params):
    print("boo")
    return {
        "result": 200,
        "boo": "boo"}

def loan_submission_failure(params):
    print("Sending an email...")
    return {"result": 200}