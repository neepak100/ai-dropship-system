# Deployment Checklist

## Pre-deployment:
1. Ensure all code is tested and reviewed.
2. Update the version number in `package.json`.
3. Check for any pending migrations.
4. Backup the database.
5. Review the changelog for important updates.

## Deployment Steps:
1. Pull the latest code from the repository:
   ```bash
   git pull origin main
   ```
2. Install any new dependencies:
   ```bash
   npm install
   ```
3. Run any new database migrations:
   ```bash
   npm run migrate
   ```
4. Restart the application service:
   ```bash
   pm2 restart <app_name>
   ```
5. Verify the application is running:
   - Check application logs for errors.
   - Perform a health check at the URL: `http://your-app-url/health`

## Post-deployment:
1. Monitor application performance.
2. Confirm user feedback is received and any issues reported are addressed.
3. Announce the deployment completion to the team.

## Additional Notes:
- Ensure that environment variables are correctly set in the production environment.
- If using Docker, ensure the Docker containers are updated accordingly.
- Consider setting up monitoring tools to alert for any deployment issues.

## Setup Instructions:
### Cloning the Repository:
1. Clone the repository:
   ```bash
   git clone https://github.com/neepak100/ai-dropship-system.git
   ```
2. Navigate into the project directory:
   ```bash
   cd ai-dropship-system
   ```

### Environment Setup:
1. Ensure you have Node.js installed (version >= 14).
2. Install necessary packages:
   ```bash
   npm install
   ```
3. Create a `.env` file based on the `.env.example` file and set required environment variables.
4. Run the application:
   ```bash
   npm start
   ```