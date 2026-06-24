import streamlit as st
import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parent / "All Data Main Trans (1).csv"

st.write("Looking for:", csv_path)
st.write("Exists:", csv_path.exists())

df = pd.read_csv(csv_path, low_memory=False)

st.dataframe(df)
