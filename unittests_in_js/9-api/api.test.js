// 9-api/api.test.js
const request = require('request');
const { expect } = require('chai');

describe('Index page', function () {
  const baseUrl = 'http://localhost:7865';

  it('should return status 200', function (done) {
    request.get(baseUrl, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct welcome message', function (done) {
    request.get(baseUrl, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', function () {
  const baseUrl = 'http://localhost:7865';

  it('should return status 200 for numeric id', function (done) {
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct message for numeric id', function (done) {
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return 404 for non-numeric id', function (done) {
    request.get(`${baseUrl}/cart/hello`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});
