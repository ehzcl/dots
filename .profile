export PATH="$PATH:$(du "$HOME/.local/bin/" | cut -f2 | tr '\n' ':' | sed 's/:*$//')"


# Default programs
export EDITOR="nvim"
#export TERMINAL="kitty"
export TERMINAL="st"
export BROWSER="firefox"
export READER="zathura"
export STATUSBAR="i3blocks"
export I3BSCRIPTS="$HOME/.config/i3blocks/python"

# directory path
export GIT="$HOME/git"
# ~/ clean-up
export WGETRC="$HOME/.config/wget/wgetrc"



# start graphical server on tty1 if not already running
[ "$(tty)" = "/dev/tty1" ] && ! pgrep -x Xorg >/dev/null && exec startx

# switch escape and caps if tty and no passwd required
