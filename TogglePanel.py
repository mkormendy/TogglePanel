import sublime_plugin

class TogglePanelCommand(sublime_plugin.WindowCommand):
    def run(self, panel='output.exec'):
        ap = self.window.active_panel()
        if ap == panel:
            self.window.run_command("hide_panel", {"panel": panel})
            // if binding to "escape" key, the following commands will also
            // hide other panels (ie. find/replace, overlays etc.)
            self.window.run_command("hide_overlay")
            self.window.run_command("hide_panel", {"cancel": "true"})
            self.window.run_command("cancel")
        else:
            self.window.run_command("show_panel", {"panel": panel})
