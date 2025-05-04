import streamlit as st
import pickle
import numpy as np


with open('BreastCancerModel.pkl', 'rb') as f:
    model = pickle.load(f)

mean_vals = np.load('mean_values.npy')

with open('scaler.pkl', 'rb') as sf:
    scaler = pickle.load(sf)

# Indices of top 10 important features
important_indices = [21, 10, 28, 7, 26, 13, 20, 23, 6, 27]



st.title("🔬 Breast Cancer Detection App")


# Input fields for top 10 features
worst_texture = st.number_input("Worst Texture")
radius_error = st.number_input("Radius Error")
worst_symmetry = st.number_input("Worst Symmetry")
mean_concave_points = st.number_input("Mean Concave Points")
worst_concavity = st.number_input("Worst Concavity")
area_error = st.number_input("Area Error")
worst_radius = st.number_input("Worst Radius")
worst_area = st.number_input("Worst Area")
mean_concavity = st.number_input("Mean Concavity")
worst_concave_points = st.number_input("Worst Concave Points")




if st.button("Predict"):
    user_inputs = [worst_texture, radius_error, worst_symmetry, mean_concave_points,
    worst_concavity, area_error, worst_radius, worst_area,
    mean_concavity, worst_concave_points]

    if prediction[0] == 1:
        st.error("⚠️ Malignant Tumor Detected")
    else:
        st.success("✅ Benign Tumor")
