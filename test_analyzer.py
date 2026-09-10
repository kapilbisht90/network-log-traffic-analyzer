import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from network_log_traffic_analyzer.analyzer import analyze_logs
from network_log_traffic_analyzer.parser import LogEntry


class AnalyzerTests(unittest.TestCase):
    def test_counts_and_blocked_entries(self):
        entries = [
            LogEntry(None, "192.168.1.2", "10.0.0.2", 50000, 443, "TCP", "ALLOW"),
            LogEntry(None, "192.168.1.3", "10.0.0.8", 40000, 22, "TCP", "DENY"),
        ]
        result = analyze_logs(entries)
        self.assertEqual(result.total_entries, 2)
        self.assertEqual(result.action_counts["DENY"], 1)
        self.assertEqual(len(result.blocked_connections), 1)


if __name__ == "__main__":
    unittest.main()
