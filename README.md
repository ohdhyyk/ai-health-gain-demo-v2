# AI Health Gain — Public Demo

**Make preventive health visible.**  
This Streamlit demo estimates the *healthy-life gain* from small changes in alcohol habits (e.g., reducing drinking days per week). It is designed for **public demo & outreach** (professors, incubators, partners).

> Educational concept only — **not medical advice**. Parameters are placeholders and will be calibrated with peer‑reviewed evidence and local data.

---

## 🏃‍♂️ Quick start
```bash
python3 -m pip install --upgrade pip
python3 -m pip install streamlit pandas
python3 -m streamlit run ai_health_gain_demo_app_public_en_v2.py
```

The app opens at `http://localhost:8501`.

---

## 🧠 What this demo shows
- Input: Age, gender, current drinking pattern, target change  
- Output: **Estimated healthy-life gain** (months/years)  
- Gentle guidance: harm‑reduction tips for users not ready to quit  
- Downloadable **TXT summary** and **CSV data** for sharing/archiving

---

## 📐 Model (demo logic, explainable)
- Uses a simple *dose–response → relative risk* approximation
- Compares two scenarios: **keep current habits** vs **improve a bit**
- Maps risk shift to **expected healthy‑life gain** (education only)
- Provides a transparent JSON block for discussion with experts

**Next (scientific) steps**
1. Replace placeholder parameters with peer‑reviewed dose–response estimates (alcohol → all‑cause/CVD risks).  
2. Calibrate age/sex baseline with life‑table methods.  
3. Add uncertainty bands and population segmentation.  
4. External review (public health / methodology).

---

## 🧭 Ethics & tone
- No judgement; **harm‑reduction** for those who still drink.  
- Positive, optional suggestions; no ultimatums.  
- Clear disclaimer; we present **healthy‑life gain**, not lifespan prediction.

---

## 📄 Files
- `ai_health_gain_demo_app_public_en_v2.py` — the app
- `one_pager.md` — one‑page summary content (for PDF export)
- `assets/demo-screenshot.png` — *(add your own screenshot here)*

---

## 📨 Contact (example)
**[Your Name]** — BSc Medical Biosciences, Imperial College London  
Email: your.email@example.com | Based in: Norway / UK
