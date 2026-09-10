# Contributing to Network Log Traffic Analyzer

First off, thank you for considering contributing to Network Log Traffic Analyzer! It's people like you that make this tool valuable for the community.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How You Can Contribute](#how-you-can-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Your First Contribution](#your-first-contribution)
- [Development Setup](#development-setup)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Documentation](#documentation)
- [Community](#community)

## Code of Conduct

This project adheres to a Contributor Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

### Our Pledge

We pledge to make participation in this project a harassment-free experience for everyone, regardless of level of experience, gender, gender identity and expression, sexual orientation, disability, personal appearance, body size, race, ethnicity, age, religion, or nationality.

## How You Can Contribute

### 1. Reporting Bugs

Found a bug? Create an issue with:
- Clear description
- Steps to reproduce
- Expected vs actual behavior
- Environment details

### 2. Suggesting Features

Have an idea? Share it:
- Describe the use case
- Explain the benefit
- Provide examples

### 3. Code Contributions

- Fix bugs
- Add new features
- Improve performance
- Refactor code
- Add tests

### 4. Documentation

- Fix typos
- Clarify unclear sections
- Add examples
- Create tutorials
- Translate to other languages

### 5. Testing

- Test on different OS (Ubuntu, Debian, CentOS, etc.)
- Test with different Python versions (3.10, 3.11, 3.12)
- Test with large log files
- Report issues

### 6. Community Support

- Answer questions in issues
- Help newcomers
- Share knowledge
- Mentor new contributors

### 7. Spread the Word

- Star the repository
- Share on social media
- Write blog posts
- Talk at meetups/conferences
- Recommend to colleagues

## Reporting Bugs

### Before Creating a Bug Report

1. **Check existing issues** - Search open and closed issues
2. **Test latest version** - Bug might already be fixed
3. **Gather information**:
   ```bash
   # Python version
   python3 --version

   # OS info
   cat /etc/os-release
   uname -a

   # Package version
   netlog-traffic --version

   # Check dependencies
   pip list | grep -E "pytest|black|flake8"
   ```

### Bug Report Template

```markdown
### Description
A clear and concise description of what the bug is.

### Steps to Reproduce
1. Install package: `pip install -e .`
2. Run command: `netlog-traffic firewall.csv --output-dir output`
3. See error: [paste error message]

### Expected Behavior
A clear description of what you expected to happen.

Example:
```
Expected output:
✓ Analyzed 1000 entries
✓ Actions: {'ALLOW': 800, 'DENY': 200}
✓ Reports: output/analysis_report.json, output/blocked_connections.csv
```

### Actual Behavior
What actually happened.

Example:
```
Actual output:
Traceback (most recent call last):
  File ".../cli.py", line 45, in main
    result = analyze_logs(entries)
  File ".../analyzer.py", line 23, in analyze_logs
    logs = list(entries)
TypeError: 'NoneType' object is not iterable
```

### Environment
- **OS**: Ubuntu 22.04.3 LTS
- **Python**: 3.10.12
- **Package version**: 1.0.0
- **Installation method**: pip install -e .

### Additional Context
Add any other context about the problem here.

- Are you using custom log format?
- How large is the log file?
- Does it happen with sample_logs.csv?
- Any recent changes to your system?

### Possible Solution
If you have ideas on how to fix it, share them!

### Screenshots
If applicable, add screenshots to help explain your problem.
```

## Suggesting Features

### Before Suggesting a Feature

1. **Check existing issues** - Feature might already be requested
2. **Check documentation** - Feature might already exist
3. **Consider scope** - Does it fit the project's goals?

### Feature Request Template

```markdown
### Problem Statement
What problem are you trying to solve?

Example:
"I'm analyzing firewall logs from multiple sources and need to compare them, but currently I can only analyze one file at a time."

### Proposed Solution
Describe the solution you'd like.

Example:
"Add support for analyzing multiple log files in a single run and generating comparative reports."

### Use Cases
Who would benefit from this feature?

Example:
- SOC analysts comparing logs from different time periods
- Security researchers analyzing logs from multiple systems
- Compliance auditors reviewing logs across infrastructure

### Examples
Show how the feature would work.

Example:
```bash
# Analyze multiple files
netlog-traffic logs1.csv logs2.csv logs3.csv --output-dir comparison

# Compare with wildcards
netlog-traffic logs-2026-09-*.csv --output-dir monthly-report

# Aggregate mode
netlog-traffic *.csv --aggregate --output-dir combined-report
```

### Alternatives Consider
What alternatives have you considered?

Example:
- Writing a bash script to merge files first
- Running tool multiple times and manually comparing
- Using different tool altogether

### Additional Context
Any other relevant information, mockups, or references.
```

## Your First Contribution

### Good First Issues

Look for issues labeled:
- `good first issue` - Perfect for beginners
- `help wanted` - Need community help
- `documentation` - Improve docs
- `tests` - Add test coverage

### Step-by-Step Guide

#### 1. Set Up Development Environment

```bash
# Fork the repository on GitHub

# Clone your fork
git clone https://github.com/YOUR_USERNAME/network-log-traffic-analyzer.git
cd network-log-traffic-analyzer

# Add upstream remote
git remote add upstream https://github.com/ORIGINAL_USERNAME/network-log-traffic-analyzer.git

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Verify installation
netlog-traffic --help
pytest tests/ -v
```

#### 2. Pick an Issue

- Browse issues labeled `good first issue`
- Read the issue carefully
- Ask questions if something is unclear
- Comment that you'd like to work on it

#### 3. Create a Branch

```bash
# Make sure you're on main branch
git checkout main

# Pull latest changes from upstream
git pull upstream main

# Create feature branch
git checkout -b fix/issue-123-bug-in-parser
# or
git checkout -b feat/add-jsonl-support
```

#### 4. Make Changes

```bash
# Edit files
vim src/network_log_traffic_analyzer/parser.py

# Run tests frequently
pytest tests/ -v

# Check code style
black src/ tests/
flake8 src/ tests/

# Commit changes
git add .
git commit -m "fix: Handle empty CSV files gracefully

- Add check for empty file in parse_csv_logs()
- Raise ValueError with clear message
- Add test case for empty file

Fixes #123"
```

#### 5. Push and Create PR

```bash
# Push to your fork
git push origin fix/issue-123-bug-in-parser

# Create PR on GitHub
# Go to: https://github.com/ORIGINAL_USERNAME/network-log-traffic-analyzer/compare
# Select your branch and create pull request
```

## Development Setup

### Prerequisites

- **Python**: 3.10 or higher
- **Git**: Latest version
- **Text Editor**: VS Code, PyCharm, Vim, etc.
- **Terminal**: Bash, Zsh, or similar

### Installation

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/network-log-traffic-analyzer.git
cd network-log-traffic-analyzer

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate

# Install in editable mode
pip install -e .

# Install development dependencies
pip install -r requirements-dev.txt

# Or install individually:
pip install pytest pytest-cov black flake8 mypy
```

### Verify Setup

```bash
# Check Python version
python3 --version  # Should be 3.10+

# Check package installation
netlog-traffic --version

# Run tests
pytest tests/ -v

# Check code style
flake8 src/ tests/

# Run with sample data
netlog-traffic data/sample_logs.csv --output-dir output

# Verify output files exist
ls -lh output/
```

### IDE Setup

#### VS Code

```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.testing.pytestEnabled": true,
    "editor.formatOnSave": true,
    "editor.rulers": [100]
}
```

#### PyCharm

1. Open project in PyCharm
2. Go to Settings → Project → Python Interpreter
3. Add virtual environment (venv)
4. Enable pytest in Settings → Tools → Python Integrated Tools
5. Enable black formatter in Settings → Tools → Black

### Development Workflow

```bash
# Start your day
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feat/your-feature

# Make changes
vim src/...

# Run tests
pytest tests/ -v

# Format code
black src/ tests/

# Check style
flake8 src/ tests/

# Commit
git add .
git commit -m "feat: Add your feature"

# Push
git push origin feat/your-feature
```

## Code Style Guidelines

### General Principles

- **Readability**: Code should be easy to read and understand
- **Consistency**: Follow existing patterns in the codebase
- **Simplicity**: Keep it simple (KISS principle)
- **Documentation**: Document why, not just what

### Python Style

Follow [PEP 8](https://pep8.org/) and [PEP 257](https://pep257.org/):

```python
"""Module docstring describing purpose."""

from dataclasses import dataclass
from typing import Iterable, Optional
import logging

logger = logging.getLogger(__name__)


@dataclass
class LogEntry:
    """Represents a parsed log entry.

    Attributes:
        timestamp: When the log event occurred
        src_ip: Source IP address
        dst_ip: Destination IP address
        src_port: Source port number
        dst_port: Destination port number
        protocol: Network protocol (TCP, UDP, etc.)
        action: Firewall action (ALLOW, DENY, DROP)
        bytes_sent: Bytes sent (optional)
        bytes_recv: Bytes received (optional)
    """

    timestamp: Optional[datetime]
    src_ip: str
    dst_ip: str
    src_port: Optional[int]
    dst_port: Optional[int]
    protocol: str
    action: str
    bytes_sent: Optional[int] = None
    bytes_recv: Optional[int] = None


def parse_csv_logs(path: Path) -> Iterable[LogEntry]:
    """Parse CSV format log files.

    Args:
        path: Path to CSV file containing log entries

    Yields:
        LogEntry objects for each row in the CSV file

    Raises:
        FileNotFoundError: If the specified file does not exist
        ValueError: If the CSV format is invalid
        UnicodeDecodeError: If the file is not valid UTF-8

    Example:
        >>> entries = list(parse_csv_logs(Path("firewall.csv")))
        >>> len(entries)
        1000
    """
    if not path.exists():
        raise FileNotFoundError(f"Log file not found: {path}")

    try:
        with path.open(newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            # Validate required columns
            required = {"src_ip", "dst_ip", "action"}
            if not required.issubset(set(reader.fieldnames or [])):
                raise ValueError(f"CSV missing required columns: {required}")

            for row_num, row in enumerate(reader, start=2):
                try:
                    yield _to_entry(row)
                except Exception as e:
                    logger.warning(f"Skipping invalid row {row_num}: {e}")

    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(
            f"File must be UTF-8 encoded: {path}"
        ) from e
```

### Naming Conventions

```python
# Variables and functions: snake_case
log_entries = []
def parse_csv_logs():
    pass

# Classes: PascalCase
class LogEntry:
    pass

# Constants: UPPER_CASE
MAX_ENTRIES = 10000
DEFAULT_TOP_N = 10

# Private functions: _prefix
def _internal_helper():
    pass

# Test functions: test_ prefix
def test_parse_csv_logs():
    pass
```

### Type Hints

Use type hints for all function signatures:

```python
from typing import Iterable, Optional, Dict, List, Tuple

def analyze_logs(
    entries: Iterable[LogEntry],
    top_n: int = 10
) -> AnalysisResult:
    """Analyze log entries and compute statistics."""
    pass

def get_top_ips(
    entries: List[LogEntry],
    n: int = 10
) -> List[Tuple[str, int]]:
    """Get top N source IPs by connection count."""
    pass

def format_report(
    result: AnalysisResult,
    output_dir: Path
) -> Dict[str, Path]:
    """Format and write analysis reports."""
    pass
```

### Error Handling

```python
def parse_csv_logs(path: Path) -> Iterable[LogEntry]:
    """Parse CSV logs with proper error handling."""

    # Check file exists
    if not path.exists():
        raise FileNotFoundError(f"Log file not found: {path}")

    # Check file is readable
    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")

    try:
        with path.open(newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                # Validate row
                if "action" not in row:
                    raise ValueError(f"Missing 'action' column in row")

                yield _to_entry(row)

    except csv.Error as e:
        raise ValueError(f"Invalid CSV format: {e}") from e
    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(
            "File must be UTF-8 encoded. "
            "Convert using: iconv -f ISO-8859-1 -t UTF-8 input.csv > output.csv"
        ) from e
```

### Logging

```python
import logging

logger = logging.getLogger(__name__)

def analyze_logs(entries: Iterable[LogEntry]) -> AnalysisResult:
    """Analyze logs with appropriate logging."""

    logger.debug("Starting log analysis")

    logs = list(entries)
    logger.info(f"Loaded {len(logs)} log entries")

    if len(logs) == 0:
        logger.warning("No log entries to analyze")

    blocked = [e for e in logs if e.action in {"DENY", "DROP", "BLOCK"}]
    logger.info(f"Found {len(blocked)} blocked connections")

    if len(blocked) > len(logs) * 0.5:
        logger.warning(
            f"High block rate: {len(blocked)/len(logs)*100:.1f}% of connections blocked"
        )

    return AnalysisResult(...)
```

## Testing

### Running Tests

```bash
# All tests
pytest tests/

# Verbose output
pytest tests/ -v

# With coverage
pytest --cov=src/network_log_traffic_analyzer tests/

# Coverage report
pytest --cov=src/ tests/ --cov-report=html
firefox htmlcov/index.html

# Specific test file
pytest tests/test_analyzer.py -v

# Specific test function
pytest tests/test_analyzer.py::TestAnalyzer::test_blocked_detection -v

# Fail fast
pytest tests/ -x

# Stop after first failure
pytest tests/ --maxfail=1
```

### Writing Tests

```python
"""Tests for analyzer module."""

import unittest
from pathlib import Path
from analyzer import analyze_logs
from parser import LogEntry


class TestAnalyzer(unittest.TestCase):
    """Test analyzer functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.sample_entries = [
            LogEntry(None, "192.168.1.1", "10.0.0.1", 50000, 443, "TCP", "ALLOW"),
            LogEntry(None, "192.168.1.2", "10.0.0.2", 50001, 22, "TCP", "DENY"),
            LogEntry(None, "192.168.1.3", "10.0.0.3", 50002, 3389, "TCP", "DROP"),
        ]

    def test_total_entries_count(self):
        """Test that total entries are counted correctly."""
        result = analyze_logs(self.sample_entries)
        self.assertEqual(result.total_entries, 3)

    def test_blocked_connections_detection(self):
        """Test that DENY and DROP actions are detected as blocked."""
        result = analyze_logs(self.sample_entries)
        self.assertEqual(len(result.blocked_connections), 2)
        self.assertEqual(result.action_counts["DENY"], 1)
        self.assertEqual(result.action_counts["DROP"], 1)

    def test_empty_log_handling(self):
        """Test that empty log files are handled gracefully."""
        result = analyze_logs([])
        self.assertEqual(result.total_entries, 0)
        self.assertEqual(len(result.blocked_connections), 0)

    def test_top_ips_ranking(self):
        """Test that top IPs are ranked by frequency."""
        entries = [
            LogEntry(None, "192.168.1.1", "10.0.0.1", 50000, 443, "TCP", "ALLOW"),
            LogEntry(None, "192.168.1.1", "10.0.0.2", 50001, 80, "TCP", "ALLOW"),
            LogEntry(None, "192.168.1.1", "10.0.0.3", 50002, 22, "TCP", "ALLOW"),
            LogEntry(None, "192.168.1.2", "10.0.0.1", 50003, 443, "TCP", "ALLOW"),
        ]
        result = analyze_logs(entries)
        self.assertEqual(result.top_src_ips[0][0], "192.168.1.1")
        self.assertEqual(result.top_src_ips[0][1], 3)

    def test_protocol_distribution(self):
        """Test protocol counting."""
        entries = [
            LogEntry(None, "192.168.1.1", "10.0.0.1", 50000, 443, "TCP", "ALLOW"),
            LogEntry(None, "192.168.1.2", "10.0.0.2", 50001, 53, "UDP", "ALLOW"),
        ]
        result = analyze_logs(entries)
        self.assertEqual(result.protocol_counts["TCP"], 1)
        self.assertEqual(result.protocol_counts["UDP"], 1)


if __name__ == "__main__":
    unittest.main()
```

### Test Coverage Goals

- **Overall**: > 80% coverage
- **Critical modules** (parser, analyzer): > 90% coverage
- **CLI**: > 70% coverage

Check coverage:
```bash
pytest --cov=src/ tests/ --cov-report=term-missing
```

## Pull Request Process

### Before Creating PR

**Checklist:**

- [ ] Code follows style guidelines (PEP 8)
- [ ] Tests are written and passing
- [ ] Code coverage maintained or improved
- [ ] Documentation updated (README, docstrings)
- [ ] Changelog updated
- [ ] No new warnings from linters
- [ ] Tested on at least one Linux distribution
- [ ] Commit messages are clear and descriptive

### Creating PR

1. **Update your branch**:
   ```bash
   git checkout main
   git pull upstream main
   git checkout your-branch
   git rebase main
   ```

2. **Final checks**:
   ```bash
   pytest tests/ -v
   black src/ tests/
   flake8 src/ tests/
   ```

3. **Push changes**:
   ```bash
   git push origin your-branch --force-with-lease
   ```

4. **Create PR on GitHub**:
   - Go to repository
   - Click "Pull requests" → "New pull request"
   - Select your branch
   - Fill out PR template

### PR Template

```markdown
## Description
Brief description of what this PR does.

Fixes #123

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that breaks existing functionality)
- [ ] Documentation update
- [ ] Code refactoring (no functional changes)
- [ ] Test addition/update
- [ ] Performance improvement

## Testing
- [ ] Tests pass locally (`pytest tests/ -v`)
- [ ] Code coverage maintained or improved
- [ ] Tested on:
  - [ ] Ubuntu 22.04
  - [ ] Debian 11
  - [ ] Other: _______

## Code Quality
- [ ] Code follows PEP 8 style guidelines
- [ ] Type hints added for new functions
- [ ] Docstrings written for public functions
- [ ] No new flake8 warnings

## Documentation
- [ ] README.md updated (if applicable)
- [ ] Docstrings added/updated
- [ ] CHANGELOG.md updated
- [ ] Usage examples added

## Screenshots (if applicable)
Add screenshots of CLI output or error messages.

## Additional Context
Any other relevant information for reviewers.

## Related Issues
- Fixes #123
- Related to #456
- Blocks #789
```

### Review Process

1. **Automated Checks**: CI runs tests and linters
2. **Maintainer Review**: Code review by maintainers
3. **Changes Requested**: Make requested changes
4. **Approval**: PR is approved
5. **Merge**: PR is merged to main branch

### After Merge

- Delete your feature branch
- Pull latest changes from main
- Celebrate! 🎉

## Documentation

### Improving Documentation

- Fix typos and grammatical errors
- Clarify unclear sections
- Add examples for common use cases
- Create troubleshooting guides
- Add FAQs
- Translate to other languages

### Documentation Standards

- Use clear, concise language
- Write for beginners and experts
- Include code examples
- Add links to related sections
- Keep formatting consistent
- Update when code changes

### Example: Adding a Tutorial

```markdown
# Tutorial: Analyzing Firewall Logs

## Prerequisites
- Python 3.10+
- Firewall logs in CSV format

## Step 1: Install
```bash
pip install network-log-traffic-analyzer
```

## Step 2: Prepare Logs
Export your firewall logs to CSV format.

## Step 3: Run Analysis
```bash
netlog-traffic firewall.csv --output-dir reports
```

## Step 4: Review Results
Open `reports/analysis_report.json` and `reports/blocked_connections.csv`.

## Next Steps
- Learn about advanced options in USAGE.md
- Contribute to the project in CONTRIBUTING.md
```

## Community

### Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Email**: For private inquiries

### Staying Informed

- Watch the repository for updates
- Follow project maintainers
- Join community discussions

### Contributing to Community

- Answer questions in issues and discussions
- Help review pull requests
- Mentor new contributors
- Share your use cases
- Write blog posts about the project

## Recognition

Contributors are recognized through:

- **README.md**: Contributors section
- **GitHub**: Contributors graph
- **Release Notes**: Significant contributions mentioned
- **Social Media**: Shout-outs for major contributions

## Thank You!

Every contribution makes this project better. Whether it's fixing a typo, reporting a bug, or adding a major feature - it all matters!

**Happy contributing! 🎉**
