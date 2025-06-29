// 4-payment.test.js
const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
  let stub;
  let consoleSpy;

  beforeEach(() => {
    // Stub Utils.calculateNumber to always return 10
    stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    // Spy on console.log
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    // Restore both stub and spy
    stub.restore();
    consoleSpy.restore();
  });

  it('should call Utils.calculateNumber with SUM, 100, 20 and log the correct message', () => {
    sendPaymentRequestToApi(100, 20);

    // Check the stub was called correctly
    expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;

    // Check console.log was called with the expected output
    expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
  });
});
