import pandas as pd
import regex as re

def match_data_uo(class_df, source_data, match_type='meta'):
    results = {}

    for key, values in source_data.items():
        best_match_index = None
        max_meta_score = 0
        max_data_score = 0

        for index, row in class_df.iterrows():
            meta_pattern = row['metadata_rules']
            data_pattern = row['data_rules'] if 'data_rules' in row else None

            # Calculate metadata match score
            meta_match = re.fullmatch(meta_pattern, key)
            if meta_match:
                meta_score = len(meta_match.group(0))
                if meta_score > max_meta_score:
                    max_meta_score = meta_score
                    best_match_index = index

            if match_type == 'both' and meta_match:
                # Calculate data match score
                for value in values:
                    if isinstance(value, str):
                        data_match = re.fullmatch(data_pattern, value) if data_pattern else False
                        if data_match:
                            data_score = len(data_match.group(0))
                            if data_score > max_data_score:
                                max_data_score = data_score
                                best_match_index = index
                    elif isinstance(value, (int, float)):
                        data_match = re.fullmatch(data_pattern, str(value)) if data_pattern else False
                        if data_match:
                            data_score = len(data_match.group(0))
                            if data_score > max_data_score:
                                max_data_score = data_score
                                best_match_index = index
        
        if best_match_index is not None:
            results[key] = class_df.iloc[best_match_index].values.tolist()

    return results


def match_data1(class_df, source_data, match_type='meta'):
    results = {}

    for key, values in source_data.items():
        best_match_index = None
        max_meta_score = 0
        max_data_score = 0

        for row in class_df.itertuples(index=True):
            meta_pattern = row.metadata_rules
            data_pattern = row.data_rules if 'data_rules' in class_df.columns else None
            index = row.Index

            # Calculate metadata match score
            meta_match = re.fullmatch(meta_pattern, key)
            if meta_match:
                meta_score = len(meta_match.group(0))
                if meta_score > max_meta_score:
                    max_meta_score = meta_score
                    best_match_index = index

            if match_type == 'both' and meta_match:
                # Calculate data match score
                for value in values:
                    if isinstance(value, str):
                        data_match = re.fullmatch(data_pattern, value) if data_pattern else False
                        if data_match:
                            data_score = len(data_match.group(0))
                            if data_score > max_data_score:
                                max_data_score = data_score
                                best_match_index = index
                    elif isinstance(value, (int, float)):
                        data_match = re.fullmatch(data_pattern, str(value)) if data_pattern else False
                        if data_match:
                            data_score = len(data_match.group(0))
                            if data_score > max_data_score:
                                max_data_score = data_score
                                best_match_index = index
        print(max_meta_score, max_data_score)
        if best_match_index is not None:
            results[key] = class_df.iloc[best_match_index].values.tolist()

    return results



def find_best_match(class_df, source_data, match_type):
    result = {}
    for key, values in source_data.items():
        best_match = None
        best_match_score = 0
        for row in class_df.itertuples():
            meta_match = re.match(row.metadata_rules, key) is not None
            data_match = all(re.match(row.data_rules, str(value)) is not None for value in values)
            if match_type == 'meta' and meta_match:
                match_score = len(re.findall(row.metadata_rules, key))
                if match_score > best_match_score:
                    best_match = row
                    best_match_score = match_score
            elif match_type == 'both' and meta_match and data_match:
                match_score = len(re.findall(row.metadata_rules, key)) + sum(len(re.findall(row.data_rules, str(value))) for value in values)
                if match_score > best_match_score:
                    best_match = row
                    best_match_score = match_score
        if best_match is not None:
            result[key] = best_match
    return result



def find_best_match_extended(class_df, source_data, match_type):
    result = {}
    for key, values in source_data.items():
        best_match_index = None
        best_match_score = 0
        for row in class_df.itertuples(index=True):
            meta_match = re.match(row.metadata_rules, key) is not None
            data_match = all(re.match(row.data_rules, str(value)) is not None for value in values)
            if match_type == 'meta' and meta_match:
                match_score = len(re.findall(row.metadata_rules, key))
                if match_score > best_match_score:
                    best_match_index = row.Index
                    best_match_score = match_score
            elif match_type == 'both' and meta_match and data_match:
                match_score = len(re.findall(row.metadata_rules, key)) + sum(len(re.findall(row.data_rules, str(value))) for value in values)
                if match_score > best_match_score:
                    best_match_index = row.Index
                    best_match_score = match_score
        if best_match_index is not None:
            result[key] = class_df.iloc[best_match_index].values.tolist()
    return result


def match_data(class_df, source_data, match_type='meta'):
    results = {}

    for key, values in source_data.items():
        best_match_index = None
        max_meta_score = 0
        max_data_score = 0

        for row in class_df.itertuples(index=True):
            meta_pattern = row.metadata_rules
            data_pattern = row.data_rules if 'data_rules' in class_df.columns else None
            index = row.Index

            meta_score = 0
            data_score = 0

            # Calculate metadata match score
            meta_match = re.fullmatch(meta_pattern, key)
            if meta_match:
                meta_score = len(meta_match.group(0))
                if meta_score > max_meta_score:
                    max_meta_score = meta_score
                    best_match_index = index

            # If match_type is 'both' or if no metadata match but data match is possible
            if match_type == 'both' or not meta_match:
                for value in values:
                    value_str = str(value)
                    data_match = re.fullmatch(data_pattern, value_str) if data_pattern else None
                    if data_match:
                        data_score = len(data_match.group(0))
                        if data_score > max_data_score:
                            max_data_score = data_score
                            best_match_index = index

        if best_match_index is not None:
            results[key] = class_df.iloc[best_match_index].values.tolist()

    return results