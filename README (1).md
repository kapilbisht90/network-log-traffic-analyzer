# Network Log Traffic Analyzer

Professional Python CLI tool for analyzing network and firewall traffic logs.

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
