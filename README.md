# LeetCode Exercises in Python

[![CI](https://github.com/illuminatus503/LeetCode-Exercises/actions/workflows/ci.yml/badge.svg)](https://github.com/illuminatus503/LeetCode-Exercises/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/illuminatus503/LeetCode-Exercises/branch/main/graph/badge.svg)](https://codecov.io/gh/illuminatus503/LeetCode-Exercises)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Description

This repository contains my solutions to LeetCode problems implemented in **Python**. Its purpose is to practice algorithms and data structures, improve my coding skills, and share knowledge with the community.

## Repository Structure

- **`src/`**
  - `easy/` — solutions to “Easy” problems
  - `medium/` — solutions to “Medium” problems
  - `hard/` — solutions to “Hard” problems
- **`tests/`**
  - `easy/` — unit tests for Easy solutions
  - `medium/` — unit tests for Medium solutions
  - `hard/` — unit tests for Hard solutions
- **`CHANGELOG.md` — a record of changes
- **`LICENSE`** — project license (MIT)
- **`README.md` — this file
- **`requirements.txt`** — project dependencies (e.g. `pytest`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/illuminatus503/LeetCode-Exercises.git
   cd leetcode-exercises
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- To run all tests:
  ```bash
  pytest
  ```

- To run tests for a specific difficulty level, e.g. Easy:
  ```bash
  pytest tests/easy
  ```

<!-- 
## Contributing

1. Fork the repository.
2. Create a new branch for your feature or fix:
   git checkout -b feature/your-feature
3. Add your solution under the appropriate `src/<difficulty>/` folder and write corresponding tests in `tests/<difficulty>/`.
4. Ensure all tests pass:
   pytest
5. Commit your changes and push to your fork:
   git add .
   git commit -m "Add solution for [problem name]"
   git push origin feature/your-feature
6. Open a pull request describing your contribution.

-->
## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

> “Keep learning, keep coding.” 🚀
