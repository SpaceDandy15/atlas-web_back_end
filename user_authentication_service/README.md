This project walks through building a basic authentication system from scratch using Flask — purely for learning purposes. 
While it’s best practice in the industry to rely on secure frameworks (like Flask-User), implementing it manually helps deepen understanding of how authentication works.

How to declare API routes in a Flask app:
Use @app.route('/path', methods=['GET', 'POST']) above a function to define a route.

How to get and set cookies:
Use request.cookies.get('cookie_name') to get, and response.set_cookie('cookie_name', value) to set a cookie.

How to retrieve request form data:
Use request.form.get('field_name') to access submitted form values.

How to return various HTTP status codes:
Use return jsonify(data), status_code to send a response with a specific HTTP status code.