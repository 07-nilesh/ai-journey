import urllib.robotparser  # Standard library built into Python to parse robots.txt files
try:
# Step 1: Initialize the robot parser tool
    robot_gatekeeper = urllib.robotparser.RobotFileParser()

# Step 2: Point it directly to the website's root notice board
    robot_gatekeeper.set_url("http://books.toscrape.com/robots.txt")

# Step 3: Read and download the rules from the site
    robot_gatekeeper.read()

# Step 4: Define the specific URL path you intend to scrape
    target_page = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

# Step 5: Ask the gatekeeper if your scraper (User-Agent: '*') is legally allowed to touch that page
    is_allowed = robot_gatekeeper.can_fetch("*", target_page)

# Step 6: Print out the final verdict
    print(f"Is it ethically safe to scrape this page? {is_allowed}")

    URLs =["/catalogue/book1.html", "/admin/delete-database", "/catalogue/book2.html"]
    for url in URLs:
        if robot_gatekeeper.can_fetch("*", url):
            print(f"Allowed to scrape: {url}")
        else:
            print(f"Not allowed to scrape: {url}")
except Exception as e:
    print(f"An error occurred while checking robots.txt: {e}")