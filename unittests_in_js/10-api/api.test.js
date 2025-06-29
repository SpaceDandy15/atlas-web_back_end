const request = require('request');
const { expect } = require('chai');

const baseUrl = 'http://localhost:7865';

describe('Index page', () => {
  it('returns correct status code and message', (done) => {
    request.get(baseUrl + '/', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', () => {
  it('returns correct status code and message when :id is a number', (done) => {
    request.get(baseUrl + '/cart/12', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('returns 404 when :id is not a number', (done) => {
    request.get(baseUrl + '/cart/hello', (error, response) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('/available_payments endpoint', () => {
  it('returns correct object with payment methods', (done) => {
    request.get(baseUrl + '/available_payments', { json: true }, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      });
      done();
    });
  });
});

describe('/login endpoint', () => {
  it('returns correct welcome message for posted username', (done) => {
    request.post(
      {
        url: baseUrl + '/login',
        json: { userName: 'Betty' },
      },
      (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Betty');
        done();
      }
    );
  });
});
