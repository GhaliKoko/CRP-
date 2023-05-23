import streamlit as st
import pickle
import requests
import time
import random
from typing import List, Tuple
from crp_model2 import UnigramLanguageModel
from streamlit_searchbox import st_searchbox
import base64
from streamlit_option_menu import option_menu

st.set_page_config(page_title="VeePee", page_icon=":sparkles:", layout="centered")


# Load your model using pickle
@st.cache_resource
def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model


def get_autocomplete_suggestions(searchterm: str) -> List[Tuple[str, any]]:
    if not searchterm:
        return []

    # Implement your function to return autocomplete suggestions based on the model
    suggestions = model.suggestion(searchterm)[:10]
    return [
        (f"{suggestion}", f"{suggestion}")
        for suggestion in suggestions
    ]


# Load your model here
model_path = 'serialized_uni_model.pickle'
model = load_model(model_path)

st.markdown("<h1 style='text-align: center; color: pink;'>Bienvenue Chez VeePee</h1>", unsafe_allow_html=True)

selected = option_menu(
    menu_title="Menu Principal",
    options=["Accueil", "Mode", "Maison", "Voyage", "Beauté", "The Place", "Vin et Gastronomie"],
    default_index=0,
    orientation="horizontal",

)

with st.container():
    st.write("")  # Empty line for spacing
    left_column, middle_column, right_column = st.columns(3)

    with middle_column:
        selected_value = st_searchbox(
            search_function=get_autocomplete_suggestions,
            placeholder="Recherchez une marque, un produit...",
            default="",
            clear_on_submit=False,
            clearable=True,
            key="autocomplete",
        )
        # st.info(f"{selected_value}")
