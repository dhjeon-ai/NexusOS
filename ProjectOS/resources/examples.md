# ProjectOS Examples

## Example starter layout

```text
my-repo/
  src/
  tests/
  docs/
    00_Project_Index.md
    01_Architecture/
      Directory_Structure.md
      Data_Flows.md
    02_Components/
      API_Service.md
      Worker_Runtime.md
    03_Decisions_ADR/
      ADR-001_Runtime_Model.md
    04_Archive/
    Active_Tasks/
      Task_Initial_Runtime_Split.md
  project_work_status.md
```

## Example component page shape

```markdown
# API Service

- Source Path: `src/app/api.py`
- Role: Handles external requests and returns normalized responses.
- Related Components: [[Worker_Runtime]]

## Key Contracts
- Input: request payload
- Output: response payload

## Policies and Constraints
- Authentication is required.
- Responses must stay backward compatible.

## Known Risks
- Queue timeout under heavy load.
```

## Example task trigger

Create an active task page when:

- a new service is added
- a refactor crosses multiple modules
- a handoff will be needed later
