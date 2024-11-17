PROMPT_TEMPLATE = dict()

PROMPT_TEMPLATE['1_shots_wo_rule'] = '''Please choose the correct relation between the entities in the query sentence below. You can choose between five relations: #RELATION_LIST#. If none of the five relations are correct, choose no_relation.

Here are some examples for each of the five relations. A relation always connects a subject and object entity. We indicate the entities with <subject> and <object> tags.

1. Relation “#RELATION_1#”
Support sentence 1: #SUPPORT_SENTENCE_1_1#

2. Relation “#RELATION_2#”
Support sentence 1: #SUPPORT_SENTENCE_2_1#

3. Relation “#RELATION_3#”
Support sentence 1: #SUPPORT_SENTENCE_3_1#

4. Relation “#RELATION_4#”
Support sentence 1: #SUPPORT_SENTENCE_4_1#

5. Relation “#RELATION_5#”
Support sentence 1: #SUPPORT_SENTENCE_5_1#

Query sentence: #QUERY_SENTENCE#

Only output the correct relation, nothing else.'''

PROMPT_TEMPLATE['5_shots_wo_rule'] = '''Please choose the correct relation between the entities in the query sentence below. You can choose between five relations: #RELATION_LIST#. If none of the five relations are correct, choose no_relation.

Here are some examples for each of the five relations. A relation always connects a subject and object entity. We indicate the entities with <subject> and <object> tags.

1. Relation “#RELATION_1#”
Support sentence 1: #SUPPORT_SENTENCE_1_1#
Support sentence 2: #SUPPORT_SENTENCE_1_2#
Support sentence 3: #SUPPORT_SENTENCE_1_3#
Support sentence 4: #SUPPORT_SENTENCE_1_4#
Support sentence 5: #SUPPORT_SENTENCE_1_5#

2. Relation “#RELATION_2#”
Support sentence 1: #SUPPORT_SENTENCE_2_1#
Support sentence 2: #SUPPORT_SENTENCE_2_2#
Support sentence 3: #SUPPORT_SENTENCE_2_3#
Support sentence 4: #SUPPORT_SENTENCE_2_4#
Support sentence 5: #SUPPORT_SENTENCE_2_5#

3. Relation “#RELATION_3#”
Support sentence 1: #SUPPORT_SENTENCE_3_1#
Support sentence 2: #SUPPORT_SENTENCE_3_2#
Support sentence 3: #SUPPORT_SENTENCE_3_3#
Support sentence 4: #SUPPORT_SENTENCE_3_4#
Support sentence 5: #SUPPORT_SENTENCE_3_5#

4. Relation “#RELATION_4#”
Support sentence 1: #SUPPORT_SENTENCE_4_1#
Support sentence 2: #SUPPORT_SENTENCE_4_2#
Support sentence 3: #SUPPORT_SENTENCE_4_3#
Support sentence 4: #SUPPORT_SENTENCE_4_4#
Support sentence 5: #SUPPORT_SENTENCE_4_5#

5. Relation “#RELATION_5#”
Support sentence 1: #SUPPORT_SENTENCE_5_1#
Support sentence 2: #SUPPORT_SENTENCE_5_2#
Support sentence 3: #SUPPORT_SENTENCE_5_3#
Support sentence 4: #SUPPORT_SENTENCE_5_4#
Support sentence 5: #SUPPORT_SENTENCE_5_5#

Query sentence: #QUERY_SENTENCE#

Only output the correct relation, nothing else.'''

def get_prompt_template(prompt_name):
    assert prompt_name in PROMPT_TEMPLATE.keys()
    
    return PROMPT_TEMPLATE[prompt_name]
