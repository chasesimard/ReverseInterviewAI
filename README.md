
✅ Features:
	• Clean layout using markdown.
	• Clear Getting Started instructions.
	• Handles .env setup & local dev.
	• Deployment tips optional.
	• Includes license & credit section.

⸻
# 🎤 Reverse Interview AI Demonstration

Get Access to Research about the Company!
![Screenshot 2025-05-20 at 1 15 22 PM](https://github.com/user-attachments/assets/9570ac0b-544f-4b05-ae3b-ad10c1244781)


Get Interview Questions and Responses
![Screenshot 2025-05-20 at 1 19 21 PM](https://github.com/user-attachments/assets/f46a3f69-4f53-4d54-8a72-18c4eb0c2997)


Get an Interview Score to see how you did!
![Screenshot 2025-05-20 at 1 19 46 PM](https://github.com/user-attachments/assets/fd7e9f04-0321-471d-b93f-d9cc4aefe332)


# 🎤 Reverse Interview AI

**ReverseInterviewAI** helps candidates **train for interviews** by simulating realistic Q&A with AI based on the target **company** and **job title**.

---

## 🚀 Features

- 🔍 Auto-generates company research
- 💬 Dynamic interview question generation
- 🧠 AI-simulated interview feedback and scoring
- 🎯 Tailored to role + company
- ⚙️ React + Vite frontend, FastAPI backend

---

## 🛠️ Tech Stack

- **Frontend:** React (TypeScript) + Vite
- **Backend:** FastAPI (Python 3.9+)
- **Styling:** Tailwind CSS (Optional)
- **AI:** OpenAI (via `.env` key)
- **CopilotKit:** (optional) for clean UI scaffolding

---

## ⚙️ Getting Started

### 1. Clone the Repo

```bash
git clone git@github.com:chasesimard/ReverseInterviewAI.git
cd ReverseInterviewAI



⸻

2. Setup Python Backend

cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload

✅ You should now have FastAPI running on http://localhost:8000

⸻

3. Setup React Frontend

cd ../frontend
npm install
npm run dev

🔥 Runs on http://localhost:5173 by default.

⸻

🔐 Environment Variables

Create a .env file in the root folder (not committed):

OPENAI_API_KEY=sk-xxxx...
SUPABASE_URL=https://xyz.supabase.co
SUPABASE_API_KEY=your_supabase_key

🧪 Add .env to .gitignore to avoid leaking secrets.

⸻

📦 Build for Production

cd frontend
npm run build
npm run preview



⸻

🧪 API Endpoints

Endpoint	Method	Description
/research	POST	Generates company summary
/interview	POST	Returns next interview question
/score	POST	Scores the full interview transcript



⸻

🖼️ UI Reference


⸻

📌 TODO
	• User login with Supabase
	• Save previous interview history
	• Add voice-to-text AI
	• Deploy via Vercel/Render

⸻

📄 License

MIT

⸻

👤 Author

Built by @chasesimard

Inspired by real-world candidate prep.
