<!-- Gemini API Demo Template By Th3-C0der-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <title>Th3-C0der's Template Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .chat-container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .chat-box {
            height: 70%;
            width: 100%;
            overflow-y: auto;
            border: 1px solid #ddd;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
            background: #fafafa;
        }
        .chat-box p {
            margin: 5px 0;
        }
        .user-input {
            display: flex;
            width: 100%;
        }
        .user-input input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 50px;
        }
        .user-input button {
            padding: 10px 20px;
            border: none;
            background: #007bff;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <h1 style="background: green;">Th3-C0der's AI</h1>
        <div class="chat-box" id="chat-box"></div>
        <form class="user-input" id="chat-form">
            <input type="text" id="prompt" placeholder="Type your message here...">
            <button type="submit">  <i class="fas fa-paper-plane"></i></button>
        </form>
    </div>

    <script>
        const chatForm = document.getElementById('chat-form');
        const chatBox = document.getElementById('chat-box');
        const promptInput = document.getElementById('prompt');

        chatForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const prompt = promptInput.value;
            displayMessage('User', prompt);
            promptInput.value = '';

            // Check for custom responses before making AJAX call
            const customResponse = getCustomResponse(prompt);
            if (customResponse) {
                displayMessage('Gemini', customResponse);
            } else {
                try {
                    const response = await fetch('/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ prompt })
                    });

                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }

                    const data = await response.json();
                    displayMessage('Bot', data.response);
                } catch (error) {
                    displayMessage('Bot', 'Sorry, there was an error processing your request.');
                }
            }
        });

        function displayMessage(sender, message) {
            const messageElement = document.createElement('p');
            messageElement.textContent = `${sender}: ${message}`;
            chatBox.appendChild(messageElement);
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        function getCustomResponse(prompt) {
            const responses = {
                'Hello': 'Hi there! How can I assist you today?',
                'What is your name?': 'I am Th3-C0der\'s Template AI, your virtual assistant.',
                'Tell me a joke': 'Why don’t scientists trust atoms? Because they make up everything!',
                'What is AI': 'AI (Artificial Intelligence) is the simulation of human intelligence processes by machines, especially computer systems.',
                'Hi': 'Hi there! How can I assist you today?'
            };
            return responses[prompt] || null;
        }
    </script>
</body>
</html>
