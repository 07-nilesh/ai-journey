# 📚 Complete AI/ML Resource Library — Your Personal Learning Bible

> **How to use this:** Every resource here is handpicked for YOUR specific profile — student, Python beginner, startup-minded, based in India. Each one has a reason why it's right for you, exactly what to cover, in what order, and pro tips so you don't waste time.
> 
> **Golden Rule:** Finish one resource before starting the next in the same category. Resource-hopping is the #1 reason people stay beginners forever.

---

## 🗂️ Resource Index

| # | Category | Resources Count |
|---|----------|----------------|
| 1 | Python Programming | 6 resources |
| 2 | Math for ML | 5 resources |
| 3 | Classical Machine Learning | 6 resources |
| 4 | Deep Learning | 5 resources |
| 5 | LLMs & Transformers | 7 resources |
| 6 | AI Product Engineering | 6 resources |
| 7 | MLOps & Deployment | 4 resources |
| 8 | Startup & Product | 5 resources |
| 9 | YouTube Channels | 10 channels |
| 10 | Newsletters & Blogs | 8 sources |
| 11 | Practice Platforms | 6 platforms |
| 12 | Communities | 6 communities |
| 13 | Books | 8 books |
| 14 | Indian-Specific Resources | 5 resources |

---

## 🐍 SECTION 1 — Python Programming

---

### 📗 Resource 1.1 — CS50P: Introduction to Programming with Python (Harvard)

**Link:** cs50.harvard.edu/python
**Type:** Free video course
**Duration:** 6–8 weeks at 1 hour/day
**When to use:** Phase 1, Days 1–30
**Difficulty:** Beginner → Intermediate

**Why this is perfect for you:**
Harvard's CS50P is the gold standard free Python course. Unlike random YouTube tutorials that are shallow or inconsistent, this course is structured like a university curriculum but explained in plain English. The instructor David Malan has taught millions of people and has a gift for making things click. Since you already have core Java, you'll fly through the early weeks and slow down at the Python-specific features like generators, decorators, and libraries — exactly what you need.

**What to cover and in what order:**

| Week | Topic | Days to spend |
|------|-------|--------------|
| Week 0 | Functions, Variables | 1 day |
| Week 1 | Conditionals | 1 day |
| Week 2 | Loops | 1 day |
| Week 3 | Exceptions | 1 day |
| Week 4 | Libraries | 2 days |
| Week 5 | Unit Tests | 2 days |
| Week 6 | File I/O | 2 days |
| Week 7 | Regular Expressions | 2 days |
| Week 8 | OOP | 3 days |
| Week 9 | Et Cetera (decorators, generators) | 3 days |

**Pro Tips:**
- Do EVERY problem set. Don't skip them. The problem sets are where 80% of learning happens.
- After each week, close the lecture and rebuild the examples from memory in a new file.
- Use the CS50 Discord if you're stuck — it's very active.
- Since you know Java OOP already, Week 8 will feel familiar but Python's approach is more flexible — pay attention to the differences.
- Submit your problem sets on the CS50 platform to get the official certificate (free and looks good on LinkedIn).

**What to skip:** Nothing. This course is already lean and well-designed.

---

### 📗 Resource 1.2 — Automate the Boring Stuff with Python

**Link:** automatetheboringstuff.com (free online)
**Type:** Free online book
**Duration:** 3–4 weeks, read alongside CS50P
**When to use:** Phase 1, Days 15–60 (parallel reading)
**Difficulty:** Beginner → Intermediate

**Why this is perfect for you:**
This book teaches Python through real automation projects — web scraping, working with files, sending emails, manipulating PDFs, working with spreadsheets. Every chapter ends with a practical project you can show people. Since you want to build products, not just pass exams, this book trains your builder instinct from the very beginning. It's completely free online and updated regularly.

**What to cover and in what order:**

| Chapters | Topic | Priority |
|----------|-------|----------|
| 1–6 | Python basics | Skip or skim (you know this from Java) |
| 7 | Pattern matching with regex | Must do |
| 8–9 | File reading/writing | Must do |
| 10 | Organizing files | Must do |
| 11 | Debugging | Must do |
| 12–13 | Web scraping | Must do — highly practical |
| 14–15 | Excel and PDFs with Python | Must do |
| 16 | CSV and JSON | Must do |
| 17–18 | Scheduling and launching programs | Do if time allows |

**Pro Tips:**
- Don't just read — open a notebook and type every single code example. Muscle memory matters.
- After each chapter project, make it yours: change the topic, add a feature, make it solve a real problem you have.
- The web scraping chapters (12–13) are especially important for building AI data pipelines later.
- Pair this with the `requests` and `BeautifulSoup` documentation as you go.

---

### 📗 Resource 1.3 — Corey Schafer Python Tutorials (YouTube)

**Link:** youtube.com — search "Corey Schafer Python"
**Type:** Free YouTube playlist
**Duration:** Watch specific videos as needed — not all at once
**When to use:** Phase 1, Days 15–98 (reference videos, not linear)
**Difficulty:** Intermediate

**Why this is perfect for you:**
Corey Schafer is the best Python tutorial creator on YouTube, period. His videos are clean, no fluff, well-paced, and cover exactly the intermediate topics that trip up beginners — OOP, decorators, generators, context managers, virtual environments. Since you're a visual learner who participates in hackathons, his style of showing code running in real time will click for you. Use his videos as targeted deep-dives when you hit a topic you need more help on.

**Specific videos to watch (in this order):**

| Video Title | When to Watch |
|-------------|--------------|
| Python OOP Series (6 videos) | Phase 1, Week 3 |
| Decorators (2 videos) | Phase 1, Week 3 |
| Generators | Phase 1, Week 3 |
| Context Managers | Phase 1, Week 3 |
| Virtual Environments (pipenv/conda) | Phase 1, Week 6 |
| Unit Testing with unittest | Phase 1, Week 7 |
| File Objects | Phase 1, Week 2 |
| String Formatting | Phase 1, Week 1 |
| Comprehensions | Phase 1, Week 2 |

**Pro Tips:**
- Watch at 1.25x speed — his pace is slightly slow for someone with programming experience.
- Pause when he writes code and try to write it yourself before he shows the answer.
- Don't binge. Watch one video, code along, practice, then watch the next.

---

### 📗 Resource 1.4 — Real Python (realpython.com)

**Link:** realpython.com
**Type:** Article library (free + paid)
**Duration:** Ongoing reference — not a course to finish
**When to use:** All phases, whenever you need clarity on a Python topic
**Difficulty:** Beginner → Advanced

**Why this is perfect for you:**
Real Python is like Stack Overflow but with proper explanations. Every article is written by experts, peer-reviewed, and includes practical examples. When you learn something in a course and still feel fuzzy on it, Real Python almost always has the definitive explanation. The free articles are extensive — you won't need the paid tier until much later, if at all.

**Must-read articles (bookmark these):**

| Article | When to Read |
|---------|-------------|
| Python OOP (series) | Phase 1, Week 3 |
| Python Decorators | Phase 1, Week 3 |
| Python Type Checking Guide | Phase 1, Week 7 |
| Python Virtual Environments Primer | Phase 1, Week 6 |
| Async IO in Python | Phase 4, Weeks 43–46 |
| Python Concurrency | Phase 1, Week 8 |
| Python Data Classes | Phase 2 onwards |
| List/Dict/Set Comprehensions | Phase 1, Week 2 |

**Pro Tips:**
- Use the search bar with specific queries — "Python generators explained" gives better results than browsing.
- Read the "Further Reading" section at the end of every article — those links are gold.
- Don't try to read it cover to cover. Use it as a reference dictionary.

---

### 📗 Resource 1.5 — Python Documentation (docs.python.org)

**Link:** docs.python.org/3/
**Type:** Official documentation
**Duration:** Ongoing reference
**When to use:** All phases
**Difficulty:** Intermediate → Advanced

**Why this is perfect for you:**
Reading official docs is a skill that separates good engineers from great ones. Start building the habit now. Python's documentation is actually very well written and readable. Every professional AI engineer reads docs daily — the sooner you get comfortable with them, the faster you'll learn everything else.

**Where to start in the docs:**

| Section | When to Read |
|---------|-------------|
| Built-in Functions | Phase 1, Week 1 |
| Data Structures Tutorial | Phase 1, Week 2 |
| `collections` module | Phase 1, Week 5 |
| `itertools` module | Phase 1, Week 5 |
| `functools` module | Phase 1, Week 3 |
| `pathlib` module | Phase 1, Week 6 |
| `asyncio` module | Phase 1, Week 8 |

**Pro Tips:**
- Bookmark the "What's New" page for the latest Python version — good for keeping up.
- Every time you use a function, check its docs page for lesser-known parameters you might be missing.
- The "HOWTO" guides in the docs are excellent mini-tutorials on specific topics.

---

### 📗 Resource 1.6 — 100 Days of Code: Python Bootcamp (Udemy — Angela Yu)

**Link:** udemy.com — search "100 Days of Code Python Angela Yu"
**Type:** Paid course (buy during Udemy sale — ₹399–₹499)
**Duration:** Use selectively — not all 100 days
**When to use:** Phase 1, parallel to CS50P
**Difficulty:** Beginner → Intermediate

**Why this is perfect for you:**
Angela Yu's course is the most popular Python course on Udemy for a reason — every day is a project, not just theory. Since you're hackathon-minded, the project-first approach will keep you engaged. You don't need to do all 100 days — pick the ones relevant to AI/ML and skip the web dev days.

**Specific days to prioritize:**

