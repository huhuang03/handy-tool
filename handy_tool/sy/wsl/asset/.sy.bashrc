alias git=git.exe
export WSL_HOST_IP=$(ip route | grep default | awk '{print $3}')
alias jump="export https_proxy=http://$WSL_HOST_IP:7890 http_proxy=http://$WSL_HOST_IP:7890 all_proxy=http://$WSL_HOST_IP:7890"
alias unjump="unset http_proxy;unset http_proxys"
alias y=yarn