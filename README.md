# RevitShell demo library

A small library of Revit apps to try the **Library** tab of the RevitShell Manager panel.

## Add it in RevitShell

Manager panel › **Library** tab › **Add library…** › `hbadi/revitshell-library-demo`.

## Layout

```
revitshell-library.toml    marks the repository as a RevitShell library
apps/                      each app: a .app.toml manifest and its plain Python files
batches/                   *.batch.toml, apps chained by id
```

Each app is described by a manifest, `<name>.app.toml`: its id, version, name, the script
it runs (`entry`) and the files that script reads (`[[file]]`: helper modules, .csv, .xaml),
which RevitShell installs with the app. The scripts themselves are plain Python.

## Channels

| Channel | Branch   | Who follows it        |
|---------|----------|-----------------------|
| stable  | `stable` | everyone (default)    |
| beta    | `main`   | authors and testers   |

A user never runs code straight from GitHub: RevitShell installs a fixed version of each
app in a local cache and keeps the previous one for rollback.

The apps only read the model. They are samples: review any app before you run it.
