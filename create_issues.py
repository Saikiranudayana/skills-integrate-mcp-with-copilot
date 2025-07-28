#!/usr/bin/env python3
"""
Script to create GitHub issues for the Mergington High School Activities enhancement
"""

import json
import os

# Issue templates for the enhancement features
issues = [
    # HIGH PRIORITY - Quick Wins
    {
        "title": "🔐 Implement User Authentication System",
        "body": """## Description
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

## Labels
enhancement, security, high-priority""",
        "labels": ["enhancement", "security", "high-priority"]
    },
    
    {
        "title": "💾 Replace In-Memory Storage with Database",
        "body": """## Description
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

## Labels
enhancement, database, high-priority""",
        "labels": ["enhancement", "database", "high-priority"]
    },
    
    {
        "title": "👤 Enhanced Student Profiles",
        "body": """## Description
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

## Labels
enhancement, user-management, high-priority""",
        "labels": ["enhancement", "user-management", "high-priority"]
    },
    
    {
        "title": "🔧 Admin Dashboard",
        "body": """## Description
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

## Labels
enhancement, admin, high-priority""",
        "labels": ["enhancement", "admin", "high-priority"]
    },
    
    {
        "title": "📧 Email Notification System",
        "body": """## Description
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

## Labels
enhancement, communication, high-priority""",
        "labels": ["enhancement", "communication", "high-priority"]
    },
    
    # MEDIUM PRIORITY - Significant Impact
    {
        "title": "📅 Calendar Integration and Scheduling",
        "body": """## Description
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
Medium - Significant UX improvement

## Labels
enhancement, calendar, medium-priority""",
        "labels": ["enhancement", "calendar", "medium-priority"]
    },
    
    {
        "title": "📋 Waitlist Management System",
        "body": """## Description
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
Medium - Improves capacity management

## Labels
enhancement, registration, medium-priority""",
        "labels": ["enhancement", "registration", "medium-priority"]
    },
    
    {
        "title": "📊 Analytics Dashboard",
        "body": """## Description
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
Medium - Valuable for decision making

## Labels
enhancement, analytics, medium-priority""",
        "labels": ["enhancement", "analytics", "medium-priority"]
    },
    
    {
        "title": "🏷️ Activity Categories and Advanced Management",
        "body": """## Description
Enhance activity management with categories, tags, prerequisites, and skill levels.

## Current State
- Simple activity list with basic information
- No categorization or filtering options

## Proposed Enhancement
- Activity categories (Sports, Arts, Academic, etc.)
- Tagging system for better organization
- Skill level requirements
- Activity prerequisites
- Equipment and resource tracking

## Acceptance Criteria
- [ ] Category system implementation
- [ ] Tag-based organization
- [ ] Skill level classification
- [ ] Prerequisite system
- [ ] Resource management
- [ ] Advanced filtering options

## Priority
Medium - Improves organization and discovery

## Labels
enhancement, organization, medium-priority""",
        "labels": ["enhancement", "organization", "medium-priority"]
    },
    
    # LONG-TERM - Advanced Features
    {
        "title": "📱 Mobile Application Development",
        "body": """## Description
Develop native mobile applications for iOS and Android platforms.

## Current State
- Web-only interface
- Limited mobile responsiveness

## Proposed Enhancement
- Native iOS application
- Native Android application
- Offline functionality for essential features
- Push notifications
- Mobile-optimized user experience

## Acceptance Criteria
- [ ] iOS app development
- [ ] Android app development
- [ ] Offline capability
- [ ] Push notification system
- [ ] App store deployment
- [ ] Mobile-specific features

## Priority
Long-term - Advanced user experience

## Labels
enhancement, mobile, long-term""",
        "labels": ["enhancement", "mobile", "long-term"]
    },
    
    {
        "title": "🎖️ Achievement and Badge System",
        "body": """## Description
Implement a gamification system with digital badges and achievements.

## Current State
- No recognition or achievement system
- No gamification elements

## Proposed Enhancement
- Digital badge system
- Achievement milestones
- Participation certificates
- Progress tracking
- Student portfolio system

## Acceptance Criteria
- [ ] Badge design and implementation
- [ ] Achievement milestone system
- [ ] Certificate generation
- [ ] Progress visualization
- [ ] Portfolio creation tools
- [ ] Sharing capabilities

## Priority
Long-term - Engagement enhancement

## Labels
enhancement, gamification, long-term""",
        "labels": ["enhancement", "gamification", "long-term"]
    },
    
    {
        "title": "💬 Discussion Forums and Communication",
        "body": """## Description
Add discussion forums and enhanced communication features.

## Current State
- No communication features between users
- No discussion or Q&A capabilities

## Proposed Enhancement
- Activity-specific discussion forums
- Direct messaging system
- Q&A sections
- Announcement system
- Parent/guardian communication portal

## Acceptance Criteria
- [ ] Forum implementation
- [ ] Messaging system
- [ ] Q&A functionality
- [ ] Announcement system
- [ ] Parent portal
- [ ] Moderation tools

## Priority
Long-term - Community building

## Labels
enhancement, communication, long-term""",
        "labels": ["enhancement", "communication", "long-term"]
    },
    
    {
        "title": "🔗 Third-Party Integration Framework",
        "body": """## Description
Develop integration capabilities with external systems and services.

## Current State
- Standalone system with no external integrations

## Proposed Enhancement
- Student Information System (SIS) integration
- Google Workspace/Microsoft 365 integration
- Payment processing for fee-based activities
- Calendar application integration
- Email service provider integration

## Acceptance Criteria
- [ ] SIS integration framework
- [ ] Google/Microsoft integration
- [ ] Payment processing setup
- [ ] Calendar app integration
- [ ] Email service integration
- [ ] API documentation

## Priority
Long-term - Enterprise features

## Labels
enhancement, integration, long-term""",
        "labels": ["enhancement", "integration", "long-term"]
    },
    
    {
        "title": "🛡️ Advanced Security and Compliance",
        "body": """## Description
Implement enterprise-grade security features and compliance measures.

## Current State
- Basic or no security measures
- No compliance considerations

## Proposed Enhancement
- Multi-factor authentication
- Data encryption and privacy compliance
- Audit trails and logging
- FERPA compliance for educational data
- Backup and disaster recovery

## Acceptance Criteria
- [ ] Multi-factor authentication
- [ ] Data encryption implementation
- [ ] Audit logging system
- [ ] Privacy compliance measures
- [ ] Backup and recovery system
- [ ] Security documentation

## Priority
Long-term - Enterprise security

## Labels
enhancement, security, compliance, long-term""",
        "labels": ["enhancement", "security", "compliance", "long-term"]
    }
]

