# Architecture

## Structure

```
src/network_log_traffic_analyzer/
├── parser.py    # Log parsing
├── analyzer.py  # Analytics
├── report.py    # Reports
└── cli.py       # CLI
```

## Flow

Log File → parser → LogEntry[] → analyzer → AnalysisResult → report → JSON/CSV
