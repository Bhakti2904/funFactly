# 🌟 FunFactly – A Fun & Trending Facts Web App

Hi! 👋 This is **FunFactly**, a lightweight and modern web app I built using **Flask**, **HTML/CSS**, and **JavaScript**.

The app gives you:

* 🎲 Random fun facts (from a public API)
* 🔥 Trending facts from Reddit (`r/todayilearned`)
* 🌓 Light & Dark mode toggle
* 📋 Copy-to-clipboard buttons (because why not!)

It’s simple, responsive, and built with love for curious minds like me 😊

---

## 🚀 What it does

* Fetches a **new random fact** on every refresh
* Shows a **trending Reddit fact** of the day
* Lets you **copy facts with a click**
* Theme stays saved (thanks to `localStorage`)
* Looks good on both desktop and mobile

---

## 📸 Screenshots

 Light Mode                      
![light](https://raw.githubusercontent.com/Bhakti2904/funFactly/main/images/light-mode.png)
 Dark Mode
![dark](https://raw.githubusercontent.com/Bhakti2904/funFactly/main/images/dark-mode.png)

---

## 💻 How to Run It Locally

```bash
git clone https://github.com/Bhakti2904/funFactly.git
cd funFactly

pip install -r requirements.txt
python app.py
```

Then open your browser and go to:

```
http://localhost:5000
```

---

## 📂 Project Structure

```
funfactly/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── images/
│   ├── light-mode.png
│   └── dark-mode.png
└── README.md
```

---

## 🛠 Tech Stack

* Python (Flask)
* HTML5 + CSS3
* JavaScript (for theme + copy button)
* Reddit & UselessFacts APIs
* Google Fonts: Inter, DM Sans

---

## 🌱 Future Plans

* [ ] Hindi ↔ English toggle
* [ ] Share to WhatsApp/Twitter
* [ ] Save favorite facts
* [ ] Daily fact memory using localStorage

---

## 👩‍💻 Made by

**Bhakti Parsaniya**
Passionate about web dev, Python, and building things people enjoy 💖
[GitHub Profile](https://github.com/Bhakti2904)

---

## 📄 License

MIT License — free to use, modify, and share.
