from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your custom GPT API endpoint and key
YOUR_API_URL = 'https://cfwus02.opapi.win/v1/chat/completions'  # Replace with your actual GPT API URL
YOUR_API_KEY = 'sk-c2W2DFWC7B5D19247e19T3BLBkFJcFcb14b504E842299535'  # Replace with your actual API key

# DingTalk robot webhook URL and token
dingtalk_robot_url = 'https://oapi.dingtalk.com/robot/send?access_token=33886bca1ae51e7462ff750b79424c1b044d32cbdb0a1607de4e9593ed6a8861'  # Replace with your actual access token


# Function to send a message to DingTalk
def send_dingding(md):
    send_message = {
        "msgtype": "markdown",
        "markdown": {
            "title": "TEST",
            "text": md,
        }
    }

    response = requests.post(dingtalk_robot_url, json=send_message)
    if response.status_code == 200:
        print('Message sent to DingTalk successfully.')
    else:
        print('Failed to send message to DingTalk:', response.text)


@app.route('/handle-request', methods=['POST'])
def handle_request():
    question = request.json['text']['content']  # Assuming the question is in the body of the request under `text.content`

    headers = {
        "Authorization": 'Bearer ' + YOUR_API_KEY
    }

    params = {
        "messages": [{
            "role": 'user',
            "content": question
        }],
        "model": 'gpt-3.5-turbo-16k-0613'  # This is the model you've chosen to use
    }

    try:
        response = requests.post(YOUR_API_URL, json=params, headers=headers)
        response.raise_for_status()  # This will raise an exception for HTTP error responses
        res_content = response.json()['choices'][0]['message']['content']

        # Send the response content to DingTalk
        send_dingding(res_content)

        print('GPT response:', res_content)
        return jsonify(res_content)
    except requests.RequestException as error:
        print('Error sending message to the GPT API:', error)
        return jsonify({'error': str(error)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)