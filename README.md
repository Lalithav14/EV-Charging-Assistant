# ⚡ EV Charging Assistant 🤖

A **ROS 2-powered, AI-integrated robotic charging assistant** for electric vehicles. It fuses computer vision, predictive maintenance, and LLM orchestration to autonomously inspect, diagnose, and assist with EV charging in a smart and futuristic way.

---

## 🚀 Features

- 🤖 **Autonomous Robotic Arm** – Ready to plug into your EV charging port
- 🎥 **Computer Vision (CV)** – Detect port position and vehicle orientation
- 🧠 **Predictive Maintenance (PM)** – Analyze battery/thermal/IMU data with LSTM
- 🧬 **LLM Orchestrator** – GPT-3.5 powered intelligent status interpreter
- 📊 **Futuristic UI Dashboard** – Live health updates, animations, and more
- 🌐 **ROS 2 Modular Architecture** – Clean, scalable, and extensible
- 🛠️ Designed for patent-readiness and deployment

---

## 📁 Repository Structure

EV-Charging-Assistant/
├── src/
│ ├── arm_control/
│ ├── cv_inspection/
│ ├── sensors_fusion/
│ ├── pm_health/
│ └── llm_orchestrator/
├── ui_dashboard/ # React-based futuristic web UI
│ ├── src/App.js
│ ├── src/App.css
│ └── package.json
├── launch/
│ └── full_launch.py # Launches all ROS nodes together
├── README.md
