# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please **do not** open a public issue.

Instead, email security concerns to: **[your-email@example.com]**

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

We will respond within 48 hours and work with you to address the issue.

## Security Best Practices

This project follows security best practices:

- ✅ Automated dependency updates (Dependabot)
- ✅ GitHub Actions security scanning (zizmor)
- ✅ Regular dependency audits
- ✅ No secrets in code or configuration
- ✅ Minimal dependencies

## Security Scanning

Pre-commit hooks include:
- **zizmor**: Scans GitHub Actions workflows for security issues
- **dependency scanning**: Via Dependabot

CI/CD pipeline validates:
- All dependencies are from trusted sources
- No known vulnerabilities in dependencies
- Secure coding practices

## Thank You

We appreciate your help in keeping this project secure!
