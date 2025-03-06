function cleanSet(set, startString = '') {
  if (typeof startString !== 'string') {
    return ''; // Return empty string if startString is not a string
  }

  const result = [...set]
    .filter(item => typeof item === 'string' && item.startsWith(startString)) // Ensure item is a string
    .map(item => item.slice(startString.length));

  return result.length === 0 ? '' : result.join('-');
}

export default cleanSet;
