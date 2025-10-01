# Silent Auction 🎯

This project is a **Python-based Silent Auction** game where multiple users can place their bids anonymously.  
The program collects all bids, ensures fair play by hiding previous entries, and then determines the highest bidder.

---

## 🚀 Features
- Allows multiple bidders to enter their bids.
- Automatically determines the highest bidder.
- Clears the screen to maintain fairness between bidders.
- Simple and interactive console-based experience.

---

## 🖥️ How It Works
1. The program starts by showing an ASCII art logo.
2. Each bidder enters their:
   - **Name**
   - **Bid Amount**
3. After each bid, the program asks if there are more bidders:
   - If **yes**, the screen is cleared and the next bidder can enter.
   - If **no**, the auction ends and the winner is announced.
   
---

## 📂 Project Structure
```
Silent-Auction/
│── art.py # Contains ASCII art logo
│── main.py # Main program logic
│── README.md # Documentation
```

---

## 🧑‍💻 Example Run

```
What is your name?: Alice
What is your bid?: $200
Are there any other bidders? Type 'yes' or 'no'.
yes

What is your name?: Bob
What is your bid?: $350
Are there any other bidders? Type 'yes' or 'no'.
no

The winner is Bob and the bid $350

```
---

## 📚 What I Learned
- How to use **dictionaries** in Python for mapping names to bid values.
- Implementing **loops and conditions** to control program flow.
- How to create **functions** for modular and reusable code.
- Simulating **screen clearing** using print statements for fairness.

---

## 🙏 Credits
This project idea and guidance comes from  
**Dr. Angela Yu’s 100 Days of Python Coding Bootcamp (Udemy Course)**.  

---

## 📜 License

This project is for educational purposes. Feel free to use or modify it for your own learning or projects.

---
