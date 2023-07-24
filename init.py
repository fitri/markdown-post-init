import os
import re
import datetime

def slugify(title):
    # Remove special characters and convert spaces to hyphens
    return re.sub(r'[^a-zA-Z0-9\s]', '', title).strip().lower().replace(' ', '-')

def create_pelican_post(title, date):
    content = f"""Title: {title}
Date: {date}

Write your content here...
"""
    return content

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def main():
    title = input("Enter the title: ")
    date = datetime.date.today().strftime('%Y-%m-%d')
    slug = slugify(title)
    filename = f"{slug}.md"

    content = create_pelican_post(title, date)
    save_to_file(filename, content)

    print(f"Pelican post '{filename}' has been created with the metadata.")

if __name__ == "__main__":
    main()
