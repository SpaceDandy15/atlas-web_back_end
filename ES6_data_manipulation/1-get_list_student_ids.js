function getListStudentIds(students) {
    if (!Array.isArray(students)) {
    return [];
  }
  // Use the map function to extract the 'id' from each student object
  return students.map(student => student.id);
}

export default getListStudentIds;
