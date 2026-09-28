# 🌾 KrishiSahayak (कृषि-सहायक)

> An open-source, AI-powered agricultural decision-support agent built for smallholder farmers in Nepal. Developed as part of **Frogtoberfest 2026**.

---

## 📌 Problem Overview
Smallholder farmers across rural Nepal frequently face severe post-harvest crop losses and unfair market pricing due to a lack of real-time, actionable decision support. Operating without localized weather forecasts or transparent wholesale market price trends (e.g., Kalimati Market rates), farmers often sell at low rates or suffer crop spoilage during unexpected rain.

## 💡 Solution
**KrishiSahayak** bridges this gap by offering a conversational, voice- and text-enabled AI agent. Farmers can ask everyday questions in spoken or typed Nepali—such as whether to harvest crops today or wait until the weekend—and receive clear, actionable decisions powered by live API data and open-weight AI models.

---

## 🤖 AI Transparency & Frogtoberfest Disclosures

In compliance with **Frogtoberfest 2026 Guidelines**:

* **Open-Weight AI Model:** Powered by **Llama-3.3-70B-Instruct** / **Qwen2.5-72B-Instruct** via open inference endpoints (Groq / Together AI). No proprietary APIs (like OpenAI, Claude, or Gemini) are used.
* **Core AI Function:** The LLM acts as an **autonomous tool-calling router and multi-variable decision engine**. It extracts structured parameters from natural Nepali queries, triggers external API tool calls in parallel (weather + market rates), and evaluates conflicting factors (e.g., rain risk vs. price trajectories) to produce optimal harvest windows.
* **Litmus Test Compliance:** The AI model is essential to core operations. Without the open-weight LLM, the system cannot interpret unstandardized spoken/typed Nepali, dynamically route tool calls, or synthesize multi-source trade-off logic.

---

## 🛠️ Tech Stack

* **AI & Agent Framework:** Open-Weight Models (`Llama-3.3-70B` / `Qwen2.5-72B`), LangChain / LlamaIndex / Custom Function-Calling Loop
* **Backend:** Python, FastAPI
* **External APIs & Tools:** 
  * Kalimati Wholesale Market Price API / Web Scraper
  * OpenWeather API / Localized Micro-climate Data
  * Agricultural Crop & Pesticide Guidelines Engine
* **Frontend / UI:** Web App (React / Streamlit) & WhatsApp / Telegram Messaging Interface

---

## 🏗️ Project Architecture & Tool Calling Flow

```mermaid
graph TD
    classDef user fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef agent fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px;
    classDef tools fill:#fff3e0,stroke:#f57c00,stroke-width:2px;
    classDef output fill:#e8f5e9,stroke:#388e3c,stroke-width:2px;

    User(["👨‍🌾 User Input<br/><i>Nepali Voice or Text</i>"]):::user --> API["⚡ FastAPI Request Router<br/><i>STT / Whisper Audio Processing</i>"]
    API --> Core["🧠 KrishiSahayak Agent Core<br/><i>Llama 3.3 / Qwen 2.5</i>"]

    subgraph Tool Calling Execution Layer
        Core -->|"1. Intent & Entity Extraction"| Tool1["🌤️ Tool 1: OpenWeather API<br/><i>Local Micro-Climate Forecast</i>"]:::tools
        Core -->|"2. JSON Function Call"| Tool2["📊 Tool 2: Kalimati Market API<br/><i>Wholesale Commodity Rates</i>"]:::tools
        Core -->|"3. Parameter Lookup"| Tool3["📚 Tool 3: Crop Knowledge Base<br/><i>Perishability & Pest Guidelines</i>"]:::tools
    end

    Tool1 -->|"Weather Data"| Engine["⚖️ Multi-Variable Tradeoff Engine<br/><i>Rain Risk vs. Price Trajectory</i>"]
    Tool2 -->|"Market Trends"| Engine
    Tool3 -->|"Crop Rules"| Engine

    Engine --> Synthesis["🗣️ Natural Language Generator<br/><i>Structured Nepali Text / TTS Audio</i>"]
    Synthesis --> Output(["📱 Actionable Farmer Output<br/><i>WhatsApp / Web Response</i>"]):::output
```

---

## 🚀 Getting Started

*(Work in Progress — Development actively underway for Frogtoberfest 2026)*

### Prerequisites
* Python 3.10+
* Git

### Local Installation
```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/krishi-sahayak.git](https://github.com/YOUR_USERNAME/krishi-sahayak.git)
cd krishi-sahayak

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

👥 Team
Built by [Your Team Name] for Frogtoberfest 2026 (Leapfrog Technology).

📜 License
Distributed under the MIT License. See LICENSE for more information.
