#!/bin/bash
cd
source ~/.bash_profile
rm -rf /Users/$USER/red-alert
git clone git@git.app.gittigidiyor.net:qa/red-alert.git
python3 /Users/$USER/red-alert/e2e_test_alerts.py
python3 /Users/$USER/red-alert/gitlab_merge_requests_alerts.py