| Days | Topic | Do it? |
|------|-------|--------|
| Days 1–14 | Python basics | Skim (you know this) |
| Day 15–17 | Coffee Machine OOP project | Yes — good OOP practice |
| Day 25–26 | CSV and Pandas intro | Yes |
| Day 36–38 | Stock trading news alert project | Yes — APIs + automation |
| Day 39–40 | Flight deal finder | Yes — real project |
| Days 55–60 | GUI + API projects | Yes |
| Days 87–89 | Data Science with Pandas | Yes |
| Days 96–100 | Professional portfolio projects | Yes |

**Pro Tips:**
- Wait for a Udemy sale — the course is almost always ₹399–₹499 (down from ₹3,000+). Never pay full price.
- Don't feel pressured to do all 100 days — you're not doing a Python bootcamp, you're building AI skills.
- Angela's explanations are beginner-friendly but can be slow for you — watch at 1.5x or 2x speed.

---

## 📐 SECTION 2 — Math for Machine Learning

---

### 📗 Resource 2.1 — 3Blue1Brown (YouTube — Grant Sanderson)

**Link:** youtube.com/@3blue1brown
**Type:** Free YouTube series
**Duration:** 3 weeks for the core playlists
**When to use:** Phase 1, Days 29–63
**Difficulty:** Beginner → Intermediate (conceptually)

**Why this is perfect for you:**
3Blue1Brown is not a math teacher — he's a visual storyteller who uses animation to make abstract math feel physical and intuitive. The "Essence of Linear Algebra" and "Essence of Calculus" series are the single best way to build the mathematical intuition you need for AI/ML. You don't need to be able to solve complex integrals — you need to understand what a gradient IS and why it matters. Grant makes that happen in a way no textbook can.

**Exactly what to watch and when:**

| Playlist | Episodes | When to Watch | Why |
|----------|----------|--------------|-----|
| Essence of Linear Algebra | All 15 episodes | Phase 1, Days 33–40 | Matrix ops are the foundation of neural networks |
| Essence of Calculus | Episodes 1–8 | Phase 1, Days 31–35 | Derivatives = gradient = how models learn |
| Neural Networks series | All 4 episodes | Phase 2, Days 99–105 | Visual intuition for how NNs work |
| But what is a GPT? | 1 video | Phase 3, Days 232–240 | Best visual intro to transformers |
| Attention in transformers | 1 video | Phase 3, Days 240–250 | Must-watch before coding attention |

**Pro Tips:**
- Watch with a notebook. Draw the visuals yourself as he draws them — active recall.
- Rewatch episodes you don't fully grasp. These are short (12–20 min each) so rewatching is worth it.
- After each video, open NumPy and code what he just showed visually. Matrix transformation → visualize with matplotlib.
- Don't rush. 1–2 videos per day is the right pace.
- Turn on subtitles if his pace is too fast at certain points.

---

### 📗 Resource 2.2 — StatQuest with Josh Starmer (YouTube)

**Link:** youtube.com/@statquest
**Type:** Free YouTube channel
**Duration:** Watch specific videos as needed — ongoing
**When to use:** Phase 1 (statistics) + Phase 2 (ML algorithms)
**Difficulty:** Absolute beginner

**Why this is perfect for you:**
Josh Starmer has one superpower: he can explain the most complex statistical and ML concepts to someone who has never taken a statistics class. His "bam" catchphrases aside, every video is structured with exceptional clarity — simple example first, formal definition second, code third. Since your statistics background may be weak (most engineering students in India don't get proper stats), StatQuest fills that gap without requiring you to take a separate statistics course.

**Must-watch videos in order:**

| Video | Watch During |
|-------|-------------|
| Statistics Fundamentals (full playlist) | Phase 1, Week 5 |
| Probability is not Likelihood | Phase 1, Day 30 |
| The Normal Distribution | Phase 1, Day 29 |
| Covariance and Correlation | Phase 1, Day 34 |
| Gradient Descent main ideas | Phase 1, Day 32 |
| Linear Regression | Phase 2, Day 99 |
| Logistic Regression | Phase 2, Day 103 |
| Decision Trees | Phase 2, Day 106 |
| Random Forests | Phase 2, Day 108 |
| XGBoost (4-part series) | Phase 2, Day 109 |
| K-means Clustering | Phase 2, Day 120 |
| PCA clearly explained | Phase 2, Day 122 |
| ROC and AUC | Phase 2, Day 113 |
| Naive Bayes | Phase 2, Day 170 |
| Neural Networks (playlist) | Phase 3, Day 197 |
| Backpropagation | Phase 3, Day 198 |

**Pro Tips:**
- Watch "Statistics Fundamentals" playlist completely in Week 5 — it's the most time-efficient stats education you can get.
- Every StatQuest ML video pairs perfectly with implementing the algorithm in sklearn right after. Watch → code.
- The "BAM!" moments are actually useful memory anchors — lean into them.
- Speed: 1.25x is comfortable for most videos.

---

### 📗 Resource 2.3 — Mathematics for Machine Learning (Coursera — Imperial College London)

**Link:** coursera.org/specializations/mathematics-machine-learning
**Type:** Free to audit (paid for certificate)
**Duration:** 3–4 months (do alongside Phase 1 and Phase 2)
**When to use:** Phase 1 Days 57–98, Phase 2 Days 99–140
**Difficulty:** Intermediate

**Why this is perfect for you:**
This is the only university-level math course designed specifically for ML practitioners — not for pure mathematicians. It covers linear algebra, multivariate calculus, and PCA in a way that's directly connected to how ML models work. You won't be solving abstract math problems — you'll be understanding WHY gradient descent works, WHY PCA reduces dimensions, and WHY neural networks can learn. The programming assignments are in Python which reinforces your coding at the same time.

**Course structure and how to take it:**

| Course | Topics | When |
|--------|--------|------|
| Course 1: Linear Algebra | Vectors, matrices, transformations, eigenvalues | Phase 1, Weeks 9–11 |
| Course 2: Multivariate Calculus | Derivatives, gradients, chain rule, Jacobians | Phase 1, Weeks 11–13 |
| Course 3: PCA | Dimensionality reduction, covariance, projections | Phase 2, Weeks 15–18 |

**Pro Tips:**
- Audit for free — don't pay for the certificate unless your company/college reimburses it.
- Do the programming assignments even if you're auditing (they're available for free in the first few weeks).
- Watch 3Blue1Brown's Linear Algebra series BEFORE starting Course 1 — it makes everything click faster.
- This course is academically rigorous — slower pace is fine. Don't rush it.
- The forums have good discussions if you get stuck on the math derivations.

---

### 📗 Resource 2.4 — Practical Deep Learning for Coders — Math Parts (fast.ai)

**Link:** course.fast.ai
**Type:** Free course (math covered in context)
**Duration:** Part of the full course
**When to use:** Phase 3, Days 197–231
**Difficulty:** Intermediate

**Why this is perfect for you:**
Jeremy Howard at fast.ai teaches math the opposite way of universities — top-down, in context. You first see a working neural network, and THEN he goes back to explain the math behind why it works. This is perfect for a builder like you because you never lose motivation wondering "when will I use this?" — you're already using it. The math covered includes exactly what you need for deep learning: matrix calculus, backpropagation math, optimization theory.

**What to focus on for math:**
- Lesson 3: Stochastic Gradient Descent from scratch
- Lesson 4: Natural language processing math
- Lesson 13: Backpropagation from foundations
- The "From Foundations" notebooks — these are pure math-to-code translations

**Pro Tips:**
- Run every notebook in Google Colab as you watch — don't just watch passively.
- The forums at forums.fast.ai have the best deep learning math discussions outside of academic papers.
- Jeremy moves fast — pause frequently and look up anything you don't immediately understand.

---

### 📗 Resource 2.5 — Khan Academy (Linear Algebra + Statistics)

**Link:** khanacademy.org
**Type:** Free video + exercises
**Duration:** Use as gap-filler — not a primary resource
**When to use:** Phase 1, whenever you feel shaky on a math concept
**Difficulty:** Beginner

**Why this is perfect for you:**
Khan Academy is not your primary math resource — it's your safety net. When 3Blue1Brown goes too fast or the Coursera course assumes too much, Khan Academy's ultra-patient explanations fill the gap. The exercises with immediate feedback are especially useful for building calculation confidence. As someone who may not have studied advanced stats formally, Khan's statistics section is a reliable foundation.

**When to use which section:**

| Section | Use When |
|---------|---------|
| Linear Algebra | You don't follow 3Blue1Brown — go here first |
| Statistics & Probability | Phase 1, Week 5 (especially distributions and hypothesis testing) |
| Calculus — Derivatives | You struggle with the chain rule concept |
| Multivariable Calculus | Reference when gradient vectors feel abstract |

**Pro Tips:**
- Don't start here — use it when you hit a wall elsewhere.
- The exercise system with hints is excellent for building actual calculation skills.
- The statistics section specifically is worth doing fully if you have no statistics background.

---

## 🤖 SECTION 3 — Classical Machine Learning

---

### 📗 Resource 3.1 — Machine Learning Specialization (Coursera — Andrew Ng)

**Link:** coursera.org/specializations/machine-learning-introduction
**Type:** Free to audit
**Duration:** 3 months (primary course for Phase 2)
**When to use:** Phase 2, Days 99–196 (the backbone of Phase 2)
**Difficulty:** Beginner → Intermediate

**Why this is perfect for you:**
Andrew Ng taught the original ML course that introduced millions of people to machine learning — including the founders of most major AI companies. This new version (2022) uses Python and scikit-learn instead of Octave, is more practical, and covers modern techniques. For a beginner, there is no better structured introduction to ML theory AND practice combined. Andrew's teaching style is patient, clear, and builds intuition before math — perfectly aligned with how you learn best.

**Course breakdown and how to take it:**

