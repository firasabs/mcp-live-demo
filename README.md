# MCP Live Demo

A tiny Python command-line task manager used to demonstrate how an AI assistant can work with a real GitHub repository through an MCP server.

## What this project does

The program stores tasks in a local JSON file and lets a user:

- List all tasks
- Add a new task
- Mark a task as completed

The project intentionally stays small so it is easy to inspect during a live MCP demonstration.

## Project structure

```text
mcp-live-demo/
├── app.py
├── tasks.json
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- No external Python packages are required

## Run the project

List tasks:

```bash
python app.py list
```

Add a task:

```bash
python app.py add "Prepare MCP presentation"
```

Complete a task:

```bash
python app.py complete 1
```

## Example

```text
$ python app.py list
[ ] 1. Prepare MCP presentation
[x] 2. Test GitHub MCP connection
```

## Known limitations

- Tasks cannot currently be deleted.
- Task IDs are simple integers.
- The app stores data only in a local JSON file.

## Why this repository exists

This repository is intentionally designed for a live MCP demo.

An AI assistant connected to GitHub through MCP can:

1. Read this README and explain the project.
2. Inspect `app.py`.
3. Check open GitHub issues.
4. Create a new issue.
5. Suggest improvements based on the repository contents.

That makes it easy to demonstrate the difference between the AI model deciding what it needs and the MCP server actually interacting with GitHub.
