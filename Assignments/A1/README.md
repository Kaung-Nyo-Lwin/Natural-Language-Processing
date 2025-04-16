# NLP Assignment 1: Word Embedding Models

This project implements and compares two popular word embedding models: Skip-gram and GloVe (Global Vectors for Word Representation). Both models are implemented from scratch and experiments are conducted to analyze their performance.

## Project Structure

- `app/`: Contains the web application code for visualization
- `figures/`: Contains generated plots and visualizations
- `st125066_a1.ipynb`: Main Jupyter notebook with implementation and experiments
- `dash.Dockerfile`: Dockerfile for the visualization dashboard
- `docker-compose.yaml`: Docker compose configuration for running the application

## Model Parameters

Both models are implemented with the following parameters:
- Window size: 2
- Embedding size: 2

## Setup and Running

1. To run the experiments and generate embeddings:
   - Open and run `st125066_a1.ipynb` in Jupyter Notebook/Lab

2. To run the visualization dashboard:
   ```bash
   docker-compose up
   ```

## Results

The experiments and visualizations can be found in:
- Jupyter notebook: `st125066_a1.ipynb`
- Generated figures: `figures/` directory
- Interactive dashboard: Available through Docker setup

### Performance Comparison

| Model | Window Size | Training Loss | Training Time | Semantic Accuracy | Syntactic Accuracy |
|-------|-------------|---------------|---------------|------------------|-------------------|
| Skipgram | 2 | 4.192191 | 34.587368 | 0.0 | 0.064103 |
| Skipgram (Neg) | 2 | 6.416509 | 40.49946 | 0.0 | 0.000000 |
| GloVe | 2 | 0.368629 | 19.605978 | 0.0 | 0.000000 |
| GloVe (Gensim) | - | - | - | 0.0 | 0.000000 |

### Test on wordsim353 with Skip Gram Model

| word1 | word2 | human(mean) | dotproduct |
|-------|--------|-------------|------------|
| production | crew | 6.25 | 0.205779 |
| energy | crisis | 5.94 | -0.352387 |
| reason | criterion | 5.91 | -0.088322 |
| change | attitude | 5.44 | 1.163571 |
| energy | laboratory | 5.09 | -0.352387 |
| consumer | energy | 4.75 | -0.352387 |
| start | year | 4.06 | 0.128941 |
| report | gain | 3.63 | -0.080974 |
| five | month | 3.38 | -0.391407 |
| announcement | production | 3.38 | 0.205779 |
| media | gain | 2.88 | -0.080974 |
| reason | hypertension | 2.31 | -0.088322 |
| month | hotel | 1.81 | -0.391407 |
| energy | secretary | 1.81 | -0.352387 |
| production | hike | 1.75 | 0.205779 |

### Test on wordsim353 with Skip Gram Model (Negative)

| word1 | word2 | human(mean) | dotproduct |
|-------|--------|-------------|------------|
| production | crew | 6.25 | -0.348614 |
| energy | crisis | 5.94 | -0.644102 |
| reason | criterion | 5.91 | 0.492290 |
| change | attitude | 5.44 | -0.084866 |
| energy | laboratory | 5.09 | -0.644102 |
| consumer | energy | 4.75 | -0.644102 |
| start | year | 4.06 | -0.663455 |
| report | gain | 3.63 | -0.120726 |
| five | month | 3.38 | -0.205596 |
| announcement | production | 3.38 | -0.348614 |
| media | gain | 2.88 | -0.120726 |
| reason | hypertension | 2.31 | 0.492290 |
| month | hotel | 1.81 | -0.205596 |
| energy | secretary | 1.81 | -0.644102 |
| production | hike | 1.75 | -0.348614 |

### Test on wordsim353 with GloVe Model

| word1 | word2 | human(mean) | dotproduct |
|-------|--------|-------------|------------|
| production | crew | 6.25 | 0.525772 |
| energy | crisis | 5.94 | -1.288290 |
| reason | criterion | 5.91 | -0.648586 |
| change | attitude | 5.44 | 0.305196 |
| energy | laboratory | 5.09 | -1.288290 |
| consumer | energy | 4.75 | -1.288290 |
| start | year | 4.06 | 0.447019 |
| report | gain | 3.63 | -0.705231 |
| five | month | 3.38 | 0.561428 |
| announcement | production | 3.38 | 0.525772 |
| media | gain | 2.88 | -0.705231 |
| reason | hypertension | 2.31 | -0.648586 |
| month | hotel | 1.81 | 0.561428 |
| energy | secretary | 1.81 | -1.288290 |
| production | hike | 1.75 | 0.525772 |

### Test on wordsim353 with GloVe Gensim Model

| word1 | word2 | human(mean) | dotproduct |
|-------|--------|-------------|------------|
| production | crew | 6.25 | 11.914396 |
| energy | crisis | 5.94 | 19.712059 |
| reason | criterion | 5.91 | 6.579437 |
| change | attitude | 5.44 | 17.136171 |
| energy | laboratory | 5.09 | 17.056881 |
| consumer | energy | 4.75 | 22.467970 |
| start | year | 4.06 | 24.899786 |
| report | gain | 3.63 | 15.000955 |
| five | month | 3.38 | 24.381931 |
| announcement | production | 3.38 | 13.073078 |
| media | gain | 2.88 | 13.176430 |
| reason | hypertension | 2.31 | 3.626410 |
| month | hotel | 1.81 | 15.351804 |
| energy | secretary | 1.81 | 16.281017 |
| production | hike | 1.75 | 11.104475 |

## Conclusion

To test the correlation, there are only 14 pairs of words that are not out of vocab. The correlation score can be summarized as follows

skipgram < skipgram(neg) < Glove < Glove(gensim)

