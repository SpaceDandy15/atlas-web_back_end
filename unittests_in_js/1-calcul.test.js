const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber()', () => {
  describe('SUM', () => {
    it('should return 6 for (1.4, 4.5)', () => {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should return 5 for (1.2, 3.7)', () => {
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    });

    it('should return -1 for (-1, 0)', () => {
      assert.strictEqual(calculateNumber('SUM', -1, 0), -1);
    });
  });

  describe('SUBTRACT', () => {
    it('should return -4 for (1.4, 4.5)', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should return 0 for (2.5, 2.4)', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 2.5, 2.4), 0);
    });

    it('should return 2 for (3.6, 1.2)', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 3.6, 1.2), 2);
    });
  });

  describe('DIVIDE', () => {
    it('should return 0.2 for (1.4, 4.5)', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return "Error" when dividing by 0', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('should return 2 for (4.5, 1.9)', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 4.5, 1.9), 2);
    });
  });

  describe('Invalid type', () => {
    it('should throw an error for unknown type', () => {
      assert.throws(() => calculateNumber('MULTIPLY', 1, 2), /Invalid operation type/);
    });
  });
});
