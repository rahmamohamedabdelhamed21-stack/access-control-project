# Vulnerable Web Application - Access Control

## Description
This project is a simple Flask web application created to demonstrate Access Control vulnerabilities.

## Vulnerabilities
- IDOR (Insecure Direct Object Reference)
- Missing Authorization

## How to Test
1. Open the home page.
2. Login as "rahma".
3. Open /profile/1.
4. Change the URL to /profile/2.
5. Open /admin.

## Expected Result
The application intentionally allows unauthorized access for educational purposes.