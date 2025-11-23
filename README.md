# Deep Learning / Generative AI Project

## Project Overview

This repository contains our Deep Learning/Generative AI project developed as part of the Data Science and AI course. The project follows a structured milestone-based approach with comprehensive evaluation criteria.

## 📋 Project Guidelines

### Group Formation

- **Team Size**: 5 members
- **Registration**: Group details submitted via Google Form
- **Assignment**: Unregistered students will be randomly assigned to groups

### Problem Statement

- **Focus Area**: Deep Learning or Generative AI
- **Approval Required**: Problem statement must be approved by course team
- **Deadline**: September 28, 2025

## 🎯 Project Evaluation (30 marks total)

| Component                | Marks | Description                                          |
| ------------------------ | ----- | ---------------------------------------------------- |
| **Milestone Completion** | 10    | Based on successful completion of all six milestones |
| **Novelty/Complexity**   | 5     | Originality and technical expertise required         |
| **Final Presentation**   | 15    | Clarity, technical understanding, and demonstration  |

## 📅 Project Milestones

### Milestone 1: Problem Definition & Literature Review

**Deadline**: October 3, 2025

- [x] Define project objectives
- [x] Review existing solutions, baselines, and benchmarks
- [x] Identify gaps and opportunities
- [x] **Deliverable**: Problem statement and literature review ([Milestone-1/Milestone_1.pdf](Milestone-1/Milestone_1.pdf), [Milestone-1/Milestone_1_v2.pdf](Milestone-1/Milestone_1_v2.pdf))

### Milestone 2: Dataset Preparation

**Deadline**: October 10, 2025

- [x] Collect or identify suitable dataset
- [x] Prepare and preprocess data for training and validation
- [x] **Deliverable**: Cleaned and preprocessed dataset ([Milestone-2/Milestone_2.pdf](Milestone-2/Milestone_2.pdf))
- [x] Artifacts: Data prep notebooks and samples ([Milestone-2/CreatePatchWithLabel.ipynb](Milestone-2/CreatePatchWithLabel.ipynb), image samples in `Milestone-2/OrgMicrostrucData/` and `Milestone-2/PatchData_images/`)

### Milestone 3: Model Architecture

**Deadline**: October 17, 2025

- [x] Select or design appropriate model architecture(s)
- [x] Justify choice of architecture
- [x] **Deliverable**: Architecture design and justification ([Milestone-3/Milestone-3.pdf](Milestone-3/Milestone-3.pdf))

### Milestone 4: Model Training

**Deadline**: October 31, 2025

- [x] Train initial models
- [x] Experiment with hyperparameters, optimization methods, and regularization techniques
- [x] **Deliverable**: Trained models and training logs ([Milestone-4/Milestone-4.pdf](Milestone-4/Milestone-4.pdf); training notebooks in `Milestone-4/` and `Milestone-4_SG/`; TensorBoard logs in `Milestone-4_SG/logs/`)

### Milestone 5: Model Evaluation & Analysis

**Deadline**: November 7, 2025

- [x] Evaluate trained models using appropriate metrics
- [x] Provide error analysis
- [x] Discuss limitations and possible improvements
- [x] **Deliverable**: Evaluation results and analysis ([Milestone-5_SG/Report_MS 5.pdf](Milestone-5_SG/Report_MS%205.pdf); evaluation notebook: [Milestone-5_SG/Evaluation_MS5.ipynb](Milestone-5_SG/Evaluation_MS5.ipynb))

### Milestone 6: Deployment & Documentation

**Deadline**: November 14, 2025

- [x] Deploy the model (API, demo interface, or Hugging Face Spaces)
- [x] Prepare comprehensive documentation
- [x] Finalize project report
- [x] **Deliverable**: Deployed model and final documentation ([Milestone-6/app.py](Milestone-6/app.py), [Milestone-6/infer.py](Milestone-6/infer.py))

## 🎤 Final Presentations

