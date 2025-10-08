# TMS
Calculadora
 A visual investment projection page was added: `investment-stages-60-months.html` — a standalone HTML file showing a 60-month (5-year) projection broken into four phases. Open it in a browser to view.
Vercel deployment tips
----------------------

- This project is a single-file static app: `investment-stages-60-months.html`.
- If you deploy the repo root to Vercel and get a 404 at `/`, add a redirect or route so `/` serves the HTML. This repo includes `index.html` (redirect) and `vercel.json` with a route to the HTML.
- After pushing to your Git remote, Vercel will pick up the repo. If you still see a 404, check the Vercel build logs and ensure static files are included (no `build` step required for pure static sites).

