# 🧠 Build a Multi-Agent AI System using Handoff

---

## 🤖 What is "Handoff" in AI Agents?

**In simple words:**

> Handoff means the **main agent assigns a task** to the **most suitable expert agent** based on what the user asks.

### 📌 Example:
If a user says:
> “Make a responsive navigation bar for my desktop website”

Then the **main agent** will hand this task to the **Web Developer agent**, because that's their area of expertise.

It works just like a real-life **project manager** assigning tasks to team members based on their skills.

---

## 🔍 Task Breakdown

We're using **Python** with the **OpenAI SDK** and **Chainlit** to build a multi-agent AI system.

### 🎯 Agents in the System:
- 🧑‍💼 **Manager Agent (Main Agent)**  
  Talks to the user and delegates the task to an expert.

- 👨‍💻 **Web Developer Agent**  
  Handles all website-related development.

- 📱 **Mobile App Developer Agent**  
  Builds and manages mobile applications.

- 🎨 **Graphic Designer Agent**  
  Designs user interfaces and visuals.

- 📢 **Marketing Agent**  
  Handles marketing-related tasks and strategies.

---

## ⚙️ Project Setup (with `uv`)

> ⚡ `uv` is a fast Python package manager and virtual environment tool.

### 1. Install `uv` (if not already installed)
pip install uv
### 2. Create and activate virtual environment
uv venv
.venv\Scripts\activate
### 3. Install dependencies
uv add [`dependency name`]
### 4. Add your API key
Create a .env file in the root directory and add this line:
GEMINI_API_KEY=

🚀 How It Works
The user starts the conversation.
The Manager Agent understands the request.
The manager chooses the correct expert agent.
The expert completes the task and returns a response.
The result is shown to the user line by line using Chainlit's chat UI.

📂 Project Structure

├── agent.py           # Agent definitions and handoff logic
├── main.py            # Chainlit app entry point
├── .env               # Environment file with your API key
├── requirements.txt   # Required Python packages
└── README.md          # Markdown file

🏁 Run the App
To start the chat interface:
uv run chainlit run main.py

Then open the browser link shown in the terminal (usually http://localhost:8000).

📚 Explore More Chainlit Features
Chainlit makes it easy to build chat-based AI tools and dashboards. You can explore more features like:

Custom UI components (buttons, input fields)
Session management
Image rendering
Streaming responses
Frontend customization

🔗 Official Chainlit Documentation:
👉 https://docs.chainlit.io

