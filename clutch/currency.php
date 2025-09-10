<?php

namespace App\Services;

use GuzzleHttp\Client;

class CurrencyService
{
    private $client;
    private $apiKey;
    private $url;

    public function __construct()
    {
        $this->client = new Client();
        $this->apiKey = env('CURRENCY_API_KEY');  // Your API key from Open Exchange Rates, CurrencyLayer, etc.
        $this->url = 'https://openexchangerates.org/api/latest.json';  // Change this URL based on the API provider
    }

    public function getExchangeRates()
    {
        $response = $this->client->get($this->url, [
            'query' => [
                'app_id' => $this->apiKey,
            ]
        ]);

        $data = json_decode($response->getBody()->getContents(), true);
        return $data['rates'];  // Returning only the exchange rates
    }
}
