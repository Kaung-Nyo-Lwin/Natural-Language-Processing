# NLP Assignment 4: BERT from Scratch

## Project Structure

- `app/`: Contains the web application code for visualization
- `figures/`: Contains generated plots and visualizations
- `st125066_a4.ipynb`: Main Jupyter notebook with implementation and experiments
- `dash.Dockerfile`: Dockerfile for the visualization dashboard
- `docker-compose.yaml`: Docker compose configuration for running the application

## Installation and Setup
    run "docker compose up"
    Webapp at localhost:9999

## Model evaluation
| Model Type       | SNLI Accuracy |
|------------------|---------------|
| S-BERT(scratch)  |         35.090909 |

## Model config
    n_layers - 12    (number of Encoder of Encoder Layer)
    n_heads  - 12    (number of heads in Multi-Head Attention)
    d_model  - 768   (Embedding Size)
    num_epoch - 2
- [Discussion](#discussion)


## Installation and Setup
    run "docker compose up"
    Webapp at localhost:9999

## Model evaluation
| Model Type       | SNLI Accuracy |
|------------------|---------------|
| S-BERT(scratch)	 |         35.090909 |

## Model config
    n_layers - 12    (number of Encoder of Encoder Layer)
    n_heads  - 12    (number of heads in Multi-Head Attention)
    d_model  - 768   (Embedding Size)
    num_epoch - 2

## Web 
<img src="./figures/a4_web.png" width="600" length="400"/>


## Discussion
In training BERT, only one percent of BookCorpus dataset is trained with 100 epochs due to the limitation of computational resources. Then, S-BERT is retrained on one percent of SNLI data. Hence, the performance of the model is not good enough to make distinction various inputs. This can be seen in the average similarity scores which is 0.99 as most of the sentences look similar to the model. However, the accuracy of prediction the labels is acceptable with 35 percent. Here, the obvious limitation is computational resource, causing the training data size reduced.

To improve the performance, we need to scale up the training data and the model size by adding more layers. Moreover, the epochs is just two as it is expensive. This is also another factor of hindrance of model performance. I believe scaling up with more epochs will improve the model performance significantly.
