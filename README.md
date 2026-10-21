<!-- Roadmap content lives in this README. After editing it, run: python3 scripts/sync_site.py (rebuilds index.html) -->
<div align="center">

# Embedded AI Engineer Roadmap

**15 months · ~12–16 hrs/week alongside university**

ML/DL mastery first → model optimization → embedded systems → deployment

[![Live Site](https://img.shields.io/badge/Live_Site-GitHub_Pages-00FF9C?style=flat-square&logo=github)](https://mgzhnn.github.io/Embedded-AI-Engineer-Role-Roadmap/)
[![License: MIT](https://img.shields.io/badge/License-MIT-A78BFA?style=flat-square)](LICENSE)

</div>

---

> **How to use this roadmap** — Work one month at a time. Hit the milestone before moving on. Slow down during exams; never skip milestones — they are the real checkpoints, not the topic lists.

---

## Overview

```
Phase 1 · Months  1– 3  →  Foundation        (Linux · Git · Python · Math · Classical ML)
Phase 2 · Months  4– 7  →  Deep Learning     (NN core · CNNs · Sequences · Optimization)
Phase 3 · Months  8–11  →  Embedded Systems  (C/C++ · MCUs · RTOS · Edge Deployment)
Phase 4 · Months 12–15  →  Integration       (Portfolio projects · MLOps · Job search)
```

---

## Phase 1 — Foundation
*Months 1–3 · Tools + Math + Classical ML · Everything else builds on this.*

<details>
<summary><strong>Month 1 — Linux, Git & Python</strong> &nbsp;·&nbsp; ~12 hrs/week</summary>

<br>

**Why this month:** Git, Linux, and Python appear in every single job post. Learn them now so they become automatic.

**Tools**
- Linux CLI — navigate, chmod, SSH, bash scripting basics
- Git — init, clone, commit, branch, merge, pull requests
- GitHub — repos, README, issues, forks
- VSCode — setup, extensions, keyboard shortcuts
- Conda / venv — Python environment management

**Code**
- Python — data types, loops, functions, classes, file I/O
- Numpy basics — arrays, broadcasting, slicing
- Write 3 small CLI Python scripts from scratch

> **✦ Milestone:** Push a real project to GitHub with a proper README.

</details>

<details>
<summary><strong>Month 2 — Math for ML</strong> &nbsp;·&nbsp; ~14 hrs/week</summary>

<br>

**Why this month:** ML is applied math. Skipping this means memorizing without understanding.

**Math**
- Linear algebra — vectors, matrices, dot product, eigenvalues
- Calculus — derivatives, chain rule, partial derivatives
- Probability — Bayes theorem, distributions, expectation
- Statistics — mean/variance, normal distribution, correlation

**Tools**
- Jupyter Notebooks
- Matplotlib + Seaborn for plotting
- Pandas for data handling

> **✦ Milestone:** Implement gradient descent from scratch using only Numpy.

</details>

<details>
<summary><strong>Month 3 — Classical ML</strong> &nbsp;·&nbsp; ~14 hrs/week</summary>

<br>

**Why this month:** Classical ML teaches you *why* models work. Deep learning makes more sense after this.

**Concepts**
- Supervised vs unsupervised learning
- Linear/logistic regression — implement from scratch
- Decision trees, random forests, SVMs
- Overfitting, underfitting, bias-variance tradeoff
- Cross-validation, train/val/test splits
- Scikit-learn — pipelines, model evaluation

**Tools**
- Docker basics — pull, run, build a simple container
- Kaggle — join 1 beginner competition (Titanic or similar)

> **✦ Milestone:** Complete a full ML pipeline on a Kaggle dataset. Push to GitHub.

</details>

---

## Phase 2 — Deep Learning
*Months 4–7 · Neural networks, then optimization · Master this before touching edge hardware.*

<details>
<summary><strong>Month 4 — Neural Networks Core</strong> &nbsp;·&nbsp; ~15 hrs/week</summary>

<br>

**Why this month:** You can't compress or optimize what you don't understand.

**Theory**
- Perceptrons → multi-layer networks
- Forward pass, backpropagation — derive it manually
- Activation functions — ReLU, sigmoid, tanh and why each exists
- Loss functions — MSE, cross-entropy
- Optimizers — SGD, Adam — understand the math

**Frameworks**
- PyTorch — tensors, autograd, nn.Module
- Build a 3-layer net on MNIST from scratch in PyTorch
- TensorFlow + Keras — same exercises in both
- Weights & Biases (W&B) — experiment tracking from day one

> **✦ Milestone:** Train MNIST classifier in both PyTorch and Keras. Log results with W&B.

</details>

<details>
<summary><strong>Month 5 — CNNs & Computer Vision</strong> &nbsp;·&nbsp; ~15 hrs/week</summary>

<br>

**Why this month:** CNNs dominate embedded vision — the #1 use case for edge AI.

**Architectures**
- Conv layers, pooling, feature maps — understand spatially
- LeNet → AlexNet → VGG → ResNet — understand each improvement
- Transfer learning — fine-tune ResNet on custom data
- Data augmentation strategies
- Object detection intro — YOLO concepts

**Tools**
- OpenCV — image processing basics
- ONNX — export a PyTorch model to ONNX format

> **✦ Milestone:** Fine-tune MobileNetV2 on a custom 5-class dataset. Achieve >85% val accuracy.

</details>

<details>
<summary><strong>Month 6 — Sequences, Transformers & Audio</strong> &nbsp;·&nbsp; ~15 hrs/week</summary>

<br>

**Why this month:** Embedded audio/NLP is growing. Know the theory even if you specialize in vision.

**Concepts**
- RNNs, LSTMs — understand the vanishing gradient problem
- Attention mechanism — derive scaled dot-product attention
- Transformer architecture overview
- Small models for edge — keyword-spotting CNNs for MCUs; DistilBERT-class models for edge boards like Jetson

**Audio**
- Spectrograms, MFCCs — what they are and why they work
- Build a keyword spotter (wake word detection) on an audio dataset

> **✦ Milestone:** Build a keyword spotter in Python. Export as ONNX.

</details>

<details>
<summary><strong>Month 7 — Model Optimization (the Bridge)</strong> &nbsp;·&nbsp; ~16 hrs/week</summary>

<br>

**Why this month:** This is where ML meets embedded. Quantization and pruning are core Embedded AI skills.

**Optimization**
- Quantization — FP32 → INT8, why it works, what breaks
- Post-training quantization (PTQ) vs quantization-aware training (QAT)
- Pruning — structured vs unstructured
- Knowledge distillation — teacher → student model
- Benchmark — latency, memory footprint, accuracy trade-off

**Tools**
- TensorFlow Model Optimization Toolkit
- PyTorch quantization — `torchao` (successor to `torch.ao.quantization`)
- Netron — visualize and debug model graphs
- Start reading MCU datasheets — understand memory specs

> **✦ Milestone:** Quantize your Month 5 CNN to INT8. Measure accuracy loss and size reduction. Document it.

</details>

---

## Phase 3 — Embedded Systems
*Months 8–11 · C/C++, RTOS, hardware interfaces · The embedded half of the job title.*

<details>
<summary><strong>Month 8 — C/C++ for Embedded</strong> &nbsp;·&nbsp; ~16 hrs/week</summary>

<br>

**Why this month:** Embedded firmware is written in C/C++. No way around it.

**C**
- Pointers, memory layout, stack vs heap
- Structs, unions, bit manipulation
- Makefiles and GCC compilation pipeline
- Debugging with GDB
- Memory management — malloc, free, common pitfalls

**C++ for Embedded**
- Classes, templates, RAII
- `std::array` vs raw arrays — when to use which
- Why to avoid exceptions and dynamic allocation on MCUs

> **✦ Milestone:** Write a C program that sorts sensor data, uses pointers, and compiles with a Makefile.

</details>

<details>
<summary><strong>Month 9 — Microcontrollers & Hardware</strong> &nbsp;·&nbsp; ~16 hrs/week</summary>

<br>

**Why this month:** You must understand the hardware the AI runs on.

**Hardware**
- MCU architecture — CPU, flash, SRAM, peripherals
- GPIO, UART, SPI, I2C — what each does and when to use it
- Interrupts, DMA, timers
- Power modes — why they matter for battery-powered edge devices

**Practice**
- Arduino Nano 33 BLE Sense or STM32 Nucleo — blink LED → UART comms → sensor read
- Read an IMU (accelerometer) via SPI or I2C
- Oscilloscope/logic analyzer basics — use simulation if no hardware

> **✦ Milestone:** Read sensor data on MCU and stream via UART to PC. Log with a Python script.

</details>

<details>
<summary><strong>Month 10 — RTOS & System Software</strong> &nbsp;·&nbsp; ~15 hrs/week</summary>

<br>

**Why this month:** Once a device juggles several concurrent jobs, an RTOS keeps it manageable; many production devices use one.

**RTOS**
- Tasks, scheduling, priorities in FreeRTOS
- Mutexes, semaphores, queues — when each is right
- Stack overflow detection
- Interrupt service routines with RTOS

**Embedded Linux**
- Linux kernel basics — device tree, modules
- Cross-compilation — build for ARM on x86
- Yocto Project intro (overview level)
- SSH, scp, rsync for embedded Linux workflows

> **✦ Milestone:** FreeRTOS project — 2 tasks, shared queue, mutex-protected UART output.

</details>

<details>
<summary><strong>Month 11 — Edge AI Deployment</strong> &nbsp;·&nbsp; ~16 hrs/week</summary>

<br>

**Why this month:** Getting trained models onto constrained hardware is the core of the job.

**Frameworks**
- LiteRT (formerly TensorFlow Lite) — flatbuffer format, interpreter API
- TFLite Micro (TFLM) — inference on MCU with no OS
- ONNX Runtime for edge
- Edge Impulse — full pipeline from data to MCU

**Hardware Accelerators**
- NPU/DSP concepts — CMSIS-NN library
- NVIDIA Jetson — TensorRT basics
- STM32 Cube.AI or equivalent vendor tool

> **✦ Milestone:** Run an INT8 image classifier on a physical MCU (a model sized to fit its flash and RAM, e.g. a small-width MobileNet at 96×96) or full MobileNetV2 on a Jetson. Measure FPS.

</details>

---

## Phase 4 — Integration & Career
*Months 12–15 · Build real systems. Ship projects. Get hired.*

<details>
<summary><strong>Month 12 — Full Pipeline Project #1</strong> &nbsp;·&nbsp; ~16 hrs/week</summary>

<br>

**Why this month:** A portfolio project beats any certificate.

**Project**
- Pick a domain — gesture recognition, anomaly detection, keyword spotting, or predictive maintenance
- Collect or find a real dataset
- Train → optimize → quantize → deploy to MCU or edge SBC
- Measure and document — accuracy, latency, power if possible

**Tools**
- GitHub Actions — basic CI for your ML code
- MLflow or W&B — log all experiments
- Write a proper README with an architecture diagram

> **✦ Milestone:** End-to-end system running on hardware. Public GitHub repo. 1-page technical writeup.

</details>

<details>
<summary><strong>Month 13 — MLOps & Productionization</strong> &nbsp;·&nbsp; ~14 hrs/week</summary>

<br>

**Why this month:** Companies want engineers who can maintain models, not just train them.

**MLOps**
- Data versioning — DVC
- Model registry concepts
- CI/CD for ML — test models before merging
- Model monitoring — drift detection basics
- OTA update concepts for embedded

**Soft Skills**
- Write a technical blog post about your Month 12 project
- Record a 10-minute talk explaining your system

> **✦ Milestone:** CI pipeline that trains, tests accuracy, and flags regressions on every commit.

</details>

<details>
<summary><strong>Month 14 — Specialization & Project #2</strong> &nbsp;·&nbsp; ~16 hrs/week</summary>

<br>

**Why this month:** Specialization makes you hireable faster.

**Pick one lane**
- Vision systems — YOLO on Jetson, object tracking
- Audio/speech — wake word, voice activity detection
- Predictive maintenance — vibration + LSTM on STM32
- Autonomous systems — sensor fusion, ROS2 basics

**Project #2**
- More complex than Project #1
- Real-world constraint — power budget, latency target, or tiny RAM
- Document trade-offs made and why

> **✦ Milestone:** Second portfolio project. Write a case study. Post on LinkedIn.

</details>

<details>
<summary><strong>Month 15 — Job Search & Interview Prep</strong> &nbsp;·&nbsp; ~10 hrs/week</summary>

<br>

**Why this month:** Skills don't speak for themselves.

**Interview Prep**
- Systems design — design an edge AI pipeline for a given use case
- Coding — LeetCode medium, arrays/trees/graphs, 30 problems
- ML theory — explain quantization, pruning, backprop out loud
- Embedded — explain interrupt handling, memory layout, DMA

**Job Search**
- Apply to 5–10 roles per week minimum
- Target — embedded software, ML systems, edge AI, firmware + ML roles
- LinkedIn — post your projects, engage with the community
- Watch TinyML Summit talks for domain knowledge

> **✦ Milestone:** Land interviews at 3+ companies.

</details>

---

## Tools Reference

*Learn these in the order shown. They appear in every serious embedded AI job.*

| Tool | Learn in | Why it matters |
|---|---|---|
| Git + GitHub | Month 1 | Version control is non-negotiable |
| Linux CLI | Month 1 | Dev tooling and embedded Linux boards (Jetson, Raspberry Pi) run on it; SSH is daily use |
| Python | Month 1 | ML glue language, scripting, tooling |
| Docker | Month 3 | Reproducible builds; most ML infra is containerized |
| PyTorch | Month 4 | Industry standard for research and prototyping |
| TensorFlow / Keras | Month 4 | Strong ecosystem for deployment and edge |
| W&B / MLflow | Month 4 | Experiment tracking used in every serious ML team |
| ONNX | Month 5 | Model interchange format between frameworks |
| OpenCV | Month 5 | Image processing in every CV project |
| Netron | Month 7 | Visualize and debug model graphs |
| C / C++ | Month 8 | Core embedded language — firmware and MCU drivers |
| Makefile / CMake | Month 8 | Build systems for C/C++ projects |
| GDB | Month 8 | Debugger for C/C++ — every embedded dev uses it |
| FreeRTOS | Month 10 | Most popular RTOS for MCUs |
| LiteRT / TFLM | Month 11 | Deploy models to MCUs, edge boards and mobile (LiteRT is the new name for TensorFlow Lite) |
| Edge Impulse | Month 11 | Full embedded ML pipeline, listed in job posts |
| GitHub Actions | Month 12 | CI/CD — expected in any software role now |

---

## Hardware

You only need one board to start. Get it by Month 9.

**Recommended — Arduino Nano 33 BLE Sense Rev2 (~$40)**
Has an IMU, microphone and environmental sensors, but no camera (the Arduino Tiny Machine Learning Kit adds a camera shield). 1 MB flash and 256 KB RAM, so size models to fit. Runs TFLite Micro. Edge Impulse supports it out of the box.

**Optional later — NVIDIA Jetson Orin Nano Super Developer Kit (launched at $249)**
GPU-accelerated inference and TensorRT practice. NVIDIA has phased out the original Jetson Nano developer kit.

---

<div align="center">

*Adjust study hours down during exams. Never skip milestones.*

</div>
