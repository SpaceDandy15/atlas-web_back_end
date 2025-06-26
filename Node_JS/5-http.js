const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');

    countStudents(database)
      .then(() => {
        // countStudents logs directly to console, not to response
        // so we need to re-implement logic here to send back as string
        const fs = require('fs');
        fs.readFile(database, 'utf8', (err, data) => {
          if (err) {
            res.end('Cannot load the database');
            return;
          }

          const lines = data.split('\n').filter((line) => line.trim() !== '');
          const students = lines.slice(1);
          const fieldCounts = {};
          const fieldNames = {};

          for (const line of students) {
            const [firstname, , , field] = line.split(',');
            if (!fieldCounts[field]) {
              fieldCounts[field] = 0;
              fieldNames[field] = [];
            }
            fieldCounts[field] += 1;
            fieldNames[field].push(firstname);
          }

          res.write(`Number of students: ${students.length}\n`);
          for (const field in fieldCounts) {
            const count = fieldCounts[field];
            const names = fieldNames[field].join(', ');
            res.write(`Number of students in ${field}: ${count}. List: ${names}\n`);
          }
          res.end();
        });
      })
      .catch(() => {
        res.end('Cannot load the database');
      });
  } else {
    res.writeHead(404);
    res.end();
  }
});

app.listen(1245);

module.exports = app;
