# Natural Language Processing Course

This repository contains assignments and projects completed as part of the Natural Language Processing course. Each assignment focuses on different aspects of NLP, from fundamental concepts to advanced applications.

## Course Structure

The course is divided into seven assignments, each exploring different NLP concepts and techniques:

### [A1: Word Embeddings](Assignments/A1)
- Implementation of Skip-gram model from scratch
- Implementation of GloVe model from scratch
- Comparison with Gensim's implementation
- Word similarity evaluation using WordSim353

### [A2: Language Models](Assignments/A2)
- Perplexity evaluation on test data
- Text generation using the trained models
- Handling out-of-vocabulary words
- Smoothing techniques implementation

### [A3: Machine Translation](Assignments/A3)
- Implementation of Neural Machine Translation
- Training on a custom language pair
- BLEU score evaluation
- Attention mechanism implementation
- Custom language creation and translation

### [A4: BERT from Scratch](Assignments/A4)
- Implementation of BERT architecture
- Pre-training with MLM and NSP tasks
- Fine-tuning for downstream tasks
- Attention visualization
- Performance comparison with HuggingFace BERT

### [A5: Direct Preference Optimization](Assignments/A5)
- Implementation of DPO algorithm
- Training with human preference data
- Model alignment with human values
- Comparison with standard fine-tuning
- Evaluation of preference learning

### [A6: Retrieval Augmented Generation (RAG)](Assignments/A6)
- Document retrieval system setup
- Integration with LLM for generation
- Custom knowledge base creation
- Evaluation of factual accuracy

### [A7: Training Distillation vs LoRA](Assignments/A7)
- Implementation of knowledge distillation
- Implementation of LoRA fine-tuning
- Performance comparison between approaches
- Model size and efficiency analysis
- Trade-off evaluation between size and accuracy

## Technologies Used

- Python
- PyTorch
- TensorFlow
- NLTK
- Gensim
- Hugging Face Transformers
- Docker (for deployments)

## Getting Started

Each assignment directory contains its own README with specific instructions, requirements, and implementation details. To get started with any assignment:

1. Navigate to the specific assignment directory
2. Read the assignment's README.md for detailed instructions
3. Install required dependencies
4. Follow the implementation guidelines

## Repository Structure

```
Natural-Language-Processing/
├── Assignments/
│   ├── A1/  # Word Embeddings
│   ├── A2/  # Language Models
│   ├── A3/  # Machine Translation
│   ├── A4/  # BERT from Scratch
│   ├── A5/  # Direct Preference Optimization
│   ├── A6/  # Retrieval Augmented Generation (RAG)
│   └── A7/  # Training Distillation vs LoRA
└── README.md
```

Each assignment folder contains its own set of code, data, documentation, and results.
