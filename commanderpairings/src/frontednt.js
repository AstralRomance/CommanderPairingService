function checkToken()
{
    if (localStorage.getItem('jwt') != null)
            fetch('/validate_token', {headers:
                                                    {
                                                        'Authorization':localStorage.getItem('jwt'),
                                                        'Content-Type': 'application/json'
                                                    },
                                                    method:'GET'})
            .then(response => response.json())
            .then(json => json.is_valid)
            .then(validate => {
                if (validate == true)
                    return true
                else
                    getToken();
            });
        else
            getToken()
}

function getToken()
{
    fetch('/token', {method:'GET'})
            .then(response => response.json())
            .then(json => json.jwt)
            .then(token => {
                localStorage.setItem('jwt',token);
                return token;
            })
}

function makePairingsPage()
{
    fetch('/get_pairings', {method:'GET', headers:
                                                    {
                                                        'Authorization':localStorage.getItem('jwt'),
                                                    }})
    .then(response => response.json())
    .then(json => json.players)
    .then(players => {
        for (let player of players)
        {
            let player_container = document.createElement('div');
            player_container.className = 'PlayerContainer';
            player_container.append(document.createTextNode(player[0]));
        }
    })
}