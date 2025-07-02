import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate


# --- Flask App Initialization ---
app = Flask(__name__)
CORS(app)

# --- LangChain and AI Model Setup ---
try:
    llm = ChatGroq(model_name="llama3-8b-8192")
    print("✅ Successfully connected to Groq Cloud API.")
except Exception as e:
    print(f"❌ Error connecting to Groq API: {e}")
    print("Please ensure you have set your GROQ_API_KEY environment variable.")
    llm = None

# --- Prompt Template Definition ---
prompt_template_text = """
As an expert programmer and algorithm teacher, please provide a detailed explanation of the following Python code snippet.

Your explanation must be clear, structured, and easy for a student preparing for coding interviews to understand.

Structure your response with the following sections:

### High-Level Approach
Briefly describe the overall strategy (e.g., "This solution uses a two-pointer approach...", "It leverages a hash map to store previously seen values...").
Also mention in which of the following categories this code falls: ["Arrays & Hashing", "Two Pointers", "Sliding Window", "Stack", "Binary Search", "Linked List", "Trees", "Heap / Priority Queue", "Backtracking", "Tries", "Graphs", "Advanced Graphs", "1-D Dynamic Programming", "2-D Dynamic Programming", "Greedy", "Intervals"]

### Data Structures Used
List and explain the key data structures used in the code (e.g., Hash Map, Array, Set). Explain *why* they were chosen for this problem.

### Algorithm Breakdown
Provide a numbered, step-by-step walkthrough of the code's logic. Explain what each major part of the code does.

### Time Complexity Analysis
State the time complexity using Big O notation (e.g., O(n), O(log n), O(n^2)). Provide a clear justification for this analysis.

### Space Complexity Analysis
State the space complexity using Big O notation (e.g., O(1), O(n)). Justify the analysis by explaining what extra space is being used.

### Optimization
Explain how the code could be optimized further, if applicable. Discuss any potential improvements in terms of time or space complexity.

Here is the code to analyze:
```python
{code_snippet}
```
"""
prompt = PromptTemplate(
    input_variables=["code_snippet"],
    template=prompt_template_text
)

if llm:
    chain = prompt | llm
else:
    chain = None

# --- API Endpoint ---
@app.route('/analyze', methods=['POST'])
def analyze_code():
    """
    This function is the API endpoint. It receives code from the frontend,
    runs the analysis chain, and returns the AI's explanation.
    """
    if not chain:
        return jsonify({"error": "LLM not initialized. Check server logs."}), 500
    
    data = request.json
    if not data or 'code' not in data:
        return jsonify({"error": "Invalid request. 'code' field is required."}), 400
    
    code_snippet = data['code']

    try:
        result = chain.invoke({"code_snippet": code_snippet})
        explanation = result.content

        return jsonify({"explanation": explanation})
    
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        return jsonify({"error": "Failed to analyze code. Check server logs."}), 500

# --- Main Execution ---
if __name__ == '__main__':
    app.run(port=5000, debug=True)