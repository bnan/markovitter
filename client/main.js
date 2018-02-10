const API_URL = 'http://localhost:1337/new/'

async function fetchGeneratedTweet(username) {
    let response = await fetch(API_URL + username)
    if (response.ok) {
        let data = await response.json()
        return data.message
    } else {
        throw new Error(response.status)
    }
}

async function handleGenerate() {
    const username = document.getElementById('username').value
    let message = await fetchGeneratedTweet(username)
    console.log(message)
    document.getElementById('result').textContent = message
}

function main() {
    document.getElementById('generate').addEventListener('click', () => handleGenerate())
}

main()

