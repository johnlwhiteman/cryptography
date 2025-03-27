#!/usr/bin/env bash
export PDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

setup_os() {
    if command -v apt &> /dev/null; then
        sudo apt update
        sudo apt install python3-venv python3-pip -y
    elif command -v dnf &> /dev/null; then
        sudo dnf update
        sudo dnf install python3-venv python3-pip -y
    elif command -v yum &> /dev/null; then
        sudo yum update
        sudo yum install python3-venv python3-pip -y
    fi
}

# Don't do this if you don't want it
set_python3_as_default() {
    sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
}

setup_python() {
    if [ ! -d "${PDIR}/venv" ]; then
        python -m venv "${PDIR}/venv"
    fi
    source "${PDIR}/venv/bin/activate"
    pip install -r requirements.txt
}

setup_os
setup_python