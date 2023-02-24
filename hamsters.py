import random
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

# Define the arrays of hamster sounds
prefixes = ['Ard', 'Bax', 'Cen', 'Dol', 'Eon', 'Fyr', 'Gin', 'Hau', 'Ivy', 'Jax', 'Kyn', 'Lio', 'Mae', 'Nyx', 'Ora', 'Paz', 'Qor', 'Raz', 'Syl', 'Tao', 'Ura', 'Vae', 'Wyn', 'Xal', 'Yin', 'Zor', 'Aer', 'Bel', 'Cir', 'Dae', 'Ela', 'Fen', 'Gra', 'Hyl', 'Ira', 'Jes', 'Kas', 'Lyn', 'Mio', 'Nas', 'Oph', 'Per', 'Qen', 'Ryn', 'Ser', 'Tia', 'Una', 'Vio', 'Wyr', 'Xen']
suffixes = ['ane', 'bel', 'cor', 'dor', 'ene', 'fyr', 'gol', 'hin', 'ice', 'jol', 'kai', 'len', 'mio', 'nys', 'ope', 'phe', 'qis', 'rym', 'syl', 'tas', 'ury', 'vyn', 'wyl', 'xen', 'yar', 'zel', 'aen', 'ben', 'col', 'dyl', 'ear', 'fyn', 'gol', 'han', 'ire', 'jon', 'kar', 'lir', 'myn', 'nal', 'oce', 'pur', 'qor', 'ryn', 'sol', 'tyl', 'ule', 'van', 'wyr', 'xal', 'yin', 'zor']
middle = ['ax', 'ble', 'cer', 'dax', 'ela', 'fiz', 'gal', 'hin', 'ixo', 'jex', 'kyl', 'lim', 'mux', 'nox', 'por', 'qel', 'rix', 'sax', 'tix', 'uvi']

# Define the array of possible destinations for the hamsters
destinations = ['an orbital trajectory', 'the furthest reaches of deep space', 'the moon', 'Mars', 'Venus', 'Jupiter', 'Saturn', 'Uranus', 'Neptune',"Pluto", "Ceres", "Eris", "Haumea", "Makemake", "Europa", "Ganymede", "Titan", "Enceladus", "Callisto", "Triton", "Oberon", "Tethys", "Iapetus", "Hyperion", "Phoebe", "Rhea", "Dione", "Charon", "Sedna"]

# Define the libraries of sentences for the hamster intro and bio
intros = [
    "Welcome to the Hamster Space Program! Today we're launching another brave hamster into the great beyond!",
    "It's time for another hamster adventure in space! Buckle up and get ready for blastoff!",
    "Our hamster space program continues to make strides in the exploration of the universe. Join us for today's launch!",
    "Are you ready for some high-flying hamster action? We're about to launch another furry friend into the cosmos!",
    "The Hamster Space Program is excited to announce another launch! Let's see where our intrepid adventurer will end up today!",
    "Get ready for some hamster space madness! We're launching another brave little explorer into the great unknown!",
    "Today's hamster space launch is sure to be out of this world! Join us as we send another furry friend into the void!",
    "It's time for another thrilling hamster space launch! Let's see where our little adventurers end up today!",
    "Hold on tight, folks! It's time for another hamster space mission! Get ready for launch!",
    "The Hamster Space Program is proud to present another launch! Join us as we send another little hero into the vast reaches of space!"
]

# Generate an introduction for the hamster space program
intro = random.choice(intros)
print(f"{BLUE}{intro}{RESET}")
print(f"{YELLOW}Time to Prepare for Launch!{RESET}")
print(f"{RED}-----------------------------------{RESET}")

# Initialize the hamster launch counter
launches = 0

# Loop until the program is manually stopped
while True:
    # Wait for a random interval of no more than one minute
    time.sleep(random.randint(1, 45))
    
    # Generate a random hamster name
    name = random.choice(prefixes) + random.choice(middle) + random.choice(suffixes)
    
    # Choose a random destination for the hamster
    destination = random.choice(destinations)
    

    # Generate a short bio about the hamster
    bios = [
        f"{name} is a daring adventurer, always seeking new challenges in the vast expanse of space. Their tenacity and fearlessness make them a valuable member of the team.",
        f"{name} is a curious explorer, constantly seeking out new worlds and discoveries. Their insatiable hunger for knowledge drives them ever forward, always pushing the boundaries of what is known.",
        f"{name} is a resourceful problem solver, able to find creative solutions to even the most complex of issues. Their ingenuity and adaptability have saved the mission more times than anyone can count.",
        f"{name} is a born leader, commanding the respect and admiration of their fellow hamsters. Their charisma and confidence inspire others to push themselves to new heights.",
        f"{name} is a master of strategy, always thinking several steps ahead of the game. Their tactical mind and quick thinking have led the team to many hard-won victories.",
        f"{name} is a dedicated scientist, committed to unlocking the secrets of the universe. Their thirst for knowledge and unrelenting focus have propelled the mission forward.",
        f"{name} is a skilled technician, able to repair and maintain even the most complex machinery. Their attention to detail and precision have kept the mission running smoothly.",
        f"{name} is a gifted artist, able to find beauty in even the most desolate of landscapes. Their creativity and imagination bring a sense of wonder and awe to the crew.",
        f"{name} is a fearless pilot, capable of navigating the most treacherous of space environments. Their steady hand and nerves of steel have saved the team from disaster more times than they can count.",
        f"{name} is a talented communicator, able to bridge the gaps between different cultures and species. Their empathy and understanding make them a valuable asset to the team.",
        f"{name} is a natural diplomat, able to negotiate even the most challenging of diplomatic situations. Their tact and diplomacy have helped to smooth over many tense moments on the mission.",
        f"{name} is a true visionary, always looking beyond the horizon to what lies ahead. Their optimism and forward thinking inspire hope and excitement in the crew.",
        f"{name} is a skilled survivalist, able to thrive even in the most hostile of environments. Their toughness and resilience have seen them through many tough times on the mission.",
        f"{name} is a gifted storyteller, able to captivate their audience with tales of adventure and wonder. Their charm and wit bring a sense of levity and humor to the crew.",
        f"{name} is a true romantic, always seeing the beauty in the world around them. Their passion and intensity bring a sense of warmth and love to the mission.",
        f"{name} is a dedicated healer, committed to ensuring the health and well-being of their fellow hamsters. Their compassion and kindness have earned them the respect and admiration of all who know them.",
        f"{name} is a fierce warrior, always ready to defend the mission against any threat. Their bravery and ferocity have kept the team safe in many dangerous situations.",
        f"{name} is a skilled chef, able to turn even the most basic of ingredients into a culinary masterpiece. Their creativity and flair bring a sense of comfort and home to the crew.",
        f"{name} is a tireless worker, always putting in the extra effort to ensure the mission's success. Their diligence and hard work are an inspiration to all who know them.",
        f"{name} is a true optimist, always seeing the bright side of any situation. Their positivity and enthusiasm bring a sense of joy and hope to the crew."
]

    bio = random.choice(bios)

    # Print the hamster bio
    print(f"{BLUE}{bio}{RESET}")

    time.sleep(3)

    # Print a message saying that a hamster is being launched
    launches += 1
    print(f"{RED}>>{RESET}{YELLOW}Launching hamster {name} to {destination}.{RESET}{RED}<<{RESET}")

    # Print the current number of hamster launches
    print(f"{GREEN}Total hamster launches: {launches}{RESET}")
    print(f"{RED}-----------------------------------{RESET}")
