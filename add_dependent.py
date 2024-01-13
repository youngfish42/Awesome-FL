import re
import requests
import time

# Path to the local markdown file  
file_path = 'README.md'  
  
# # Regular expression to match URLs enclosed in parentheses  
url_pattern = re.compile(r'\(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\)')  
# # Regular expression to match Github project URLs  
github_url_pattern = re.compile(r'^http[s]?://github.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/?$')  
# Regular expression to match Github project URLs with optional additional paths  
# github_url_pattern = re.compile(r'^http[s]?://github.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(/.*)?/?$') 


github_links = set()  # Use a set to automatically remove duplicates  

# Read the markdown file  
with open(file_path, 'r', encoding='utf-8') as f:  
    for line in f:  
        # Find all URLs in the line  
        urls = re.findall(url_pattern, line)  
        # Remove parentheses from URLs  
        urls = [url[1:-1] for url in urls]  
        # Filter out Github project URLs and add them to the set  
        github_links.update([url for url in urls if re.match(github_url_pattern, url)])  

# Sort the links
github_links = sorted(github_links)

# Save the github_links into file
with open('github_links.txt', 'w') as f:  
    for link in github_links:  
        f.write(link + '\n')

# Get the commit hashes for each project
commit_hashes = {}  
headers = {"Authorization": "Input Your key"}  # replace "your_token" with your Github token
for link in github_links:
    try:
        # Remove http:// or https:// from the URL  
        link = link.replace('http://', '').replace('https://', '')
        owner, repo = link.split("/")[1:3]  
        url = f"https://api.github.com/repos/{owner}/{repo}/commits/main"  
        response = requests.get(url,headers=headers)  
        response.raise_for_status()  
        commit_hashes[link] = response.json()["sha"]
        print(f"Got commit hash for {link}: {commit_hashes[link]}")
    except requests.exceptions.HTTPError as e:  
        if e.response.status_code == 422:  
            print(f"'main' branch not found for {link}, trying 'master' branch")  
            try:  
                url = f"https://api.github.com/repos/{owner}/{repo}/commits/master"
                response = requests.get(url,headers=headers)  
                response.raise_for_status()  
                commit_hashes[link] = response.json()["sha"]  
            except Exception as e:  
                print(f"Error fetching commit info for {link}: {e}")  
        else:  
            print(f"Error fetching commit info for {link}: {e}")  
    except Exception as e:
        print(f"Error getting commit hash for {link}: {e}")
    time.sleep(61)  # Wait 61 second to avoid rate limiting


# Start the go.mod file with the module line  
go_mod = "module github.com/youngfish42/Awesome-FL\n\n"  # replace "mymodule" with your module name  
# Add the Go version  
go_mod += "go 1.16\n\n"  # replace "1.16" with your Go version  
# Start the require block  
go_mod += "require (\n"  
# Add the dependencies  
for link,hash in commit_hashes.items():  
    go_mod += f"    {link} {hash} // indirect\n"  #
# End the require block  
go_mod += ")\n"  
  
# Save the go.mod file  
with open('go.mod', 'w') as f:  
    f.write(go_mod)  