- **Schedule**: Week 10 & Week 11 (November 23 onwards)
- **Format**: Live demonstration, code walkthrough, and report presentation
- **Requirements**:
  - Live demonstration of the working model
  - Code walkthrough explaining implementation
  - Presentation of final report
- **Presentation Slides**: [Google Slides Presentation](https://docs.google.com/presentation/d/1gPP-0P3yKtRZC3c6Hnbw_NeYe7-GnaK6GVNle20nbTE/edit?usp=sharing)

## 📁 Repository Structure

```
DS_AI_Project/
├── README.md                 # This file
├── Milestone-1/             # Problem definition & literature review PDFs
├── Milestone-2/             # Data prep notebook and sample images
├── Milestone-3/             # Model architecture report
├── Milestone-4/             # Training datasets and notebooks
├── Milestone-4_SG/          # Training experiments, logs, and report
├── Milestone-5_SG/          # Evaluation notebook and report
└── (additional code/artifacts as added per milestone)
```

## 🛠️ Technical Requirements

### Code Quality Standards

- **Modularity**: Code should be well-organized and modular
- **Readability**: Clear, documented, and maintainable code
- **Reproducibility**: Results should be reproducible with provided scripts
- **Version Control**: Proper Git practices with meaningful commit messages

### Repository Contents

- Training and evaluation notebooks under milestone folders
- TensorBoard logs under `Milestone-4_SG/logs/`
- Milestone reports in respective folders
- Requirements and dependencies (to be added if code environment is shared)

## 📊 Progress Tracking

### Project Status

✅ **PROJECT OFFICIALLY COMPLETE** - All milestones have been successfully completed as of November 23, 2025.

### Weekly Meetings

- **Frequency**: Mandatory weekly meetings with TAs
- **Purpose**: Progress tracking and milestone guidance
- **Format**: Progress updates and feedback sessions

### Milestone Tracking

- [x] Milestone 1: Problem Definition & Literature Review
- [x] Milestone 2: Dataset Preparation
- [x] Milestone 3: Model Architecture
- [x] Milestone 4: Model Training
- [x] Milestone 5: Model Evaluation & Analysis
- [x] Milestone 6: Deployment & Documentation

## 🚀 Getting Started

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd DS_AI_Project
   ```

2. **Set up environment**

   ```bash
   pip install -r requirements.txt
   ```

3. **Open notebooks and reproduce results**

   - Data prep: `Milestone-2/CreatePatchWithLabel.ipynb`
   - Training: `Milestone-4/Microstructure_VGG19_Experiment.ipynb`, `Milestone-4/Train_VGG19_RestNet50_With_Hyperperameter.ipynb`, and `Milestone-4_SG/classification.ipynb`
   - Evaluation: `Milestone-5_SG/Evaluation_MS5.ipynb`

4. **(Optional) View training logs**
   - Launch TensorBoard pointing to `Milestone-4_SG/logs/`

## 📝 Documentation

- **Reports**:
  - Milestone 1: [Milestone-1/Milestone_1.pdf](Milestone-1/Milestone_1.pdf), [Milestone-1/Milestone_1_v2.pdf](Milestone-1/Milestone_1_v2.pdf)
  - Milestone 2: [Milestone-2/Milestone_2.pdf](Milestone-2/Milestone_2.pdf)
  - Milestone 3: [Milestone-3/Milestone-3.pdf](Milestone-3/Milestone-3.pdf)
  - Milestone 4: [Milestone-4_SG/Report_MS 4.pdf](Milestone-4_SG/Report_MS%204.pdf)
  - Milestone 5: [Milestone-5_SG/Report_MS 5.pdf](Milestone-5_SG/Report_MS%205.pdf)
- **Notebooks**: See milestone folders
- **Code Documentation**: Inline comments and docstrings
- **Deployment Guide**: To be added in Milestone 6

## 👥 Team Members

_[To be updated with actual team member names and roles]_

## 📞 Contact

For questions or clarifications regarding the project, please contact the course team or your assigned TA.

---

**Note**: This project follows the academic guidelines provided by the Data Science and AI course. All milestones and deadlines are subject to course requirements and TA feedback.
