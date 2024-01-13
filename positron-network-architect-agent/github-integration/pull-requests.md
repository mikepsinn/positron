# positron-network-architect-agent/github-integration/pull-requests.md

# Updated GitHub Actions Configuration

name: Pull Requests

on:
  pull_request:
    types:
      - opened
      - synchronize
      - reopened

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      # Add your build and test steps here

      - name: Run tests
        run: |
          # Add your test commands here

      - name: Deploy to production
        if: github.event.pull_request.merged == true
        run: |
          # Add your deployment commands here
