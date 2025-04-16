
# GenAI Hybrid Log Classification System

## 📌 Overview

This project presents a **hybrid log classification system** that optimally combines **Regex-based patterns**, **BERT embeddings**, and **LLM-driven classification** to efficiently and cost-effectively categorize system logs. The primary goal is to minimize inference costs by applying lightweight techniques first (like Regex) and progressively moving to heavier models only when needed.

---

## 📊 Workflow

1. **RegexProcessor**: Quickly classifies logs using predefined regex rules.
2. **BERTProcessor**: Converts logs to embeddings and uses a classification model for unclassified logs.
3. **LLMProcessor**: Invokes a Large Language Model (LLM) as a final fallback for complex logs.
4. **Server**: A FastAPI server exposing an endpoint to classify incoming logs via the hybrid pipeline.

---

## 📁 Project Structure

```
GenAI-Hybrid-Log-Classification-System/
│
├── models/               # Pre-trained BERT model and classifier
├── resources/            # Regex rules and config files
├── training/             # Notebook for training BERT classifier
│
├── bert_processor.py     # BERT-based log classification
├── regex_processor.py    # Regex-based log classification
├── llm_processor.py      # LLM-based log classification (OpenAI API or similar)
├── classify.py           # Unified classifier combining all processors
├── server.py             # FastAPI server exposing classification endpoint
├── main.py               # Example driver script for local testing
│
├── .gitignore.txt
├── .env                  # API keys and sensitive configs (not committed)
├── README.md
```

---

## 🚀 How to Run

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup Environment Variables**
   
      Add your Groq API key in .env file present in the root:

   ```
   GROQ_API_KEY="<Your_Api_Key>"
   ```

3. **Start Server**
   ```bash
   python server.py
   ```

4. **Test API**
   Send a POST request to `http://localhost:8000/classify` with:
   ```json
   {
     "log": "Your log message here"
   }
   ```

---

## 📖 Training

- Use the notebook in `training/` to train your BERT classifier on labeled log data.
- Save the trained model in the `models/` directory.

---

## 💡 Features

- Cost-efficient: Applies Regex first, then BERT, then LLM if required.
- Modular Processors: Easy to plug-in custom regex patterns or switch out models.
- FastAPI-powered backend for scalable deployment.

---

## 📜 License

This project is under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

Inspired by operational log analysis practices and hybrid AI pipelines for enterprise monitoring systems.
