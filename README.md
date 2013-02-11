DashedComments for Sublime Text 2
=================================

This plugin inserts the comments block just before the current line with the same length by striping whitespaces. This is mainly used for ruby programmers.

## Requirement
  - RubyFormat plugin to format your ruby code after inserting the comment block since it will strip the blank spaces which may have introduced by the indentation settings.


## Installation

### Package Control

Using [Package Control](http://wbond.net/sublime_packages/package_control), a package manager for Sublime Text 2.

In Sublime Text 2, press "win(cmd) + shift + p" and then type "install".

Once you see "Package Control: Install Package", enter.

When the packages load, another selection window will appear. 

Type DashedComments and enter. All done!

### Manual Installation
Open a terminal. change the path to Sublime Text 2 's packages folder.
Then type the command like this:
```bash
  cd "~/Library/Application Support/Sublime Text 2/Packages/"
  git clone git://github.com/email2vimalraj/DashedComments.git
```

Example:
-------
```ruby
#--------------------
# This is the comment
def comment_code
  
  #-----------------------------
  add_comment_block_on_top_of_me 
end
```

## Useful

### Key Binding
```
ctrl + alt + d on Windows
ctrl + alt + d on Linux
shift + cmd + d on Mac OS X
```

## TODO List
- Try to avoid the RubyFormat
