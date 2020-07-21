#Check http://crc.nd.edu/wiki for login problems
#Contact crcsupport@nd.edu if further problems

if [ -r /opt/crc/Modules/current/init/bash ]; then
        source /opt/crc/Modules/current/init/bash
fi

#Additional aliases
#alias geckodriver=$HOME/geckodriver

alias ls='ls --color=auto'
alias grep='grep --color=auto'

#Additional modules

# prettify the console prompt
#PS1='${debian_chroot:+($debian_chroot)}\[\033[01;35m\][\u\033[01;31m\]@\033[01;35m\]\h]\[\033[00m\]: \[\033[01;34m\]\w\[\033[00m\]\033[01;32m\] $git_branch\033[01;35m\]$git_dirty\n\$\[\033[00m\] '

PS1='${debian_chroot:+($debian_chroot)}\[\033[01;33m\]{\u\033[01;35m\]@\033[01;33m\]\h}\[\033[00m\]: \[\033[01;34m\]\w\[\033[00m\]\033[01;32m\] $git_branch\033[01;35m\]$git_dirty\n\$\[\033[00m\] '

# To help the remote system being sshed into determine its color. 
# Note that there are other ways to do this, specifically by passing it via ssh
export TERM="xterm-256color"

module add conda
. /opt/crc/c/conda/miniconda2/4.5.4/etc/profile.d/conda.sh
