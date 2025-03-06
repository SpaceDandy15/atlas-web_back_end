function cleanSet(set, startString) {
  if (!startString) {
    return ''; // If no startString is provided, return an empty string.
  }
  
  return [...set]
    .filter(item => item.startsWith(startString))
    .map(item => item.slice(startString.length))
    .join('-');
}

export default cleanSet;
