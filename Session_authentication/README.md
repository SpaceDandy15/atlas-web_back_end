Session Authentication
This project implements a basic Session Authentication system using Flask, without relying on external modules or packages.

The purpose is educational: while real-world applications typically use built-in or third-party solutions (e.g., Flask-Login or Flask-HTTPAuth), this project walks through the core mechanics of session handling manually to provide a deeper understanding.

What is authentication?
Authentication is the process of verifying the identity of a user or system. It ensures that someone or something is who they claim to be before granting access to resources.

What is session authentication?
Session authentication is a method where the server creates and maintains a session for a user after they log in. The session ID is stored in a cookie on the client side and sent with each request to identify the authenticated user without needing to log in again.

What are cookies?
Cookies are small pieces of data that a server sends to the client’s browser. The browser stores them and sends them back with subsequent requests to the same server. Cookies can be used to maintain session state, remember preferences, or track users.

How to send cookies?
Cookies are sent by the server in the HTTP response headers using the Set-Cookie header. For example, after a successful login, the server sends a session cookie to the client.

How to parse cookies?
Cookies sent by the client are included in the HTTP request headers under the Cookie header. The server parses this header to retrieve cookie values and identify the session or user data.