const express = require('express');
const fs = require('fs');

const app = express();
const database = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
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

      const output = [];
      output.push(`Number of students: ${students.length}`);
      for (const field in fieldCounts) {
        const count = fieldCounts[field];
        const names = fieldNames[field].join(', ');
        output.push(`Number of students in ${field}: ${count}. List: ${names}`);
      }

      resolve(output.join('\n'));
    });
  });
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  countStudents(database)
    .then((result) => {
      res.send(`This is the list of our students\n${result}`);
    })
    .catch(() => {
      res.send('This is the list of our students\nCannot load the database');
    });
});

app.listen(1245);

module.exports = app;
