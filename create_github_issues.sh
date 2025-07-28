#!/bin/bash
# Script to create GitHub issues using GitHub CLI
# Make sure you have GitHub CLI installed and authenticated

echo "Creating GitHub issues for Mergington High School Activities enhancements..."

# High Priority Issues
gh issue create \
  --title "🔐 Implement User Authentication System" \
  --body "## Description
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
High - Foundation for other features" \
  --label "enhancement,security,high-priority"

gh issue create \
  --title "💾 Replace In-Memory Storage with Database" \
  --body "## Description
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
High - Critical for production use" \
  --label "enhancement,database,high-priority"

gh issue create \
  --title "👤 Enhanced Student Profiles" \
  --body "## Description
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
High - Needed for proper student management" \
  --label "enhancement,user-management,high-priority"

gh issue create \
  --title "🔧 Admin Dashboard" \
  --body "## Description
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
High - Essential for content management" \
  --label "enhancement,admin,high-priority"

gh issue create \
  --title "📧 Email Notification System" \
  --body "## Description
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
High - Improves user experience significantly" \
  --label "enhancement,communication,high-priority"

# Medium Priority Issues
gh issue create \
  --title "📅 Calendar Integration and Scheduling" \
  --body "## Description
Replace static schedule text with an interactive calendar system.

## Current State
- Schedules stored as plain text
- No conflict detection
- No calendar visualization

## Proposed Enhancement
- Interactive calendar interface
- Schedule conflict detection
- Calendar export functionality (iCal)
- Recurring activity support
- Holiday and event integration

## Acceptance Criteria
- [ ] Calendar view for activities
- [ ] Schedule conflict detection
- [ ] iCal export functionality
- [ ] Recurring event support
- [ ] Holiday calendar integration
- [ ] Mobile-responsive calendar

## Priority
Medium - Significant UX improvement" \
  --label "enhancement,calendar,medium-priority"

gh issue create \
  --title "📋 Waitlist Management System" \
  --body "## Description
Implement waitlist functionality when activities reach maximum capacity.

## Current State
- Simple max participant limit with rejection
- No queuing system for popular activities

## Proposed Enhancement
- Automatic waitlist when activities are full
- Waitlist position tracking
- Automatic enrollment when spots open
- Waitlist notifications
- Priority registration options

## Acceptance Criteria
- [ ] Waitlist queue implementation
- [ ] Position tracking and display
- [ ] Automatic enrollment from waitlist
- [ ] Waitlist notification system
- [ ] Priority registration rules
- [ ] Waitlist management for admins

## Priority
Medium - Improves capacity management" \
  --label "enhancement,registration,medium-priority"

gh issue create \
  --title "📊 Analytics Dashboard" \
  --body "## Description
Create an analytics dashboard to track participation, trends, and system usage.

## Current State
- No data analytics or reporting
- No insights into activity popularity or trends

## Proposed Enhancement
- Student participation analytics
- Activity popularity metrics
- Attendance tracking
- Engagement trend analysis
- Usage statistics and reports

## Acceptance Criteria
- [ ] Participation rate analytics
- [ ] Activity popularity charts
- [ ] Student engagement metrics
- [ ] Trend analysis over time
- [ ] Exportable reports
- [ ] Real-time dashboard updates

## Priority
Medium - Valuable for decision making" \
  --label "enhancement,analytics,medium-priority"

echo "✅ Created 8 issues (5 high-priority, 3 medium-priority)"
echo ""
echo "Run 'gh issue list' to see all created issues"
echo "Visit your repository on GitHub to view and manage the issues"
