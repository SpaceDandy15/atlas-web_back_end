const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1); // remove header

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

    console.log(`Number of students: ${students.length}`);
    for (const field in fieldCounts) {
      const count = fieldCounts[field];
      const names = fieldNames[field].join(', ');
      console.log(`Number of students in ${field}: ${count}. List: ${names}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
