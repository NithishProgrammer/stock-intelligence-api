
-----

# 📈 Stock Intelligence API

[](https://www.python.org/)
[](https://fastapi.tiangolo.com/)
[](https://opensource.org/licenses/MIT)

A high-frequency **asynchronous financial monitoring engine** designed to track live market data. This API specializes in high-speed polling (4-second intervals) to capture real-time price volatility and serve it through a non-blocking JSON interface.

-----

## 🚀 Key Features

  * **⏱️ 4-Second Live Polling**: Precision-engineered to capture short-term price momentum and stock market volatility.
  * **🧠 Intelligent State Management**: Uses a global `notebook` architecture. The `/show` endpoint serves cached data instantly (\<10ms) without needing to re-scrape the web.
  * **🕵️ Advanced Request Masking**: Implements a full browser-grade header stack to ensure stable connections and bypass basic bot detection.
  * **🧹 Data Sanitization**: Automatically isolates the Company Name and converts raw price strings into clean, processable numerical formats.
  * **⚡ Async/Await Core**: Built on `httpx` and `asyncio` to ensure the background engine never slows down the API response time.

-----

## 🛠️ Installation & Setup

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/NithishProgrammer/stock-intelligence-api.git
    cd stock-intelligence-api
    ```

2.  **Install Dependencies**

    ```bash
    pip install fastapi uvicorn httpx beautifulsoup4
    ```

3.  **Start the Engine**

    ```bash
    python -m uvicorn main:app --reload
    ```

    *The API will be live at: `http://127.0.0.1:8000`*

-----

## 📡 API Documentation

> **⚠️ Restriction:** This API **strictly accepts** Yahoo Finance URLs only.

### 1\. Initialize Engine (The Tracker)

**Endpoint:** `GET /s`  
**Query Parameter:** `url` (A valid Yahoo Finance Stock/Company Quote URL)  
**Action:** Dispatches the background "Helper" to start the 4-second "Fetch & Update" loop.

### 2\. View Live Ticker (The Output)

**Endpoint:** `GET /show`  
**Description:** Retrieves the latest snapshot from the internal `notebook`.  
**Note:** You must refresh the page to see the updated price every 4 seconds.

**Sample Output:**

```json
{
  "company_name": "NVIDIA Corporation (NVDA)",
  "price": "USD 903.56",
}
```

-----

## ⚖️ Rules, Regulations & Ethical Use

> **Notice:** This project is an **Educational Tool** for programming practice. Use it responsibly:

1.  **Strict URL Policy**: Do not attempt to pass URLs from other domains. The parsing logic is hard-coded specifically for Yahoo Finance's DOM structure.
2.  **Market Hours**: Prices may stay static outside of active exchange hours (e.g., NYSE 7:00 PM – 1:30 AM IST).
3.  **IP Integrity**: 4 seconds is an aggressive polling rate. Running multiple trackers simultaneously may result in a temporary IP "Throttle" or Block from Yahoo Finance.
4.  **No Financial Advice**: This tool is for data visualization practice. The developer is not liable for any financial decisions or trading losses made using this data.

-----

## 🗺️ Project Roadmap

  - [x] 4-Second High-Frequency Polling
  - [x] Background Task State Management
  - [x] Automated Data Sanitization
  - [ ] **Next Step:** Implement "Percent Change" calculation (Up/Down) per session.
  - [ ] **Next Step:** Webhook support for mobile notifications on price targets.

-----

## 📜 License

Distributed under the **MIT License**.

**Developed by [Nithish](https://github.com/NithishProgrammer) | Puducherry, India 🇮🇳**

-----

### Your Next Step:

Now that you have the "Big Three" (Amazon, eBay, and Stock Intelligence), would you like me to show you how to host these for free on a service like **Render** or **Railway** so you can access them from your phone anywhere in Puducherry?
