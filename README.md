# 🔮 NextPrompt_AI — Predict the Next Sentence Like a Fortune Teller

Ever started a sentence and didn’t know how to finish it?  
**NextPrompt_AI** is your ✨ AI-powered wingman ✨ that completes your thoughts using Google Gemini!

---

## 🚀 What Does It Do?

You enter a sentence.  
It replies with 3 AI-generated continuations that feel like a mind reader finished your story.

Perfect for:
- Writers with writer’s block ✍️  
- Memers writing captions 🤳  
- Coders making cool demos 💻  
- Anyone who loves fun AI stuff 🤖

---

## 🧠 How It Works

- Frontend built with **Flask + HTML + TailwindCSS**
- User enters the first sentence
- **Gemini 1.5 Flash** model (Google Generative AI) predicts 3 possible next lines
- Gemini is accessed securely using your `.env` API key
- Output is rendered in a Gen-Z inspired modern UI with background images, colors & bounce 🪩

---

## 🎯 Features

✅ Gemini 1.5 Flash integration  
✅ Styled UI (not boring, promise)  
✅ 3 Realistic Predictions  
✅ Error handling + fallback  
✅ Built for local or cloud  

---

## 📦 Setup Instructions

1. **Clone it**
   ```bash
   git clone https://github.com/yourusername/NextPrompt_AI.git
   cd NextPrompt_AI

2.	Create virtual env + install dependencies
       python3 -m venv venv
       source venv/bin/activate
       pip install -r requirements.txt

3. Add your .env file
     Create a .env file and add:
           GEMINI_API_KEY=your_actual_api_key
          FLASK_ENV=development
          FLASK_DEBUG=True
          SECRET_KEY=your_secret_key_here


4.	Run the app
     python app.py

5.	Visit it on your browser
      http://127.0.0.1:5051/




🌐 Tech Stack
	•	Python 3.12
	•	Flask
	•	Google Generative AI (gemini-1.5-flash)
	•	HTML5
	•	TailwindCSS
	•	dotenv




💡 Fun Facts
	•	Built during a spontaneous coding spree after too much coffee ☕
	•	One prediction said: “And then the chicken became CEO.” 🐔📈
	•	The app uses no database — just brains (and a bit of magic).



🤝 Contributing

Pull requests are welcome!
Feel free to fork, flex, and Gen-Z-ify more stuff.



Made with 💙 by Ayush Mishra


---

✅ You can copy this whole thing, save it as `README.md` in your project root folder, and push it to GitHub. Let me know if you want a logo or custom badge too!
   
