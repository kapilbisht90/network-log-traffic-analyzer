"""Unit tests."""

import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from network_log_traffic_analyzer.analyzer import analyze_logs
from network_log_traffic_analyzer.parser import LogEntry


class AnalyzerTests(unittest.TestCase):
    def test_total_entries(self):
        entries = [
            LogEntry(None, "192.168.1.1", "10.0.0.1", 50000, 443, "TCP", "ALLOW"),
            LogEntry(None, "192.168.1.2", "10.0.0.2", 50001, 80, "TCP", "ALLOW"),
        ]
        result = analyze_logs(entries)
        self.assertEqual(result.total_entries, 2)

    def test_blocked_detection(self):
        entries = [
            LogEntry(None, "192.168.1.1", "10.0.0.1", 50000, 443, "TCP", "ALLOW"),
            LogEntry(None, "192.168.1.2", "10.0.0.2", 50001, 22, "TCP", "DENY"),
            LogEntry(None, "192.168.1.3", "10.0.0.3", 50002, 3389, "TCP", "DROP"),
        ]
        result = analyze_logs(entries)
        self.assertEqual(len(result.blocked_connections), 2)


if __name__ == "__main__":
    unittest.main()
