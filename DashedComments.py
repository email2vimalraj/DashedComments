#========================================================================================
# Version        : 1.0
# Author         : Vimal Raj
# Description    : This plugin inserts the comment block just before with the same length  
#                  of the current line (like: #-------------)
# Pre-requisites : RubyFormat plugin is required to format the code
#========================================================================================
import sublime, sublime_plugin

class DashedCommentsCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      for region in self.view.sel():
         if region.empty():
            line = self.view.line(region)
            line_contents = str(self.view.substr(line)).strip()
            length = len(line_contents)
            new_comment_chars = "#"
            i = 1
            for char in line_contents:
               if length != i:
                  new_comment_chars = new_comment_chars + "-"
               i = i + 1
            new_comment_chars += "\n"
            self.view.insert(edit, line.begin(), new_comment_chars)
