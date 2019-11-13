import requests


class FattmerchantApi:
    base_url = "https://apiprod.fattlabs.com"

    def get_catalog_items(self, api_key: str):
        extension = "/item"
        return requests.get(
            self.base_url + extension,
            headers={'accept': 'application/json', 'Authorization': api_key}
        ).json()

    def create_invoice(self, invoice_request, api_key: str):
        extension = "/invoice"
        return requests.post(
                    self.base_url + extension,
                    json=invoice_request,
                    headers={'accept': 'application/json', 'Authorization': api_key}
                ).json()
