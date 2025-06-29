 Unit Tests in JavaScript
This project demonstrates how to write and organize unit and integration tests in JavaScript using mocha, chai, sinon, and express.

🔧 Tools & Libraries
Mocha – Testing framework

Chai – Assertion library

Sinon – Spies and stubs

Express – Simple API endpoints for integration testing

Request – HTTP client for testing API responses

🧪 What’s Covered
✅ Unit Testing
calculateNumber function with multiple test cases

Use of assert and chai.expect for testing logic

Stubbing and spying on function calls (e.g., console.log, API mocks)

🔍 Testing Techniques
Spies – Monitor how functions are called

Stubs – Replace functions with mock behavior

Hooks – Setup/teardown logic with beforeEach and afterEach

Async Testing – Validate Promises using done callback

Skipping Tests – Mark tests as .skip() when troubleshooting

🌐 Integration Testing (8-10-api)
Built an Express server with endpoints like:

GET /

GET /cart/:id

GET /available_payments

POST /login

Verified status codes, responses, and deep equality using Chai and Request