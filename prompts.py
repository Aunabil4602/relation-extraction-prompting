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

PROMPT_TEMPLATE['1_shots_wo_rule_w_des'] = '''Please choose the correct relation between the entities in the query sentence below. You can choose between five relations: #RELATION_LIST#. If none of the five relations are correct, choose no_relation.

Here are some examples for each of the five relations along with the description of the relation. A relation always connects a subject and object entity. We indicate the entities with <subject> and <object> tags.

1. Relation “#RELATION_1#”
Relation Description: #RELATION_DESCRIPTION_1#
Support sentence 1: #SUPPORT_SENTENCE_1_1#

2. Relation “#RELATION_2#”
Relation Description: #RELATION_DESCRIPTION_2#
Support sentence 1: #SUPPORT_SENTENCE_2_1#

3. Relation “#RELATION_3#”
Relation Description: #RELATION_DESCRIPTION_3#
Support sentence 1: #SUPPORT_SENTENCE_3_1#

4. Relation “#RELATION_4#”
Relation Description: #RELATION_DESCRIPTION_4#
Support sentence 1: #SUPPORT_SENTENCE_4_1#

5. Relation “#RELATION_5#”
Relation Description: #RELATION_DESCRIPTION_5#
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

PROMPT_TEMPLATE['5_shots_wo_rule_w_des'] = '''Please choose the correct relation between the entities in the query sentence below. You can choose between five relations: #RELATION_LIST#. If none of the five relations are correct, choose no_relation.

Here are some examples for each of the five relations along with the description of the relation. A relation always connects a subject and object entity. We indicate the entities with <subject> and <object> tags.

1. Relation “#RELATION_1#”
Relation Description: #RELATION_DESCRIPTION_1#
Support sentence 1: #SUPPORT_SENTENCE_1_1#
Support sentence 2: #SUPPORT_SENTENCE_1_2#
Support sentence 3: #SUPPORT_SENTENCE_1_3#
Support sentence 4: #SUPPORT_SENTENCE_1_4#
Support sentence 5: #SUPPORT_SENTENCE_1_5#

2. Relation “#RELATION_2#”
Relation Description: #RELATION_DESCRIPTION_2#
Support sentence 1: #SUPPORT_SENTENCE_2_1#
Support sentence 2: #SUPPORT_SENTENCE_2_2#
Support sentence 3: #SUPPORT_SENTENCE_2_3#
Support sentence 4: #SUPPORT_SENTENCE_2_4#
Support sentence 5: #SUPPORT_SENTENCE_2_5#

3. Relation “#RELATION_3#”
Relation Description: #RELATION_DESCRIPTION_3#
Support sentence 1: #SUPPORT_SENTENCE_3_1#
Support sentence 2: #SUPPORT_SENTENCE_3_2#
Support sentence 3: #SUPPORT_SENTENCE_3_3#
Support sentence 4: #SUPPORT_SENTENCE_3_4#
Support sentence 5: #SUPPORT_SENTENCE_3_5#

4. Relation “#RELATION_4#”
Relation Description: #RELATION_DESCRIPTION_4#
Support sentence 1: #SUPPORT_SENTENCE_4_1#
Support sentence 2: #SUPPORT_SENTENCE_4_2#
Support sentence 3: #SUPPORT_SENTENCE_4_3#
Support sentence 4: #SUPPORT_SENTENCE_4_4#
Support sentence 5: #SUPPORT_SENTENCE_4_5#

5. Relation “#RELATION_5#”
Relation Description: #RELATION_DESCRIPTION_5#
Support sentence 1: #SUPPORT_SENTENCE_5_1#
Support sentence 2: #SUPPORT_SENTENCE_5_2#
Support sentence 3: #SUPPORT_SENTENCE_5_3#
Support sentence 4: #SUPPORT_SENTENCE_5_4#
Support sentence 5: #SUPPORT_SENTENCE_5_5#

Query sentence: #QUERY_SENTENCE#

Only output the correct relation, nothing else.'''

RELATION_DESCRIPTION = {
    "org:alternate_names": "an organization's alternate names",
    "org:city_of_headquarters": "an organization's city of headquarters",
    "org:country_of_headquarters": "an organization's country of headquarters",
    "org:dissolved": "an organization's date of dissolution",
    "org:founded": "an organization's date of founding",
    "org:founded_by": " an organization's founder",
    "org:member_of": "an organization's membership of another entity",
    "org:members": "an organization's members",
    "org:number_of_employees/members": "an organization's number of employees or members",
    "org:parents": "an organization's parents",
    "org:political/religious_affiliation": "an organization's political or religious affiliation",
    "org:shareholders": "an organization's shareholders",
    "org:stateorprovince_of_headquarters": "an organization's state or province of headquarters",
    "org:subsidiaries": "an organization's subsidiaries",
    "org:top_members/employees": "an organization's top members or employees",
    "org:website": "an organization's website",
    "per:age": "a person's age",
    "per:alternate_names": "a person's alternate names",
    "per:cause_of_death": "a person's cause of death",
    "per:charges": "a person's criminal charges",
    "per:children": "a person's children",
    "per:cities_of_residence": "a person's cities of residence",
    "per:city_of_birth": "a person's city of birth",
    "per:city_of_death": "a person's city of death",
    "per:countries_of_residence": "a person's countries of residence",
    "per:country_of_birth": "a person's country of birth",
    "per:country_of_death": "a person's country of death",
    "per:date_of_birth": "a person's date of birth",
    "per:date_of_death": "a person's date of death",
    "per:employee_of": "a person's employer",
    "per:origin": "a person's city or country of origin",
    "per:other_family": "a person's other family",
    "per:parents": "a person's parents",
    "per:religion": "a person's religion",
    "per:schools_attended": "schools attended by a person",
    "per:siblings": "a person's siblings",
    "per:spouse": "a person's spouse",
    "per:stateorprovince_of_birth": "a person's state or province of birth",
    "per:stateorprovince_of_death": "a person's state or province of death",
    "per:stateorprovinces_of_residence": "a person's state or province of residence",
    "per:title": "a person's title",
}

def get_prompt_template(prompt_name):
    assert prompt_name in PROMPT_TEMPLATE.keys()
    
    return PROMPT_TEMPLATE[prompt_name]

def get_relation_description(relation):
    assert relation in RELATION_DESCRIPTION.keys()

    return RELATION_DESCRIPTION[relation]
