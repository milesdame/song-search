from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/csc342groups")
def csc_342_groups():
    songs = [
    {
        "title": "Pink Pony Club",
        "artists": [
            "Chappell Roan"
        ],
        "popularity": 88,
        "explicit": false,
        "url": "https://open.spotify.com/track/1k2pQc5i348DCHwbn5KTdc",
        "duration_mins": 4.3,
        "genres": [
            "indie pop"
        ]
    },
    {
        "title": "Naked In Manhattan",
        "artists": [
            "Chappell Roan"
        ],
        "popularity": 79,
        "explicit": true,
        "url": "https://open.spotify.com/track/4LKYOetuIF5c9XjeLBL9av",
        "duration_mins": 3.52,
        "genres": [
            "indie pop"
        ]
    },
    {
        "title": "HOT TO GO!",
        "artists": [
            "Chappell Roan"
        ],
        "popularity": 90,
        "explicit": false,
        "url": "https://open.spotify.com/track/4xdBrk0nFZaP54vvZj0yx7",
        "duration_mins": 3.08,
        "genres": [
            "indie pop"
        ]
    },
    {
        "title": "California",
        "artists": [
            "Chappell Roan"
        ],
        "popularity": 72,
        "explicit": false,
        "url": "https://open.spotify.com/track/6dA1JQt3f3meGzahhNN75m",
        "duration_mins": 3.3,
        "genres": [
            "indie pop"
        ]
    },
    {
        "title": "Red Wine Supernova",
        "artists": [
            "Chappell Roan"
        ],
        "popularity": 86,
        "explicit": true,
        "url": "https://open.spotify.com/track/7FOgcfdz9Nx5V9lCNXdBYv",
        "duration_mins": 3.21,
        "genres": [
            "indie pop"
        ]
    },
    {
        "title": "Femininomenon",
        "artists": [
            "Chappell Roan"
        ],
        "popularity": 83,
        "explicit": true,
        "url": "https://open.spotify.com/track/53IRnAWx13PYmoVYtemUBS",
        "duration_mins": 3.66,
        "genres": [
            "indie pop"
        ]
    },
    {
        "title": "Casual",
        "artists": [
            "Chappell Roan"
        ],
        "popularity": 86,
        "explicit": true,
        "url": "https://open.spotify.com/track/3WSOUb3U7tqURbBSgZTrZX",
        "duration_mins": 3.88,
        "genres": [
            "indie pop"
        ]
    },
    {
        "title": "Picture You",
        "artists": [
            "Chappell Roan"
        ],
        "popularity": 76,
        "explicit": false,
        "url": "https://open.spotify.com/track/5KtvumPgVZmt8wg9xONE0T",
        "duration_mins": 3.12,
        "genres": [
            "indie pop"
        ]
    },
    {
        "title": "Cherry",
        "artists": [
            "Lana Del Rey"
        ],
        "popularity": 73,
        "explicit": true,
        "url": "https://open.spotify.com/track/1Ym6aMuT5bliaZMC67AmPp",
        "duration_mins": 3.02,
        "genres": [
            "art pop",
            "pop"
        ]
    },
    {
        "title": "Bed Chem",
        "artists": [
            "Sabrina Carpenter"
        ],
        "popularity": 92,
        "explicit": false,
        "url": "https://open.spotify.com/track/1UHS8Rf6h5Ar3CDWRd3wjF",
        "duration_mins": 2.86,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Let The Light In (feat. Father John Misty)",
        "artists": [
            "Lana Del Rey",
            "Father John Misty"
        ],
        "popularity": 78,
        "explicit": false,
        "url": "https://open.spotify.com/track/4qG7hWhljsqqENL5PaLA2z",
        "duration_mins": 4.64,
        "genres": [
            "art pop",
            "pop",
            "chamber pop",
            "indie rock",
            "singer-songwriter",
            "stomp and holler"
        ]
    },
    {
        "title": "Taste",
        "artists": [
            "Sabrina Carpenter"
        ],
        "popularity": 95,
        "explicit": false,
        "url": "https://open.spotify.com/track/5G2f63n7IPVPPjfNIGih7Q",
        "duration_mins": 2.62,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Please Please Please",
        "artists": [
            "Sabrina Carpenter"
        ],
        "popularity": 93,
        "explicit": true,
        "url": "https://open.spotify.com/track/5N3hjp1WNayUPZrA8kJmJP",
        "duration_mins": 3.11,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Sign of the Times",
        "artists": [
            "Harry Styles"
        ],
        "popularity": 80,
        "explicit": false,
        "url": "https://open.spotify.com/track/5Ohxk2dO5COHF1krpoPigN",
        "duration_mins": 5.68,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Kaleidoscope",
        "artists": [
            "Chappell Roan"
        ],
        "popularity": 72,
        "explicit": false,
        "url": "https://open.spotify.com/track/4ROYC4vHfPZ28mqz0eLrzL",
        "duration_mins": 3.71,
        "genres": [
            "indie pop"
        ]
    },
    {
        "title": "Liability",
        "artists": [
            "Lorde"
        ],
        "popularity": 68,
        "explicit": false,
        "url": "https://open.spotify.com/track/6Kkt27YmFyIFrcX3QXFi2o",
        "duration_mins": 2.86,
        "genres": [
            "art pop",
            "metropopolis",
            "nz pop",
            "pop"
        ]
    },
    {
        "title": "Good Luck, Babe!",
        "artists": [
            "Chappell Roan"
        ],
        "popularity": 95,
        "explicit": false,
        "url": "https://open.spotify.com/track/0WbMK4wrZ1wFSty9F7FCgu",
        "duration_mins": 3.64,
        "genres": [
            "indie pop"
        ]
    },
    {
        "title": "Sin Eater",
        "artists": [
            "Penelope Scott"
        ],
        "popularity": 37,
        "explicit": false,
        "url": "https://open.spotify.com/track/27fjK3KaOnt2thZBYMpiXH",
        "duration_mins": 5.33,
        "genres": [
            "alt z",
            "modern indie pop",
            "pov: indie"
        ]
    },
    {
        "title": "The Air That I Breathe - 2008 Remaster",
        "artists": [
            "The Hollies"
        ],
        "popularity": 64,
        "explicit": false,
        "url": "https://open.spotify.com/track/3P3fymPrC9KgV2Kf5oMnx0",
        "duration_mins": 4.29,
        "genres": [
            "album rock",
            "british invasion",
            "classic rock",
            "folk rock",
            "mellow gold",
            "merseybeat",
            "soft rock"
        ]
    },
    {
        "title": "Not Like Us",
        "artists": [
            "Kendrick Lamar"
        ],
        "popularity": 91,
        "explicit": true,
        "url": "https://open.spotify.com/track/6AI3ezQ4o3HUoP6Dhudph3",
        "duration_mins": 4.57,
        "genres": [
            "conscious hip hop",
            "hip hop",
            "rap",
            "west coast rap"
        ]
    },
    {
        "title": "Tornado Warnings",
        "artists": [
            "Sabrina Carpenter"
        ],
        "popularity": 65,
        "explicit": true,
        "url": "https://open.spotify.com/track/5kcuHw8WtxauIWI5crMcLM",
        "duration_mins": 3.4,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Good Hearted Man",
        "artists": [
            "Lera Lynn"
        ],
        "popularity": 10,
        "explicit": true,
        "url": "https://open.spotify.com/track/4ZqVYqgc0lQNM8Jmzfv0L1",
        "duration_mins": 2.17,
        "genres": [
            "alternative country",
            "new americana"
        ]
    },
    {
        "title": "After Midnight",
        "artists": [
            "Chappell Roan"
        ],
        "popularity": 79,
        "explicit": false,
        "url": "https://open.spotify.com/track/4rlQza35DE4Prh5yonxnCs",
        "duration_mins": 3.41,
        "genres": [
            "indie pop"
        ]
    },
    {
        "title": "Coffee",
        "artists": [
            "Chappell Roan"
        ],
        "popularity": 73,
        "explicit": false,
        "url": "https://open.spotify.com/track/6GdUMm5xMw9hJckIc0qsGb",
        "duration_mins": 3.43,
        "genres": [
            "indie pop"
        ]
    },
    {
        "title": "Green Light",
        "artists": [
            "Lorde"
        ],
        "popularity": 70,
        "explicit": false,
        "url": "https://open.spotify.com/track/6ie2Bw3xLj2JcGowOlcMhb",
        "duration_mins": 3.91,
        "genres": [
            "art pop",
            "metropopolis",
            "nz pop",
            "pop"
        ]
    },
    {
        "title": "East Side of Sorrow",
        "artists": [
            "Zach Bryan"
        ],
        "popularity": 72,
        "explicit": true,
        "url": "https://open.spotify.com/track/00syWkRGIVQvYsg2OwfBUw",
        "duration_mins": 3.49,
        "genres": [
            "classic oklahoma country"
        ]
    },
    {
        "title": "Meet Me At Our Spot",
        "artists": [
            "THE ANXIETY",
            "WILLOW",
            "Tyler Cole"
        ],
        "popularity": 72,
        "explicit": true,
        "url": "https://open.spotify.com/track/07MDkzWARZaLEdKxo6yArG",
        "duration_mins": 2.71,
        "genres": [
            "modern alternative pop",
            "afrofuturism",
            "pop",
            "post-teen pop",
            "pov: indie",
            "bedroom soul"
        ]
    },
    {
        "title": "Good Graces",
        "artists": [
            "Sabrina Carpenter"
        ],
        "popularity": 89,
        "explicit": true,
        "url": "https://open.spotify.com/track/102YUQbYmwdBXS7jwamI90",
        "duration_mins": 3.09,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Super Graphic Ultra Modern Girl",
        "artists": [
            "Chappell Roan"
        ],
        "popularity": 79,
        "explicit": false,
        "url": "https://open.spotify.com/track/1rNSCrsOoWyhKH4g47mehU",
        "duration_mins": 3.06,
        "genres": [
            "indie pop"
        ]
    },
    {
        "title": "get him back!",
        "artists": [
            "Olivia Rodrigo"
        ],
        "popularity": 76,
        "explicit": true,
        "url": "https://open.spotify.com/track/2gyxAWHebV7xPYVxqoi86f",
        "duration_mins": 3.52,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Rock Me Gently",
        "artists": [
            "Andy Kim"
        ],
        "popularity": 50,
        "explicit": false,
        "url": "https://open.spotify.com/track/2qh2VGAOYFXLsMbdATRf6w",
        "duration_mins": 3.47,
        "genres": [
            "bubblegum pop",
            "classic uk pop"
        ]
    },
    {
        "title": "My Kink Is Karma",
        "artists": [
            "Chappell Roan"
        ],
        "popularity": 82,
        "explicit": false,
        "url": "https://open.spotify.com/track/32fSZSbxeVoiZShMQKLc6Z",
        "duration_mins": 3.71,
        "genres": [
            "indie pop"
        ]
    },
    {
        "title": "Francis Forever",
        "artists": [
            "Mitski"
        ],
        "popularity": 75,
        "explicit": false,
        "url": "https://open.spotify.com/track/5411TEB6tlzvuF5A4oyldr",
        "duration_mins": 2.49,
        "genres": [
            "brooklyn indie",
            "pov: indie"
        ]
    },
    {
        "title": "BIRDS OF A FEATHER",
        "artists": [
            "Billie Eilish"
        ],
        "popularity": 98,
        "explicit": false,
        "url": "https://open.spotify.com/track/6dOtVTDdiauQNBQEDOtlAB",
        "duration_mins": 3.51,
        "genres": [
            "art pop",
            "pop"
        ]
    },
    {
        "title": "Nonsense",
        "artists": [
            "Sabrina Carpenter"
        ],
        "popularity": 87,
        "explicit": false,
        "url": "https://open.spotify.com/track/6dgUya35uo964z7GZXM07g",
        "duration_mins": 2.73,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Born to Run",
        "artists": [
            "Bruce Springsteen"
        ],
        "popularity": 71,
        "explicit": false,
        "url": "https://open.spotify.com/track/6hTcuIQa0sxrrByu9wTD7s",
        "duration_mins": 4.5,
        "genres": [
            "heartland rock",
            "mellow gold",
            "permanent wave",
            "rock",
            "singer-songwriter"
        ]
    },
    {
        "title": "The Morning",
        "artists": [
            "The Weeknd"
        ],
        "popularity": 70,
        "explicit": true,
        "url": "https://open.spotify.com/track/4jBfUB4kQJCWOrjGLQqhO0",
        "duration_mins": 5.24,
        "genres": [
            "canadian contemporary r&b",
            "canadian pop",
            "pop"
        ]
    },
    {
        "title": "Maggie May",
        "artists": [
            "Rod Stewart"
        ],
        "popularity": 69,
        "explicit": false,
        "url": "https://open.spotify.com/track/6rovOdp3HgK1DeAMYDzoA7",
        "duration_mins": 5.84,
        "genres": [
            "mellow gold",
            "soft rock"
        ]
    },
    {
        "title": "Gasoline",
        "artists": [
            "Lera Lynn"
        ],
        "popularity": 7,
        "explicit": false,
        "url": "https://open.spotify.com/track/5SldPhuAXgmsMWqvn7vsF1",
        "duration_mins": 3.27,
        "genres": [
            "alternative country",
            "new americana"
        ]
    },
    {
        "title": "Run Away With Me",
        "artists": [
            "Carly Rae Jepsen"
        ],
        "popularity": 59,
        "explicit": false,
        "url": "https://open.spotify.com/track/0FS7B5o3QyvOD8eWjnbLoO",
        "duration_mins": 4.19,
        "genres": [
            "canadian pop",
            "dance pop",
            "pop"
        ]
    },
    {
        "title": "Guilty Pleasure",
        "artists": [
            "Chappell Roan"
        ],
        "popularity": 71,
        "explicit": false,
        "url": "https://open.spotify.com/track/0q8TNCQhwnDwnzq38IVV4l",
        "duration_mins": 3.74,
        "genres": [
            "indie pop"
        ]
    },
    {
        "title": "Writer In The Dark",
        "artists": [
            "Lorde"
        ],
        "popularity": 61,
        "explicit": false,
        "url": "https://open.spotify.com/track/193Dm5SqYy3hTSbuzxbwKc",
        "duration_mins": 3.61,
        "genres": [
            "art pop",
            "metropopolis",
            "nz pop",
            "pop"
        ]
    },
    {
        "title": "Hard Feelings/Loveless",
        "artists": [
            "Lorde"
        ],
        "popularity": 57,
        "explicit": true,
        "url": "https://open.spotify.com/track/1Dp7JGFNjvg8Nk0CtMCcnr",
        "duration_mins": 6.12,
        "genres": [
            "art pop",
            "metropopolis",
            "nz pop",
            "pop"
        ]
    },
    {
        "title": "Don't Worry Baby - Remastered 2001",
        "artists": [
            "The Beach Boys"
        ],
        "popularity": 65,
        "explicit": false,
        "url": "https://open.spotify.com/track/1GLmaPfulP0BrfijohQpN5",
        "duration_mins": 2.83,
        "genres": [
            "baroque pop",
            "classic rock",
            "folk rock",
            "mellow gold",
            "psychedelic rock",
            "rock",
            "singer-songwriter",
            "sunshine pop"
        ]
    },
    {
        "title": "CUFF IT",
        "artists": [
            "Beyonc\u00e9"
        ],
        "popularity": 75,
        "explicit": true,
        "url": "https://open.spotify.com/track/1xzi1Jcr7mEi9K2RfzLOqS",
        "duration_mins": 3.76,
        "genres": [
            "pop",
            "r&b"
        ]
    },
    {
        "title": "Juno",
        "artists": [
            "Sabrina Carpenter"
        ],
        "popularity": 88,
        "explicit": true,
        "url": "https://open.spotify.com/track/21B4gaTWnTkuSh77iWEXdS",
        "duration_mins": 3.72,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Tough",
        "artists": [
            "Quavo",
            "Lana Del Rey"
        ],
        "popularity": 82,
        "explicit": false,
        "url": "https://open.spotify.com/track/22DH8NChecsgPxDjA4pqer",
        "duration_mins": 3.15,
        "genres": [
            "atl hip hop",
            "melodic rap",
            "rap",
            "trap",
            "art pop",
            "pop"
        ]
    },
    {
        "title": "I Bet on Losing Dogs",
        "artists": [
            "Mitski"
        ],
        "popularity": 81,
        "explicit": false,
        "url": "https://open.spotify.com/track/2Co0IjcLTSHMtodwD4gzfg",
        "duration_mins": 2.84,
        "genres": [
            "brooklyn indie",
            "pov: indie"
        ]
    },
    {
        "title": "Make You OK",
        "artists": [
            "Lera Lynn"
        ],
        "popularity": 18,
        "explicit": false,
        "url": "https://open.spotify.com/track/2P5LrxFYiqTtZroqxGVYua",
        "duration_mins": 4.29,
        "genres": [
            "alternative country",
            "new americana"
        ]
    },
    {
        "title": "Silver Springs - 2004 Remaster",
        "artists": [
            "Fleetwood Mac"
        ],
        "popularity": 60,
        "explicit": false,
        "url": "https://open.spotify.com/track/2Y8BloifAHEn6GproQgPs7",
        "duration_mins": 4.81,
        "genres": [
            "album rock",
            "classic rock",
            "rock",
            "soft rock",
            "yacht rock"
        ]
    },
    {
        "title": "Gross",
        "artists": [
            "Penelope Scott"
        ],
        "popularity": 32,
        "explicit": false,
        "url": "https://open.spotify.com/track/1HYgoVdKAo9pDhbtdYNoJ8",
        "duration_mins": 4.41,
        "genres": [
            "alt z",
            "modern indie pop",
            "pov: indie"
        ]
    },
    {
        "title": "obsessed",
        "artists": [
            "Olivia Rodrigo"
        ],
        "popularity": 79,
        "explicit": true,
        "url": "https://open.spotify.com/track/6tNgRQ0K2NYZ0Rb9l9DzL8",
        "duration_mins": 2.84,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Time of My Life",
        "artists": [
            "Penelope Scott"
        ],
        "popularity": 28,
        "explicit": false,
        "url": "https://open.spotify.com/track/0OIo0Dl0qJ5oJIkbJ88ttH",
        "duration_mins": 3.4,
        "genres": [
            "alt z",
            "modern indie pop",
            "pov: indie"
        ]
    },
    {
        "title": "Kill Bill",
        "artists": [
            "SZA"
        ],
        "popularity": 77,
        "explicit": false,
        "url": "https://open.spotify.com/track/3OHfY25tqY28d16oZczHc8",
        "duration_mins": 2.57,
        "genres": [
            "pop",
            "r&b",
            "rap"
        ]
    },
    {
        "title": "Water",
        "artists": [
            "Tyla"
        ],
        "popularity": 84,
        "explicit": false,
        "url": "https://open.spotify.com/track/5aIVCx5tnk0ntmdiinnYvw",
        "duration_mins": 3.34,
        "genres": []
    },
    {
        "title": "Whiskey",
        "artists": [
            "Lera Lynn"
        ],
        "popularity": 15,
        "explicit": false,
        "url": "https://open.spotify.com/track/1wrIi0pTCV1jZRQuMiICCW",
        "duration_mins": 4.39,
        "genres": [
            "alternative country",
            "new americana"
        ]
    },
    {
        "title": "ceilings",
        "artists": [
            "Lizzy McAlpine"
        ],
        "popularity": 52,
        "explicit": false,
        "url": "https://open.spotify.com/track/4MgryRe2yavUKiCucotL9C",
        "duration_mins": 3.05,
        "genres": [
            "alt z",
            "boston folk",
            "indie pop",
            "singer-songwriter pop"
        ]
    },
    {
        "title": "Standing on the Moon",
        "artists": [
            "Lera Lynn"
        ],
        "popularity": 18,
        "explicit": false,
        "url": "https://open.spotify.com/track/3Dr8VDCgZwwgo5rZrGd6bN",
        "duration_mins": 4.34,
        "genres": [
            "alternative country",
            "new americana"
        ]
    },
    {
        "title": "I Just Wasn't Made For These Times",
        "artists": [
            "The Beach Boys"
        ],
        "popularity": 40,
        "explicit": false,
        "url": "https://open.spotify.com/track/7Jljbi0t6TIusvUm3HnCAb",
        "duration_mins": 3.35,
        "genres": [
            "baroque pop",
            "classic rock",
            "folk rock",
            "mellow gold",
            "psychedelic rock",
            "rock",
            "singer-songwriter",
            "sunshine pop"
        ]
    },
    {
        "title": "Wouldn't It Be Nice",
        "artists": [
            "The Beach Boys"
        ],
        "popularity": 69,
        "explicit": false,
        "url": "https://open.spotify.com/track/4IHc6SzGPnzSPuHVEPzpJc",
        "duration_mins": 2.55,
        "genres": [
            "baroque pop",
            "classic rock",
            "folk rock",
            "mellow gold",
            "psychedelic rock",
            "rock",
            "singer-songwriter",
            "sunshine pop"
        ]
    },
    {
        "title": "Pseudophed",
        "artists": [
            "Penelope Scott"
        ],
        "popularity": 37,
        "explicit": false,
        "url": "https://open.spotify.com/track/75Utu6uTy9ZqHznhR4YKNc",
        "duration_mins": 1.28,
        "genres": [
            "alt z",
            "modern indie pop",
            "pov: indie"
        ]
    },
    {
        "title": "Shuffle",
        "artists": [
            "Penelope Scott"
        ],
        "popularity": 36,
        "explicit": false,
        "url": "https://open.spotify.com/track/7FKkJ0NDrMobvDw1jD8w58",
        "duration_mins": 2.72,
        "genres": [
            "alt z",
            "modern indie pop",
            "pov: indie"
        ]
    },
    {
        "title": "Dead of Night",
        "artists": [
            "Orville Peck"
        ],
        "popularity": 58,
        "explicit": false,
        "url": "https://open.spotify.com/track/08unC8N1V1dEcqiyi06g6W",
        "duration_mins": 3.98,
        "genres": [
            "alternative country",
            "queer country"
        ]
    },
    {
        "title": "Agora Hills",
        "artists": [
            "Doja Cat"
        ],
        "popularity": 76,
        "explicit": true,
        "url": "https://open.spotify.com/track/5PyDJG7SQRgWXefgexqIge",
        "duration_mins": 4.42,
        "genres": [
            "dance pop",
            "pop"
        ]
    },
    {
        "title": "Say So",
        "artists": [
            "Doja Cat"
        ],
        "popularity": 74,
        "explicit": true,
        "url": "https://open.spotify.com/track/3Dv1eDb0MEgF93GpLXlucZ",
        "duration_mins": 3.96,
        "genres": [
            "dance pop",
            "pop"
        ]
    },
    {
        "title": "Feel Better",
        "artists": [
            "Penelope Scott"
        ],
        "popularity": 62,
        "explicit": true,
        "url": "https://open.spotify.com/track/0mfHN9LcAPidSI3JCPqYml",
        "duration_mins": 4.21,
        "genres": [
            "alt z",
            "modern indie pop",
            "pov: indie"
        ]
    },
    {
        "title": "bad idea right?",
        "artists": [
            "Olivia Rodrigo"
        ],
        "popularity": 79,
        "explicit": true,
        "url": "https://open.spotify.com/track/3IX0yuEVvDbnqUwMBB3ouC",
        "duration_mins": 3.08,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Kiss Me More (feat. SZA)",
        "artists": [
            "Doja Cat",
            "SZA"
        ],
        "popularity": 72,
        "explicit": true,
        "url": "https://open.spotify.com/track/748mdHapucXQri7IAO8yFK",
        "duration_mins": 3.48,
        "genres": [
            "dance pop",
            "pop",
            "r&b",
            "rap"
        ]
    },
    {
        "title": "Calm Down (with Selena Gomez)",
        "artists": [
            "Rema",
            "Selena Gomez"
        ],
        "popularity": 79,
        "explicit": false,
        "url": "https://open.spotify.com/track/0WtM2NBVQNNJLh6scP13H8",
        "duration_mins": 3.99,
        "genres": [
            "afrobeats",
            "nigerian pop",
            "pop",
            "post-teen pop"
        ]
    },
    {
        "title": "ballad of a homeschooled girl",
        "artists": [
            "Olivia Rodrigo"
        ],
        "popularity": 65,
        "explicit": false,
        "url": "https://open.spotify.com/track/5lfHlUT9WtSGw12jw7dSkk",
        "duration_mins": 3.39,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Read your Mind",
        "artists": [
            "Sabrina Carpenter"
        ],
        "popularity": 75,
        "explicit": false,
        "url": "https://open.spotify.com/track/4Wos0h9ECU2Z3oJMTQxpbc",
        "duration_mins": 3.46,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Espresso",
        "artists": [
            "Sabrina Carpenter"
        ],
        "popularity": 59,
        "explicit": true,
        "url": "https://open.spotify.com/track/5KRy7KqBVoxYVSnzdkdq2w",
        "duration_mins": 2.92,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "love is embarrassing",
        "artists": [
            "Olivia Rodrigo"
        ],
        "popularity": 65,
        "explicit": true,
        "url": "https://open.spotify.com/track/3jhlwdu8nU7hFTEGHUomN3",
        "duration_mins": 2.58,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Oklahoma Smokeshow",
        "artists": [
            "Zach Bryan"
        ],
        "popularity": 81,
        "explicit": false,
        "url": "https://open.spotify.com/track/0OWhKvvsHptt6vnnNUSM9a",
        "duration_mins": 3.53,
        "genres": [
            "classic oklahoma country"
        ]
    },
    {
        "title": "Brooklyn Baby",
        "artists": [
            "Lana Del Rey"
        ],
        "popularity": 81,
        "explicit": true,
        "url": "https://open.spotify.com/track/1NZs6n6hl8UuMaX0UC0YTz",
        "duration_mins": 5.86,
        "genres": [
            "art pop",
            "pop"
        ]
    },
    {
        "title": "Out to Sea",
        "artists": [
            "Lera Lynn"
        ],
        "popularity": 23,
        "explicit": false,
        "url": "https://open.spotify.com/track/37B5EOUbYGfLjayLDQblv2",
        "duration_mins": 5.87,
        "genres": [
            "alternative country",
            "new americana"
        ]
    },
    {
        "title": "Crying All the Time",
        "artists": [
            "Alexandra Savior"
        ],
        "popularity": 3,
        "explicit": false,
        "url": "https://open.spotify.com/track/2qLXPvrlhdPsR2NpO7CKSN",
        "duration_mins": 3.51,
        "genres": [
            "modern dream pop"
        ]
    },
    {
        "title": "Eye Know",
        "artists": [
            "De La Soul",
            "Otis Redding"
        ],
        "popularity": 58,
        "explicit": false,
        "url": "https://open.spotify.com/track/4xQMFoD33vx6stB1UzfA6s",
        "duration_mins": 4.21,
        "genres": [
            "east coast hip hop",
            "golden age hip hop",
            "hip hop",
            "jazz rap",
            "classic soul",
            "memphis soul",
            "soul",
            "soul blues",
            "southern soul",
            "vocal jazz"
        ]
    },
    {
        "title": "Fade into the Black",
        "artists": [
            "Lera Lynn"
        ],
        "popularity": 12,
        "explicit": false,
        "url": "https://open.spotify.com/track/64ASHSZlyBfn8sQMfMlr0e",
        "duration_mins": 5.79,
        "genres": [
            "alternative country",
            "new americana"
        ]
    },
    {
        "title": "29",
        "artists": [
            "Demi Lovato"
        ],
        "popularity": 52,
        "explicit": true,
        "url": "https://open.spotify.com/track/0REv856zadB0e8IM1brlwr",
        "duration_mins": 2.72,
        "genres": [
            "pop",
            "post-teen pop"
        ]
    },
    {
        "title": "Until I Found You",
        "artists": [
            "Stephen Sanchez"
        ],
        "popularity": 76,
        "explicit": false,
        "url": "https://open.spotify.com/track/0T5iIrXA4p5GsubkhuBIKV",
        "duration_mins": 2.96,
        "genres": [
            "gen z singer-songwriter"
        ]
    },
    {
        "title": "Wild West - Roadhouse Mix",
        "artists": [
            "Lissie"
        ],
        "popularity": 25,
        "explicit": false,
        "url": "https://open.spotify.com/track/0qrEuCoIEKh9jjOb8a2Xhg",
        "duration_mins": 3.65,
        "genres": [
            "folk-pop"
        ]
    },
    {
        "title": "Thunder",
        "artists": [
            "Lana Del Rey"
        ],
        "popularity": 66,
        "explicit": true,
        "url": "https://open.spotify.com/track/4y9vLiQ9mQb6XNEtc4K6ou",
        "duration_mins": 4.32,
        "genres": [
            "art pop",
            "pop"
        ]
    },
    {
        "title": "Hate It Or Love It",
        "artists": [
            "The Game",
            "50 Cent"
        ],
        "popularity": 78,
        "explicit": true,
        "url": "https://open.spotify.com/track/2wGSgTmgSF3xjRrHkTc25R",
        "duration_mins": 3.44,
        "genres": [
            "detroit hip hop",
            "gangster rap",
            "hip hop",
            "pop rap",
            "rap",
            "southern hip hop",
            "trap",
            "east coast hip hop",
            "queens hip hop"
        ]
    },
    {
        "title": "Respiration",
        "artists": [
            "Black Star",
            "Common"
        ],
        "popularity": 49,
        "explicit": true,
        "url": "https://open.spotify.com/track/5mxVKAuunOKqcBfR5ivbRf",
        "duration_mins": 6.09,
        "genres": [
            "east coast hip hop",
            "hip hop",
            "political hip hop",
            "alternative hip hop",
            "chicago rap",
            "conscious hip hop",
            "hardcore hip hop"
        ]
    },
    {
        "title": "Bobby Baby",
        "artists": [
            "Lera Lynn"
        ],
        "popularity": 17,
        "explicit": false,
        "url": "https://open.spotify.com/track/1pSZeFwGTfjuugdBI2Bpam",
        "duration_mins": 3.23,
        "genres": [
            "alternative country",
            "new americana"
        ]
    },
    {
        "title": "Devil In A New Dress",
        "artists": [
            "Kanye West",
            "Rick Ross"
        ],
        "popularity": 76,
        "explicit": true,
        "url": "https://open.spotify.com/track/1UGD3lW3tDmgZfAVDh6w7r",
        "duration_mins": 5.87,
        "genres": [
            "chicago rap",
            "hip hop",
            "rap",
            "dirty south rap",
            "gangster rap",
            "southern hip hop",
            "trap"
        ]
    },
    {
        "title": "Drew Barrymore",
        "artists": [
            "SZA"
        ],
        "popularity": 70,
        "explicit": true,
        "url": "https://open.spotify.com/track/06u5LrUpbosQlQ1QJFhPpG",
        "duration_mins": 3.86,
        "genres": [
            "pop",
            "r&b",
            "rap"
        ]
    },
    {
        "title": "Talkin' Bout Hey Love",
        "artists": [
            "De La Soul"
        ],
        "popularity": 30,
        "explicit": false,
        "url": "https://open.spotify.com/track/0oPw55L3rJFrFUm4xnpHHk",
        "duration_mins": 2.46,
        "genres": [
            "east coast hip hop",
            "golden age hip hop",
            "hip hop",
            "jazz rap"
        ]
    },
    {
        "title": "Kissing Lessons",
        "artists": [
            "Lucy Dacus"
        ],
        "popularity": 47,
        "explicit": false,
        "url": "https://open.spotify.com/track/3KRdLDjxlAY7ku93tOG0b1",
        "duration_mins": 1.91,
        "genres": [
            "art pop",
            "indie pop"
        ]
    },
    {
        "title": "Stakes Is High",
        "artists": [
            "De La Soul"
        ],
        "popularity": 45,
        "explicit": true,
        "url": "https://open.spotify.com/track/5sfXK6yQlY9vSzuR3f3oD8",
        "duration_mins": 5.51,
        "genres": [
            "east coast hip hop",
            "golden age hip hop",
            "hip hop",
            "jazz rap"
        ]
    },
    {
        "title": "ballad of a homeschooled girl",
        "artists": [
            "Olivia Rodrigo"
        ],
        "popularity": 70,
        "explicit": false,
        "url": "https://open.spotify.com/track/5sp71CUt0jXRNqHblPGp7b",
        "duration_mins": 3.39,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Put Your Hands Where My Eyes Could See (feat. Jamal)",
        "artists": [
            "Busta Rhymes",
            "Jamal"
        ],
        "popularity": 60,
        "explicit": true,
        "url": "https://open.spotify.com/track/1NHwvBmrUje4L1dxfWnXCH",
        "duration_mins": 3.24,
        "genres": [
            "east coast hip hop",
            "hardcore hip hop",
            "hip hop",
            "pop rap",
            "rap",
            "polish hip hop",
            "polish reggae"
        ]
    },
    {
        "title": "Here Comes The Hotstepper",
        "artists": [
            "iNi Kamoze"
        ],
        "popularity": 16,
        "explicit": true,
        "url": "https://open.spotify.com/track/6IBBIAfwhrouVmgjycQLNE",
        "duration_mins": 4.23,
        "genres": [
            "reggae",
            "reggae fusion",
            "roots reggae"
        ]
    },
    {
        "title": "Halftime",
        "artists": [
            "Nas"
        ],
        "popularity": 58,
        "explicit": true,
        "url": "https://open.spotify.com/track/2PRsh2LNPxoxC9OnErnelg",
        "duration_mins": 4.35,
        "genres": [
            "conscious hip hop",
            "east coast hip hop",
            "gangster rap",
            "hardcore hip hop",
            "hip hop",
            "queens hip hop",
            "rap"
        ]
    },
    {
        "title": "Check the Rhime",
        "artists": [
            "A Tribe Called Quest"
        ],
        "popularity": 63,
        "explicit": false,
        "url": "https://open.spotify.com/track/4HfxDJ0uLHTLe0fZrx0MbQ",
        "duration_mins": 3.61,
        "genres": [
            "conscious hip hop",
            "east coast hip hop",
            "golden age hip hop",
            "hip hop",
            "jazz rap",
            "queens hip hop"
        ]
    },
    {
        "title": "Music To Watch Boys To",
        "artists": [
            "Lana Del Rey"
        ],
        "popularity": 66,
        "explicit": false,
        "url": "https://open.spotify.com/track/34rRFl0bz9PocxWuO2ca5J",
        "duration_mins": 4.84,
        "genres": [
            "art pop",
            "pop"
        ]
    },
    {
        "title": "Letters",
        "artists": [
            "Lera Lynn"
        ],
        "popularity": 16,
        "explicit": false,
        "url": "https://open.spotify.com/track/2SrJu4ppnT0UOtiGBXNuAa",
        "duration_mins": 4.01,
        "genres": [
            "alternative country",
            "new americana"
        ]
    },
    {
        "title": "Keepin' the Faith",
        "artists": [
            "De La Soul"
        ],
        "popularity": 34,
        "explicit": false,
        "url": "https://open.spotify.com/track/0gkhZoy5NAo8HpWo5EFJ3M",
        "duration_mins": 4.75,
        "genres": [
            "east coast hip hop",
            "golden age hip hop",
            "hip hop",
            "jazz rap"
        ]
    },
    {
        "title": "Ring Ring Ring (Ha Ha Hey)",
        "artists": [
            "De La Soul"
        ],
        "popularity": 41,
        "explicit": false,
        "url": "https://open.spotify.com/track/1zRW3vr3uw0tdG7iLWUZpn",
        "duration_mins": 5.09,
        "genres": [
            "east coast hip hop",
            "golden age hip hop",
            "hip hop",
            "jazz rap"
        ]
    },
    {
        "title": "Dealer",
        "artists": [
            "Lana Del Rey"
        ],
        "popularity": 71,
        "explicit": true,
        "url": "https://open.spotify.com/track/7iqQz931tn59mK6IZ3knRx",
        "duration_mins": 4.57,
        "genres": [
            "art pop",
            "pop"
        ]
    },
    {
        "title": "Eli, The Barrow Boy",
        "artists": [
            "Audra Mae"
        ],
        "popularity": 5,
        "explicit": false,
        "url": "https://open.spotify.com/track/2fdjuE9589q0fihNYyqMuw",
        "duration_mins": 4.31,
        "genres": [
            "alternative roots rock"
        ]
    },
    {
        "title": "Fishtail",
        "artists": [
            "Lana Del Rey"
        ],
        "popularity": 61,
        "explicit": false,
        "url": "https://open.spotify.com/track/4Cg9XRHLP3s5ZiQaIdL4zW",
        "duration_mins": 4.04,
        "genres": [
            "art pop",
            "pop"
        ]
    },
    {
        "title": "R\u00e4t",
        "artists": [
            "Penelope Scott"
        ],
        "popularity": 69,
        "explicit": true,
        "url": "https://open.spotify.com/track/4blPH3Uy89WnOnYlIv7Ev4",
        "duration_mins": 3.24,
        "genres": [
            "alt z",
            "modern indie pop",
            "pov: indie"
        ]
    },
    {
        "title": "Lotta True Crime",
        "artists": [
            "Penelope Scott"
        ],
        "popularity": 63,
        "explicit": true,
        "url": "https://open.spotify.com/track/18jbMG8etanCMt6C5wFRDa",
        "duration_mins": 3.37,
        "genres": [
            "alt z",
            "modern indie pop",
            "pov: indie"
        ]
    },
    {
        "title": "Anti-Hero",
        "artists": [
            "Taylor Swift"
        ],
        "popularity": 82,
        "explicit": false,
        "url": "https://open.spotify.com/track/0V3wPSX9ygBnCm8psDIegu",
        "duration_mins": 3.34,
        "genres": [
            "pop"
        ]
    },
    {
        "title": "Come Down",
        "artists": [
            "Anderson .Paak"
        ],
        "popularity": 62,
        "explicit": true,
        "url": "https://open.spotify.com/track/276zciJ7Fg7Jk6Ta6QuLkp",
        "duration_mins": 2.83,
        "genres": [
            "escape room",
            "hip hop",
            "indie soul",
            "neo soul"
        ]
    },
    {
        "title": "Emily I'm Sorry",
        "artists": [
            "boygenius",
            "Julien Baker",
            "Phoebe Bridgers",
            "Lucy Dacus"
        ],
        "popularity": 60,
        "explicit": true,
        "url": "https://open.spotify.com/track/693xmBAOD4xwkS4W71W1Jn",
        "duration_mins": 3.58,
        "genres": [
            "indie pop",
            "pov: indie",
            "ambient folk",
            "la indie",
            "art pop"
        ]
    },
    {
        "title": "Regulate",
        "artists": [
            "Warren G",
            "Nate Dogg"
        ],
        "popularity": 72,
        "explicit": true,
        "url": "https://open.spotify.com/track/7nYvUtkQMx1v80S2FH2s9J",
        "duration_mins": 4.15,
        "genres": [
            "g funk",
            "gangster rap",
            "hardcore hip hop",
            "hip hop",
            "west coast rap"
        ]
    },
    {
        "title": "I Got Love",
        "artists": [
            "Nate Dogg"
        ],
        "popularity": 55,
        "explicit": true,
        "url": "https://open.spotify.com/track/52riputZ4Vo5PG9MOSy6r5",
        "duration_mins": 3.94,
        "genres": [
            "g funk",
            "gangster rap",
            "hardcore hip hop",
            "hip hop",
            "west coast rap"
        ]
    },
    {
        "title": "God Knows I Tried",
        "artists": [
            "Lana Del Rey"
        ],
        "popularity": 58,
        "explicit": false,
        "url": "https://open.spotify.com/track/5R65WfxdtxpTNSIloTfIdM",
        "duration_mins": 4.68,
        "genres": [
            "art pop",
            "pop"
        ]
    },
    {
        "title": "The Night They Drove Old Dixie Down",
        "artists": [
            "Joan Baez"
        ],
        "popularity": 52,
        "explicit": false,
        "url": "https://open.spotify.com/track/0uHYplBhwLYey7f9qAmnSM",
        "duration_mins": 3.43,
        "genres": [
            "american folk revival",
            "folk",
            "folk rock",
            "singer-songwriter"
        ]
    },
    {
        "title": "Bad Habit",
        "artists": [
            "Steve Lacy"
        ],
        "popularity": 73,
        "explicit": true,
        "url": "https://open.spotify.com/track/5CM4UuQ9Gnd6K2YyKGPMoK",
        "duration_mins": 3.87,
        "genres": [
            "afrofuturism"
        ]
    },
    {
        "title": "Night Shift",
        "artists": [
            "Lucy Dacus"
        ],
        "popularity": 66,
        "explicit": true,
        "url": "https://open.spotify.com/track/1yYlpGuBiRRf33e1gY61bN",
        "duration_mins": 6.53,
        "genres": [
            "art pop",
            "indie pop"
        ]
    }
]