import re  
from markdown import markdown  
from bs4 import BeautifulSoup  
  
# Path to the local markdown file  
file_path = 'README.md'  
  
# Regular expression to match Github project URLs with optional additional paths  
github_url_pattern = re.compile(r'^https://github.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(/.*)?/?$')  
  
github_links = set()  # Use a set to automatically remove duplicates  
  
# Read the markdown file  
with open(file_path, 'r', encoding='utf-8') as f:  
    md_content = f.read()  
  
# Convert markdown to HTML  
html_content = markdown(md_content)  
  
# Parse HTML  
soup = BeautifulSoup(html_content, 'html.parser')  
  
# Find all links  
for link in soup.find_all('a'):  
    url = link.get('href')  
    # Filter out Github project URLs and add them to the set  
    if url and re.match(github_url_pattern, url):  
        github_links.add(url)  
  
# Start the go.mod file with the module line  
go_mod = "https://github.com/youngfish42/Awesome-FL\n\n"  # replace "mymodule" with your module name  
  
# Add the Go version  
go_mod += "go 1.16\n\n"  # replace "1.16" with your Go version  
  
# Start the require block  
go_mod += "require (\n"  
  
# Add the dependencies  
for link in github_links:  
    go_mod += f"    {link} v0.0.0\n"  # replace "v0.0.0" with the actual version if known  
  
# End the require block  
go_mod += ")\n"  
  
# Save the go.mod file  
with open('go.mod', 'w') as f:  
    f.write(go_mod)  