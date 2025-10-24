
import streamlit as st
import io
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="AI Health Gain — Demo", page_icon="🌿", layout="centered")

# ---------- Core model (demo version) ----------
def health_gain_demo(age, sex, drinking_days, drinks_per_occ, years_drinking, target_days):
    drinks_per_week_now = drinking_days * drinks_per_occ
    drinks_per_week_after = target_days * drinks_per_occ

    binge_now = 1 if drinks_per_occ >= 5 else 0
    binge_after = binge_now  # In this simple demo we only change the number of days

    # Placeholder parameters (to be calibrated with literature later)
    a, b, c = 0.02, 0.15, 0.10
    sex_adj = 0.95 if str(sex).lower() in ["female", "f", "woman"] else 1.0
    age_adj = max(0.6, 1.2 - (age - 20) * 0.01)  # from ~1.2 at 20y to ~0.6 at 80y
    adjust = sex_adj * age_adj

    rr_now = 1 + a * drinks_per_week_now + b * binge_now + c * (years_drinking / 20.0)
    rr_after = 1 + a * drinks_per_week_after + b * binge_after + c * (years_drinking / 20.0)

    rr_now = max(rr_now, 0.8)
    rr_after = max(rr_after, 0.8)

    k = 8.0
    gain_years = k * (rr_now - rr_after) / rr_now * adjust

    gain_years = max(0.0, min(gain_years, 3.0))  # cap at +3 years for demo visuals
    gain_months = round(gain_years * 12)

    headline = f"If you reduce your drinking days from {drinking_days} to {target_days} per week, you could gain about +{gain_months} months of healthy life."
    detail = {
        "age": age, "sex": sex,
        "now_drinks_per_week": drinks_per_week_now,
        "after_drinks_per_week": drinks_per_week_after,
        "rr_now": round(rr_now, 3),
        "rr_after": round(rr_after, 3),
        "gain_years": round(gain_years, 2),
        "gain_months": gain_months
    }
    return headline, detail

# ---------- UI ----------
st.markdown("# 🌿 AI Health Gain — Demo")
st.markdown("See how small changes can lead to **visible health gains**. *Educational concept only — not medical advice.*")

with st.form("inputs"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age (years)", min_value=15, max_value=90, value=28, step=1)
        sex = st.selectbox("Gender", ["Male", "Female"])
        years_drinking = st.number_input("Years of drinking", min_value=0, max_value=60, value=5, step=1)
    with col2:
        drinking_days = st.slider("Current drinking days per week", 0, 7, 4)
        drinks_per_occ = st.slider("Approx. drinks per occasion", 0, 10, 2)
        target_days = st.slider("Goal: reduce drinking days to", 0, 7, 2)

    submitted = st.form_submit_button("Calculate health gain")

if submitted:
    st.subheader("Your estimated gain")
    headline, detail = health_gain_demo(
        age=age, sex=sex, drinking_days=drinking_days,
        drinks_per_occ=drinks_per_occ, years_drinking=years_drinking,
        target_days=target_days
    )
    st.success(headline)

    st.markdown("**Health lifespan bar**")
    cap_months = 36
    progress = min(detail["gain_months"], cap_months) / cap_months
    st.progress(progress)

    st.markdown("### 💬 Gentle tips")
    if target_days < drinking_days:
        st.write(f"- Great start — moving from **{drinking_days}** to **{target_days}** days. Keep this pace 🌱")
        if drinking_days - target_days >= 2:
            st.write("- If helpful, reduce by 1 day first and build your rhythm.")
        st.write("- Eating before drinking and ~3 workouts/week can further support heart health.")
    else:
        st.write("- Try reducing by 1 day per week first and build a sustainable rhythm.")

    with st.expander("See model details (demo, explainable)"):
        st.json(detail)

    # ---- Downloads ----
    st.markdown("---")
    st.markdown("### ⬇️ Save your result")
    txt = f"""AI Health Gain – Demo Result
Time: {datetime.utcnow().isoformat()}Z

{headline}

Inputs:
- Age: {detail['age']}
- Sex: {detail['sex']}
- Drinking days (now→goal): {drinking_days} → {target_days}
- Drinks per occasion: {drinks_per_occ}
- Years drinking: {years_drinking}

Model (demo):
- RR now / after: {detail['rr_now']} / {detail['rr_after']}
- Healthy life gain: {detail['gain_months']} months
"""
    st.download_button("Download summary (.txt)", txt, file_name="ai_health_gain_result.txt")

    df = pd.DataFrame([detail])
    csv_buf = io.StringIO()
    df.to_csv(csv_buf, index=False)
    st.download_button("Download data (.csv)", csv_buf.getvalue(), file_name="ai_health_gain_result.csv")

st.markdown("---")
st.caption("Disclaimer: Educational demo only — not medical advice. Parameters are placeholders and will be calibrated with peer‑reviewed evidence and local data.")
