import streamlit as st


def run_app(ckip_nlp_models, cwn_upgrade) -> None:
    st.title("LOPE")


if __name__ == "__main__":
    ckip_nlp_models = ["bert-base", "albert-tiny", "bert-tiny", "albert-base"]
    run_app(ckip_nlp_models, cwn_upgrade=False)
