# Configuring GitHub Copilot for Visual Studio Code

<a name="settings"></a>
# Settings for the Extension

To configure GitHub Copilot's basic settings, open a [Visual Studio Code settings](https://code.visualstudio.com/docs/getstarted/settings) tab, 
and navigate to the GitHub Copilot extension section. You can set the following settings in the dialog:

* **Inline Suggestions : Enable** (`github.copilot.inlineSuggest.enable`)<br />
  Turns inline suggestions on or off.

* **Languages** (`github.copilot.enable`)<br />
  Configure the languages that are enabled for GitHub Copilot.
  This string is of the form<br /> 
  `{ "python": true, "markdown": false, ...}`.

<a name="shortcuts"></a>
## Keyboard shortcuts

These are the most common VS Code keyboard shortcuts relevant for GitHub
Copilot.
If you wish to rebind the shortcuts, use the Keyboard Shortcuts editor and
search for the command name below, or directly configure the shortcuts in your `keybindings.json` file. For more information, see [Key Bindings for Visual Studio Code](https://code.visualstudio.com/docs/getstarted/keybindings) in the VS Code documentation.

* Accept an inline suggestion: `Tab`.
   `editor.action.inlineSuggest.commit`

* Dismiss an inline suggestion: `Esc`.
   `editor.action.inlineSuggest.hide`

* Show next inline suggestion: `Alt + ]` or `Option + ]`.
   `editor.action.inlineSuggest.showNext`

* Show previous inline suggestion: `Alt + [` or `Option + [`.
   `editor.action.inlineSuggest.showPrevious`

* Trigger inline suggestion: `Alt + \` or `Option + \`.
   `editor.action.inlineSuggest.trigger`

* Open Copilot (10 suggestions in separate pane): `Ctrl + Enter`.
   `github.copilot.generate`

* Copilot toggle on/off: _No default shortcut_.
   `github.copilot.toggleCopilot`
   
<a name="more"></a>
## Learn More

To learn more about GitHub Copilot, go to the [documentation table of
contents](README.md).

