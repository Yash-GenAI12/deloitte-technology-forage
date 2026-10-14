# GitHub upload guide

Yeh guide project ki ek nayi local copy ko GitHub par publish karne ke liye hai. Existing clone par sirf later updates wala section use karein.

## 1 Create an empty public repository

[GitHub New Repository](https://github.com/new) par:

- Repository name: `deloitte-technology-forage`
- Description: `Python telemetry conversion and software development proposal from the Deloitte Australia Technology Job Simulation on Forage.`
- Visibility: **Public**
- README, .gitignore aur license options ko initialize **mat** karein; files local folder mein already hain.
- Create repository click karke HTTPS URL copy karein.

Yeh GitHub ke [official existing-project workflow](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github) ke mutabik hai.

## 2 Open the prepared project directory

PowerShell mein:

```powershell
Set-Location -LiteralPath 'C:\Projects\deloitte-technology-forage'
```

Command Prompt mein is alternative ko use karein:

```bat
cd /d "C:\Projects\deloitte-technology-forage"
```

Agar ZIP kisi doosre folder mein extract kiya hai, us folder ka path use karein. Aage ke Git commands PowerShell aur Command Prompt dono mein same hain. Commands ko order mein chalayein; koi command fail ho to pehle us error ko resolve karein.

## 3 Run the tests and initialize Git

```bash
python main.py
git init -b main
```

Commit identity ke liye neeche ke do values replace karein. GitHub Settings > Emails se apna exact GitHub-provided noreply address copy kar sakte hain; example ko actual email samajh kar use na karein. Yeh configuration sirf is repository par apply hoti hai.

```bash
git config user.name "YOUR_NAME"
git config user.email "YOUR_GITHUB_NOREPLY_EMAIL"
```

## 4 Check files and make the first commit

```bash
git status --short --ignored
git add .
git diff --cached --name-only
git diff --cached --stat
git diff --cached --check
```

Staged list mein `private_reference/`, `.env`, certificates, screenshots ya credentials nahi hone chahiye. `.gitignore` common filename patterns ko exclude karta hai; arbitrary files ke andar credentials detect nahi karta. Review complete hone par:

```bash
git commit -m "Add telemetry conversion and development proposal"
```

## 5 Connect and push

`YOUR_GITHUB_USERNAME` ko apne GitHub username se replace karein. Repository name wahi rakhein jo step 1 mein banaya tha.

```bash
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/deloitte-technology-forage.git
git remote -v
git push -u origin main
```

Sign-in prompt aaye to Git credential manager/browser login complete karein. HTTPS Git operations ke liye normal GitHub account password supported nahi hai; credential manager ya personal access token use hota hai. Token ko remote URL ya tracked file mein paste na karein. [GitHub authentication documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)

## 6 Verify the upload

```bash
git status
git log -1 --oneline
git ls-remote --heads origin main
```

GitHub repository refresh karke README, Python files, demo data aur proposal check karein. `private_reference/` publish nahi hona chahiye.

## Later updates

```bash
python main.py
git add .
git diff --cached --stat
git commit -m "Describe your update"
git push
```

## Common fixes

- **python not found:** Windows par `py -3 main.py` try karein, ya Python install karke terminal dobara kholein.
- **Author identity unknown:** step 3 ke repository-local name/email commands complete karein.
- **remote origin already exists:** `git remote -v` inspect karein. Agar URL galat hai, `git remote set-url origin https://github.com/YOUR_GITHUB_USERNAME/deloitte-technology-forage.git` se correct karein.
- **Repository not found:** URL, repository spelling, sign-in account aur access check karein.
- **Push rejected because the remote has commits:** repository shayad README/license ke saath initialize hui hai. Force push na karein; remote changes ko review aur integrate karein, ya ek nayi empty repository use karein.

Public file set mein independently authored demo fixtures aur an unbranded portfolio proposal hain. Original simulation resources sirf local ignored reference folder mein rakhe gaye hain.
