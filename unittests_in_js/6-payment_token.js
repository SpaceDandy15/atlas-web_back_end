// 6-payment_token.js
function getPaymentTokenFromAPI(success) {
  if (success) {
    return Promise.resolve({ data: 'Successful response from the API' });
  }
  // When success is false, it does nothing (returns undefined)
}

module.exports = getPaymentTokenFromAPI;
