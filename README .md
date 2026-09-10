# Network Log Traffic Analyzer

Network Log Traffic Analyzer — a Python CLI tool I wrote to make sense of firewall logs. Instead of manually scrolling through thousands of log entries, you can run this and instantly see: which IPs are sending the most traffic, which ports are being scanned or targeted, how many connections were allowed vs blocked, and detailed lists of denied traffic. Supports CSV, JSONL, and text log formats. I use it for quick security analysis and threat hunting. Outputs are in JSON and CSV so you can plug them into dashboards or SIEM tools.

## Quick Start

```bash
pip install -e .
netlog-traffic data/sample_logs.csv --output-dir output
```

## Features

- Multi-format log parsing (CSV, JSONL, plain text)
- Traffic analytics: top IPs, ports, protocols
- Blocked connections detection
- JSON and CSV report generation
- Zero external dependencies

## Installation

```bash
git clone https://github.com/yourusername/network-log-traffic-analyzer.git
cd network-log-traffic-analyzer
pip install -e .
```

## Usage

```bash
netlog-traffic firewall.csv
netlog-traffic logs.jsonl --format jsonl
netlog-traffic /var/log/ufw.log --format text --top 20
```

## Output

- `analysis_report.json` — Summary metrics
- `blocked_connections.csv` — Blocked connections

## Documentation

- [USAGE.md](USAGE.md) — Detailed usage guide
- [ARCHITECTURE.md](ARCHITECTURE.md) — Code structure
- [CONTRIBUTING.md](CONTRIBUTING.md) — How to contribute

## License

MIT
