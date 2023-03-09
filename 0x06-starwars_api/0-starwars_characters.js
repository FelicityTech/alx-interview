const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
	  if (error) {
		      console.error(error);
		    } else {
			        const movie = JSON.parse(body);
			        const characterUrls = movie.characters;
			        const promises = characterUrls.map(url => {
					      return new Promise((resolve, reject) => {
						              request(url, function (error, response, body) {
								                if (error) {
											            reject(error);
											          } else {
													              const character = JSON.parse(body);
													              resolve(character.name);
													            }
								              });
						            });
					    });
			        Promise.all(promises)
			          .then(names => {
					          names.forEach(name => console.log(name));
					        })
			          .catch(error => {
					          console.error(error);
					        });
			      }
});
1~
