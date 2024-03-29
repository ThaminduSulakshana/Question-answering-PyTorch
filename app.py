from flask import Flask, render_template, request
from transformers import pipeline
import pickle

app = Flask(__name__)

# Load the question-answering pipeline from the pickle file
with open('question_answerer_pipeline.pkl', 'rb') as model_file:
    question_answerer = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    context = request.form['context']
    question = request.form['question']

    # Use the question-answering pipeline to get the answer
    answer = question_answerer(question=question, context=context)

    return render_template('index.html', context=context, question=question, answer=answer['answer'])

if __name__ == '__main__':
    app.run(debug=True)
