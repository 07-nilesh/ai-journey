# 🤖 Complete AI / ML Roadmap — From Beginner to Expert

> **Your goal:** Student / Fresher with Python basics → AI Engineer → AI Product Builder → Founder
> **Total timeline:** ~18–24 months of focused, consistent learning
> **Update this page:** Check off tasks as you complete them. Review weekly.

---

## 📌 How to Use This Roadmap

- Go **phase by phase** — don't jump ahead
- Spend **2–4 hours daily** on learning + building
- Every phase ends with a **project** — build it, push it to GitHub
- Track progress using the checkboxes below
- **Build in public** — post weekly updates on LinkedIn / Twitter

---

## 🗺️ Overview — The Full Path

| Phase | Name | Duration | Goal |
|-------|------|----------|------|
| 0 | Pre-flight checklist | Week 1–2 | Set up your environment |
| 1 | Python & math foundation | Month 1–4 | Write clean Python, understand the math |
| 2 | Core machine learning | Month 4–8 | Train and evaluate real ML models |
| 3 | Deep learning & LLMs | Month 8–12 | Build with neural networks and transformers |
| 4 | AI product engineering | Month 12–18 | Ship full-stack AI products |
| 5 | Startup & go to market | Month 18+ | Build your company |

---

## ⚙️ Phase 0 — Pre-Flight Checklist (Week 1–2)

> Set up everything before you write a single line of AI code.

### 🖥️ Tools to Install

