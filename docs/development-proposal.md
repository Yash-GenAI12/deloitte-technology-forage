# Daikibo Machine Health Dashboard Proposal

## Overview

We propose a private dashboard displaying the health of 36 machines across Daikibo's four factories. A single browser page will help authorised employees identify equipment that needs attention and inspect its status history.

Access will be limited to the client's intranet. Employees will use their existing company accounts through the internal authentication server. The application will read telemetry that Daikibo already collects and present it consistently.

The indicative delivery estimate is 120 person-hours over three working weeks. It includes development, testing, intranet integration, deployment instructions and a short user guide.

## Scope

**Factory and device views.** The page will list four factories with nine machines each. Factory groups can expand or collapse; expanding a device reveals its timestamped history. Current status, device identity and last-update time will be shown clearly, with text labels alongside icons.

**History.** The hierarchy runs from factory to device to status history. For example, expanding a factory and its CNC device will reveal Healthy and Unhealthy entries with timestamps. Load More will retrieve older records without leaving the page.

**Data and access.** The dashboard will refresh through the existing telemetry interface at an agreed interval. Failed requests, stale readings and missing data will be labelled explicitly. Factory summaries will flag unhealthy machines. The page and its data endpoints will require valid company sessions and intranet access.

**Delivery boundaries.** The release includes application configuration, deployment notes, user guidance and rollback instructions. Machine control, new sensors, public access and new alerting or predictive analytics are excluded.

<!-- pagebreak -->

## Estimate

The total indicative effort is **120 person-hours**, equivalent to 15 working days at eight hours per day for one developer. The estimate covers engineering effort through handover, with timely client IT and operations input.

- **Development - 72 hours:** requirements and interface design 12; factory/device views 28; current-status mapping and refresh 16; history and Load More 16.
- **Testing - 24 hours:** data and history accuracy 8; navigation and browser behaviour 8; access controls, session expiry, stale data and errors 8.
- **Integration and deployment - 24 hours:** authentication integration 8; telemetry and intranet configuration 8; production release 4; documentation and handover 4.

Ongoing support is agreed separately. Undocumented interfaces, new history storage or changes in scope require a revised estimate.

## Timeline

The schedule begins after approval and provision of system access. Each week contains 40 person-hours; milestones are relative to kickoff.

**Week 1 - Confirm design and establish access.** Agree data contracts, status rules, refresh interval and history period. Obtain test accounts, demonstrate company sign-in and build the factory/device structure. Milestone: approved design and working dashboard skeleton. Allocation: 32 development hours and 8 integration hours.

**Week 2 - Complete the dashboard.** Implement current-status refresh, history, Load More and error states. Verify mapping and navigation with representative records from all four factories. Milestone: a feature-complete version for client review. Allocation: 32 development hours and 8 testing hours.

**Week 3 - Validate and release.** Complete security and acceptance checks, resolve defects, configure production access, deploy and hand over. Milestone: client acceptance and production release. Allocation: 8 development hours, 16 testing hours and 16 integration hours.

<!-- pagebreak -->

## Support

We propose continuous product support through an agreed maintenance arrangement. Employees will raise tickets through the designated service desk, recording the affected factory or device and issue time. Tickets will be prioritised by operational impact and tracked through resolution.

A proposed two-week stabilisation period after launch will focus on defects, data mismatches and access issues. Subsequent maintenance will address bug fixes, compatibility updates and coordination with telemetry and authentication teams. Support coverage, response targets and fees will be agreed before go-live.

Requests for new functionality will be logged, assessed and estimated for approval. Changes will be tested separately before release through the agreed deployment process.

## Assumptions

- Documented telemetry and historical records are accessible through an agreed interface.
- The internal authentication server supports application integration, with test accounts available.
- Intranet hosting, TLS certificates and deployment access are ready.
- Client representatives confirm status definitions, refresh interval, history period and acceptance criteria before implementation.
- Changes to those dependencies may affect the estimate and delivery dates.

## Acceptance criteria

The client will verify that all four factories and 36 machines appear in the correct groups; factory and device controls expand independently; current states and timestamped history match their sources; and errors or stale readings are clear.

Company sign-in, session expiry and rejection of unauthorised or external access must pass testing. Client acceptance, deployment documentation and rollback readiness are required before production approval.
