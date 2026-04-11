# ProjectOS Activation Checklist

## Step 1. Inspect before scaffolding

Review only the minimum repository surface:

- root files and folders
- any existing README or project index
- main code root
- existing docs root, if present

## Step 2. Decide which layer fits

Choose Layer 1 only if most of these are true:

- the repository is new or still small
- the team does not need formal task continuity yet
- subagent coordination is not expected soon
- the goal is mainly to create a clean structure and entry point

Choose Layer 1 plus Layer 2 if most of these are true:

- the repository will grow over multiple sessions
- tasks will often span multiple files
- handoff or collaboration matters
- subagent coordination may be useful
- reporting consistency matters
- risk-sensitive work is likely

## Step 3. Ask the user to confirm one choice

Use this exact style:

`Do you want ProjectOS core structure only, or core structure plus operating rules?`

## Step 4. Apply only the confirmed scope

- If the user chooses Layer 1 only:
  - scaffold the core structure
  - stop after core docs are in place
- If the user chooses Layer 1 plus Layer 2:
  - scaffold the core structure
  - add the operating rule pack and wire it into the docs