| Course | Content | Weeks |
|--------|---------|-------|
| Course 1: Supervised ML | Linear regression, logistic regression, gradient descent | Weeks 15–17 |
| Course 2: Advanced Algorithms | Decision trees, neural networks, debugging ML models | Weeks 17–21 |
| Course 3: Unsupervised + Recommenders + RL | Clustering, anomaly detection, collaborative filtering | Weeks 21–25 |

**Topics to pay extra attention to:**
- Week 1: Cost functions and gradient descent — understand every line of math
- Week 2: Regularization — this will save your models from overfitting forever
- Week 3: Decision boundary visualization — run the notebooks yourself
- Course 2, Week 2: Bias/variance diagnosis — this is how professionals debug ML systems
- Course 2, Week 3: Machine learning development process — real-world insight from Andrew's career

**Pro Tips:**
- Audit for free — skip the graded assignments if needed but DO the optional labs.
- The optional labs are Jupyter notebooks — run every cell and modify the code to test your understanding.
- After each concept, immediately implement it from scratch in NumPy. Don't just use the provided code.
- Andrew's lectures are methodical — if you're in a rush, watch at 1.5x but always pause for the math slides.
- Join the Coursera discussion forums — your exact question has probably been answered.
- Take handwritten notes — the act of writing encodes the formulas better than typing.

---

### 📗 Resource 3.2 — Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (Book — Aurélien Géron)

**Link:** Buy on Amazon/Flipkart — ~₹600–₹800 (2nd or 3rd edition)
**Type:** Book (physical or PDF)
**Duration:** 3–4 months (read alongside Phase 2 and Phase 3)
**When to use:** Phase 2 Days 99–196, Phase 3 Days 197–260
**Difficulty:** Intermediate

**Why this is perfect for you:**
This is the single most recommended book in the ML/AI community by practitioners who actually work in the field. Andrew Ng gives you the theory — Géron shows you how professionals implement it. Every chapter has working code, real datasets, and the reasoning behind every design decision. The book covers the full pipeline from data cleaning to deployment, which is exactly what a product-builder like you needs. It's the reference book you'll return to throughout your entire career.

**Chapter-by-chapter guide:**

| Chapter | Topic | Read During |
|---------|-------|------------|
| 1 | ML landscape overview | Phase 2, Day 99 |
| 2 | End-to-end ML project | Phase 2, Days 100–105 |
| 3 | Classification | Phase 2, Days 106–110 |
| 4 | Training models (math) | Phase 2, Days 110–115 |
| 5 | SVM | Phase 2, Days 115–118 |
| 6 | Decision Trees | Phase 2, Days 106–109 |
| 7 | Ensemble Learning | Phase 2, Days 108–112 |
| 8 | Dimensionality Reduction | Phase 2, Days 120–126 |
| 9 | Unsupervised Learning | Phase 2, Days 120–130 |
| 10 | Neural Networks Intro | Phase 3, Days 197–203 |
| 11 | Training Deep Networks | Phase 3, Days 204–215 |
| 12 | Custom Models in TensorFlow | Phase 3, Days 215–225 |
| 13 | Loading Data at Scale | Phase 3, Days 225–235 |
| 14 | CNNs | Phase 3, Days 210–217 |
| 15 | RNNs and LSTMs | Phase 3, Days 224–231 |
| 16 | NLP with RNNs & Attention | Phase 3, Days 232–240 |
| 17 | Representation Learning | Phase 3, Days 245–255 |

**Pro Tips:**
- Chapter 2 (end-to-end project) is worth reading twice — it's a masterclass in professional ML workflow.
- Code every example yourself — don't copy-paste. Type it. Debug it.
- The exercises at the end of each chapter are excellent — do at least 3 per chapter.
- Get the 3rd edition if possible — it's updated with more modern techniques.
- Pair each chapter with the corresponding topic in Andrew Ng's course for maximum retention.

---

### 📗 Resource 3.3 — Kaggle Learn — Machine Learning Micro-courses

**Link:** kaggle.com/learn
**Type:** Free interactive micro-courses
**Duration:** 1–2 days per course
**When to use:** Phase 1 Days 1–98 (Python, Pandas) + Phase 2 (ML courses)
**Difficulty:** Beginner → Intermediate

**Why this is perfect for you:**
Kaggle's micro-courses are the fastest, most practical way to learn specific tools. Each course takes 4–8 hours and ends with working code you can immediately use. Since you're a builder, the fact that every lesson runs in a live Jupyter notebook (no setup needed) means you spend zero time on configuration and 100% time on learning. Kaggle also gives you certificates for each course — useful for your LinkedIn profile early on.

**Complete these in order:**

| Course | Days to Complete | Do During |
|--------|-----------------|-----------|
| Python | 2 days | Phase 0, Days 7–8 |
| Pandas | 2 days | Phase 0–1, Days 13–14 |
| Data Visualization | 2 days | Phase 1, Day 34 |
| Intro to Machine Learning | 1 day | Phase 2, Day 99 |
| Intermediate Machine Learning | 2 days | Phase 2, Day 140 |
| Feature Engineering | 2 days | Phase 2, Day 170 |
| Data Cleaning | 1 day | Phase 1, Day 43 |
| Intro to SQL | 2 days | Phase 1, Day 46 |
| Advanced SQL | 2 days | Phase 2, Day 160 |
| Intro to Deep Learning | 2 days | Phase 3, Day 197 |
| Computer Vision | 2 days | Phase 3, Day 210 |
| NLP | 2 days | Phase 3, Day 224 |
| LLMs | 2 days | Phase 3, Day 250 |
| Intro to AI Ethics | 1 day | Phase 3, Day 270 |

**Pro Tips:**
- Always edit the provided notebooks — change hyperparameters, add a new cell, try a different approach.
- After each micro-course, apply the techniques immediately to a new Kaggle dataset.
- Collect all the certificates and add them to your LinkedIn profile — they signal consistency.
- The Kaggle competitions that pair with these micro-courses are perfect first competitions.

---

### 📗 Resource 3.4 — Scikit-Learn Official Documentation

**Link:** scikit-learn.org/stable/user_guide.html
**Type:** Official documentation
**Duration:** Ongoing reference
**When to use:** Phase 2 onwards (every time you use an sklearn model)
**Difficulty:** Intermediate

**Why this is perfect for you:**
The sklearn documentation is exceptionally well-written — every algorithm page has the math, parameters, examples, and a list of what to read next. As a future AI engineer, you need to be fluent in reading technical documentation because the industry moves too fast for courses to keep up. Sklearn's docs are a good first documentation to get comfortable with.

**Key pages to bookmark:**

| Page | Read When |
|------|----------|
| User Guide — Supervised Learning | Phase 2, Day 99 |
| User Guide — Model Evaluation | Phase 2, Day 113 |
| User Guide — Preprocessing | Phase 2, Day 115 |
| User Guide — Pipeline | Phase 2, Day 120 |
| User Guide — Cross-validation | Phase 2, Day 117 |
| User Guide — Tuning Hyperparameters | Phase 2, Day 125 |
| User Guide — Feature Selection | Phase 2, Day 165 |

**Pro Tips:**
- The "Examples" section for each algorithm shows real datasets — more valuable than theory pages.
- Read the "Notes" section at the bottom of each algorithm page — that's where the expert-level detail lives.
- The sklearn cheat sheet (available on their site) is worth printing and keeping on your desk.

---

### 📗 Resource 3.5 — fast.ai — Practical Machine Learning for Coders

**Link:** course.fast.ai/Lessons/lesson1.html
**Type:** Free course
**Duration:** 4–6 weeks
**When to use:** Phase 2, Days 150–196 (after Andrew Ng — for practical depth)
**Difficulty:** Intermediate

**Why this is perfect for you:**
Fast.ai's philosophy is the opposite of traditional education: build first, understand the theory later. Jeremy Howard, who co-founded the company that created ULMFiT (the precursor to modern NLP), teaches you to train state-of-the-art models in the first lesson and spends the rest of the course explaining why they work. As someone who wants to build products and startups, this top-down approach keeps you motivated and ships working things faster than any bottom-up approach.

**Lesson-by-lesson guide:**

| Lesson | Topic | Week |
|--------|-------|------|
| Lesson 1 | Image classification (get a working model fast) | Phase 2, Day 150 |
| Lesson 2 | Deployment (build and ship something real) | Phase 2, Day 155 |
| Lesson 3 | Neural Net Foundations | Phase 2–3 transition |
| Lesson 4 | NLP, fine-tuning | Phase 3, Day 232 |
| Lesson 5 | From-scratch model | Phase 3, Day 240 |
| Lesson 6 | Random Forests deep dive | Phase 2, Day 180 |
| Lesson 7 | Collaborative Filtering | Phase 2, Day 185 |

**Pro Tips:**
- Run all notebooks on Kaggle (they provide free GPUs) — just click "Copy and Edit" on the course notebooks.
- The fast.ai forums are one of the best ML communities — search before asking, your question is likely already answered.
- Don't wait to "feel ready" for fast.ai — the deliberate jump into complexity is the point.
- Jeremy has strong opinions about top-down learning — trust the process even when it feels uncomfortable.

---

### 📗 Resource 3.6 — Kaggle Competitions (Titanic, House Prices, Playground Series)

**Link:** kaggle.com/competitions
**Type:** Competitions (free to enter)
**Duration:** 1–2 weeks per competition
**When to use:** Phase 2, Days 110–196 (multiple competitions)
**Difficulty:** Intermediate

**Why this is perfect for you:**
Kaggle competitions are where ML theory meets real messy data. You'll discover things no course teaches — that data cleaning matters more than model choice, that feature engineering beats fancy algorithms, that your first model is never your best model. Looking at other people's public notebooks ("kernels") on Kaggle is like having access to thousands of expert solutions. Start with the "Getting Started" competitions before moving to the timed ones.

