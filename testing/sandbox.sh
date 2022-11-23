 curl \
 -H "X-CMC_PRO_API_KEY: 3192c5fa-2b0f-49a8-9f8c-2ca57de6c442" \
  -H "Accept: application/json" \
  -d "start=1&limit=5000&convert=USD" \
  -G https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest