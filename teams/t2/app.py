from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from common.dashboard_app import run_app

run_app(Path(__file__).resolve().parent, "T2")
st.caption("Historico disponivel: Sprints 0, 1 e 3. Os dados da Sprint 2 do T2 ainda nao estao disponiveis neste repositorio; isso nao significa zero respostas.")
