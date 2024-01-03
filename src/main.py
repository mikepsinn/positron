import flask
from agent_core import AgentCore
from chat_ui import chat

app = flask.Flask(__name__)
agent = AgentCore()

@app.route('/')
def home():
    return chat()

@app.route('/send_message', methods=['POST'])
def send_message():
    message = flask.request.form['message']
    response = agent.process_request(message)
    return flask.jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True)