**Competition progression:**

| Competition | When | Goal |
|-------------|------|------|
| Titanic (binary classification) | Phase 2, Day 110 | First submission — top 50% |
| House Prices (regression) | Phase 2, Day 120 | Top 30% |
| Digit Recognizer (CNN intro) | Phase 3, Day 210 | Top 30% |
| Playground Series (monthly) | Phase 2–3 ongoing | Compete monthly |
| Spaceship Titanic | Phase 2, Day 150 | Top 20% |

**Pro Tips:**
- Submit early — even a terrible model. The act of submitting a working end-to-end pipeline teaches more than 10 tutorials.
- Read the top 3 public notebooks after your first submission — see what you missed.
- Study the data leaderboard: what score separates top 10% from top 50%? That's your target.
- Join competition discussion forums — the feature engineering tips shared there are invaluable.
- Don't worry about the prize money at the start — focus on learning, not winning.

---

## 🧠 SECTION 4 — Deep Learning

---

### 📗 Resource 4.1 — Deep Learning Specialization (Coursera — Andrew Ng)

**Link:** coursera.org/specializations/deep-learning
**Type:** Free to audit
**Duration:** 3 months
**When to use:** Phase 3, Days 197–260
**Difficulty:** Intermediate

**Why this is perfect for you:**
Andrew Ng's Deep Learning Specialization is the most structured path from understanding neural networks mathematically to building CNNs, RNNs, and modern architectures. Like his ML course, it builds intuition before math and math before code. This is the course that gave thousands of engineers the deep foundation to later work at DeepMind, OpenAI, and Google Brain. For your path to LLMs and AI products, this course gives you the theoretical grounding that prevents you from being a "prompt engineer who can't debug a model."

**Course-by-course breakdown:**

| Course | Topics | Phase Days |
|--------|--------|-----------|
| Course 1: Neural Networks & Deep Learning | Forward/backprop, vectorization, shallow networks | Days 197–210 |
| Course 2: Improving Deep Neural Networks | Regularization, optimization, hyperparameter tuning | Days 210–225 |
| Course 3: Structuring ML Projects | ML strategy, error analysis, human-level performance | Days 225–232 |
| Course 4: Convolutional Neural Networks | CNNs, object detection, face recognition, style transfer | Days 232–250 |
| Course 5: Sequence Models | RNNs, LSTMs, GRUs, attention, transformers | Days 250–270 |

**Must-focus topics:**
- Course 1, Week 2: Vectorization — this is how NumPy operations map to neural networks
- Course 2: The systematic approach to debugging ML models — career-defining skill
- Course 3: How to decide what to build and fix next — the most underrated course of the 5
- Course 5, Week 3–4: Attention mechanism — the bridge to transformers

**Pro Tips:**
- Course 3 (Structuring ML Projects) has no programming assignments — do it in a single focused day.
- The programming assignments use TensorFlow — convert them to PyTorch for extra practice.
- Take notes on the "Heroes of Deep Learning" interview videos — Andrew interviews pioneers, and the career advice is priceless.
- After Course 5, you're ready to read the "Attention is All You Need" paper.

---

### 📗 Resource 4.2 — Neural Networks: Zero to Hero (YouTube — Andrej Karpathy)

**Link:** youtube.com/@AndrejKarpathy — "Neural Networks: Zero to Hero" playlist
**Type:** Free YouTube series
**Duration:** 3–4 weeks
**When to use:** Phase 3, Days 197–232 (alongside Andrew Ng)
**Difficulty:** Intermediate → Advanced

**Why this is perfect for you:**
Andrej Karpathy is the former Director of AI at Tesla and was at OpenAI when GPT was built. This YouTube series is him teaching neural networks the way he wished someone had taught him — building everything from absolute scratch in Python with no ML libraries. If Andrew Ng gives you the intuition and theory, Karpathy gives you the deep mechanical understanding. After watching "Let's build GPT from scratch," you will understand transformers at a level that 95% of people working with LLMs don't have. This is your secret weapon.

**Video-by-video guide:**

| Video | Topic | Watch During | Importance |
|-------|-------|-------------|-----------|
| micrograd | Backpropagation engine from scratch | Phase 3, Day 197 | 🔴 Critical |
| makemore Part 1 | Bigram language model | Phase 3, Day 200 | 🔴 Critical |
| makemore Part 2 | MLP, embedding | Phase 3, Day 205 | 🔴 Critical |
| makemore Part 3 | BatchNorm, activations | Phase 3, Day 210 | 🟡 Important |
| makemore Part 4 | Backprop through time | Phase 3, Day 215 | 🟡 Important |
| makemore Part 5 | WaveNet architecture | Phase 3, Day 220 | 🟡 Important |
| Let's build GPT | Full GPT from scratch | Phase 3, Day 232 | 🔴 Critical — watch twice |
| Let's build the tokenizer | BPE tokenization | Phase 3, Day 245 | 🟡 Important |
| Intro to LLMs | 1-hour lecture | Phase 3, Day 250 | 🟡 Important |

**Pro Tips:**
- Code along in real time — don't just watch. Pause after every cell and understand it.
- "micrograd" is 2.5 hours — do it in one sitting with no distractions. It's the most important single video for understanding deep learning.
- "Let's build GPT" should be watched twice: once to follow along, once to rebuild from memory.
- After each video, push your implementation to GitHub with comments explaining every function.
- These videos assume you can write clean Python — make sure Phase 1 is solid before starting.

---

### 📗 Resource 4.3 — PyTorch Official Tutorials

**Link:** pytorch.org/tutorials/
**Type:** Official documentation + tutorials
**Duration:** 2–3 weeks for core tutorials
**When to use:** Phase 3, Days 202–231
**Difficulty:** Intermediate

**Why this is perfect for you:**
PyTorch is THE framework for AI/ML in 2024–2025 — used by virtually every major research lab and most production AI teams. Learning from the official tutorials means you learn the correct patterns, not workarounds you'll have to unlearn later. The tutorials are practical, well-organized, and connect directly to real use cases. Since you're heading toward building AI products, being fluent in PyTorch is non-negotiable.

**Tutorials to complete in order:**

| Tutorial | When | Time |
|----------|------|------|
| Learn the Basics (full series) | Phase 3, Day 202 | 2 days |
| Introduction to PyTorch on YouTube | Phase 3, Day 202 | 1 day |
| Learning PyTorch with Examples | Phase 3, Day 204 | 1 day |
| Neural Networks Tutorial | Phase 3, Day 205 | 1 day |
| Training a Classifier | Phase 3, Day 206 | 1 day |
| Transfer Learning Tutorial | Phase 3, Day 217 | 1 day |
| Saving and Loading Models | Phase 3, Day 220 | half day |
| Text Classification with TorchText | Phase 3, Day 224 | 2 days |

**Pro Tips:**
- Use Google Colab with a GPU runtime for all PyTorch tutorials — training on CPU is painfully slow.
- After each tutorial, build a variation — same concept but different dataset or architecture.
- Learn `torch.nn.Module`, `DataLoader`, and the training loop pattern deeply — everything else builds on these 3.
- Read the PyTorch documentation for every function you use — the docs explain nuances that tutorials skip.

---

### 📗 Resource 4.4 — Dive into Deep Learning (d2l.ai)

**Link:** d2l.ai (free online book)
**Type:** Free interactive online textbook
**Duration:** Reference book — not read cover to cover
**When to use:** Phase 3, Days 197–294 (reference alongside Karpathy and fast.ai)
**Difficulty:** Intermediate → Advanced

**Why this is perfect for you:**
D2L is the most comprehensive practical deep learning textbook — used as the official textbook at Stanford, MIT, CMU, and Oxford. Unlike Goodfellow's "Deep Learning" (which is pure theory), D2L shows code for every concept in PyTorch, TensorFlow, and JAX simultaneously. You use it as a reference — when Karpathy explains something fast, d2l has the slower, more detailed version with multiple code examples.

**Key chapters to bookmark:**

| Chapter | Use It When |
|---------|------------|
| Ch 3: Linear Neural Networks | Phase 3, Day 197 |
| Ch 4: Multilayer Perceptrons | Phase 3, Day 200 |
| Ch 5: Deep Learning Computation | Phase 3, Day 205 |
| Ch 6: Convolutional Neural Networks | Phase 3, Day 210 |
| Ch 8: Recurrent Neural Networks | Phase 3, Day 224 |
| Ch 10: Attention Mechanisms | Phase 3, Day 240 |
| Ch 11: Optimization Algorithms | Phase 3, Day 215 |
| Ch 15: NLP Pretraining | Phase 3, Day 245 |

**Pro Tips:**
- Don't try to read this linearly — use it as a reference dictionary.
- The "Summary" section at the end of each chapter is excellent for quick review.
- The exercises in d2l are harder than most courses — attempt them when you want a challenge.

---

### 📗 Resource 4.5 — The Illustrated Series (Jay Alammar Blog)

**Link:** jalammar.github.io
**Type:** Free blog articles with stunning visuals
**Duration:** 30–60 minutes per article
**When to use:** Phase 3, Days 232–294 (transformer and LLM concepts)
**Difficulty:** Intermediate

**Why this is perfect for you:**
Jay Alammar's illustrated articles are the most-shared ML educational content on the internet. His visual explanations of transformers, BERT, and GPT have been referenced in research papers, Stanford courses, and used by engineers at Google and OpenAI to explain things to colleagues. If you struggle to visualize how attention works or what positional encoding does, one of Jay's articles will make it click in 20 minutes what a textbook can't do in 20 pages.

**Articles to read in this exact order:**

