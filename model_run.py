######## imports

import logging
import os
import sys
import time

# import openai
import torch
import transformers
from huggingface_hub import login, notebook_login
from openai import OpenAI
from sklearn.metrics import f1_score, precision_score, recall_score
from transformers import pipeline

import scorer
import util

####### Logging

def setup_logger(model_id, prompt_type):

    log_file_name = 'log/' + util.get_simple_model_name(model_id) + '-' + prompt_type + util.get_current_date_time() + '.log'

    logging.basicConfig(
        filename=log_file_name,  # Output file
        level=logging.INFO,  # Log level
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Set the console log level
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logging.getLogger().addHandler(console_handler)

    def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

    sys.excepthook = log_uncaught_exceptions

    print(f"Configuring the logs to file: {log_file_name}")
    return log_file_name


######## authentications

def do_authentication():
    logging.info("Doing authentication")

    # huggingface
    transformers.logging.set_verbosity_error()
    login(token=os.environ['HF_TOKEN'])

    # OpenAI
    # client = OpenAI()

    logging.info("Authentication successfull")

######## models

def setup_model(model_id):
    logging.info("Setting up model.")

    model_download_start_time = time.time()

    pipe= pipeline(
        "text-generation",
        model=model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        max_new_tokens = 16
    )

    logging.info(f"model downloaded or loaded from cache. time taken {time.time() - model_download_start_time}s")

    return pipe

def get_reply(pipe, prompt):
    # # openai
    # completion = client.chat.completions.create(
    #     model="gpt-4o-2024-08-06",
    #     messages=[
    #         {"role": "user", "content": prompt}
    #     ]
    # )
    # result = completion.choices[0].message.content

    # huggingface model
    messages = [{"role": "user", "content": prompt}]
    reply = pipe(messages)[0]['generated_text'][1]['content']

    return reply

######## run

def run(model_id, pipe, prompt_type, prompt_details):
    logging.info(f"Running the model: {model_id}")

    NO_RELATION = 'no_relation'
    PRINT_EVERY = 100

    time_start = time.time()

    golds = []
    preds = []
    full_data = []
    precision_list = []
    recall_list = []
    f1_list = []

    for file in os.listdir('data'):
        if file.endswith('.json') and prompt_type in file and '160290' in file:
            file_path = os.path.join('data', file)
            data = util.read_json_file(file_path)

            episodes = data[0]

            logging.info(f"Started to run file: {file}")

            total_episodes = len(episodes)

            for idx_episode, episode in enumerate( episodes):
                prompt, query_relation, relation_list = util.build_prompt(episode, few_shot_type = prompt_type + prompt_details)

                assert NO_RELATION not in relation_list

                reply = get_reply(pipe, prompt)

                full_data.append((prompt, query_relation, relation_list, reply))

                if query_relation in relation_list:
                    golds.append(query_relation)
                else:
                    golds.append(NO_RELATION)

                preds.append(reply)

                if idx_episode > 0 and idx_episode % PRINT_EVERY == 0:
                    current_time = time.time()
                    elapsed_time = current_time - time_start

                    log_step_message = f"Episode: {idx_episode}/{total_episodes}, time passed: {(elapsed_time/60):.2f} mins"
                    logging.info(log_step_message)

            logging.info(f"End running the file: {file}")

            precision, recall, f1 = scorer.score(golds, preds, False)
            precision_list.append(precision)
            recall_list.append(recall)
            f1_list.append(f1)

            logging.info(f'Avg Precision: {precision:.2f}\n')
            logging.info(f'Avg Recall: {recall:.2f}\n')
            logging.info(f'Avg F1: {f1:.2f}\n')

            util.report_per_file_results(model_id, full_data, file)

            break
    
    util.report_score_avg(model_id, prompt_type + prompt_details, precision_list, recall_list, f1_list)

    logging.info(f"Completed the model: {model_id}")
    
####### main

if __name__ == "__main__":
    # meta-llama/Llama-3.2-3B-Instruct
    # meta-llama/Llama-3.2-90B-Vision-Instruct
    # meta-llama/Llama-3.1-70B-Instruct
    # # meta-llama/Llama-3.1-405B-Instruct-FP8 
    # # meta-llama/Llama-3.1-405B-Instruct

    MODEL_ID = "meta-llama/Llama-3.1-70B-Instruct"
    PROMPT_TYPE = '1_shots'
    PROMPT_DETAILS = '_w_rule' # _wo_rule_w_des, _wo_rule, _w_rule

    setup_logger(MODEL_ID, PROMPT_TYPE + PROMPT_DETAILS)

    logging.info("Application started.")
    logging.info(f"Running for model: {MODEL_ID}")
    logging.info(f"Running for prompt_type: {PROMPT_TYPE + PROMPT_DETAILS}")

    do_authentication()
    pipe = setup_model(MODEL_ID)
    run(MODEL_ID, pipe, PROMPT_TYPE, PROMPT_DETAILS)

    logging.info("Application end.")
