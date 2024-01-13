
import os
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from pytube import Playlist, YouTube


def upcount(seconds):
    """
    Perform a countdown from the specified number of seconds to 1.

    Parameters:
    - seconds (int): The number of seconds for the countdown.
    """
    for i in range(seconds):
        time.sleep(1)
        print(i+1)
        i+=1

def inhale_exhale(sec_in, sec_out, sec_keep, exhale_type):
    """
    Simulate breathing exercises with inhale and exhale phases.

    Parameters:
    - sec_in (int): Duration of inhale countdown.
    - sec_out (int): Duration of exhale countdown.
    - sec_keep (int): Duration to hold breath after inhale.
    - exhale_type (str): Type of breathing exercise.
    """
    print(exhale_type, ": \nbreathe ", sec_in)
    upcount(sec_in)
    time.sleep(sec_keep)
    print(exhale_type, " ", sec_out)
    upcount(sec_out)
    print("done")

def embouchure_exercise():
    """
    Perform a sequence of embouchure exercises using the inhale_exhale function.
    """
    inhale_exhale(4, 4, 0,"exhale in embouchure")
    time.sleep(1)
    inhale_exhale(2, 8, 0, "exhale in embouchure")
    time.sleep(1)
    inhale_exhale(4, 12, 0, "exhale in embouchure")
    time.sleep(1)
    inhale_exhale(1, 16, 0, "exhale in embouchure")
    print("exercise done")

def long_tone():
    """
    Simulate a long tone exercise by counting up to 100.
    """
    print("long tone:")
    upcount(100)
    print("done!")

def book_exercises(how_many):
    """
    Print exercise numbers and random exercise IDs based on the specified range.

    Parameters:
    - how_many (int): The number of exercises to display.
    """
    print("---\n" + "do exercise number: ")
    for i in range(how_many):
        print(i+1, ".", random.randint(1,252))
        # replace the number 252 with your number of exercises in your exercise book

def random_piece():
    """
    Select a random music score from a specified directory and print its information.
    """
    dir_path = r' LOCAL_PATH_TO_SCORES '
    files = []
    for pathh in os.listdir(dir_path):
    # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, pathh)):
            files.append(pathh)
    files.remove('Thumbs.db') # REMOVE THIS IF YOU DO NOT USE WINDOWS
    rand = random.choice(files)[:-4]
    pathh = " LOCAL_PATH_TO_SCORES "[:-1] + rand + ".pdf"
    print("---\n" + rand + "\n" + pathh)

def youtube_random(playlist_link):
    """
    Select and print a random video from a YouTube playlist.

    Parameters:
    - playlist_link (str): The link to the YouTube playlist.
    """
    video_links = Playlist(playlist_link).video_urls
    def get_video_info(link):
        title = YouTube(link).title
        return {"title": title, "link": link}
    processes = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url in video_links:
            processes.append(executor.submit(get_video_info, url))
    video_info_list = []
    for task in as_completed(processes):
        video_info_list.append(task.result())

    chosen = random.choice(video_info_list)
    print("---\n" + chosen["title"] + "\n" + chosen["link"])

def countdown(exercise):
    """
    Perform a countdown and then execute a specified exercise.

    Parameters:
    - exercise (function): The exercise function to be executed after the countdown.
    """
    print(exercise.__name__ + ":")
    time.sleep(1)
    print("start in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    exercise()

# Example usage of functions
    
countdown(embouchure_exercise)

countdown(long_tone)

book_exercises(1)

random_piece()

youtube_random(" YOUTUBE_PLAYLIST_LINK_HERE ")