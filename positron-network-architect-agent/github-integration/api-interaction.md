name: API Interaction

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  api-interaction:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Node.js environment
        uses: actions/setup-node@v2
        with:
          node-version: 14

      - name: Install dependencies
        run: npm ci

      - name: Run API interaction script
        run: node api-interaction.js
```

### API Interaction

To interact with the GitHub API using GitHub Actions, we can use the `@actions/github` package. This package provides convenient methods for making API requests and handling responses.

To import the necessary modules and entities, add the following code at the beginning of your `api-interaction.js` file:

```javascript
const { Octokit } = require("@octokit/rest");
const octokit = new Octokit();
```

Now, you can use the `octokit` object to make API requests. Here's an example of how to get information about a repository:

```javascript
const getRepository = async (owner, repo) => {
  try {
    const response = await octokit.rest.repos.get({
      owner,
      repo,
    });
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
};

getRepository("positron", "positron-network-architect-agent");
