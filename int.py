import unittest
from todo import TaskManager

class TestIntegrationDifferent(unittest.TestCase):

    def test_mark_multiple_tasks_done(self):
        manager = TaskManager()

        # Add tasks
        manager.add_task("Task A")
        manager.add_task("Task B")
        manager.add_task("Task C")

        manager.mark_task_done(1)

        self.assertEqual(manager.tasks[0].status, "pending")
        self.assertEqual(manager.tasks[1].status, "done")
        self.assertEqual(manager.tasks[2].status, "pending")

if __name__ == "__main__":
    unittest.main()
