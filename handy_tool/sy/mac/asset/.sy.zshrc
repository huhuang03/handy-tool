alias jump="export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890"
alias unjump="unset http_proxy;unset http_proxys"
alias y=yarn
autoload -Uz compinit && compinit

alias ii=open

parse_git_branch() {
    git branch 2> /dev/null | sed -n -e 's/^\* \(.*\)/[\1]/p'
}

if [ -n "${ZSH}" ]; then
    setopt PROMPT_SUBST
    # https://apple.stackexchange.com/questions/397027/how-to-change-my-command-prompt-to-show-current-working-directory
    export PROMPT='%1~ ${COLOR_GIT}$(parse_git_branch)${COLOR_DEF} %# '
fi

alias ec=emacsclient
alias xcode="open -a /Applications/Xcode.app"