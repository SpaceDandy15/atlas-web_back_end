const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber()', () => {
  describe('SUM', () => {
    it('should return 6 for (1.4, 4.5)', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should return 5 for (1.2, 3.7)', () => {
      expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
    });

    it('should return -1 for (-1, 0)', () => {
      expect(calculateNumber('SUM', -1, 0)).to.equal(-1);
    });
  });

  describe('SUBTRACT', () => {
    it('should return -4 for (1.4, 4.5)', () => {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should return 1 for (2.5, 2.4)', () => {
      expect(calculateNumber('SUBTRACT', 2.5, 2.4)).to.equal(1);
    });

    it('should return 3 for (3.6, 1.2)', () => {
      expect(calculateNumber('SUBTRACT', 3.6, 1.2)).to.equal(3);
    });
  });

  describe('DIVIDE', () => {
    it('should return 0.2 for (1.4, 4.5)', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return "Error" when dividing by 0', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('should return 2.5 for (4.5, 1.9)', () => {
      expect(calculateNumber('DIVIDE', 4.5, 1.9)).to.equal(2.5);
    });
  });

  describe('Invalid type', () => {
    it('should throw an error for unknown type', () => {
      expect(() => calculateNumber('MULTIPLY', 1, 2)).to.throw('Invalid operation type');
    });
  });
});
