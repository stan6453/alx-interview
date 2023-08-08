#!/usr/bin/node

const request = require('request');
const movieId = parseInt(process.argv[2], 10);

request.get(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, async (error, response, body) => {
  if (error) return;
  const movie = JSON.parse(body);

  for (const character of movie.characters) {
    const characterName = await new Promise((resolve, reject) => {
      request.get(character, (error, response, body) => {
        if (error) return;
        const characterInfo = JSON.parse(body);
        resolve(characterInfo.name);
      });
    });
    console.log(characterName);
  }
});
