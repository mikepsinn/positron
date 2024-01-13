# Pull Requests

To contribute to the Positron Network Architect Agent project, follow the steps below to set up and configure GitHub Actions.

## GitHub Actions Setup and Configuration

1. Create a new file named `.github/workflows/main.yml` in the root directory of your repository.
2. Copy the following content into the `main.yml` file:

```yaml
name: Positron Network Architect Agent GitHub Actions

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build-and-test:
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

      - name: Run tests
        run: npm test

      - name: Publish test results
        uses: actions/upload-artifact@v2
        with:
          name: test-results
          path: test-results.xml
```

3. Save the file.

## GitHub Actions Imports and Entities

To interact with the GitHub API using GitHub Actions, you can use the `@actions/github` package. This package provides convenient methods for making API requests and handling responses.

To import the necessary modules and entities, add the following code at the beginning of your workflow file:

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
