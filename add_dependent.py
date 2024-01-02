import re  

# Path to the local markdown file  
file_path = 'README.md'  
  
# # Regular expression to match URLs enclosed in parentheses  
url_pattern = re.compile(r'\(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\)')  
# # Regular expression to match Github project URLs  
# github_url_pattern = re.compile(r'^https://github.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/?$')  
# Regular expression to match Github project URLs with optional additional paths  
github_url_pattern = re.compile(r'^https://github.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(/.*)?/?$') 


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

# Save the github_links into file
with open('github_links.txt', 'w') as f:  
    for link in github_links:  
        f.write(link + '\n')


# Start the go.mod file with the module line  
go_mod = "module https://github.com/youngfish42/Awesome-FL\n\n"  # replace "mymodule" with your module name  
# Add the Go version  
go_mod += "go 1.16\n\n"  # replace "1.16" with your Go version  
# Start the require block  
go_mod += "require (\n"  
# Add the dependencies  
for link in github_links:  
    # Remove http:// or https:// from the URL  
    link = link.replace('http://', '').replace('https://', '')
    go_mod += f"    {link} v0.0.0 // indirect\n"  # replace "v0.0.0" with the actual version if known  
# End the require block  
go_mod += ")\n"  
  
# Save the go.mod file  
with open('go.mod', 'w') as f:  
    f.write(go_mod)  