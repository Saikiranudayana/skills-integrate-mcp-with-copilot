# PowerShell script to create GitHub issues
# Make sure you have GitHub CLI installed and authenticated first

Write-Host "Creating GitHub issues for Mergington High School Activities enhancements..." -ForegroundColor Green

# Function to create an issue
function New-GitHubIssue {
    param(
        [string]$Title,
        [string]$Body,
        [string]$Labels
    )
    
    Write-Host "Creating issue: $Title" -ForegroundColor Yellow
    gh issue create --title $Title --body $Body --label $Labels
}

# High Priority Issues
New-GitHubIssue -Title "🔐 Implement User Authentication System" -Body @"
## Description
Replace the current email-based system with proper user authentication.

## Current State
- Students are identified only by email strings
- No login/logout functionality
- No user sessions or security

## Proposed Enhancement
- User registration and login system
- Session management
- Password security (hashing)
- User roles (student, instructor, admin)

## Acceptance Criteria
- [ ] Users can register with email and password
- [ ] Users can login and logout
- [ ] Sessions are properly managed
- [ ] Passwords are securely hashed
- [ ] Basic role-based access control

## Priority
High - Foundation for other features
"@ -Labels "enhancement,security,high-priority"

New-GitHubIssue -Title "💾 Replace In-Memory Storage with Database" -Body @"
## Description
Implement persistent database storage to replace the current in-memory data structure.

## Current State
- All data stored in memory (Python dictionaries)
- Data is lost when server restarts
- No data persistence or reliability

## Proposed Enhancement
- SQLite database for development
- PostgreSQL for production
- Proper data models and schemas
- Database migrations

## Acceptance Criteria
- [ ] Database schema designed and implemented
- [ ] All current functionality works with database
- [ ] Data persists across server restarts
- [ ] Basic database migration system
- [ ] Environment-specific database configuration

## Priority
High - Critical for production use
"@ -Labels "enhancement,database,high-priority"

New-GitHubIssue -Title "👤 Enhanced Student Profiles" -Body @"
## Description
Expand student information beyond just email addresses to include comprehensive profiles.

## Current State
- Students identified only by email
- No additional student information stored

## Proposed Enhancement
- Full student profiles (name, grade, student ID)
- Contact information and emergency contacts
- Profile photos
- Academic information
- Activity history

## Acceptance Criteria
- [ ] Student profile data model created
- [ ] Profile creation and editing interface
- [ ] Profile photo upload functionality
- [ ] Contact information management
- [ ] Activity participation history

## Priority
High - Needed for proper student management
"@ -Labels "enhancement,user-management,high-priority"

New-GitHubIssue -Title "🔧 Admin Dashboard" -Body @"
## Description
Create an administrative interface for managing activities, students, and system settings.

## Current State
- No administrative interface
- Activities are hardcoded in the application
- No user management tools

## Proposed Enhancement
- Dedicated admin dashboard
- Activity creation and management
- Student management interface
- System configuration options
- Usage statistics and reports

## Acceptance Criteria
- [ ] Admin-only access control
- [ ] Activity CRUD operations
- [ ] Student management interface
- [ ] Basic system statistics
- [ ] Settings configuration panel

## Priority
High - Essential for content management
"@ -Labels "enhancement,admin,high-priority"

New-GitHubIssue -Title "📧 Email Notification System" -Body @"
## Description
Implement automated email notifications for activity updates and important events.

## Current State
- No automated communications
- Students must manually check for updates

## Proposed Enhancement
- Email notifications for activity signup confirmations
- Reminders for upcoming activities
- Activity cancellation or change notifications
- Welcome emails for new registrations
- Configurable notification preferences

## Acceptance Criteria
- [ ] Email service integration (SMTP)
- [ ] Signup confirmation emails
- [ ] Activity reminder system
- [ ] Change notification emails
- [ ] User email preferences
- [ ] Email templates

## Priority
High - Improves user experience significantly
"@ -Labels "enhancement,communication,high-priority"

Write-Host "`n✅ Created 5 high-priority issues!" -ForegroundColor Green
Write-Host "`nTo create medium and long-term priority issues, you can:" -ForegroundColor Cyan
Write-Host "1. Run this script again with the remaining issues" -ForegroundColor White
Write-Host "2. Use the GitHub web interface to create issues manually" -ForegroundColor White
Write-Host "3. Use the generated github_issues.json file" -ForegroundColor White
Write-Host "`nRun 'gh issue list' to see all created issues" -ForegroundColor Yellow
