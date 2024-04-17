# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
from transformers import pipeline

pipe = pipeline("text-classification")

# %%
print(pipe("El jamón ibérico es bastante bueno"))

# %%
print(pipe("Pero la ternera gallega es lo peor del mundo"))

# %%
