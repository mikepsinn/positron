# Collabathons

> 🚧 Work in progress.  Pull requests with improvement suggestions welcome.

## Overview

Collabathons are like hackathons, but all participants work together on the same open-source project. Judges vote on what contributions get accepted and the rewards for them. These produce more long-term value than just creating little projects typically abandoned after the hackathon.

Positron Collabathons are designed
to maximize wish fulfillment and minimize suffering by:
- creating autonomous agents to produce public goods
- supporting non-profit organizations in their missions
- counterbalancing the inevitable wave of extractive and malevolent AI agents that will soon be draining the productive, cooperative economy

## Collabathon Details
- **Location**: Hybrid online/IRL
- **Participation Incentive**: Maybe $1000 in prizes per week
- **Challenge Creation**: Non-Profits create "Wishes" for agents with highly specific SMART (Specific, Measurable, Achievable, Relevant, Time-bound) objectives that would advance their missions.
- **Submission Platform**: Participants make submissions of their implementation via GitHub pull requests which are reviewed and voted on by judges.

## Submission Guidelines

**Avoiding Wheel Reinvention**

Positron is not intended to be a standalone autonomous agent framework.
There are already a lot of great autonomous agent frameworks such as Autogen, OpenAgents, TaskWeaver, AutoGPT, SuperAGI, etc.

The Positron repository is meant to be a collection of specific operationalized autonomous agents that these existing frameworks and libraries to create operational agents that can be run in GitHub Actions.


### Types of Contributions

1. **Autonomous Public Good (APG) Agents**: Directly creates a real public good that improves the world in a measurable way. [Examples below](#example-public-good-agents)
2. **Autonomous Non-Profit (ANP) Agents**: Supports a non-profit organization in its mission in accordance with the [Six Practices of High-Impact Nonprofits](../../autonomous-nonprofit-designer-gpt/instructions.md).
3. **Positron Framework Contributions**: Bring the Positron framework closer to the long-term vision of a self-improving repository capable of sustaining itself and autonomously granting prosocial wishes submitted as GitHub issues.
4. **External Framework Contributions**: Improvements to third-party open-source libraries or other autonomous agent frameworks that are used by Positron agents or the Positron Framework should be encouraged and rewarded.  One should provide a link to their external repo-commits and an illustration of the benefits with an agent implementation.

### Prize Eligibility Requirements
- **Open-Source**: Must be licensed under [GPLv3](../../LICENSE).
- **Functional Implementation**: Must include a [GitHub Action Configuration](https://docs.github.com/en/actions) be functional in a pull request to the [Positron repository](https://github.com/wishocracy/positron).
  - **Web Deployments**: If your contribution has an API component or web-based UI interface, your GitHub Action should also include an automated deployment configuration to a platform like [Vercel](https://vercel.com/).
  - **Headless Agents**: If your contribution is a headless agent, it should include a GitHub Action that runs the agent on a schedule or trigger.
- **Documentation**: Must include a README.md file with a description of the agent, its purpose, and its implementation.
  - **Agent Impact**: Must include a description of the agent's impact in terms of its lead and lag measures.
  - **Usage Instructions**: Must include instructions for how to use the agent.

### Bonus Points

- **Open-Source AI Models**: Model-agnostic configuration options are highly desirable as opposed to hard-coding dependency on closed-source proprietary APIs.
- **Task-Optimized Small Language Models with RL** - Open-source small language models that are optimized for specific tasks have been shown to be more efficient and capable than generalized large language models in various tasks.

**Preferred Technologies**: 

- **JavaScript**: It's the most popular programming language and the only one that can be run in the following environments without any additional setup:
  - GitHub Actions
  - Vercel
  - the browser
  - most OSes
- **Python where necessary**: Has the most AI libraries and is the most popular language for AI development.

## Evaluation and Rewards
**Judging Process**:
Review and voting on pull requests in Positron repository.
- Submissions via pull requests.
- Judges review, approve, or request changes.
- Rationale and feedback provided in comments.

- **Prize Distribution**: Divided among successful pull request merges.

### Example Public Good Agents
1. **Research Agents**: Examples include: Identifying the most promising interventions to create a volume knob for suffering, leaderboard creation for collective intelligence tools, analysis of life-extension projects and interventions to enhance efficiency through coordination and resource pooling, etc.
2. **Public Policy Analysis Agent**: Comparative analysis of policies for societal benefits.
3. **Human Rights Watch Agent**: Identification and publicity of global human rights abuses.
4. **Immigration Causes Analysis Agent**: Addressing root causes of excess immigration.
5. **Opioid Crisis Addressing Agent**: Identifying and addressing universal pain and unhappiness.
6. **Elderly Care Agent**: Regular check-ins with elderly, monitoring health and wellbeing.
7. **AI-Driven FDA Agent**: Data collection and analysis on food, medication, and health impacts.
8. **Cybersecurity Agent**: Protection against cybercrime and support for victims.
9. **Animal Welfare Agent**: Identification of suffering in factory farms and advocacy efforts.

## Required Resources
1. **Event Costs**: promotion, prizes, food (vegetarian, please! 🐮), venue, etc.
2. **Coordinator**: an AI Engineer to manage collabathons and provide technical support
3. **Agent Compute Costs**: funding to run the most impactful winning agents
