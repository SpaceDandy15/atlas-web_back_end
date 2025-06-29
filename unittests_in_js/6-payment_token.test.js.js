// 6-payment_token.test.js
const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('should return successful response when success is true', (done) => {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.be.an('object');
        expect(response).to.have.property('data', 'Successful response from the API');
        done();
      })
      .catch(done); // call done with error if promise rejects
  });
});
