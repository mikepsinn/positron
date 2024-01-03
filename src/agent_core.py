import github_api
import nlp


class AgentCore:
    def __init__(self):
        pass

    def process_request(self, request):
        request_type = nlp.get_request_type(request)
        if request_type == 'data_retrieval':
            return github_api.get_data(request)
        elif request_type == 'repository_analysis':
            return github_api.analyze_repository(request)
        elif request_type == 'issue_management':
            return github_api.manage_issue(request)
        elif request_type == 'pull_request_management':
            return github_api.manage_pull_request(request)
        else:
            return "Request type not recognized."

    def handle_event(self, event_id):
        event_data = self.fetch_event_data(event_id)
        return self.process_event_data(event_data)

    def fetch_event_data(self, event_id):
        return github_api.get_event_data(event_id)

    def process_event_data(self, event_data):
        event_type = event_data['type']
        if event_type == 'IssueEvent':
            return github_api.handle_issue_event(event_data)
        elif event_type == 'PullRequestEvent':
            return github_api.handle_pull_request_event(event_data)
        else:
            return "Event type not recognized."

    def run(self):
        while True:
            request = input("Enter a request: ")
            print(self.process_request(request))
            event_id = input("Enter an event ID: ")
            print(self.handle_event(event_id))
