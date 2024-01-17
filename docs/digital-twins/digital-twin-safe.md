# Digital Twin Safe Product Requirements

![digital-twin-safe-no-text.png](../../images/digital-twin-safe-no-text.png)

This outlines the requirements for a tool to allow people to create and manage their digital twin. The platform will leverage automation, API integration, and AI to streamline the digital twin creation process.

### High-Level Requirements
1. **Automated Digital Twin Creation:** 
   - Anyone should be able to automatically generate a digital twin by:
      - importing data via APIs or 
      - through web research AI agents
      - uploading data through a web interface
      - editing files using tools like [Obsidian](https://obsidian.md/)

2. **Data Import:**
   - Scheduled data imports from Google Drive, OneDrive, Notion, and various health apps and wearables.
   - Utilize Next.js and NextAuth for the framework and authentication.
   - NextAuth has built-in support for authentication and importing data from:
     - Google Drive
     - Gmail
     - Google Calendar
     - Google Contacts
     - Google Sheets
     - Google Tasks
     - OneDrive
     - Notion
     - Slack
     - Twitter
     - Spotify
     - Strava
     - Fitbit
     - GitHub
     - GitLab
     - Facebook
     - Discord
     - Instagram
     - LinkedIn
     - Reddit
     - Dropbox
     - WordPress
     - Whatever else people use
   - URLs: 
     - Overview: https://{username}.wishonia.ai/admin/add-connector
     - Specific Connection Management Page: https://{username}.wishonia.ai/admin/admin/connectors/{connector_name}

3. **Chat Interface to Directly Talk to Your Digital Twin:** 
   - a chat UI at https://{username}.wishonia.ai/chat to interact with their digital twin
   - In order to preserve privacy and control costs, the analog twin should be able to configure a paywall for their digital twin.

4. **A Personal API for Your Digital Twin:**
   - Your Digital Twin's API is an easy way for you to interact with your digital twin.
   - Enable users to sign up for an API key to communicate with their digital twin.
   - Incorporate usage monitoring and Stripe integration for billing.
   - URL: https://{user_name}.wishonia.ai/api

5. **API Documentation:**
   - Provide interactive OpenAPI documentation.
   - URL: https://{user_name}.wishonia.ai/api/docs

6. **SDK Auto-generation:**
   - This allows developers to include Digital Twins in their own applications (or virtual worlds) with minimal effort.
   - SDKs require API keys to access the Digital Twin API

7. **OAuth2 Server Integration:** 
   - Allow users to grant third-party applications access to their Digital Twin data.

8. **User-Specific URLs:** Assign individual URLs for each user's digital twin and related functionalities.

9. **User Dashboard:** Create a user dashboard for managing the digital twin, settings, billing, etc.

10. **Git Repository Synchronization:** 
    - Your safe will sync user data to their Digital Twin GitHub repository in markdown and CSV formats.  
    - The benefits of storing data in a GitHub repository are:
       - Version control
         - Users can easily revert to previous versions of their data if necessary.
       - Collaboration
         - For Digital Twins of organizations, teams can contribute to a shared data repository with fine-grained access controls.
       - Openness
       - Portability
         - By being able to easily clone the repository anywhere, it can be easily used in other systems without having to deal with API integrations.
       - Security
         - GitHub has heavy built-in security features and fine-grained access controls
       - Automation
         - Automatically update vector database embeddings when data is added or changed using a GitHub action
       - **URL:** https://{username}.wishonia.ai/admin/git-sync

11. **Customization Options:** 
    - Allow users to customize their digital twin's
      - personality traits
      - edit responses to specific questions in the question/answer history
      - set all the properties listed in the [Digital Twin Data Model](digital-twin-data-model.md)

12. **Privacy Settings:**
    - Provide robust privacy controls for users to manage who can access their digital twin and what data is shared.
    - Create multiple personas for your digital twin to interact with different groups of people with access to different "collections" of data

13. **Notification System:**
    - Implement notifications for
      - important updates
      - scheduled data imports
      - API usage alerts
      - billing
      - import errors
      - handoffs to the analog twin for specific types of questions or people

14. **User Support and Tutorial:**
    - Include a help section with tutorials on creating and managing digital twins, and a support system for user inquiries.

15. **Feedback Mechanism:**
    - Users speaking to the digital twin in the chat UI should be able to thumbs up or thumbs down responses.  These ratings should be able to be applied to improve future responses using reinforcement learning.
    - The analog twin should be able to review all previous conversations and provide superior responses which will be incorporated and heavily weighted in training data or vector DB search rankings. 
    - users to provide feedback on the platform, contributing to continuous improvement.

16. **Mobile Responsiveness:** 
    - Ensure that the web interface is fully responsive and accessible on various devices, including tablets and smartphones.

## Learn More
- [Why Digital Twins?](why-digital-twins.md) - Why we need digital twins to create a better world.
- [How to Create a Digital Twin](how-to-build-a-digital-twin.md) - How to create a digital twin.
- [Digital Twin Safe](digital-twin-safe.md)
  - [Site Map](dts-site-map.md)
- [Data Sources](digital-twin-data-sources.md)
- [Data Model](digital-twin-data-model.md)
