Unit testing is the process of verifying that a specific function or method behaves correctly given various inputs.
The focus is on testing isolated units of logic — ensuring that a function returns the expected output for both standard and edge-case inputs.
A unit test should only validate the logic within the function being tested.
Dependencies such as network requests, file operations, or database access should be mocked to prevent external factors from affecting the test.

The key question a unit test answers is:

“If everything else in the system works correctly, does this function do what it's supposed to?”

Integration testing, on the other hand, checks how different parts of the system work together. These tests follow a full execution path and aim to catch issues that might arise when components are integrated.

Integration tests are typically end-to-end.

External calls (HTTP requests, file I/O, databases, etc.) are sometimes mocked, but more often left real if part of the system’s workflow.

They help ensure that the system behaves as expected in a real-world scenario, not just in isolation.

Run tests with:

```bash
python3 -m unittest test_utils.py