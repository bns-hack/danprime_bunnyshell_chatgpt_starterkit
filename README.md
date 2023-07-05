3 Services
1. Backend (FastAPI)
2. Database (MySQL)
3. FrontEnd - (Bootstrap)

## Build
1. Copy example.env to `.env` file and set the `OPENAI_API_KEY` to be secret key
1. Run `docker-compose up --build`


## What
This creates a set of containers to interact OPENAI's ChatGPT.
Just plugin your [OpenAI API Key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key) as an environment variable and build.
Navigate to the built-in swagger api docs e.g. http://localhost:1313/docs
Find the /prompt and click on Execute.

Now you have connected your API to ChatGPT. Build more endpoints. Play around with the weights!


### Backend FastAPI
- Connect to it via localhost:1313
`/docs` - Shows documentation of the server

### MySQL Backend
- Connect to it via localhost:1314 root/root
- Default Database chatgpt_docs setup

