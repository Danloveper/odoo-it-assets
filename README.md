# Odoo IT Assets Module

## Overview

The **IT Assets** module is a custom Odoo addon designed to manage and request technological assets within a company. It provides an internal form for employees to submit asset requests and integrates with the Odoo website for external submissions. The module includes workflow management for approval processes and generates dynamic reports for tracking requests.

This module is built for Odoo 18 and extends the base functionality to handle IT asset requests efficiently.

## Features

- **Asset Request Management**: Create and manage requests for various IT assets including laptops, monitors, keyboards, mice, and software licenses.
- **Workflow States**: Track requests through draft, submitted, approved, and rejected states.
- **Priority Levels**: Assign priorities (No Priority, Low, Medium, High) to requests.
- **Employee Integration**: Capture employee details and email for request tracking.
- **Cost Estimation**: Include estimated costs with validation to prevent negative values.
- **Approval Process**: Buttons for submitting, approving, and rejecting requests.
- **Website Integration**: Public forms for asset requests via the Odoo website.
- **Dynamic Reports**: Generate printable reports for asset requests.
- **Security**: Role-based access control for managing requests.
- **Sequence Numbering**: Automatic numbering for requests using Odoo sequences.

## Installation

### Prerequisites

- Odoo 18 installed and running.
- Access to the Odoo addons directory.
- Python dependencies as per Odoo's requirements.

### Steps

1. **Clone or Download the Module**:
   Place the `it_asset_request` folder in your Odoo addons directory (e.g., `/path/to/odoo/addons/`).

2. **Update Addons Path**:
   Ensure your Odoo configuration includes the path to this module. For example, in `odoo.conf`:
   ```
   addons_path = /path/to/odoo/addons,/path/to/odoo-it-assets
   ```

3. **Install the Module**:
   - Log in to Odoo as an administrator.
   - Go to **Apps** > **Update Apps List**.
   - Search for "IT Assets" and install the module.

4. **Database Update**:
   If updating an existing installation, run:
   ```
   odoo-bin --update=it_asset_request
   ```

## Configuration

### Security Groups

The module includes access controls defined in `security/ir.model.access.csv`. Ensure users have appropriate permissions:

- **IT Asset Request User**: Can create and view requests.
- **IT Asset Request Manager**: Can approve/reject requests.

### Sequences

A sequence for request numbering is defined in `data/sequence.xml`. It generates codes like `AR/00001`.

### Website Integration

The module provides website templates in `views/website_templates.xml` for public asset request forms. Publish the page via Odoo's website builder.

## Usage

### Creating a Request (Internal)

1. Navigate to **IT Assets > Asset Requests**.
2. Click **Create**.
3. Fill in details: Employee Name, Email, Asset Type, Justification, Priority, Estimated Cost.
4. Save as Draft or click **Send** to submit.

### Approval Workflow

- **Submitted**: Request is pending approval.
- **Approved/Rejected**: Managers can change the state via buttons.

### Website Submission

- Access the public form (configure URL in website settings).
- Fill and submit the form.

### Reports

- Generate reports from the request form or list view.

## Development

### Module Structure

```
it_asset_request/
├── __manifest__.py          # Module manifest
├── models/
│   └── asset_request.py     # Main model
├── views/
│   ├── asset_request_views.xml # Form, list search 
|   |                           #views
│   ├── asset_request_menus.xml    # Menu definitions
│   └── website_templates.xml   # Website integration
├── report/
│   └── asset_request_report.xml   # Report templates
├── security/
│   └── ir.model.access.csv        # Access rights
├── data/
│   └── sequence.xml           # Sequence definitions
└── demo/                       # Demo data (if any)
```

### Key Components

- **Model**: `it.asset.request` with fields for request details and computed display name.
- **Views**: Tree, form, and search views for backend management.
- **Reports**: QWeb reports for printing requests.
- **Website**: Public forms using Odoo's website framework.

### Extending the Module

- Add new asset types by modifying the `asset_type` selection in `asset_request.py`.
- Customize workflows by adding new states or transitions.
- Integrate with other modules (e.g., HR, Inventory) by adding dependencies.

### Testing

- Use Odoo's test framework for unit tests.
- Ensure constraints (e.g., positive cost) are validated.

## Dependencies

- **Odoo Base**: Core functionality.
- No external Python libraries required beyond Odoo's standard dependencies.

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make changes and test thoroughly.
4. Submit a pull request with a clear description.

Follow Odoo's coding standards and ensure compatibility with Odoo 18.

## License

This module is licensed under LGPL-3. See the LICENSE file for details.

## Author

**William Daniel Vargas Acevedo**

For support or questions, contact via the provided website or email.

## Changelog

- **v0.1**: Initial release with basic asset request functionality.
