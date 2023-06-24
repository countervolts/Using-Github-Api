# GitHub API Python Client

This Python program allows you to interact with the GitHub API using your Personal Access Token (API key). It provides various functionalities to search for repositories, clone repositories, create repositories, upload files, and write files in repositories.

## How to Use

1. Clone the repository to your local machine.
2. Install the required dependencies using the following command:
   ```
   pip install requests base64
   ```
3. Run the program using the following command:
   ```
   python API.py
   ```
4. The program will automatically prompt you to enter your GitHub API key (Personal Access Token). Follow these steps to obtain your API key:
   - Go to [GitHub Settings](https://github.com/settings/profile).
   - Click on "Developer settings" in the left sidebar.
   - Click on "Personal access tokens".
   - Generate a new token with the necessary scopes (e.g., repo access for creating and managing repositories).
5. Enter your GitHub API key (Personal Access Token) when prompted by the program.
6. Once authenticated, you can choose from the available options in the main menu to interact with the GitHub API.

## Functionality

The GitHub API Python Client provides the following functionalities:

1. **Search repositories**: Enter a search term to find repositories matching the search query. Choose a repository to view its details and optionally clone it.

2. **Clone a repository**: Enter the name of the repository you want to clone. The program will clone the repository and display the file path where it was cloned.

3. **List user repositories**: Enter a GitHub username to view a list of repositories owned by that user.

4. **Create a repository**: Enter a name for the new repository. The program will create a new repository on your GitHub account.

5. **Upload a file**: Enter the name of the repository where you want to upload a file and provide the file path of the file you want to upload. The program will upload the file to the specified repository.

6. **Write a file**: Enter the name of the repository where you want to write a file, provide the name of the file to write, and enter the content to write into the file. The program will create or update the file in the specified repository.

## Note

- Replace the `<OWNER_USERNAME>` placeholders in the code with the actual owner's username in the respective API URLs.

- Make sure to keep your GitHub API key (access token) confidential. Do not share it with others or commit it to version control systems.

- For more information about the GitHub API and how to generate a Personal Access Token, refer to the [GitHub Developer Documentation](https://docs.github.com/en/rest/).

- Feel free to update the code if you would like to add more functionality to the code.
