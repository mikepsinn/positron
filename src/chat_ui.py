from agent_core import AgentCore
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
agent = AgentCore()

@app.route('/')
def chat():
    return render_template('chat.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    response = agent.process_request(message)
    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True)
