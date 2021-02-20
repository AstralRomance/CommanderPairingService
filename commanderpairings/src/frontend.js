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

function makePairingsPage()
{
    fetch('/get_players', {method:'GET', headers:
                                                    {
                                                        'Authorization':localStorage.getItem('jwt'),
                                                    }})
    .then(response => response.json())
    .then(json => json.players)
    .then(players => {
        let html_container = document.getElementById('playerName');
        for (let player of players)
        {
            let player_container = document.createElement('div');
            player_container.className = 'PlayerContainer';
            player_container.append(document.createTextNode(player['player_name']));
            player_container.append(document.createTextNode(' '));
            player_container.append(document.createTextNode(player['player_commander']));
            player_container.append(document.createTextNode(' - '));
            player_container.append(document.createTextNode(player['points']));
            html_container.append(player_container);
        }
    })
}
