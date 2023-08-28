alias jump="export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890"
alias unjump="unset http_proxy;unset http_proxys"
alias y=yarn
autoload -Uz compinit && compinit

COLOR_DEF=$'\e[0m'
COLOR_USR=$'\e[38;5;243m'
COLOR_DIR=$'\e[38;5;197m'
COLOR_GIT=$'\e[38;5;39m'

function git_branch_name()
{
  branch=$(git symbolic-ref HEAD 2> /dev/null | awk 'BEGIN{FS="/"} {print $NF}')
  if [[ $branch == "" ]];
  then
    :
  else
    echo $branch
  fi
}

alias ii=open


parse_git_branch() {
    git branch 2> /dev/null | sed -n -e 's/^\* \(.*\)/[\1]/p'
}
COLOR_DEF='%f'
COLOR_USR='%F{243}'
COLOR_DIR='%F{197}'
COLOR_GIT='%F{39}'
NEWLINE=$'\n'
setopt PROMPT_SUBST

# https://apple.stackexchange.com/questions/397027/how-to-change-my-command-prompt-to-show-current-working-directory
export PROMPT='%1~ ${COLOR_GIT}$(parse_git_branch)${COLOR_DEF} %# '

alias ec=emacsclient
alias xcode="open -a /Applications/Xcode.app"