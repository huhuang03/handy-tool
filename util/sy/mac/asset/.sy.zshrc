alias c="export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890"
alias uc="unset http_proxy;unset http_proxys"
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

eval "$(jump shell)"

alias ii=open

# Enable substitution in the prompt.
# setopt prompt_subst

# https://medium.com/pareture/simplest-zsh-prompt-configs-for-git-branch-name-3d01602a6f33
# prompt='%1~ ${COLOR_GIT}$(git_branch_name)${COLOR_DEF} %# '