def save_issues_json():
    """Save issues to a JSON file for easy import"""
    with open('github_issues.json', 'w') as f:
        json.dump(issues, f, indent=2)
    print(f"Created github_issues.json with {len(issues)} issues")

def print_issue_summary():
    """Print a summary of all issues"""
    print("\n" + "="*80)
    print("MERGINGTON HIGH SCHOOL ACTIVITIES - ENHANCEMENT ISSUES")
    print("="*80)
    
    high_priority = [i for i in issues if 'high-priority' in i.get('labels', [])]
    medium_priority = [i for i in issues if 'medium-priority' in i.get('labels', [])]
    long_term = [i for i in issues if 'long-term' in i.get('labels', [])]
    
    print(f"\n🔥 HIGH PRIORITY ({len(high_priority)} issues):")
    for issue in high_priority:
        print(f"   • {issue['title']}")
    
    print(f"\n⚡ MEDIUM PRIORITY ({len(medium_priority)} issues):")
    for issue in medium_priority:
        print(f"   • {issue['title']}")
    
    print(f"\n🚀 LONG-TERM ({len(long_term)} issues):")
    for issue in long_term:
        print(f"   • {issue['title']}")
    
    print(f"\nTotal: {len(issues)} enhancement issues")
    print("\nTo create these issues in GitHub:")
    print("1. Use the GitHub web interface")
    print("2. Install GitHub CLI and run the creation script")
    print("3. Use the GitHub API with the generated JSON file")

if __name__ == "__main__":
    save_issues_json()
    print_issue_summary()
