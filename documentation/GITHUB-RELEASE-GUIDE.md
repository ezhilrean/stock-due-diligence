# GitHub Release Guide for Versioned Plugin ZIPs

This guide explains how to create a GitHub Release and attach the matching plugin ZIP archive.

Repository example: https://github.com/ezhilrean/stock-due-diligence

## Before you start

For each version, have:
- The exact ZIP archive for that version.
- A Git branch or commit containing that version's source.
- A version tag, using the `v` prefix (for example, `v0.1.1`).
- A release title and concise release notes.

Do not publish a historical release from a branch that contains the wrong source snapshot. If all version branches point to the same commit, correct the branches or select the appropriate commit before tagging.

## Create a release in the GitHub website

1. Open the repository.
2. Select **Releases**. You can also open https://github.com/ezhilrean/stock-due-diligence/releases.
3. Click **Draft a new release** or **Create a new release**.
4. In **Choose a tag**, select the existing tag for the version. If it does not exist, type the version tag and choose GitHub's option to create it.
5. Set **Target** to the branch or commit that contains the correct version's source.
6. Enter a release title, such as `Stock Due Diligence v0.1.1`.
7. Write release notes describing the version's contents and changes.
8. In the attachment area, upload the exact matching ZIP archive, for example `stock-due-diligence-chatgpt-plugin-v0.1.1.zip`.
9. Review the tag, target, title, notes, and asset filename.
10. Click **Publish release**.
11. Return to the Releases page and verify that the release appears and the ZIP can be downloaded.

## Suggested version mapping

| Version | Tag | Release title | ZIP asset |
|---|---|---|---|
| 0.1.1 | `v0.1.1` | Stock Due Diligence v0.1.1 | `stock-due-diligence-chatgpt-plugin-v0.1.1.zip` |
| 0.1.2 | `v0.1.2` | Stock Due Diligence v0.1.2 | `stock-due-diligence-chatgpt-plugin-v0.1.2.zip` |
| 0.1.3 | `v0.1.3` | Stock Due Diligence v0.1.3 | `stock-due-diligence-chatgpt-plugin-v0.1.3.zip` |
| 0.1.4 | `v0.1.4` | Stock Due Diligence v0.1.4 | `stock-due-diligence-chatgpt-plugin-v0.1.4.zip` |
| 0.1.5 | `v0.1.5` | Stock Due Diligence v0.1.5 | `stock-due-diligence-chatgpt-plugin-v0.1.5.zip` |

Use these names only if they match the actual supplied archive filenames. Never rename or substitute an archive in a way that misrepresents its contents.

## Example release notes

For an initial release:

```markdown
## Stock Due Diligence v0.1.1

Initial version of the Stock Due Diligence plugin.

Includes the stock due diligence skill and supporting research guidance, checklist, definition of done, and deliverable template.

**Asset:** `stock-due-diligence-chatgpt-plugin-v0.1.1.zip`
```

For later versions, replace the description with the actual changes included in that version. Do not claim features or fixes without checking the source or changelog.

## Troubleshooting

### GitHub says “No releases published”
No GitHub Releases have been published yet, or the current account cannot see them. Branches and tags alone do not count as releases. Drafts are not published releases either.

### The tag dropdown does not show the version
Type the intended tag name and use GitHub's create-tag option if offered. Ensure the target commit is correct before publishing.

### The release exists but no ZIP is downloadable
Edit the release and attach the matching ZIP file, then save/update the release.

### The wrong source was tagged
Do not quietly publish it as the intended historical version. Correct the tag/target or recreate the release using the right commit, following your repository's release policy.

## Release verification checklist

- [ ] Tag uses the expected version, such as `v0.1.5`.
- [ ] Tag points to the correct commit.
- [ ] Target branch/commit contains the intended source.
- [ ] Release title matches the version.
- [ ] Release notes describe actual changes.
- [ ] Correct version-specific ZIP is attached.
- [ ] Release is published, not merely saved as a draft.
- [ ] Release appears at the repository's Releases page.
- [ ] ZIP download works and its contents have been checked.

## Release page

https://github.com/ezhilrean/stock-due-diligence/releases