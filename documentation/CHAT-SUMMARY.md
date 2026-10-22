# Stock Due Diligence Plugin — Chat Summary

Date: 2026-10-22

## User requests covered

1. Help create a ChatGPT plugin using Plugin Creator.
2. Work on a private stock due diligence plugin and keep its versioned source backed up in GitHub.
3. Use the GitHub repository `ezhilrean/stock-due-diligence` to preserve plugin source and version information.
4. Create branches named for versions `v0.1.1` through `v0.1.5`.
5. Publish the supplied ZIP files as GitHub Releases, with each release using the matching version tag and ZIP asset.
6. Investigate why GitHub showed “No releases published.”
7. Provide a repeatable guide for creating and publishing GitHub releases.
8. Create documentation in the repository and commit/publish it.
9. Turn the workflow into reusable instructions for future projects.

## Project facts recorded during the chat

- Plugin name: `stock-due-diligence`
- Plugin ID: `plugins_6ada26384798819191722437eddeb00b`
- Plugin URL: https://chatgpt.com/plugins/plugins_6ada26384798819191722437eddeb00b
- Scope: private/user
- Published plugin version: `0.1.5`
- Latest plugin release ID: `pluginrel_6ada27ba2dd88191a7683c23c6c15dc7`
- GitHub repository: https://github.com/ezhilrean/stock-due-diligence
- Source commit for the current v0.1.5 snapshot: https://github.com/ezhilrean/stock-due-diligence/commit/814ff9401f5902ea5bf5bb0be423c51b79f9073a
- The current source tree includes plugin manifests, the skill, and reference documents including checklist, definition of done, deliverable template, playbook, and research standards.
- Branches `v0.1.1`, `v0.1.2`, `v0.1.3`, `v0.1.4`, and `v0.1.5` were created. At the time of the discussion, these branches were all based on the same current source snapshot, not verified historical snapshots of each ZIP.
- The GitHub Releases API returned an empty list during the check, so no GitHub Releases had been published at that point.

## Important distinction

A plugin version published in ChatGPT, a Git branch, a Git tag, a GitHub Release, and a downloadable ZIP asset are different things:

- A **plugin version** is managed by the plugin platform.
- A **branch** is a movable pointer to a line of Git development.
- A **tag** identifies a specific Git commit.
- A **GitHub Release** is a published release record, normally associated with a tag.
- A **ZIP asset** is the downloadable archive attached to a release.

Creating a branch does not publish a GitHub Release. A release is complete only after the correct tag and release record exist and the intended archive is attached.

## Outstanding validation

Before publishing each historical version, verify that the matching branch or tag points to the exact source represented by that version's ZIP. Do not assume all versions are identical. After publishing, open the Releases page and confirm the release and asset are visible.

Releases page: https://github.com/ezhilrean/stock-due-diligence/releases