# Test Cases - IndiaFirst Life Plan

## 1. Basic Details Page
| ID | Title | Description | Expected Result |
|----|-------|-------------|-----------------|
| TC_01 | UI Load | Verify page elements load correctly. | All input fields and CTA visible. |
| TC_02 | Form Validation | Submit with empty fields. | Error messages displayed. |
| TC_03 | Valid Flow | Enter valid data and click Continue. | Redirects to Plan Options page. |
| TC_04 | Invalid Email | Enter 'user@invalid'. | 'Enter a valid email' warning appears. |
| TC_05 | Mobile Length | Enter 5 digits in Mobile field. | Validation error for 10-digit requirement. |

## 2. Product Features
| ID | Title | Description | Expected Result |
|----|-------|-------------|-----------------|
| TC_06 | Brochure Link | Click the Brochure download icon. | PDF opens in a new tab. |
| TC_07 | Gender Toggle | Switch between Male/Female/Other. | Selection updates correctly. |
