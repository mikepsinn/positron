import requests


class GitHubAPI:
    def __init__(self, token):
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"token {token}"}

    def get_data(self, url):
        response = requests.get(f"{self.base_url}/{url}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_issue(self, repo, title, body):
        url = f"repos/{repo}/issues"
        data = {"title": title, "body": body}
        response = requests.post(f"{self.base_url}/{url}", headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def manage_issue(self, repo, issue_number, action):
        url = f"repos/{repo}/issues/{issue_number}"
        data = {"state": action}
        response = requests.patch(f"{self.base_url}/{url}", headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def create_pull_request(self, repo, title, body, head, base):
        url = f"repos/{repo}/pulls"
        data = {"title": title, "body": body, "head": head, "base": base}
        response = requests.post(f"{self.base_url}/{url}", headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def manage_pull_request(self, repo, pull_number, action):
        url = f"repos/{repo}/pulls/{pull_number}"
        data = {"state": action}
        response = requests.patch(f"{self.base_url}/{url}", headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()
