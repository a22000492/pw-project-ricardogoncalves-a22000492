"use strict";

const APIS = {
  initRandomFacts: function() {
    const factsResultEl = document.querySelector('.facts-result');
    fetch('https://random-facts2.p.rapidapi.com/getfact', {
        method: 'GET',
        headers: {
          'X-RapidAPI-Host': 'random-facts2.p.rapidapi.com',
          'X-RapidAPI-Key': '5915d68d21msh17eb76504c6dc1cp1c9e94jsnbf7f934d2716'
        }
      })
      .then(res => res.json())
      .then(response => {
        factsResultEl.innerText = response.Fact;
      })
      .catch(err => console.error('error:' + err));
  },
  updateWeatherResult: function(weatherInfo) {
    const resultContainerEl = document.querySelector('.result-container');
    const cityNameEl = document.querySelector('.city-name');
    const cityTempEl = document.querySelector('.city-temperature');
    const weatherCity = document.querySelector('.weather-city').value;

    cityNameEl.innerText = weatherCity;
    cityTempEl.innerText = weatherInfo;
    resultContainerEl.classList.remove('hidden');
  },
  getWeather: function(city) {
    const _this = this;
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city.join('+')}&APPID=258938c7d111aa6cb8df7dfb9aef19c0`)
      .then(res => res.json())
      .then(wttInfo => {
        try {
          if(wttInfo.cod === 200) {
            return _this.updateWeatherResult(`${Math.round(wttInfo.main.temp - 273.15)}ºC`);
          }
          _this.updateWeatherResult("Localização inválida");
        }
        catch(e) {
          _this.updateWeatherResult("Localização inválida");
        }
      });
  },
  weatherForm: function(event) {
    event.preventDefault();
    const weatherCity = document.querySelector('.weather-city').value;
    this.getWeather(weatherCity.split(' '));
  },
  defineEventListeners: function() {
    const weatherForm = document.querySelector('.weather-form');
    weatherForm.addEventListener('submit', this.weatherForm.bind(this));
  },
  init: function() {
    this.defineEventListeners();
    this.initRandomFacts();
  },
};

document.addEventListener('DOMContentLoaded', APIS.init());