| Article | Read During |
|---------|------------|
| The Illustrated Word2Vec | Phase 3, Day 232 |
| The Illustrated Transformer | Phase 3, Day 235 — must-read |
| The Illustrated BERT | Phase 3, Day 245 |
| The Illustrated GPT-2 | Phase 3, Day 248 |
| How GPT3 Works | Phase 3, Day 250 |
| The Illustrated Stable Diffusion | Phase 3, Day 270 |
| Interfaces for Explaining Transformer Language Models | Phase 3, Day 260 |

**Pro Tips:**
- "The Illustrated Transformer" should be read slowly — zoom into every diagram. This is the single best transformer explanation ever written.
- After reading each article, close it and try to draw the architecture from memory on paper.
- Share the Illustrated Transformer with your accountability partner — teaching it to someone else locks it in.
- Read before watching Karpathy's GPT video — it makes the code make more sense.

---

## 🔧 SECTION 5 — LLMs & Transformers

---

### 📗 Resource 5.1 — Hugging Face NLP Course

**Link:** huggingface.co/learn/nlp-course
**Type:** Free course
**Duration:** 4–6 weeks
**When to use:** Phase 3, Days 240–270
**Difficulty:** Intermediate

**Why this is perfect for you:**
Hugging Face is the GitHub of AI models — every major company and research lab hosts models there, and the `transformers` library is the industry standard for working with LLMs. Their official NLP course teaches you to use the library the way the people who built it intended — not through hacked-together tutorials. After this course you'll be able to load, fine-tune, and deploy any model on Hugging Face Hub, which is the practical skill at the center of most AI engineering jobs.

**Chapter-by-chapter plan:**

| Chapter | Topic | Days |
|---------|-------|------|
| 0 | Setup | Day 240 |
| 1 | Transformer Models | Day 241–242 |
| 2 | Using Transformers | Day 243–244 |
| 3 | Fine-tuning a Pretrained Model | Day 245–248 |
| 4 | Sharing Models and Tokenizers | Day 249 |
| 5 | The Hugging Face Datasets Library | Day 250–251 |
| 6 | The Tokenizers Library | Day 252–253 |
| 7 | Main NLP Tasks | Day 254–260 |
| 8 | How to Ask for Help | Day 261 |
| 9 | Building and Sharing Demos | Day 262–265 |

**Pro Tips:**
- Run every notebook in Google Colab — Hugging Face provides "Open in Colab" buttons on every page.
- Chapter 3 (fine-tuning) is the most important — spend extra time here and do it on a custom dataset, not just the example one.
- Chapter 9 (Gradio demos) is what lets you share your work — don't skip this.
- After the course, explore the Model Hub and find 5 models relevant to a problem you care about.
- Join the Hugging Face Discord (huggingface.co/join/discord) — the team and community are very responsive.

---

### 📗 Resource 5.2 — DeepLearning.AI Short Courses

**Link:** learn.deeplearning.ai
**Type:** Free short courses (1–3 hours each)
**Duration:** 1–2 days per course
**When to use:** Phase 3–4, Days 250–350 (specific courses as needed)
**Difficulty:** Intermediate

**Why this is perfect for you:**
DeepLearning.AI's short courses are co-created with the companies that built the tools — so you're learning LangChain from the LangChain founders, RAG from the Pinecone team, and agents from the people who run the leading agent research. Each course is hyper-focused, runs in a browser-based environment (no setup), and is designed for practitioners building real things. These are the fastest way to get productive with specific AI engineering tools.

**Courses to take in this exact order:**

| Course | Created With | Take During | Time |
|--------|-------------|-------------|------|
| ChatGPT Prompt Engineering for Developers | OpenAI | Phase 3, Day 250 | 1 day |
| Building Systems with ChatGPT API | OpenAI | Phase 4, Day 295 | 1 day |
| LangChain for LLM Application Development | LangChain | Phase 4, Day 300 | 2 days |
| LangChain: Chat with Your Data | LangChain | Phase 4, Day 305 | 2 days |
| Building and Evaluating Advanced RAG | LlamaIndex | Phase 4, Day 315 | 2 days |
| Finetuning Large Language Models | Lamini | Phase 3, Day 260 | 2 days |
| How Diffusion Models Work | | Phase 3, Day 275 | 1 day |
| Building Generative AI Applications with Gradio | | Phase 3, Day 265 | 1 day |
| Vector Databases: from Embeddings to Applications | Weaviate | Phase 4, Day 308 | 2 days |
| Functions, Tools and Agents with LangChain | LangChain | Phase 4, Day 379 | 2 days |
| AI Agents in LangGraph | LangChain | Phase 4, Day 385 | 2 days |
| Building Agentic RAG with LlamaIndex | LlamaIndex | Phase 4, Day 395 | 2 days |

**Pro Tips:**
- New courses are added regularly — check the site monthly and pick up any that match your current phase.
- Don't binge — take each course right before you implement that technique in a project.
- The courses use Jupyter notebooks in the browser — re-implement every notebook in your local environment after.
- These pair perfectly with the roadmap: the RAG course right before you build your RAG project, agents course before your agent project.

---

### 📗 Resource 5.3 — Attention Is All You Need (Original Paper)

