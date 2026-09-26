# RevitShell demo library

A small library of Revit apps to try the **Library** tab of the RevitShell Manager panel.

## Add it in RevitShell

Manager panel › **Library** tab › **Add library…** › `hbadi/revitshell-library-demo`.

## Layout

```
revitshell-library.toml    marks the repository as a RevitShell library
apps/                      one .py per app, or a folder with app.toml
batches/                   *.batch.toml, apps chained by id
```

Each app declares its identity in a `# /// revitshell` header (`id`, `version`, `name`…).
Files an app reads next to itself (helper modules, .csv, .xaml) are listed in `files`,
so RevitShell installs them with the app.

## Channels

| Channel | Branch   | Who follows it        |
|---------|----------|-----------------------|
| stable  | `stable` | everyone (default)    |
| beta    | `main`   | authors and testers   |

A user never runs code straight from GitHub: RevitShell installs a fixed version of each
app in a local cache and keeps the previous one for rollback.

The apps only read the model. They are samples: review any app before you run it.
