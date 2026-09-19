# GitHub Pages Deployment Instructions

## Automatic Deployment Setup

Your project is now ready for GitHub Pages! Follow these steps to enable it:

### Step 1: Go to Repository Settings
1. Visit your repository: https://github.com/varungupta132/ML_hackathon
2. Click on **Settings** (top navigation bar)

### Step 2: Enable GitHub Pages
1. Scroll down to **Pages** in the left sidebar (under "Code and automation")
2. Under **Source**, select **Deploy from a branch**
3. Under **Branch**, select **main** and **/ (root)**
4. Click **Save**

### Step 3: Wait for Deployment
- GitHub will automatically deploy your site
- It usually takes 1-2 minutes
- You'll see a green checkmark when ready

### Step 4: Access Your Site
Your site will be live at:
**https://varungupta132.github.io/ML_hackathon/**

---

## What Gets Deployed?

The `index.html` file in your repository root serves as the landing page for your GitHub Pages site. It showcases:
- Project overview
- Key features
- Technology stack
- Installation instructions
- Links to the GitHub repository

---

## Note About Streamlit App

⚠️ **Important**: GitHub Pages only hosts static HTML/CSS/JS files. The Streamlit application (`app.py`) cannot run directly on GitHub Pages.

### To Run the Streamlit App:

Users need to run it locally by:

1. Cloning the repository
```bash
git clone https://github.com/varungupta132/ML_hackathon.git
cd ML_hackathon
```

2. Installing dependencies
```bash
pip install -r requirements.txt
```

3. Running the app
```bash
streamlit run app.py
```

---

## Alternative Deployment Options for Streamlit

If you want to deploy the live Streamlit app (not just documentation), consider these platforms:

1. **Streamlit Community Cloud** (Free)
   - Visit: https://streamlit.io/cloud
   - Connect your GitHub repository
   - Deploy with one click
   - Best option for Streamlit apps!

2. **Heroku** (Has free tier)
   - Requires Procfile and setup.sh
   - Good for production apps

3. **Render** (Free tier available)
   - Easy deployment
   - Auto-deploys on git push

4. **Hugging Face Spaces** (Free)
   - Great for ML projects
   - Easy integration

---

## Current Setup

✅ **GitHub Pages**: Landing page with documentation (index.html)
✅ **Source Code**: Full Streamlit application available in repository
✅ **Instructions**: Clear setup guide for local usage

For the best experience, use GitHub Pages as your project showcase and documentation, while directing users to run the Streamlit app locally or deploy to Streamlit Community Cloud.

---

**Your project is now ready! 🚀**
