# FitYou 1.1 — Vercel export

## Deploy

1. Extract this ZIP. `index.html`, `vercel.json` and the `vendor` folder must be together at your repository root (or the Root Directory selected in Vercel).
2. Upload all extracted files and folders to your Git repository. Do not upload only the ZIP or only README.md.
3. Import/deploy that repository on Vercel. Use the Other framework preset, no build command, and `.` for Output Directory. The included vercel.json declares these settings.
4. Open the deployed HTTPS URL directly in Safari/Chrome. Reload after deployment. The status should say **Ready • FitYou 1.1**.
5. Tap Play guide to verify the buttons respond; tap Enable camera to request camera permission.

README.md is documentation and may be included safely. Do not replace index.html with the README content. Do not rename index.template.html to index.html: the template needs bundling first.

## What changed

The interface CSS and JavaScript are embedded in index.html, removing separate startup requests for style.css and app.js. The pose-tracking module/model remain in vendor and load only after requesting camera access. A startup error now appears if JavaScript fails to initialise. A model-loading failure preserves the camera preview, pauses live feedback and allows retry. This does not identify or guarantee a fix for your specific deployment without inspecting its URL.

## Source edits

Edit app.js, style.css or index.template.html, then run `python3 build.py` to regenerate index.html before redeploying. No build is needed for the bundled files as provided. Keep all vendor files and embedded license notices.

## Checks

Browser checks: Play guide changes to Pause guide; choosing Stationary lunge updates cues; Enable camera displays a response (HTTPS guidance on the HTTP test host). Simulated model-loading failure preserves preview and enables retry. JavaScript syntax passed. Physical iPad camera/pose inference has not been tested.

## Limitations

Video is processed locally without recording/upload. Feedback uses approximate 2D pose heuristics, not a complete assessment of exercise technique. No built-in sign-in or native app packaging. Hosting privacy must be configured separately. Google Fonts is optional; remove the first CSS @import and rebuild to avoid that request. The supplied source does not include a PWA manifest/service worker.
