# Psychology Bot - Mental Health Chatbot with RAG

## Introduction
Psychology Bot is a chatbot designed to provide mental health knowledge and support using Retrieval-Augmented Generation (RAG). This chatbot utilizes a dataset of mental health-related questions and answers to generate responses based on user input, offering helpful insights and coping strategies.

## Features
- **Retrieval-Augmented Generation (RAG)**: Enhances responses by retrieving relevant information from a pre-built dataset before generating answers.
- **Natural Language Processing (NLP)**: Uses a transformer-based model (e.g., BERT or GPT) to understand and respond to user queries.
- **Mental Health Support**: Provides information on common mental health concerns such as stress, anxiety, depression, and coping mechanisms.
- **CSV-Based Knowledge Base**: Uses a structured CSV file containing Q&A pairs to retrieve relevant answers.

## Installation
### Prerequisites
- Python 3.8+
- Required Python libraries:
  ```sh
  pip install transformers pandas faiss-cpu torch
  ```

### Clone the Repository
```sh
git clone https://github.com/Ramidajpn/Psychology-Bot.git
cd Psychology-Bot
```

## Usage
1. **Prepare the CSV dataset**: Ensure `mental_health_chatbot_responses.csv` contains questions and answers in the following format:
   ```csv
   Question,Answer
   "I feel anxious","Try deep breathing exercises and grounding techniques. If anxiety persists, consider talking to a therapist."
   "How to manage stress?","Practicing mindfulness, exercising, and maintaining a balanced lifestyle can help manage stress effectively."
   ```
2. **Run the chatbot**:
   ```sh
   python chatbot.py
   ```
3. **Interact with the bot**: Type your queries, and the chatbot will provide responses based on the retrieved context.

## Example Interaction
```
You: I'm feeling sad
Bot: It's okay to feel this way. Try engaging in activities you enjoy, talking to a close friend, or practicing self-care.
```

## Future Improvements
- Expand the knowledge base with more diverse mental health topics.
- Implement a web interface for easier accessibility.
- Integrate with professional mental health resources.

## Disclaimer
This chatbot is for informational purposes only and does not provide medical or professional advice. If you need urgent help, please contact a qualified mental health professional.
