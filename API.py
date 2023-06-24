import os
import requests
import base64

base_url = "https://api.github.com"
access_token = ""

def get_user_input(prompt):
    return input(prompt).strip()

def get_user_info():
    global access_token
    if os.path.isfile("key"):
        with open("key", "r") as file:
            access_token = file.read().strip()
    else:
        print("Welcome to the GitHub API Python Client!")
        print("Please provide your GitHub Personal Access Token (API key).")
        print("If you don't have one, you can generate it following the instructions in the README.")
        access_token = get_user_input("Enter your GitHub API key: ")
        with open("key", "w") as file:
            file.write(access_token)

def search_repositories(search_term, page):
    url = f"{base_url}/search/repositories"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {
        "q": search_term,
        "per_page": 5,
        "page": page
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data["items"]

def get_repository_description(repo_fullname):
    url = f"{base_url}/repos/{repo_fullname}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data.get("description", "No description available.")

def get_repository_size(repo_fullname):
    url = f"{base_url}/repos/{repo_fullname}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data.get("size", 0)

def clone_repository(repo_name):
    choice = get_user_input(f"Do you want to clone the repository '{repo_name}'? (Y/N): ")
    if choice.lower() == "y":
        print("Cloning repository...")
        repo_fullname = f"<OWNER_USERNAME>/{repo_name}"  # replace <OWNER_USERNAME> with the actual owner username
        repo_size = get_repository_size(repo_fullname)
        print(f"Cloned repository to: /path/to/repo/{repo_name}")  # replace with the actual file path
        print(f"Total size: {repo_size} KB")

def list_user_repositories(username):
    url = f"{base_url}/users/{username}/repos"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    repositories = response.json()
    if repositories:
        print(f"Repositories for {username}:")
        for repo in repositories:
            print(f"- {repo['name']}")
    else:
        print("No repositories found.")

def create_repository(repo_name):
    url = f"{base_url}/user/repos"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "name": repo_name,
        "auto_init": True
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
    else:
        print(f"Failed to create repository '{repo_name}'. Please try again.")

def upload_file(repo_name, file_path):
    url = f"{base_url}/repos/<OWNER_USERNAME>/{repo_name}/contents/{file_path}"  # replace <OWNER_USERNAME> with the actual owner username
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    with open(file_path, "rb") as file:
        file_content = file.read()
    encoded_content = base64.b64encode(file_content).decode("utf-8")
    payload = {
        "message": "Upload file",
        "content": encoded_content
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 201:
        print(f"File '{file_path}' uploaded successfully.")
    else:
        print(f"Failed to upload file '{file_path}'. Please try again.")

def write_file(repo_name, file_path, content):
    url = f"{base_url}/repos/<OWNER_USERNAME>/{repo_name}/contents/{file_path}"  # replace <OWNER_USERNAME> with the actual owner username
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    payload = {
        "message": "Write file",
        "content": encoded_content
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 201:
        print(f"File '{file_path}' written successfully.")
    else:
        print(f"Failed to write file '{file_path}'. Please try again.")

def main_menu():
    while True:
        print("\n--- GitHub API Python Client ---")
        print("1. Search repositories")
        print("2. Clone a repository")
        print("3. List user repositories")
        print("4. Create a repository")
        print("5. Upload a file")
        print("6. Write a file")
        print("0. Exit")
        choice = get_user_input("Enter your choice: ")
        if choice == "1":
            search_term = get_user_input("Enter a search term for repositories: ")
            page = 1
            while True:
                repositories = search_repositories(search_term, page)
                num_results = min(len(repositories), 5)
                for i in range(num_results):
                    print(f"{i+1}. {repositories[i]['name']}")
                if num_results == 0:
                    print("No more repositories found.")
                    break
                choice = get_user_input("Enter the number of the repository to choose (N for next page): ")
                if choice.lower() == "n":
                    page += 1
                    continue
                elif choice.isdigit() and 1 <= int(choice) <= num_results:
                    repo = repositories[int(choice)-1]
                    description = get_repository_description(repo["full_name"])
                    print(f"\nRepository: {repo['full_name']}")
                    print(f"Description: {description}")
                    clone_repository(repo["name"])
                    go_back = get_user_input("Press enter to go back to the list or enter any key to exit: ")
                    if not go_back:
                        continue
                    else:
                        break
                else:
                    print("Invalid choice. Exiting...")
                    break
        elif choice == "2":
            repo_name = get_user_input("Enter the name of the repository to clone: ")
            clone_repository(repo_name)
        elif choice == "3":
            username = get_user_input("Enter the GitHub username to list repositories: ")
            list_user_repositories(username)
        elif choice == "4":
            repo_name = get_user_input("Enter the name for the new repository: ")
            create_repository(repo_name)
        elif choice == "5":
            repo_name = get_user_input("Enter the name of the repository to upload a file: ")
            file_path = get_user_input("Enter the path of the file to upload: ")
            upload_file(repo_name, file_path)
        elif choice == "6":
            repo_name = get_user_input("Enter the name of the repository to write a file: ")
            file_path = get_user_input("Enter the name of the file to write: ")
            content = get_user_input("Enter the content to write: ")
            write_file(repo_name, file_path, content)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    get_user_info()
    main_menu()

if __name__ == "__main__":
    main()
