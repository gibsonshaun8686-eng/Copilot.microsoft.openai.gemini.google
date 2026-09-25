import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import main


class AutomationTests(unittest.TestCase):
    def test_load_tasks_reads_json_array(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tasks.json"
            path.write_text(json.dumps([{"name": "test", "action": "noop"}]), encoding="utf-8")

            self.assertEqual(main.load_tasks(str(path)), [{"name": "test", "action": "noop"}])

    def test_echo_task_succeeds(self):
        result = main.run_task({
            "name": "test-echo",
            "action": "echo",
            "payload": {"message": "hello"},
        })

        self.assertEqual(result, {"status": "ok", "message": "hello"})

    def test_write_file_task_creates_file(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "output.txt"
            result = main.run_task({
                "name": "test-write",
                "action": "write_file",
                "payload": {"path": str(output), "content": "hello"},
            })

            self.assertEqual(result, {"status": "ok", "path": str(output)})
            self.assertEqual(output.read_text(encoding="utf-8"), "hello")

    def test_unsupported_action_fails(self):
        with self.assertRaises(ValueError):
            main.run_task({"name": "bad", "action": "unknown"})


if __name__ == "__main__":
    unittest.main()
