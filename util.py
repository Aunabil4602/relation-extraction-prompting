import prompts
import json
from datetime import datetime
import logging

def get_sentence_with_tags(meta_data):
    token_with_tags = meta_data['token'].copy()

    token_with_tags[meta_data['subj_start']] = '<subject>' + token_with_tags[meta_data['subj_start']]
    token_with_tags[meta_data['subj_end']] = token_with_tags[meta_data['subj_end']] + '</subject>'
    token_with_tags[meta_data['obj_start']] = '<object>' + token_with_tags[meta_data['obj_start']]
    token_with_tags[meta_data['obj_end']] = token_with_tags[meta_data['obj_end']] + '</object>'

    return ' '.join(token_with_tags)

def setup_ways(ways, prompt, few_shot_type):
    relation_list = []

    for idx_way, way in enumerate(ways):
        idx_way = idx_way + 1

        assert len(way) > 0

        relation = way[0]['relation']
        prompt = prompt.replace(f'#RELATION_{idx_way}#', relation)
        relation_list.append(relation)

        if '_w_des' in few_shot_type:
            prompt = prompt.replace(f'#RELATION_DESCRIPTION_{idx_way}#', prompts.get_relation_description(relation))

        for idx_shot, shot in enumerate(way):
            idx_shot = idx_shot + 1

            assert shot['relation'] == relation

            sentence = get_sentence_with_tags(shot)
            prompt = prompt.replace(f'#SUPPORT_SENTENCE_{idx_way}_{idx_shot}#', sentence)

    prompt = prompt.replace('#RELATION_LIST#', ', '.join(relation_list))

    return prompt, relation_list

def setup_query(query, prompt):

    sentence = get_sentence_with_tags(query)
    prompt = prompt.replace('#QUERY_SENTENCE#', sentence)

    return prompt, query['relation']

def build_prompt(episode, few_shot_type = None):
    ways = episode['meta_train']
    query = episode['meta_test'][0]

    prompt = prompts.get_prompt_template(few_shot_type)

    prompt, relation_list = setup_ways(ways, prompt, few_shot_type)
    prompt, query_relation = setup_query(query, prompt)

    return prompt, query_relation, relation_list

def read_json_file(file_path):
  with open(file_path, 'r') as f:
    data = json.load(f)
  return data

def get_current_date_time():
    current_time = datetime.now()
    formatted_time = current_time.strftime('%Y%m%d-%H%M%S%f')

    return formatted_time

def get_simple_model_name(model_id):
    return model_id.replace('/', '-').replace('.', '').replace(':', '-')

def report_per_file_results(model_id, full_data, test_file):
    logging.info(f"reporting result for file: {test_file}")

    output_file = 'result/' + get_simple_model_name(model_id) + '-' + test_file + '-' + get_current_date_time() + '.txt'

    logging.info(f'Logging results of the test set to file: {output_file}')

    with open(output_file, 'w+') as f:
        
        f.write(model_id + '\n')

        for dd in full_data:
            f.write('@@@@@@@@@@@@@@@@@@@@@@@\n')
            f.write(dd[0] + '\n')
            f.write('$$$$$ query relation\n')
            f.write(dd[1] + '\n')
            f.write('$$$$$ relation list\n')
            f.write(str(dd[2]) + '\n')
            f.write('$$$$$ result\n')
            f.write(dd[3] + '\n')

def report_score_avg(model_id, test_type, precision_list, recall_list, f1_list):
    logging.info(f"reporting result for model: {model_id}")

    assert len(precision_list) == len(recall_list)
    assert len(precision_list) == len(f1_list)
    
    n = len(precision_list)
    assert n > 0

    logging.info("calculating avg over {n} files")

    avg_precision = sum(precision_list) / n
    avg_recall = sum(recall_list) / n
    avg_f1 = sum(f1_list) / n

    logging.info(f'Combined Avg Precision: {avg_precision:.2f}\n')
    logging.info(f'Combined Avg Recall: {avg_recall:.2f}\n')
    logging.info(f'Combined Avg F1: {avg_f1:.2f}\n')

    output_file = 'result/' + get_simple_model_name(model_id) + '-' + test_type + '-' + get_current_date_time() + '.txt'

    logging.info(f'Logging avg results of all test sets to file: {output_file}')

    with open(output_file, 'w+') as f:
        f.write(model_id + '\n')
        f.write(test_type + '\n')
        f.write(f'Avg Precision: {avg_precision:.2f}\n')
        f.write(f'Avg Recall: {avg_recall:.2f}\n')
        f.write(f'Avg F1: {avg_f1:.2f}\n')
