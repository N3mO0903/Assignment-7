class TestIntegration(unittest.TestCase):

    def test_mark_task_done_(self):
        manager = TaskManager()

        manager.add_task("Task 1")
        manager.add_task("Task 2")

        manager.mark_task_done(0)

        self.assertEqual(manager.tasks[0].status, "done")

if __name__ == "__main__":
    unittest.main()
