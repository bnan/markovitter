const API_URL = 'http://localhost:1337/new/'

async function fetchGeneratedTweet(username) {
    let response = await fetch(API_URL + username)
    if (response.ok) {
        let data = await response.json()
        if (!data.success) {
            throw new Error(data.message)
        }
        return data
    } else {
        throw new Error(response.status)
    }
}

async function handleGenerate(e) {
    e.preventDefault()
    const username = document.getElementById('username').value
    const message = document.getElementById('message')
    const name = document.getElementById('name')
    const avatar = document.getElementById('avatar')

    try {
        let tweet = await fetchGeneratedTweet(username)
        console.log(tweet)

        message.textContent = tweet.message
        name.textContent = tweet.name
        avatar.src = tweet.avatar

        name.style.display = 'block'
        avatar.style.display = 'block'
    } catch(e) {
        name.style.display = 'none'
        avatar.style.display = 'none'

        message.textContent = 'Oops! An error occurred'
    }
}

function main() {
    document.getElementById('generate').addEventListener('click', (e) => {
        handleGenerate(e)
        const name = document.getElementById('name')
        const avatar = document.getElementById('avatar')
        name.style.display = 'none'
        avatar.style.display = 'none'
        document.getElementById('message').textContent = 'Loading...'
    })
}

main()

