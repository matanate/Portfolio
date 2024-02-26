from flask import Flask, render_template
import os


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

PORT_DICT = {
    1: {
        "name": "Movies & TV Shows Review Database",
        "url": "https://movie-and-tv-show-database-web.onrender.com/",
        "git_repo": "https://github.com/matanate/Movie-and-TV-Show-Database-Web-Application",
        "overview": "This is a Flask web application that serves as a movie and TV show database. Users can sign up, log in, search for titles, view details of individual titles, add reviews, and explore the top-rated movies and TV shows. Additionally, administrators have access to functionalities like adding and deleting titles.",
        "preview_img": "movietvdb.png",
        "filters": ["web", "database", "flask", "python", "js"],
    },
    2: {
        "name": "Breakout Game",
        "url": "https://breakout-cxy3.onrender.com/",
        "git_repo": "https://github.com/matanate/Breakout",
        "overview": "This is a simple implementation of the classic Breakout game using Flask for the backend and JavaScript for the frontend. The game features a paddle, a bouncing ball, and blocks to be cleared. The player's goal is to keep the ball bouncing, hitting and clearing the blocks, while avoiding letting the ball fall off the screen.",
        "preview_img": "breakout.png",
        "filters": ["web", "games", "flask", "python", "js"],
    },
    3: {
        "name": "Cafe Database",
        "url": "https://cafe-db.onrender.com/",
        "git_repo": "https://github.com/matanate/cafe-db",
        "overview": "A Flask web application serving as an interactive café database. Discover random cafés, retrieve details on all cafés, or search by location or name. Ideal for developers looking to incorporate café information into their projects. Examples provided for successful queries and error responses.",
        "preview_img": "cafedb.png",
        "filters": ["web", "database", "flask", "python", "js"],
    },
    4: {
        "name": "Watermarker",
        "url": None,
        "git_repo": "https://github.com/matanate/Watermarker",
        "overview": "The Watermarker is a user-friendly application for adding watermarks to images, allowing customization of various properties such as text, font, color, size, opacity, rotation, and tiling.",
        "preview_img": "watermarker.png",
        "preview_vid": "watermarker_demo.mp4"
        "filters": ["tkinter", "python"],
    },
    5: {
        "name": "Typing Speed Tester",
        "url": None,
        "git_repo": "https://github.com/matanate/Typing_Speed_Test",
        "overview": "The Typing Speed Test App is a simple and interactive application designed to measure and improve your typing speed and accuracy. This app provides a platform for users to practice typing a set of randomly shuffled words and evaluates their typing speed in words per minute (WPM) and characters per minute (CPM).",
        "preview_img": "typingspeedtest.png",
        "preview_vid": "typingspeedtest_demo.mp4"
        "filters": ["games", "tkinter", "python"],
    },
    6: {
        "name": "Morse Code Engine",
        "url": "https://trinket.io/embed/python3/66233462a9?outputOnly=true&runOption=run&start=result",
        "git_repo": "https://github.com/matanate/morse_code",
        "overview": "This Python program allows users to encrypt and decrypt strings using a dictionary-based approach for Morse code, The encryption and decryption dictionaries are predefined, mapping characters to their Morse code equivalents.",
        "preview_img": "morsecode.png",
        "filters": ["command", "python"],
    },
    7: {
        "name": "Tic Tac Toe Game",
        "url": "https://trinket.io/embed/python3/7aed658123?outputOnly=true&runOption=run&start=result",
        "git_repo": "https://github.com/matanate/tic-tac-toe",
        "overview": "This is a simple command-line Tic-Tac-Toe game implemented in Python. The game allows two players to take turns marking spaces on a 3x3 grid, and the first player to get three in a row wins. The game board is displayed in the console.",
        "preview_img": "tiktaktoe.png",
        "filters": ["games", "command", "python"],
    },
}


@app.route("/")
def home():
    return render_template("home.html", port_dict=PORT_DICT)


@app.route("/portfolio-<int:port_num>")
def portfolio(port_num):
    return render_template(
        "portfolio-page.html", port_num=port_num, port_dict=PORT_DICT
    )


if __name__ == "__main__":
    app.run(debug=True)