- [ ] **Python 3.11+** — python.org (don't use older versions)
- [ ] **VS Code** — code.visualstudio.com (best free editor)
- [ ] **VS Code Extensions:** Python, Pylance, Jupyter, GitLens
- [ ] **Git** — git-scm.com
- [ ] **GitHub account** — github.com (this is your portfolio, treat it seriously)
- [ ] **Anaconda or Miniconda** — for managing Python environments
- [ ] **Jupyter Notebook** — comes with Anaconda or `pip install notebook`
- [ ] **Google Colab account** — colab.research.google.com (free GPU in the cloud)

### 📁 File & Folder System

Create this folder structure on your computer:

```
/ai-journey/
  /phase-1-python/
  /phase-2-ml/
  /phase-3-deep-learning/
  /phase-4-products/
  /projects/
  /notes/
```

### 🌐 Accounts to Create

- [ ] GitHub (portfolio)
- [ ] Kaggle (competitions + datasets)
- [ ] Hugging Face (models + spaces)
- [ ] Google Colab (free GPU)
- [ ] LinkedIn (build in public)
- [ ] Twitter/X (AI community is very active here)
- [ ] Notion (this document!)

### 📖 Daily Habits to Build Now

- [ ] Read 1 AI article every morning (follow Towards Data Science, The Batch by deeplearning.ai)
- [ ] Code for at least 1 hour every day — no exceptions
- [ ] Keep a learning journal — write 3 sentences daily about what you learned
- [ ] Join Discord communities: Hugging Face, fast.ai, AI Engineer Foundation

---

## 🐍 Phase 1 — Python & Math Foundation (Month 1–4)

> You already know basics. Now make Python your superpower.

### 📘 Part 1A — Intermediate Python (Month 1–2)

**Goal:** Write clean, professional Python code that data scientists and engineers actually use.

#### Topics to Master

**Core Python (Week 1–2)**
- [ ] List comprehensions and generator expressions
- [ ] Lambda functions, `map()`, `filter()`, `zip()`
- [ ] `*args` and `**kwargs`
- [ ] Decorators (understand what `@` means)
- [ ] Context managers (`with` statements)
- [ ] File I/O — reading and writing CSV, JSON, TXT files
- [ ] Error handling — `try / except / finally`
- [ ] f-strings and string formatting

**Object Oriented Python (Week 3)**
- [ ] Classes, `__init__`, `self`
- [ ] Inheritance and method overriding
- [ ] Dunder methods (`__str__`, `__len__`, `__repr__`)
- [ ] When to use classes vs functions

**Python for Data (Week 4–6)**
- [ ] **NumPy** — arrays, broadcasting, vectorized operations
  - Creating arrays: `np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`
  - Array operations: slicing, indexing, reshaping, transposing
  - Math ops: dot product, matrix multiply (`@`), `np.sum`, `np.mean`, `np.std`
- [ ] **Pandas** — the most used data tool in AI
  - Series and DataFrames — creating and loading data
  - `read_csv`, `read_json`, `to_csv`
  - Selecting, filtering, sorting: `.loc`, `.iloc`, boolean masking
  - Handling missing values: `dropna`, `fillna`, `isnull`
  - GroupBy and aggregations: `groupby`, `agg`, `pivot_table`
  - Merging and joining DataFrames
- [ ] **Matplotlib & Seaborn** — visualizing data
  - Line plots, bar charts, scatter plots, histograms
  - Heatmaps (very important for ML)
  - Subplots and figure formatting

**Advanced Python (Week 7–8)**
- [ ] Virtual environments (`conda create`, `pip install`, `requirements.txt`)
- [ ] Modules and packages — building your own
- [ ] `collections` module: `Counter`, `defaultdict`, `namedtuple`
- [ ] `itertools` module
- [ ] Type hints: `def func(x: int) -> str:`
- [ ] Writing and running unit tests with `pytest`

#### 📚 Resources for Phase 1A

| Resource | Type | Cost | Link |
|----------|------|------|------|
| CS50P (Python) — Harvard | Video Course | Free | cs50.harvard.edu/python |
| Python for Everybody — Dr. Chuck | Video Course | Free | coursera.org |
| Automate the Boring Stuff | Book | Free online | automatetheboringstuff.com |
| 100 Days of Code Python | Udemy | Paid (~₹500 sale) | udemy.com |
| Real Python | Articles | Free + Paid | realpython.com |
| Kaggle Learn Python | Micro-course | Free | kaggle.com/learn/python |
| Kaggle Learn Pandas | Micro-course | Free | kaggle.com/learn/pandas |

#### ✅ Phase 1A Project — Data Analysis Project

**Project: "Analyze India's startup ecosystem data"**
- Download a dataset from Kaggle (Indian startups, stock market, cricket stats — pick one you care about)
- Clean it with Pandas (handle missing values, remove duplicates)
- Create 5 meaningful visualizations with Matplotlib/Seaborn
- Write a 500-word summary of what you found
- Push to GitHub with a proper README

---

### 📐 Part 1B — Math for Machine Learning (Month 2–4)

> You don't need a math degree. You need enough to understand *why* algorithms work.

**Linear Algebra (Most Important)**
- [ ] Vectors — what they are, addition, dot product, magnitude
- [ ] Matrices — addition, multiplication, transpose
- [ ] Matrix-vector multiplication (the heart of neural networks)
- [ ] Identity matrix and inverse matrix
- [ ] Eigenvalues and eigenvectors (needed for PCA)
- [ ] Understanding dimensions — (batch_size, features) shapes in ML

**Statistics & Probability**
- [ ] Mean, median, mode, variance, standard deviation
- [ ] Normal distribution (Gaussian) — why it appears everywhere
- [ ] Probability basics — P(A), P(A|B), Bayes' theorem
- [ ] Covariance and correlation
- [ ] Hypothesis testing, p-values (basic understanding)
- [ ] Train/validation/test split — why we do it

**Calculus (Only What You Need)**
- [ ] What a derivative is — rate of change
- [ ] The chain rule — this powers backpropagation
- [ ] Gradient — derivative in multiple dimensions
- [ ] What a gradient means geometrically (going uphill/downhill)
- [ ] You don't need to compute complex integrals — just understand gradients

**Key Concept: Gradient Descent**
This is how every ML model learns. Understand this deeply:
- Loss function — a number that measures how wrong your model is
- Gradient — points in the direction of steepest increase
- We go opposite to the gradient to reduce loss
- Learning rate — how big a step we take
- Iterations until convergence

#### 📚 Resources for Phase 1B Math

| Resource | Type | Cost |
|----------|------|------|
| 3Blue1Brown — Essence of Linear Algebra | YouTube | Free |
| 3Blue1Brown — Essence of Calculus | YouTube | Free |
| StatQuest with Josh Starmer | YouTube | Free |
| Khan Academy Linear Algebra | Videos | Free |
| Mathematics for Machine Learning (Coursera) | Course | Free audit |
| Practical Deep Learning (fast.ai) covers math in context | Course | Free |

> **Tip:** Don't spend months on pure math. Learn it in context — when you hit a concept in ML you don't understand, go learn just that math. Don't try to do all math before touching ML code.

---

## 🤖 Phase 2 — Core Machine Learning (Month 4–8)

> Build real ML models. Understand what's happening mathematically AND in code.

### 📘 Part 2A — Classical Machine Learning

**Supervised Learning**
- [ ] Linear Regression — predicting continuous values
  - Ordinary Least Squares
  - Gradient descent implementation
  - R² score, MSE, RMSE
- [ ] Logistic Regression — predicting categories
  - Sigmoid function
  - Cross-entropy loss
  - Decision boundary
- [ ] Decision Trees
  - Gini impurity and entropy
  - Overfitting and pruning
- [ ] Random Forests
  - Ensemble learning
  - Bagging and feature importance
- [ ] Gradient Boosting — XGBoost, LightGBM (industry standard)
  - Why boosting beats a single model
  - Hyperparameter tuning
- [ ] Support Vector Machines
  - Margin and support vectors
  - Kernel trick
- [ ] K-Nearest Neighbors — intuition and limitations

**Unsupervised Learning**
- [ ] K-Means Clustering
  - Elbow method for choosing K
  - Limitations of K-Means
- [ ] Hierarchical Clustering
- [ ] PCA (Principal Component Analysis) — dimensionality reduction
  - Why high dimensions are a problem
  - Explained variance ratio
- [ ] t-SNE and UMAP — visualizing high-dimensional data

**Core ML Concepts — Master These**
- [ ] Overfitting vs underfitting — the most important concept in ML
- [ ] Bias-variance tradeoff
- [ ] Regularization — L1 (Lasso), L2 (Ridge)
- [ ] Train/validation/test split — why all three
- [ ] Cross-validation (k-fold)
- [ ] Feature engineering — creating new features from existing ones
- [ ] Feature scaling — StandardScaler, MinMaxScaler
- [ ] Handling imbalanced datasets — SMOTE, class weights
- [ ] Evaluation metrics:
  - Classification: Accuracy, Precision, Recall, F1-score, ROC-AUC, Confusion Matrix
  - Regression: MAE, MSE, RMSE, R²
- [ ] Hyperparameter tuning — GridSearchCV, RandomizedSearchCV, Optuna

**Scikit-Learn — The Standard ML Library**
- [ ] The `.fit()` / `.predict()` / `.score()` pattern
- [ ] `Pipeline` — chain preprocessing + model
- [ ] `ColumnTransformer` — apply different transforms to different columns
- [ ] `GridSearchCV` and `RandomizedSearchCV`
- [ ] Model persistence — `joblib.dump` and `joblib.load`

#### 📚 Resources for Phase 2A

| Resource | Type | Cost |
|----------|------|------|
| Machine Learning Specialization — Andrew Ng (Coursera) | Course | Free audit |
| Hands-On ML with Scikit-Learn & TensorFlow — Aurélien Géron | Book | Buy it (~₹600) |
| Kaggle Learn — ML courses | Micro-courses | Free |
| StatQuest — all ML videos | YouTube | Free |
| fast.ai Practical ML for Coders | Course | Free |

#### ✅ Phase 2A Project — ML Competition on Kaggle

**Project: Kaggle Titanic + House Prices**
- Complete the Titanic competition (binary classification)
- Complete House Prices competition (regression)
- Try to reach top 25% leaderboard on each
- Document your feature engineering decisions
- Write a Kaggle notebook explaining your approach

---

### 📘 Part 2B — Data Engineering for ML

Often skipped by beginners — don't skip it.

- [ ] SQL for data extraction — SELECT, JOIN, GROUP BY, subqueries
- [ ] Data cleaning patterns — outlier detection, imputation strategies
- [ ] Working with different data formats — CSV, JSON, Parquet, HDF5
- [ ] Web scraping with `BeautifulSoup` and `requests`
- [ ] APIs — calling REST APIs, handling JSON responses
- [ ] Basic data pipelines — reading from source → cleaning → saving
- [ ] Understanding train/test leakage — a common and costly mistake

---

## 🧠 Phase 3 — Deep Learning & LLMs (Month 8–12)

> This is the core of modern AI. Neural networks, transformers, and large language models.

### 📘 Part 3A — Neural Networks & Deep Learning

**Foundations**
- [ ] What a neuron is — weighted sum + activation function
- [ ] Layers — input, hidden, output
- [ ] Forward pass — how prediction works
- [ ] Loss function for regression (MSE) and classification (cross-entropy)
- [ ] Backpropagation — chain rule applied to a network
  - Understand this conceptually, not just mathematically
- [ ] Gradient descent variants — SGD, Momentum, Adam (use Adam by default)
- [ ] Learning rate schedules — step decay, cosine annealing
- [ ] Batch size — effect on training stability and speed

**Architectures**
- [ ] Fully Connected / Dense Networks (MLPs)
- [ ] Convolutional Neural Networks (CNNs) — for images
  - Convolution operation
  - Pooling layers
  - Famous architectures: LeNet, VGG, ResNet, EfficientNet
- [ ] Recurrent Neural Networks (RNNs) — for sequences
  - Vanishing gradient problem
  - LSTMs and GRUs — how they solve it
- [ ] **Transformers — THE most important architecture today**
  - Attention mechanism — "what should I pay attention to?"
  - Self-attention vs cross-attention
  - Multi-head attention
  - Positional encoding
  - Encoder vs Decoder
  - BERT (encoder) vs GPT (decoder) architectures

**Training Tricks**
- [ ] Dropout — regularization for deep networks
- [ ] Batch Normalization — stabilizes training
- [ ] Early stopping — prevent overfitting
- [ ] Data augmentation — artificially expand your dataset
- [ ] Transfer learning — use a pre-trained model, fine-tune on your data
- [ ] Weight initialization — why it matters

**PyTorch — The Standard Deep Learning Framework**
- [ ] Tensors — PyTorch's version of NumPy arrays
- [ ] `autograd` — automatic differentiation
- [ ] `nn.Module` — building blocks for neural networks
- [ ] Custom Dataset and DataLoader
- [ ] Writing a training loop from scratch
- [ ] Saving and loading model weights (`.pth` files)
- [ ] GPU training — `.to(device)`, `CUDA`
- [ ] TorchVision for computer vision tasks

#### 📚 Resources for Phase 3A

| Resource | Type | Cost |
|----------|------|------|
| Deep Learning Specialization — Andrew Ng (Coursera) | Course | Free audit |
| fast.ai Practical Deep Learning Part 1 | Course | Free |
| Neural Networks: Zero to Hero — Andrej Karpathy | YouTube | Free |
| PyTorch Official Tutorials | Docs | Free |
| Dive into Deep Learning (d2l.ai) | Book | Free online |
| The Illustrated Transformer — Jay Alammar | Blog | Free |

> **Must Watch:** Andrej Karpathy's "Let's build GPT from scratch" on YouTube. This alone will teach you more than most courses.

---

### 📘 Part 3B — Large Language Models (LLMs)

This is what's changing the world right now.

**Understanding LLMs**
- [ ] What a language model is — predicting the next token
- [ ] Tokenization — how text becomes numbers (BPE, WordPiece)
- [ ] Pre-training — learning on massive internet text
- [ ] Fine-tuning — adapting to specific tasks
- [ ] RLHF — Reinforcement Learning from Human Feedback (how ChatGPT is trained)
- [ ] Instruction tuning — why models follow instructions
- [ ] Context window — why it matters and its limitations
- [ ] Temperature, Top-P, Top-K — controlling generation randomness
- [ ] Hallucination — why LLMs make things up and how to reduce it

**Important LLM Families to Know**
- [ ] GPT series (OpenAI) — GPT-3.5, GPT-4, GPT-4o
- [ ] Claude series (Anthropic) — Haiku, Sonnet, Opus
- [ ] Llama series (Meta) — open source, can run locally
- [ ] Gemini (Google)
- [ ] Mistral — efficient open source models
- [ ] Qwen, Phi — small but capable models

**Prompt Engineering (Practical & Important)**
- [ ] Zero-shot prompting
- [ ] Few-shot prompting — giving examples in the prompt
- [ ] Chain-of-thought (CoT) — "think step by step"
- [ ] System prompts vs user prompts
- [ ] Structured output — getting JSON from LLMs
- [ ] ReAct pattern — reasoning + acting
- [ ] Role prompting

**Fine-tuning LLMs**
- [ ] When to fine-tune vs prompt engineer
- [ ] Supervised Fine-Tuning (SFT)
- [ ] LoRA and QLoRA — fine-tuning on consumer hardware
- [ ] PEFT library from Hugging Face
- [ ] Creating a fine-tuning dataset
- [ ] Evaluating fine-tuned models

**Hugging Face Ecosystem**
- [ ] `transformers` library — loading and using models
- [ ] `datasets` library — loading and processing datasets
- [ ] `tokenizers` library
- [ ] `peft` — parameter-efficient fine-tuning
- [ ] `trl` — training with reinforcement learning
- [ ] Model Hub — finding pre-trained models
- [ ] Hugging Face Spaces — deploying demos for free

#### 📚 Resources for Phase 3B

| Resource | Type | Cost |
|----------|------|------|
| Hugging Face NLP Course | Course | Free |
| LLM University — Cohere | Course | Free |
| LangChain & Vector Databases — DeepLearning.AI | Short course | Free |
| Andrej Karpathy — "Let's build GPT" | YouTube | Free |
| The Illustrated BERT — Jay Alammar | Blog | Free |
| LLM Bootcamp — Full Stack Deep Learning (2023) | YouTube | Free |

#### ✅ Phase 3 Project — Fine-Tune an LLM

**Project: Fine-tune a small LLM for a specific task**
- Choose a task: customer support bot, code explainer, recipe generator, etc.
- Collect/create 500–1000 examples (instruction + response)
- Fine-tune `Llama 3.2 1B` or `Phi-3-mini` using QLoRA on Google Colab (free)
- Push the fine-tuned model to Hugging Face Hub
- Deploy a Gradio demo on Hugging Face Spaces

---

## 🏗️ Phase 4 — AI Product Engineering (Month 12–18)

> Stop building notebooks. Build real products that real people use.

### 📘 Part 4A — LLM APIs & Application Layer

**Working with LLM APIs**
- [ ] OpenAI API — `openai` Python library, chat completions, streaming
- [ ] Anthropic API — `anthropic` library, Messages API
- [ ] API key management — environment variables, `.env` files, never hardcode keys
- [ ] Rate limits and error handling — retries, exponential backoff
- [ ] Streaming responses — `stream=True` for real-time output
- [ ] Token counting — why cost management matters
- [ ] Structured outputs — JSON mode, function calling / tool use

**LangChain & LlamaIndex**
- [ ] What they are — frameworks for building LLM applications
- [ ] Chains — connect LLM calls in sequence
- [ ] Prompt templates — reusable prompt structures
- [ ] Memory — giving chatbots short and long-term memory
- [ ] Tools and Agents — letting LLMs use external tools (search, calculators, APIs)
- [ ] When to use LangChain vs raw API (hint: raw API is often better for simple cases)
- [ ] LlamaIndex — specialized for document question-answering

**RAG — Retrieval Augmented Generation**
This is the #1 pattern for real AI products right now.

- [ ] What RAG is and why you need it
  - LLMs have knowledge cutoff dates
  - LLMs can't access your private data
  - RAG = search relevant docs → feed to LLM → generate answer
- [ ] Vector embeddings — turning text into numbers that capture meaning
- [ ] Cosine similarity — how we find similar chunks
- [ ] Chunking strategies — how to split documents
- [ ] Vector databases:
  - [ ] **Chroma** — local, easy to start, great for prototypes
  - [ ] **Pinecone** — managed cloud vector DB, production-ready
  - [ ] **Weaviate** — open source alternative
  - [ ] **Qdrant** — fast, open source
  - [ ] **FAISS** — Facebook's library, very fast, local
- [ ] Embedding models — `text-embedding-3-small` (OpenAI), `all-MiniLM-L6-v2` (local)
- [ ] Full RAG pipeline from scratch:
  1. Load documents (PDF, web pages, Notion, etc.)
  2. Chunk into smaller pieces
  3. Embed each chunk
  4. Store in vector DB
  5. On query: embed query, find similar chunks, feed to LLM
- [ ] Advanced RAG:
  - Hybrid search (vector + keyword)
  - Re-ranking results
  - Hypothetical document embeddings (HyDE)
  - Multi-query retrieval

**AI Agents**
- [ ] What an agent is — LLM that can take actions
- [ ] ReAct loop — Reason, Act, Observe, Repeat
- [ ] Tool calling / function calling — giving LLMs access to code
- [ ] Building tools: web search, calculator, database queries, file operations
- [ ] Multi-agent systems — agents that work together
- [ ] Agent frameworks: LangGraph, AutoGen, CrewAI
- [ ] When agents go wrong — loops, hallucinations, safety

---

### 📘 Part 4B — Backend & APIs

- [ ] **FastAPI** — the Python framework for AI backends
  - Creating endpoints with `@app.get` and `@app.post`
  - Pydantic models for request/response validation
  - Async endpoints (`async def`)
  - Middleware and CORS
  - Background tasks
  - Streaming responses (for LLM output)
- [ ] REST API design — GET, POST, PUT, DELETE, status codes
- [ ] Authentication — JWT tokens, API keys
- [ ] Databases:
  - [ ] **SQLite** — local development
  - [ ] **PostgreSQL** — production relational DB
  - [ ] **SQLAlchemy** — Python ORM
  - [ ] **Supabase** — postgres as a service (great for indie hackers)
- [ ] Environment management — `.env`, `python-dotenv`
- [ ] Containerization with Docker:
  - Writing a `Dockerfile`
  - `docker build` and `docker run`
  - `docker-compose` for multi-service apps
- [ ] Basic understanding of async programming — `asyncio`, `await`

---

### 📘 Part 4C — Frontend (Enough to Ship)

You don't need to be a frontend expert. You need enough to ship.

**Option 1: Python-native UIs (Fastest to start)**
- [ ] **Streamlit** — turn Python scripts into web apps in minutes
  - `st.text_input`, `st.button`, `st.file_uploader`
  - `st.chat_message` for chatbots
  - Deploying on Streamlit Cloud (free)
- [ ] **Gradio** — great for ML demos
  - `gr.ChatInterface` for instant chatbot UI
  - Deploying on Hugging Face Spaces (free)

**Option 2: Basic Web Stack (More control)**
- [ ] HTML/CSS basics (you may already have this)
- [ ] JavaScript fundamentals — `fetch`, DOM manipulation, async/await
- [ ] **Next.js** (React framework) — the standard for AI web apps
  - Pages and routing
  - API routes
  - Vercel AI SDK — built-in streaming, chat, etc.
- [ ] **Tailwind CSS** — utility-first styling
- [ ] Deploying on Vercel (free tier)

---

### 📘 Part 4D — Deployment & MLOps Basics

- [ ] **Cloud platforms basics:**
  - AWS — EC2, S3, Lambda (most used)
  - Google Cloud — Vertex AI, Cloud Run
  - Azure — Azure OpenAI Service
- [ ] Deployment options for AI apps:
  - Streamlit Cloud — free, Python apps
  - Hugging Face Spaces — free, great for ML demos
  - Vercel — great for Next.js + API routes
  - Railway — simple container deployment
  - Render — free tier for small apps
  - AWS EC2 / Google Cloud Run — production
- [ ] **Model serving:**
  - `Modal` — serverless GPU inference (great for LLMs)
  - `Replicate` — deploy models with one click
  - `Together.ai` / `Groq` — fast open-source LLM inference APIs
- [ ] MLOps basics (learn as you scale):
  - Experiment tracking with **MLflow** or **Weights & Biases**
  - Model versioning
  - Monitoring — tracking latency, cost, errors in production
  - CI/CD basics — GitHub Actions for auto-deploy

---

### ✅ Phase 4 Projects — Build Real Products

**Project 1: Personal AI Research Assistant**
- RAG pipeline on your own notes/PDFs
- Chat interface with Streamlit
- Deployed on Streamlit Cloud
- Skills: RAG, vector DB, FastAPI or Streamlit, LLM API

**Project 2: AI-powered SaaS tool**
- Pick a niche (HR, legal, medical, education, coding)
- Build a tool that solves 1 specific problem with AI
- Real authentication (Supabase Auth or Clerk)
- Payment integration (Stripe — basic)
- Deploy and get 10 real users
- Skills: Full stack, LLM APIs, deployment, user feedback

**Project 3: Autonomous AI Agent**
- Agent that can browse the web + run code + take actions
- Built on LangGraph or LangChain Agents
- Skills: Tool calling, agents, async Python

---

## 🚀 Phase 5 — Startup & Go to Market (Month 18+)

> You can build. Now build something people pay for.

### Finding Your Idea

- [ ] Talk to 20 people about their work problems before writing any code
- [ ] Look for: repetitive tasks, painful manual processes, information overload
- [ ] Focus on niches you understand (your college, your city, your previous industry)
- [ ] Questions to ask users:
  - What takes you the most time at work?
  - What do you do manually that feels like it should be automated?
  - What information do you constantly look up but can't find fast enough?
- [ ] Validate before building — can you get 5 people to pay ₹500/month for this?

**Hot AI Startup Ideas in India (2024–2025)**
- AI for regional language content creation (Hindi, Telugu, Tamil, etc.)
- AI for CA / tax filing assistance
- AI tutors for competitive exams (JEE, UPSC, NEET)
- AI for SME customer support
- AI for legal document review (Indian law)
- AI for agricultural advisory
- AI for healthcare record summarization
- AI coding assistants for regional developers

### Building Your MVP

- [ ] Keep scope tiny — 1 core workflow, nothing else
- [ ] Ship in 2 weeks or less
- [ ] Build with tools you already know (don't learn new things during MVP)
- [ ] Charge from day 1 — even ₹199/month per user validates demand
- [ ] Talk to every user personally

### Getting Your First Users

- [ ] Post on Twitter/X with #buildinpublic
- [ ] Post in relevant WhatsApp groups and Telegram communities
- [ ] LinkedIn posts about the problem you're solving (not the product)
- [ ] Reach out cold on LinkedIn to potential users
- [ ] Post on Reddit communities (r/India, r/entrepreneur, relevant niche subs)
- [ ] Apply to IndieHackers, Product Hunt (for launch)

### Funding & Programs to Apply To

| Program | Description | Apply When |
|---------|-------------|------------|
| Y Combinator (YC) | World's best accelerator, $500k for 7% | When you have traction |
| Antler India | Pre-seed, ₹1.5 Cr for 10% | Idea or early stage |
| Surge (Sequoia) | South Asia, $1–2M | Early stage |
| iStart MP | Madhya Pradesh state program (you're in Indore!) | Any stage |
| Atal Innovation Mission | Government, free grants | Student/early |
| IIM Indore incubator | Close to home, network access | Idea stage |
| NASSCOM 10K Startups | Free resources, visibility | Any stage |

### Build in Public Strategy

Post on LinkedIn and Twitter every week:
- **What you built** this week
- **What you learned** (even failures)
- **User feedback** you received
- **Metrics** (even if small)

This builds your audience, attracts co-founders, and creates inbound user interest.

---

## 🔄 Skills to Build Throughout (Parallel Track)

These are not phases — build them continuously from Day 1.

### Communication & Presence
- [ ] Write a technical blog post every 2 weeks (Medium, Substack, or personal site)
- [ ] Post 3 times/week on LinkedIn about your learning
- [ ] Attend local AI/tech meetups (Indore has a growing tech community)
- [ ] Speak at a college hackathon or event — even a 10-minute talk
- [ ] Practice explaining complex ideas simply (the Feynman technique)

### Product Thinking
- [ ] Read "The Mom Test" — how to talk to users
- [ ] Read "Shape Up" by Basecamp — how to scope projects
- [ ] Practice writing clear product specs before coding
- [ ] Study products you love — why do they feel good to use?
- [ ] Do competitor analysis before every project

### Open Source
- [ ] Star and fork interesting AI repos on GitHub
- [ ] Fix a small bug or improve documentation in an open-source AI project
- [ ] Submit at least 3 PRs (pull requests) in a year
- [ ] Good repos to contribute to: LangChain, Haystack, LlamaIndex, Hugging Face

### Networking
- [ ] Connect with 5 AI professionals on LinkedIn every week
- [ ] DM people whose work you admire (be genuine and specific)
- [ ] Join hackathons — Devfolio, Unstop, MLH, Hackerearth
- [ ] Attend AI conferences (NASSCOM, iSPIRT, local events)

---

## 📚 Master Resource List

### Free Courses (Best of the Best)

| Course | Platform | Focus Area | Time |
|--------|----------|------------|------|
| Machine Learning Specialization | Coursera (Andrew Ng) | Core ML | 3 months |
| Deep Learning Specialization | Coursera (Andrew Ng) | Deep learning | 3 months |
| Practical Deep Learning | fast.ai | Applied DL | 2 months |
| Neural Networks: Zero to Hero | YouTube (Karpathy) | LLMs from scratch | 3 weeks |
| Hugging Face NLP Course | huggingface.co | Transformers | 1 month |
| LLM University | Cohere | LLMs + RAG | 3 weeks |
| Full Stack Deep Learning | YouTube | Production ML | 2 weeks |
| CS50P | Harvard | Python | 6 weeks |
| Kaggle Learn (all tracks) | kaggle.com | Applied ML | Ongoing |
| DeepLearning.AI Short Courses | deeplearning.ai | Various AI topics | 1–2 hrs each |

### Must-Read Books

| Book | Why Read It |
|------|------------|
| Hands-On ML with Scikit-Learn & TF — Géron | Best practical ML book |
| Deep Learning — Goodfellow et al. | The bible of deep learning (free online) |
| Designing ML Systems — Chip Huyen | How ML works in production |
| The Lean Startup — Eric Ries | For building products |
| Zero to One — Peter Thiel | For startup thinking |
| The Mom Test — Rob Fitzpatrick | How to talk to users |

### YouTube Channels (Subscribe to All)

| Channel | What You'll Learn |
|---------|------------------|
| Andrej Karpathy | LLMs from scratch, deep intuition |
| StatQuest with Josh Starmer | ML/stats explained simply |
| 3Blue1Brown | Math intuition (linear algebra, calculus) |
| Yannic Kilcher | Paper walkthroughs and AI news |
| Sentdex | Python and ML tutorials |
| Two Minute Papers | Research paper summaries |
| AI Explained | LLM news and analysis |
| Sebastian Raschka | Deep learning and LLM papers |

### Websites & Blogs to Follow Daily

| Website | Content |
|---------|---------|
| Papers With Code | ML research + code |
| Towards Data Science | Applied ML articles |
| The Batch (deeplearning.ai) | Weekly AI newsletter |
| LessWrong | AI safety + deep thinking |
| Hugging Face Blog | New models and research |
| OpenAI Blog | GPT releases and research |
| Anthropic Blog | Claude updates and safety research |
| Sebastian Raschka's newsletter | LLM papers summarized |

### Communities to Join

| Community | Platform | Why |
|-----------|----------|-----|
| Hugging Face Discord | Discord | LLMs, open-source AI |
| fast.ai Forums | forums.fast.ai | Practical DL community |
| Kaggle | kaggle.com | Competitions and notebooks |
| AI Engineer Foundation | Discord | AI engineering community |
| Indie Hackers | indiehackers.com | Building AI products |
| r/MachineLearning | Reddit | Research discussions |
| r/learnmachinelearning | Reddit | Beginner friendly |
| Local AI/tech WhatsApp groups | WhatsApp | Indore/MP startup scene |

---

## 📅 Weekly Schedule Template

Use this as a starting point. Adjust to your college schedule.

| Day | Focus | Time |
|-----|-------|------|
| Monday | New concept — watch lecture, take notes | 2 hrs |
| Tuesday | Code the concept — implement from scratch | 2 hrs |
| Wednesday | Project work — build something real | 2 hrs |
| Thursday | New concept (continue) OR deep-dive a paper | 2 hrs |
| Friday | Project work | 2 hrs |
| Saturday | Hackathon, open source, or Kaggle | 4 hrs |
| Sunday | Weekly review + write about what you learned | 1 hr |

---

## 📊 Progress Tracker

Copy this to a new Notion page and check off as you go.

### Phase 0 — Setup
- [ ] All tools installed
- [ ] GitHub account created
- [ ] Google Colab tested
- [ ] All accounts created (Kaggle, HF, etc.)

### Phase 1 — Python & Math
- [ ] List comprehensions, lambdas, decorators mastered
- [ ] NumPy arrays — create, slice, multiply
- [ ] Pandas — load, clean, group, merge DataFrames
- [ ] Matplotlib — 5 different chart types
- [ ] Linear algebra concepts understood
- [ ] Statistics basics understood
- [ ] Gradient descent understood conceptually
- [ ] Phase 1 project pushed to GitHub

### Phase 2 — Classical ML
- [ ] Linear regression — implemented from scratch + with sklearn
- [ ] Logistic regression — understood sigmoid + cross-entropy
- [ ] Decision tree + Random Forest trained on real dataset
- [ ] XGBoost used on a Kaggle competition
- [ ] Overfitting/underfitting — can diagnose and fix
- [ ] Cross-validation implemented
- [ ] Kaggle Titanic notebook complete
- [ ] Kaggle House Prices notebook complete

### Phase 3 — Deep Learning & LLMs
- [ ] Neural network built from scratch in NumPy
- [ ] PyTorch tensors and autograd understood
- [ ] Trained a CNN on image classification
- [ ] Transformer architecture understood
- [ ] Attention mechanism understood
- [ ] Fine-tuned a small LLM with QLoRA
- [ ] Model uploaded to Hugging Face Hub
- [ ] Gradio demo deployed on HF Spaces

### Phase 4 — AI Product Engineering
- [ ] RAG pipeline built end-to-end
- [ ] FastAPI backend with LLM endpoint
- [ ] Streamlit or Next.js frontend connected
- [ ] Product 1 deployed (AI Research Assistant)
- [ ] Product 2 deployed with real users
- [ ] Agent built with tool use
- [ ] Docker basics understood

### Phase 5 — Startup
- [ ] 20 user interviews completed
- [ ] MVP built and shipped
- [ ] First paying user
- [ ] Applied to at least 1 accelerator/program
- [ ] Building in public consistently

---

## 💡 Mindset Notes — Read This When You Feel Stuck

**On slow progress:** Learning AI is genuinely hard. If it feels hard, that means you're learning. The people who succeed are not smarter — they just stayed consistent longer.

**On tutorials vs building:** After following a tutorial, close it and rebuild the same thing from memory. If you can't, you haven't learned it yet. The discomfort of building from scratch is where learning actually happens.

**On comparison:** Don't compare your beginning to someone else's middle. Most people you see posting impressive AI projects have been doing this for 3–5 years.

**On India-specific advantage:** You are in one of the world's fastest-growing AI markets. Problems in India — language, agriculture, healthcare, education, SME — are not well-solved by tools built in Silicon Valley. Your local knowledge is a genuine competitive advantage.

**On building vs learning:** After Phase 2, spend at least 50% of your time building, not consuming courses. You learn 10× more from debugging a real product than from watching a lecture.

**On asking for help:** The AI community is genuinely generous. Tweet at researchers, ask questions on forums, DM people on LinkedIn. Most will respond if your question is specific and shows you've tried.

---

*Last updated: 2025 | Built for: AI enthusiast, student, startup-minded builder*
*Location context: Indore, MP — leverage iStart MP, IIM Indore ecosystem*