**Link:** arxiv.org/abs/1706.03762
**Type:** Research paper
**Duration:** 3–4 hours for full careful reading
**When to use:** Phase 3, Day 235 (after Jay Alammar's Illustrated Transformer)
**Difficulty:** Advanced

**Why this is perfect for you:**
Every modern LLM — GPT-4, Claude, Gemini, Llama — is built on this 2017 paper. Reading the original paper shows you what the architecture actually does without any simplification. It's also a short paper (15 pages) compared to most research. More importantly, building the habit of reading research papers early puts you in a different league from people who only watch YouTube videos. By Day 300, you should be able to read and implement papers — this is your first one.

**How to read it:**

| Pass | What to Read | Goal |
|------|-------------|------|
| Pass 1 (30 min) | Abstract, Introduction, Conclusion | Get the big picture |
| Pass 2 (1 hour) | Section 3 (Model Architecture) with Jay Alammar's article open | Understand the architecture |
| Pass 3 (2 hours) | Full paper with code implementation open | Connect equations to code |

**Pro Tips:**
- Read Jay Alammar's "Illustrated Transformer" the day before — it's the visual companion to this paper.
- Watch Yannic Kilcher's walkthrough of this paper on YouTube after your first read.
- Don't get stuck on equations you don't understand — annotate with "I don't understand this yet" and move on.
- After reading, try to explain the multi-head attention mechanism to someone else or write it in your notes.

---

### 📗 Resource 5.4 — LLM University (Cohere)

**Link:** docs.cohere.com/docs/llmu
**Type:** Free course
**Duration:** 2–3 weeks
**When to use:** Phase 3, Days 250–270
**Difficulty:** Intermediate

**Why this is perfect for you:**
Cohere built this course to teach practitioners how to work with LLMs in production, not just in tutorials. The modules on text embeddings, semantic search, and RAG are the most practical explanation of these concepts you'll find for free. Since you're going toward building AI products, understanding embeddings and semantic search deeply is directly applicable to every RAG system you'll build.

**Modules to prioritize:**

| Module | Priority | Read During |
|--------|----------|------------|
| What are Large Language Models? | Must do | Phase 3, Day 250 |
| Text Embeddings | Must do | Phase 3, Day 252 |
| Semantic Search | Must do | Phase 3, Day 254 |
| The Generate Endpoint | Must do | Phase 3, Day 256 |
| Prompt Engineering | Must do | Phase 3, Day 258 |
| Reranking | Must do | Phase 4, Day 315 |
| Fine-tuning | Do | Phase 3, Day 260 |

**Pro Tips:**
- The embeddings module is the best free explanation of how semantic search works — essential for RAG.
- Code every example in the module even if they provide working code.
- After each module, test the concept with the Cohere free API tier (generous free credits).

---

### 📗 Resource 5.5 — Full Stack LLM Bootcamp 2023 (YouTube)

**Link:** youtube.com — search "Full Stack LLM Bootcamp 2023"
**Type:** Free recorded lectures
**Duration:** 2 weeks
**When to use:** Phase 4, Days 295–315
**Difficulty:** Intermediate → Advanced

**Why this is perfect for you:**
This bootcamp covers the full stack of building LLM applications in production — from prompt engineering to deployment to evaluation to cost management. The speakers include practitioners from Weights & Biases, LangChain, and other companies that are building the infrastructure of the AI industry. It's the closest thing to working at an AI startup for free — pure practitioner knowledge, zero academic padding.

**Sessions to watch:**

| Session | Topic | Watch During |
|---------|-------|-------------|
| 1 | Learn to Spell: Prompt Engineering | Phase 3, Day 260 |
| 2 | LLMOps | Phase 4, Day 295 |
| 3 | UX for Language Interfaces | Phase 4, Day 320 |
| 4 | What's next for LLM apps? | Phase 4, Day 330 |
| 5 | Fireside Chat | Phase 4, Day 340 |
| 6 | Augmented Language Models | Phase 4, Day 350 |
| 7 | LLM Foundations | Phase 3, Day 250 |

**Pro Tips:**
- Watch LLM Foundations (Session 7) first even though it's listed last.
- Take notes on the production war stories — the mistakes they describe are exactly what you'll face.

---

### 📗 Resource 5.6 — LangChain Documentation

**Link:** python.langchain.com/docs/
**Type:** Official documentation
**Duration:** Ongoing reference
**When to use:** Phase 4, Days 300–420
**Difficulty:** Intermediate

**Why this is perfect for you:**
LangChain is the most widely used framework for building LLM-powered applications. The documentation has both conceptual guides and working code examples. Learning to navigate and use framework documentation fluently is a core professional skill — LangChain's docs are among the better-written ones in the AI ecosystem.

**Key sections to master:**

| Section | Master It During |
|---------|----------------|
| Installation + Quickstart | Phase 4, Day 300 |
| LLMs and Chat Models | Phase 4, Day 301 |
| Prompt Templates | Phase 4, Day 302 |
| Document Loaders | Phase 4, Day 305 |
| Text Splitters | Phase 4, Day 306 |
| Vector Stores | Phase 4, Day 308 |
| Retrievers | Phase 4, Day 310 |
| Chains | Phase 4, Day 312 |
| Agents | Phase 4, Day 379 |
| Memory | Phase 4, Day 315 |

**Pro Tips:**
- LangChain updates fast — always check the docs version matches your installed version (`pip show langchain`).
- The "How-to guides" section has recipes for every common task — bookmark it.
- When something breaks, check the GitHub issues before Stack Overflow — LangChain issues are often framework-level.

---

### 📗 Resource 5.7 — Anthropic Claude API Documentation

**Link:** docs.anthropic.com
**Type:** Official documentation
**Duration:** Ongoing reference
**When to use:** Phase 4, Days 295+
**Difficulty:** Intermediate

**Why this is perfect for you:**
Claude (the AI you're talking to right now) has one of the best-documented APIs in the industry. Anthropic's documentation includes not just technical API docs but also guides on prompt engineering, building reliable AI systems, and thinking about safety. Since you're building AI products, learning to work with Claude's API (alongside OpenAI) gives you more flexibility and often better results on complex reasoning tasks.

**Key sections:**

| Section | Read When |
|---------|----------|
| Getting Started | Phase 4, Day 295 |
| Messages API | Phase 4, Day 295 |
| Prompt Engineering Guide | Phase 3, Day 250 |
| Tool Use | Phase 4, Day 379 |
| Vision | Phase 4, Day 385 |
| Claude Models Overview | Phase 4, Day 295 |

---

## 🏗️ SECTION 6 — AI Product Engineering

---

### 📗 Resource 6.1 — FastAPI Official Documentation

**Link:** fastapi.tiangolo.com
**Type:** Official documentation (one of the best-written docs ever)
**Duration:** 1–2 weeks for core tutorial
**When to use:** Phase 4, Days 323–340
**Difficulty:** Intermediate

**Why this is perfect for you:**
FastAPI is the dominant Python web framework for AI backends — used by Netflix, Uber, and most AI startups. The documentation is legendary in the developer community for its clarity and completeness. Since you'll be building APIs for your AI products, FastAPI gives you the speed of Python with the performance of Node.js and auto-generated API documentation that impresses clients and co-founders. Sebastian Ramirez (creator) writes the docs himself and they read like a great tutorial, not a reference manual.

**Tutorial sections to complete in order:**

| Section | Complete During |
|---------|----------------|
| Tutorial — First Steps | Phase 4, Day 323 |
| Path Parameters | Phase 4, Day 323 |
| Query Parameters | Phase 4, Day 323 |
| Request Body (Pydantic) | Phase 4, Day 324 |
| Response Models | Phase 4, Day 324 |
| Error Handling | Phase 4, Day 325 |
| Background Tasks | Phase 4, Day 326 |
| CORS | Phase 4, Day 327 |
| SQL Database | Phase 4, Day 330 |
| Security — OAuth2 with JWT | Phase 4, Day 335 |
| WebSockets (for streaming LLM) | Phase 4, Day 340 |

**Pro Tips:**
- Build your first API endpoint the same day you read about it — do not just read.
- The automatic `/docs` endpoint FastAPI generates is a killer feature — use it to test every endpoint.
- Pydantic models (for input validation) are half of what makes FastAPI great — spend extra time on this.
- For streaming LLM responses, use `StreamingResponse` — learn this early, it's used in every AI chatbot.

---

### 📗 Resource 6.2 — Streamlit Documentation

**Link:** docs.streamlit.io
**Type:** Official documentation
**Duration:** 1 week
**When to use:** Phase 4, Days 315–330
**Difficulty:** Beginner → Intermediate

**Why this is perfect for you:**
Streamlit lets you turn a Python script into a shareable web app in under 1 hour — no HTML, CSS, or JavaScript needed. For a student who wants to show real working AI products without spending weeks on frontend development, Streamlit is the ultimate shortcut. Every AI demo you build in the next 6 months should start as a Streamlit app before you invest in a "real" frontend.

**What to learn:**

| Feature | Learn During |
|---------|-------------|
| st.write, st.title, st.markdown | Phase 4, Day 315 |
| st.text_input, st.button, st.slider | Phase 4, Day 315 |
| st.file_uploader | Phase 4, Day 316 |
| st.chat_message, st.chat_input | Phase 4, Day 317 |
| st.session_state (for memory) | Phase 4, Day 318 |
| st.sidebar | Phase 4, Day 319 |
| Deploying on Streamlit Cloud | Phase 4, Day 320 |
| Streaming LLM responses | Phase 4, Day 321 |

**Pro Tips:**
- The "30 Days of Streamlit" challenge on their website is excellent — do it in 10 days by doubling up.
- Every AI project you build should have a Streamlit frontend first — deploy to Streamlit Cloud for free.
- `st.session_state` is the key to maintaining conversation history in chatbots — understand it deeply.
- Streamlit Cloud free tier is generous — you can have multiple public apps running for free.

---

### 📗 Resource 6.3 — Vercel AI SDK Documentation

**Link:** sdk.vercel.ai/docs
**Type:** Official documentation
**Duration:** 1–2 weeks
**When to use:** Phase 4, Days 350–380
**Difficulty:** Intermediate

**Why this is perfect for you:**
When you're ready to move beyond Streamlit to a real web product, Vercel's AI SDK is the fastest path to a production-quality AI chat interface. It handles streaming, tool calls, and multi-modal inputs out of the box for both React and Next.js. The free deployment on Vercel means you can share a polished product with potential users and investors in minutes.

**What to cover:**
- Getting started with Next.js + AI SDK
- `useChat` hook — the core of every AI chat interface
- Streaming text responses
- Tool calling integration
- Deploying to Vercel (free tier)

---

### 📗 Resource 6.4 — Supabase Documentation

**Link:** supabase.com/docs
**Type:** Official documentation
**Duration:** 1 week
**When to use:** Phase 4, Days 340–360
**Difficulty:** Intermediate

**Why this is perfect for you:**
Supabase is PostgreSQL as a service with built-in authentication, real-time subscriptions, and storage — everything a solo founder needs to ship an AI product without managing backend infrastructure. It has a generous free tier and an excellent Python client. For indie hackers and early-stage startups in India, Supabase eliminates the need for a backend engineer.

**What to cover:**
- Setting up a project and connecting from Python
- Creating tables and running queries
- Supabase Auth — email/password and Google OAuth
- Row Level Security (protect user data)
- Python client library (`supabase-py`)
- Storing and retrieving user chat history for your AI apps

---

### 📗 Resource 6.5 — Docker Official Getting Started

**Link:** docs.docker.com/get-started/
**Type:** Official tutorial
**Duration:** 3–5 days
**When to use:** Phase 4, Days 330–340
**Difficulty:** Intermediate

**Why this is perfect for you:**
Docker is how you package your AI application so it runs identically on any computer, server, or cloud platform. Every AI startup uses Docker. The "works on my machine" problem disappears. Learning Docker early means your projects can be deployed to any cloud provider without rewriting anything — a huge practical advantage when you're pitching to investors or onboarding your first users.

**What to cover in order:**
1. What containers are and why they matter (1 hour reading)
2. Your first Dockerfile for a Python app
3. `docker build`, `docker run`, `docker ps`, `docker logs`
4. Multi-stage builds for smaller images
5. `docker-compose` for running FastAPI + database together
6. Pushing an image to Docker Hub
7. Deploying your container to Railway or Render

**Pro Tips:**
- Build a Docker image for each project from Phase 4 onwards — make it a habit.
- Learn `docker-compose` early — it's how you run multiple services (API + database + Redis) locally.
- The official "Docker in 100 Seconds" video by Fireship on YouTube is the best 2-minute intro.

---

### 📗 Resource 6.6 — Full Stack Deep Learning (2022 Course)

**Link:** fullstackdeeplearning.com/course/2022/
**Type:** Free recorded course
**Duration:** 2–3 weeks
**When to use:** Phase 4, Days 295–330
**Difficulty:** Intermediate → Advanced

**Why this is perfect for you:**
FSDL teaches everything that university ML courses skip — how to actually ship ML systems. Testing ML code, data labeling pipelines, monitoring models in production, infrastructure choices, team workflows. This is what separates a machine learning student from a machine learning engineer. As someone who wants to build AI products and a startup, this course will save you from expensive beginner mistakes in production.

**Lectures to prioritize:**

| Lecture | Topic | Watch During |
|---------|-------|-------------|
| 1 | Course Vision and When to Use ML | Phase 4, Day 295 |
| 2 | Development Infrastructure & Tooling | Phase 4, Day 300 |
| 3 | Troubleshooting & Testing | Phase 4, Day 305 |
| 5 | ML Projects | Phase 4, Day 310 |
| 6 | Infrastructure & Tooling | Phase 4, Day 315 |
| 8 | Data Management | Phase 4, Day 320 |
| 9 | Experiment Management | Phase 4, Day 325 |
| 11 | Deployment & Monitoring | Phase 4, Day 330 |

---

## 🚀 SECTION 7 — MLOps & Deployment

---

### 📗 Resource 7.1 — Weights & Biases (W&B) Documentation & Courses

**Link:** docs.wandb.ai + wandb.ai/courses
**Type:** Documentation + free courses
**Duration:** 1 week
**When to use:** Phase 3, Day 260+
**Difficulty:** Intermediate

**Why this is perfect for you:**
W&B is the industry standard tool for tracking ML experiments — used by OpenAI, DeepMind, and nearly every serious ML team. When you're training models, you need to track: which hyperparameters you used, what your loss curve looked like, how different model versions compare. Without this, you're flying blind. The free tier is sufficient for all your learning projects.

**What to learn:**
- `wandb.init()` and `wandb.log()` — 2 lines to track any training run
- Dashboard visualization
- Hyperparameter sweeps with W&B Sweeps
- Model versioning with W&B Artifacts
- Free "MLOps Course" on their website (6 modules)

---

### 📗 Resource 7.2 — Designing Machine Learning Systems (Book — Chip Huyen)

**Link:** Buy on Amazon/Flipkart ~₹700
**Type:** Book
**Duration:** Read over 4–6 weeks
**When to use:** Phase 4, Days 295–370
**Difficulty:** Intermediate → Advanced

**Why this is perfect for you:**
Chip Huyen worked at NVIDIA, Snorkel AI, and is a Stanford ML lecturer. This book is the manual for building ML systems that actually work in production — not in a notebook. It covers data pipelines, feature engineering at scale, model deployment, monitoring, and the organizational challenges of ML teams. As someone building AI products, this book will prevent you from making the expensive mistakes most self-taught engineers make when they first try to "productionize" their models.

**Read it in this order:**

| Chapter | Read During |
|---------|------------|
| Ch 1–2: ML in Production | Phase 4, Day 295 |
| Ch 3: Data Engineering | Phase 4, Day 310 |
| Ch 4: Feature Engineering | Phase 4, Day 320 |
| Ch 5: Model Development | Phase 4, Day 330 |
| Ch 6: Model Evaluation | Phase 4, Day 340 |
| Ch 7: Deployment | Phase 4, Day 350 |
| Ch 8: Data Distribution Shifts | Phase 4, Day 360 |
| Ch 9: Continual Learning | Phase 4, Day 370 |

---

### 📗 Resource 7.3 — Modal Documentation

**Link:** modal.com/docs
**Type:** Official documentation
**Duration:** 2–3 days
**When to use:** Phase 4, Days 395–420
**Difficulty:** Intermediate

**Why this is perfect for you:**
Modal lets you run GPU-intensive workloads (like LLM inference) serverlessly with just a few lines of Python — no cloud account setup, no Kubernetes, no DevOps. For a solo founder who wants to deploy an LLM-powered product without a huge cloud bill or a DevOps engineer, Modal is a game changer. The free tier gives you $30/month of compute.

**What to learn:**
- Running Python functions in the cloud with `@app.function`
- GPU access with `gpu="A10G"`
- Serving a FastAPI app on Modal
- Running LLM inference serverlessly
- Scheduled jobs and webhooks

---

### 📗 Resource 7.4 — GitHub Actions Documentation

**Link:** docs.github.com/en/actions
**Type:** Official documentation
**Duration:** 1 week
**When to use:** Phase 4, Days 360–380
**Difficulty:** Intermediate

**Why this is perfect for you:**
GitHub Actions automates your deployment pipeline — every time you push code, it runs tests, builds Docker images, and deploys to your server automatically. This is CI/CD (Continuous Integration / Continuous Deployment) and every professional software team uses it. For a solo founder, it means you can ship code to production with confidence and zero manual deployment steps.

**What to learn:**
- Creating your first workflow file (`.github/workflows/main.yml`)
- Running Python tests on every push
- Building and pushing a Docker image on merge to main
- Deploying to a cloud provider automatically
- Secrets management (API keys in GitHub Secrets)

---

## 🌱 SECTION 8 — Startup & Product Building

---

### 📗 Resource 8.1 — The Mom Test (Book — Rob Fitzpatrick)

**Link:** momtestbook.com — buy on Amazon/Flipkart ~₹400
**Type:** Book (short — 130 pages)
**Duration:** Read in 1 weekend
**When to use:** Phase 5, Day 421 — but honestly, read it in Month 3
**Difficulty:** Beginner

**Why this is perfect for you:**
The Mom Test is the most important book for anyone building a product. It teaches you how to talk to potential users in a way that gets honest feedback instead of polite lies. Most startups fail because founders build things nobody wants. This book gives you the exact questions to ask, how to ask them, and how to validate ideas before writing a single line of code. Since you want to build an AI startup, this should be read early — before you get attached to an idea.

**Key concepts to apply immediately:**
- Ask about past behavior, not future intentions ("Would you use this?" is a bad question)
- Talk about their life, not your idea
- "That's so cool!" means nothing — dig for specifics
- Bad data: compliments, hypotheticals, generic statements
- Good data: specific stories, current behavior, money already spent

---

### 📗 Resource 8.2 — Y Combinator Startup Library

**Link:** ycombinator.com/library
**Type:** Free articles and videos
**Duration:** Read 2–3 pieces per week from Phase 5 onwards
**When to use:** Phase 5, Day 421+ (but start reading in Phase 4)
**Difficulty:** Beginner

**Why this is perfect for you:**
Y Combinator has funded Airbnb, Stripe, Dropbox, and hundreds of other companies. Their library contains the best free startup education available — from Paul Graham's famous essays to recorded lectures from YC's internal curriculum. Since your goal includes potentially founding an AI startup, reading the YC library is like getting access to the startup playbook that most founders only discover after their first failed company.

**Must-read pieces:**

| Piece | Read During |
|-------|------------|
| Do Things That Don't Scale — Paul Graham | Phase 4, Day 350 |
| How to Get Startup Ideas — Paul Graham | Phase 5, Day 421 |
| Before the Startup — Paul Graham | Phase 4, Day 370 |
| Default Alive or Default Dead? | Phase 5, Day 435 |
| The 18 Mistakes That Kill Startups | Phase 5, Day 440 |
| How to Talk to Users (YC video) | Phase 5, Day 421 |
| Startup = Growth — Paul Graham | Phase 5, Day 425 |

---

### 📗 Resource 8.3 — Indie Hackers

**Link:** indiehackers.com
**Type:** Community + interviews
**Duration:** Read 3–5 interviews per week from Phase 4 onwards
**When to use:** Phase 4, Day 330+
**Difficulty:** Beginner

**Why this is perfect for you:**
Indie Hackers interviews founders who built profitable products — mostly solo or with tiny teams — and asks them to share revenue numbers, how they got users, what went wrong. Since your path involves building AI products independently before (potentially) raising funding, these interviews show you what's actually achievable for a solo builder in 12–24 months. Many of the most inspiring stories are from people who started exactly where you are.

**How to use it:**
- Filter by "AI" and "SaaS" — read 3 interviews per week
- Pay attention to: how they found their idea, how they got first users, what almost killed them
- The forum is active — post updates about your own journey there
- The "Products" section shows what people have built and their revenue — grounding for realistic expectations

---

### 📗 Resource 8.4 — Lenny's Newsletter (Substack)

**Link:** lennysnewsletter.com
**Type:** Paid newsletter (free tier available)
**Duration:** Read weekly
**When to use:** Phase 4 onwards
**Difficulty:** Intermediate

**Why this is perfect for you:**
Lenny Rachitsky is a former Airbnb PM and one of the most respected product thinkers in the industry. His newsletter covers growth, retention, product strategy, and building teams — all the things you'll face as an AI founder. The free tier gives you enough content to learn the fundamentals. His "How the best PMs think" and "Growth" content is directly applicable to building and growing AI products.

**Free articles worth bookmarking:**
- How to find product-market fit
- The most important metrics for SaaS
- How to price your product
- Building a growth machine

---

### 📗 Resource 8.5 — iStart Rajasthan & iStart MP

**Link:** istart.rajasthan.gov.in + startupindia.gov.in
**Type:** Government programs
**When to use:** Phase 5, Day 460+
**Difficulty:** Beginner

**Why this is perfect for you:**
You're in Indore — Madhya Pradesh has one of the most active state startup ecosystems in India with iStart MP. These government programs offer: free co-working space, seed funding (up to ₹10–30 lakhs), mentorship, legal/accounting support, and connections to angel networks. Many AI startups founded by students in Tier-2 cities have gotten their initial funding through state programs. Apply early — the process takes time.

**Steps to take:**
- Register on Startup India portal (startupindia.gov.in) — takes 30 minutes
- Apply to iStart MP recognition
- Check IIM Indore's incubation centre — they accept external founders
- Connect with NASSCOM 10,000 Startups — free resources and visibility
- Follow @StartupIndia on Twitter for program announcements

---

## 📺 SECTION 9 — YouTube Channels (Subscribe to All)

---

| Channel | Why Subscribe | Watch From | Speed |
|---------|--------------|-----------|-------|
| **Andrej Karpathy** | The deepest technical explanations of neural networks and LLMs from someone who helped build GPT. His "Neural Networks Zero to Hero" series is irreplaceable. | Phase 3 | 1x |
| **3Blue1Brown** | The best math visualization content ever made. Linear algebra and calculus become intuitive instead of abstract. Mandatory before Phase 2. | Phase 1 | 1x |
| **StatQuest with Josh Starmer** | Every ML algorithm explained from first principles with zero assumed knowledge. Best free statistics education available. | Phase 1 | 1.25x |
| **Yannic Kilcher** | Deep research paper walkthroughs and AI news commentary. He reads papers you need to understand and explains them clearly. | Phase 3 | 1x |
| **Sentdex** | Practical Python and ML projects. His series on building things from scratch in Python is excellent for solidifying fundamentals. | Phase 1–2 | 1.5x |
| **Two Minute Papers** | 2-minute summaries of the most important AI research papers. Keeps you current without reading full papers daily. | All phases | 1.25x |
| **AI Explained** | The best analysis of LLM capabilities, limitations, and news. For staying current on the state of AI. | Phase 3+ | 1.25x |
| **Sebastian Raschka** | Ex-Apple ML researcher, now a professor. His explanations of LLM papers and training techniques are unusually clear and practical. | Phase 3+ | 1x |
| **Fireship** | Fast, entertaining 100-second explainers on every tech tool. When you need a quick overview of Docker, Next.js, or any new tech. | Phase 4 | 1.5x |
| **Corey Schafer** | The most consistently excellent Python tutorials on YouTube. OOP, decorators, generators — everything intermediate Python. | Phase 1 | 1.25x |

---

## 📰 SECTION 10 — Newsletters & Blogs

---

| Newsletter/Blog | Link | Why Read It | Read How Often |
|----------------|------|------------|---------------|
| **The Batch** (deeplearning.ai) | deeplearning.ai/the-batch | Andrew Ng's weekly newsletter. Best signal-to-noise ratio for AI news. Covers research and industry in simple language. | Every week |
| **Towards Data Science** | towardsdatascience.com | Community blog with 1000s of practical ML/AI tutorials. Best for implementation-level articles. | 2–3 articles/week |
| **Sebastian Raschka's Newsletter** | magazine.sebastianraschka.com | Deep LLM paper summaries and practical tips. One of the few newsletters that goes technically deep. | Every week |
| **Hugging Face Blog** | huggingface.co/blog | First to know about new open-source models, datasets, and tools. Essential for staying current. | Every week |
| **Anthropic Research** | anthropic.com/research | Deep thinking on how LLMs work and safety. Unusually honest and technically rigorous. | Monthly |
| **Lenny's Newsletter** | lennysnewsletter.com | Product strategy, growth, and building teams. For your startup phase. | Every week |
| **Paul Graham Essays** | paulgraham.com/articles.html | The most important startup thinking available for free. Read slowly, not all at once. | 1 essay/week |
| **Papers With Code** | paperswithcode.com | Every significant ML paper with its open-source code implementation. Your research compass. | Browse weekly |

---

## 💻 SECTION 11 — Practice Platforms

---

| Platform | Link | What to Practice | When to Start |
|----------|------|-----------------|--------------|
| **Kaggle** | kaggle.com | Competitions, datasets, notebooks. The best place to apply ML to real data. Enter your first competition in Phase 2. | Phase 1 (micro-courses), Phase 2 (competitions) |
| **LeetCode** | leetcode.com | Python data structures and algorithms. Do 3 easy/medium problems per week. Not the focus but builds coding fluency. | Phase 1, Day 12 |
| **HackerRank** | hackerrank.com | Python challenges and ML challenges. Good for structured daily coding practice. | Phase 1, Day 12 |
| **Google Colab** | colab.research.google.com | Free GPU notebook environment. Run all deep learning and LLM experiments here. | Phase 3 onwards |
| **Hugging Face Spaces** | huggingface.co/spaces | Deploy Gradio demos for free. Share your ML projects with the world. | Phase 3, Day 265 |
| **Replit** | replit.com | Quick Python prototyping with no setup. Good for testing ideas fast. | Phase 1 onwards |

---

## 👥 SECTION 12 — Communities to Join

---

| Community | Platform | Why Join | How to Participate |
|-----------|----------|---------|-------------------|
| **Hugging Face Discord** | discord.gg/huggingface | 100k+ AI practitioners. Best place for LLM and open-source AI questions. | Join the #beginners channel first. Ask specific questions with code. |
| **fast.ai Forums** | forums.fast.ai | Jeremy Howard and thousands of practical deep learning learners. Excellent for course-related questions. | Post your project work. Get feedback. Help others in your phase. |
| **r/learnmachinelearning** | reddit.com | 600k+ beginners. Great for motivation, project feedback, and resource recommendations. | Post your weekly progress. Ask questions. Share project links. |
| **r/MachineLearning** | reddit.com | Research discussions and paper links. More advanced — better for Phase 3+. | Read and bookmark. Don't worry about not understanding everything early on. |
| **AI Engineer Foundation Discord** | discord.gg/AIEngineers | The community for AI application builders. Most relevant to your startup goals. | Share what you're building. Find co-founders and early users here. |
| **Indie Hackers Community** | indiehackers.com | Solo founders sharing revenue, growth, and struggles. Directly relevant to your Phase 5 goals. | Post your build updates. Comment on others' progress. Find accountability partners. |

---

## 📖 SECTION 13 — Books (Full List)

---

| Book | Author | Read During | Why |
|------|--------|------------|-----|
| **Hands-On ML with Scikit-Learn, Keras & TF** | Aurélien Géron | Phase 2–3 | The definitive practical ML book. You will reference this for years. |
| **Deep Learning** | Goodfellow, Bengio, Courville | Phase 3+ (reference) | The mathematical bible of deep learning. Free at deeplearningbook.org. Don't read cover to cover — use as reference. |
| **Designing ML Systems** | Chip Huyen | Phase 4 | How ML works in production. Essential for building real AI products. |
| **The Mom Test** | Rob Fitzpatrick | Phase 4–5 | How to validate ideas by talking to users. Short (130 pages) but career-changing. |
| **Zero to One** | Peter Thiel | Phase 5 | Contrarian startup thinking. Read once slowly. |
| **The Lean Startup** | Eric Ries | Phase 5 | Build-measure-learn loop for startups. Still the best startup methodology book. |
| **Automate the Boring Stuff** | Al Sweigart | Phase 1 | Free online. Python for automation and real projects. Builds builder instinct early. |
| **Python Crash Course** | Eric Matthes | Phase 1 (backup) | Best Python beginner book if CS50P feels too fast. Buy only if needed. |

---

## 🇮🇳 SECTION 14 — India-Specific Resources

---

### 📗 Resource 14.1 — IIT Madras BSc in Data Science and Applications

**Link:** onlinedegree.iitm.ac.in
**Why relevant to you:** IIT Madras offers a legitimately credentialed BSc in Data Science that's fully online and significantly more affordable than a traditional degree (₹20,000–40,000/year). If you want formal credentialing alongside your self-taught journey, this is the most respected option in India. Alumni are placed at top companies.

---

### 📗 Resource 14.2 — NPTEL AI/ML Courses

**Link:** nptel.ac.in
**Why relevant to you:** NPTEL is IIT/IISc faculty teaching free courses online. Several AI/ML courses are available and the certifications are respected by Indian employers. Courses by Prof. Mitesh Khapra (IIT Madras) on Deep Learning and NLP are particularly excellent and taught with a focus on modern techniques.

**Best NPTEL courses for your path:**
- Deep Learning — Prof. Mitesh Khapra (IIT Madras)
- Introduction to Machine Learning — Prof. Sudeshna Sarkar (IIT Kharagpur)
- Natural Language Processing — IIT Bombay

---

### 📗 Resource 14.3 — Startup India & iStart MP

**Link:** startupindia.gov.in + istart.mp.gov.in
**Why relevant to you:** You are in Indore. Madhya Pradesh's iStart program is specifically designed for founders in the state and offers funding, mentorship, and co-working. Register early — even if you're not ready to apply, being in their system gets you notified about events, funding calls, and networking opportunities.

**Immediate actions:**
- Register on Startup India (free, 20 minutes)
- Follow iStart MP on social media for events
- Attend at least one startup event in Indore every 2 months

---

### 📗 Resource 14.4 — IIM Indore Incubation Centre

**Link:** iimidr.ac.in/research/incubation/
**Why relevant to you:** You are in Indore. IIM Indore's incubation centre accepts external founders (you don't have to be an IIM student). The network, mentors, and credibility of being an IIM Indore incubated startup is significant in India. Apply when you have a working MVP.

---

### 📗 Resource 14.5 — AI4Bharat

**Link:** ai4bharat.iitm.ac.in
**Why relevant to you:** AI4Bharat is an IIT Madras initiative building AI tools for Indian languages. If you want to build AI products for regional language users (Hindi, which is massive in MP), their open-source models and datasets are exactly what you need. Opportunities to contribute to open source while building domain expertise in India-specific AI.

---

## 📅 Resource Usage Timeline Summary

| Phase | Primary Resources | Secondary Resources |
|-------|------------------|-------------------|
| Phase 0 (Days 1–14) | CS50P, Kaggle Python, Kaggle Pandas | Automate the Boring Stuff Ch 1–6 |
| Phase 1 (Days 15–98) | CS50P, Automate the Boring Stuff, 3Blue1Brown (Linear Algebra + Calculus), StatQuest (Statistics) | Corey Schafer YouTube, Real Python, Mathematics for ML Coursera |
| Phase 2 (Days 99–196) | Andrew Ng ML Specialization, Hands-On ML Book, Kaggle Competitions | StatQuest (ML algorithms), fast.ai, Kaggle ML micro-courses |
| Phase 3 (Days 197–294) | Karpathy Zero to Hero, Deep Learning Specialization, PyTorch Docs, Hugging Face NLP Course | Jay Alammar Blog, d2l.ai, DeepLearning.AI Short Courses |
| Phase 4 (Days 295–420) | DeepLearning.AI Short Courses (RAG, Agents), FastAPI Docs, Streamlit Docs, LangChain Docs | FSDL 2022, Vercel AI SDK, Supabase Docs, Designing ML Systems |
| Phase 5 (Days 421+) | The Mom Test, YC Library, Indie Hackers, iStart MP | Lenny's Newsletter, Paul Graham Essays |

---

*Resource library compiled for: AI/ML journey, student to expert to founder*
*Profile: Python basics + Java, hackathon experience, Indore India, startup-minded*
*Last curated: 2025 — verify links are current before using*
