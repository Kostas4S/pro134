import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("star_with_gravity.csv")
df.head()

stars =[]
for f in df.Distance:
    if f<=100:
        stars.append(True)
    else:
        stars.append(False)

is_dist = pd.Series(stars)
star_dist=df[is_dist]
is_dist.head()
star_dist=df[is_dist]
star_dist.reset_index(inplace=True,drop=True)
star_dist.head()
star_dist.shape

gravity_stars  = []
for g in star_dist.Gravity:
    if g<=350 and g>=150:
        gravity_stars .append(True)
    else :
        gravity_stars .append(False)

is_gravity = pd.Series(gravity_stars )
final_stars = star_dist[is_gravity]
final_stars.head()
final_stars.shape
final_stars.reset_index(inplace=True,drop=True)
final_stars.head()
final_stars.to_csv("filtered_stars.csv")