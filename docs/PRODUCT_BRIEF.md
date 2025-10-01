# Jobsy - Job Querying and Management System

## Project Overview / Description

Jobsy is a comprehensive job querying system that searches for job openings across the web based on user preferences. The system integrates with external APIs to fetch job data, stores it in a database, and allows users to save and manage their job applications with custom tracking information. Additionally, Jobsy features AI-powered capabilities for generating personalized cover letters and tailored resumes for selected job applications. 

## Target Audience

- **Primary**: Job seekers who want to efficiently search, apply and track job opportunities
- **Secondary**: Career changers exploring opportunities in different fields or locations
- **Tertiary**: Professionals who want to stay informed about relevant job market trends

## Primary Benefits / Features

### Core Features
- **Job Querying System**: Search for job openings across the web based on user preferences
- **External API Integration**: Fetch job data from multiple external sources
- **Database Storage**: Store job listings in a centralized database for efficient retrieval
- **Job Management**: Save jobs to a separate table for personal tracking and customization
- **Application Tracking**: Add custom information such as application status, notes, and application dates
- **User Preferences**: Configure search criteria to match individual job search needs
- **AI-Powered Cover Letter Generation**: Generate personalized cover letters for jobs
- **AI-Powered Resume Tailoring**: Generate tailored resumes optimized for job applications

### Key Benefits
- **Centralized Job Search**: Single platform to query jobs from multiple sources
- **Personal Job Management**: Save and customize job listings with personal tracking information
- **Application Organization**: Track application status, notes, and important dates
- **Efficient Data Management**: Store and retrieve job data efficiently through database integration
- **Customizable Tracking**: Add personal notes and status updates to saved jobs
- **AI-Enhanced Applications**: Generate professional cover letters and tailored resumes for better application success

## High-Level Tech/Architecture

### Backend Stack
- **Database**: Supabase for storing job listings and user-saved jobs
- **Language**: Python for core application logic and API integrations
- **External APIs**: Integration with job data providers for fetching job openings
- **AI Integration**: OpenAI for cover letter generation and resume tailoring
- **Design Pattern**: CSR (Controller-Service-Repository) architecture pattern

### System Components
- **Job Querying Engine**: System for searching and filtering job openings based on user preferences
- **Data Storage Layer**: Database tables for job listings and user-saved jobs with custom fields
- **API Integration Layer**: External API connections for job data retrieval
- **User Management**: System for managing user preferences and saved job collections

### Architecture Details
- **Controller Layer**: API endpoints handling HTTP requests and responses
- **Service Layer**: Business logic services for job processing and user management
- **Repository Layer**: Data access abstraction for database operations
- **External API Integration**: Third-party job data providers (e.g., TheStack API)


