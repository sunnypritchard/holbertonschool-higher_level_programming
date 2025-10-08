# cURL (Client URL)

cURL is a command-line tool and library for transferring data with URLs. It supports various protocols, including HTTP, HTTPS, FTP, and more. cURL is widely used for testing APIs, downloading files, and automating web requests.

## Installation
cURL is pre-installed on most Unix-based systems (Linux, macOS). For Windows, you can download it from the [official cURL website](https://curl.se/download.html).
To check if cURL is installed, run:
```bash
curl --version
```
If it's not installed, you can install it using your package manager. For example, on Ubuntu:
```bash
sudo apt-get install curl
```
On macOS, you can use Homebrew:
```bash
brew install curl
```

## Basic Usage
The basic syntax for using cURL is:
```bash
curl [options] [URL]
```

### Common Options
- `-X, --request <command>`: Specify the request method to use (e.g., GET, POST, PUT, DELETE).
- `-d, --data <data>`: Send specified data in a POST request.
- `-H, --header <header>`: Add a header to the request.
- `-i, --include`: Include the HTTP response headers in the output.
- `-o, --output <file>`: Write the output to a file instead of stdout.
- `-L, --location`: Follow redirects.
- `-u, --user <user:password>`: Specify user and password for server authentication.
- `-I, --head`: Fetch the headers only.

### Examples

1. Feching posts from JSONPlaceholder:
```bash
curl https://jsonplaceholder.typicode.com/posts
``` 

This command retrieves a list of posts from the JSONPlaceholder API, each having an userId, ID, title, and body.

2. Feching only the headers:
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```
This command retrieves only the HTTP headers showing status code, content type, and other metadata.

3. Making a POST request:
```bash
curl -X POST https://jsonplaceholder.typicode.com/posts -d '{"title":"foo","body":"bar","userId":1}' -H "Content-Type: application/json"
```
This command creates a new post by sending a JSON payload with title, body, and userId to the server.