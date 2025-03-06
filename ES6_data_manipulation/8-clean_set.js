function cleanSet(set, startString = '') {
  if (typeof startString !== 'string') {
    return ''; // Return empty string if startString is not a string
  }

  return [...set]
    .filter(item => typeof item === 'string' && item.startsWith(startString)) // Ensure item is a string
    .map(item => item.slice(startString.length))
    .join('-');
}

export default cleanSet;
