# Overview

ToolSphere is a Django-based web application that provides a collection of utility tools and converters. The platform features a multi-tool hub with various calculators and unit converters including length, area, volume, temperature, speed, currency, time, numeral systems, BMI calculator, basic calculator, and home loan calculator. The application includes user authentication and registration functionality, allowing users to access the tools after logging in.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
The frontend uses Django's template system with HTML templates and static CSS/JavaScript files. The application follows a traditional server-side rendered approach with:
- Template inheritance for consistent layouts
- Static files organization with separate CSS and JavaScript files for each tool
- Responsive design with CSS Grid and Flexbox
- Client-side JavaScript for interactive calculations and conversions
- Dark theme with green accent colors for modern UI aesthetics

## Backend Architecture
The backend is built on Django framework with:
- **Django Project Structure**: Main project named "zero" with an app called "appz"
- **MVC Pattern**: Django's Model-View-Template architecture
- **URL Routing**: Centralized URL configuration with app-specific URL patterns
- **View Functions**: Function-based views handling authentication and tool rendering
- **Form Handling**: Django forms for user registration with built-in validation
- **Session Management**: Django's built-in session framework for user authentication

## Authentication System
- Uses Django's built-in User model and authentication system
- Custom registration form extending UserCreationForm with email field
- Login/logout functionality with session-based authentication
- Protected views with authentication checks
- Redirect logic for authenticated and unauthenticated users

## Static File Organization
- Structured static files with separate directories for CSS and JavaScript
- Tool-specific stylesheets and scripts for modular development
- Shared styling variables using CSS custom properties
- Interactive JavaScript for real-time calculations and unit conversions

## Template Structure
- Base templates for consistent layout across the application
- Tool-specific templates with shared styling patterns
- Authentication templates for login and registration
- Conditional navigation based on user authentication status

# External Dependencies

## Core Framework
- **Django 5.1**: Primary web framework for backend development
- **Python 3.x**: Runtime environment

## Frontend Libraries
- **System Fonts**: Using system-ui and -apple-system for native look
- **CSS Grid/Flexbox**: For responsive layouts
- **Vanilla JavaScript**: For client-side interactivity and calculations

## Third-party Services
- **ExchangeRate-API**: External API for real-time currency conversion rates
- **Email Backend**: Django's email system for user communications (configured in settings)

## Development Tools
- **VS Code Extensions**: BlackBox AI extension recommended for development
- **Static Files**: Django's static file handling for CSS, JavaScript, and images

## Database
- **SQLite**: Default Django database for development (configured via Django settings)
- **Django ORM**: Database abstraction layer
- **User Model**: Django's built-in User model for authentication

The application is designed to be easily deployable with Django's standard deployment practices and can be extended with additional tools following the established patterns.