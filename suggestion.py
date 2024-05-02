import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import csv

# Load movies from CSV
def load_movies(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        movies = list(csv_reader)
    return movies

# Filter movies by category
def filter_movies_by_category(movies, category):
    if category.lower() in ['movie', 'tv series', 'tv miniseries']:
        return [movie for movie in movies if movie[7].lower() == category.lower().replace(' ', '')]
    else:
        return movies

# Get random suggestion
def get_random_suggestion(movies):
    if movies:
        return random.choice(movies)
    else:
        messagebox.showinfo("No Suggestions", "No suggestions found in this category.")

# Display suggestion
def display_suggestion(category):
    filtered_movies = filter_movies_by_category(movies, category)
    suggestion = get_random_suggestion(filtered_movies)
    if suggestion:
        title_label.config(text=f"{suggestion[5]} ({suggestion[7]})")
        imdb_id = suggestion[1]
        imdb_link = f"https://www.imdb.com/title/{imdb_id}/"
        imdb_button.config(command=lambda: webbrowser.open_new(imdb_link))
        
        # Construct YouTube trailer link
        movie_name = suggestion[5]  # Assuming movie name is in the 5th column
        trailer_query = '+'.join(movie_name.split()) + '+trailer'
        trailer_link = f"https://www.youtube.com/results?search_query={trailer_query}"
        
        trailer_button.config(command=lambda: webbrowser.open_new(trailer_link))
        trailer_button.pack(side=tk.LEFT, padx=5, pady=10)
    else:
        title_label.config(text="")
        panel.config(image="")

# Load movies from CSV
file_path = 'WATCHLIST.csv'
try:
    movies
except NameError:
    movies = load_movies(file_path)

# Create GUI
root = tk.Tk()
root.title("Movie Suggestions")
root.configure(bg='black')

options = ["Movie", "TV Series", "TV Miniseries", "Random"]

frame = tk.Frame(root, bg='black')
frame.pack()

for option in options:
    btn = tk.Button(frame, text=option, bg='black', fg='white', font=('Arial', 12), width=15, height=2,
                    command=lambda o=option: display_suggestion(o))
    btn.pack(side=tk.LEFT, padx=5, pady=5)

title_label = tk.Label(root, text="", bg='black', fg='white', font=('Arial', 14))
title_label.pack()

panel = tk.Label(root, bg='black')
panel.pack()

imdb_button = tk.Button(root, text="IMDb", bg='black', fg='white', font=('Arial', 12), width=10, command=lambda: None)
imdb_button.pack(side=tk.LEFT, padx=5, pady=10)

trailer_button = tk.Button(root, text="Trailer", bg='black', fg='white', font=('Arial', 12), width=10, command=lambda: None)
root.mainloop()