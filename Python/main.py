import math
from collections import Counter

def plurality_val(examples, target_attribute='class'):

    if not examples:
        return None
    classifications = [example[target_attribute] for example in examples]
    most_common_classification = Counter(classifications).most_common(1)

    if most_common_classification:
        return most_common_classification[0][0]
    return None


def calculate_entropy(examples, target_attribute='class'):
    if not examples:
        return 0.0  # An empty set has zero entropy

    num_examples = len(examples)
    if num_examples == 0:
        return 0.0

    # Count occurrences of each class label
    class_counts = Counter(example[target_attribute] for example in examples)
    entropy = 0.0

    # Apply the entropy formula
    for count in class_counts.values():
        probability = count / num_examples
        if probability > 0:  # Avoid math.log2(0) which is undefined
            entropy -= probability * math.log2(probability)
    return entropy


def calculate_information_gain(examples, attribute, target_attribute='class'):

    if not examples:
        return 0.0

    total_entropy = calculate_entropy(examples, target_attribute)

    attribute_values = set(example[attribute] for example in examples)

    weighted_avg_entropy = 0.0
    # Calculate the weighted average entropy of subsets formed by splitting on 'attribute'
    for value in attribute_values:
        subset = [e for e in examples if e[attribute] == value]

        if subset:  # Ensure the subset is not empty to avoid division by zero or errors
            # Weight the entropy of the subset by its proportion in the total examples
            weighted_avg_entropy += (len(subset) / len(examples)) * calculate_entropy(subset, target_attribute)

    return total_entropy - weighted_avg_entropy


# --- Part 2: Main Decision Tree Learning Algorithm (Algorithm 4) ---

def dt_learning(examples, attributes, parent_examples, target_attribute='class'):
    # --- Base Cases of the Recursion (Stopping Conditions) ---

    # 1. if empty(examples) then return PLURALITY-VAL(parent examples)
    #    This occurs when a specific branch (e.g., 'A=0') leads to no training examples.
    #    In this case, we use the majority class from the parent node's examples.
    if not examples:
        return plurality_val(parent_examples, target_attribute)

    # 2. else if all examples have same classification then return the classification
    #    If all examples at this node belong to the same class, this node is pure,
    #    and we can make a definitive classification. This node becomes a leaf.
    classifications_at_node = set(example[target_attribute] for example in examples)
    if len(classifications_at_node) == 1:
        return classifications_at_node.pop()  # Return the single classification value

    # 3. else if empty(attributes) then return PLURALITY-VAL(examples)
    #    If there are no more attributes left to split on, but the examples
    #    are still mixed (not all same classification), we can't split further.
    #    We make this node a leaf, returning the majority class among the current examples.
    if not attributes:
        return plurality_val(examples, target_attribute)

    # --- Recursive Step (Finding the Best Split) ---

    # 4. else: (Proceed with finding the best attribute to split on)

    #    A <- argmax_{a in attributes} IMPORTANCE(a, examples)
    #    Find the attribute that provides the highest Information Gain.
    best_attribute = None
    max_gain = -1.0  # Initialize with a very low value

    for attribute in attributes:
        gain = calculate_information_gain(examples, attribute, target_attribute)
        if gain > max_gain:
            max_gain = gain
            best_attribute = attribute

    # If no attribute provides any gain (e.g., all remaining attributes are irrelevant)
    # or if max_gain is still -1 (meaning no attributes were processed or available),
    # then we default to a plurality vote for the current examples.
    if best_attribute is None:
        return plurality_val(examples, target_attribute)

    # tree <- a new decision tree with root test A
    # Create the node for the chosen best attribute
    tree = {best_attribute: {}}

    # Determine the possible binary values for the best_attribute.
    # Assuming binary attributes are 0 and 1. If your data uses 'Yes'/'No' or 'True'/'False',
    # you might need to adjust this list directly (e.g., binary_attribute_values = ['Yes', 'No']).
    # Getting values from current examples ensures we consider values that actually appear.
    # Sorting ensures consistent branch order (e.g., 0 then 1).
    possible_attribute_values = sorted(list(set(example[best_attribute] for example in examples)))

    for vk in possible_attribute_values:
        exs = [e for e in examples if e[best_attribute] == vk]
        subtree = dt_learning(
            exs,
            [attr for attr in attributes if attr != best_attribute],
            examples,
            target_attribute
        )
        tree[best_attribute][vk] = subtree

    return tree



if __name__ == "__main__":
    training_data_set_my_choice = [
        {'A': 1, 'B': 1, 'C': 0, 'class': 1},
        {'A': 1, 'B': 0, 'C': 0, 'class': 0},
        {'A': 0, 'B': 1, 'C': 1, 'class': 1},
        {'A': 0, 'B': 0, 'C': 1, 'class': 0},
        {'A': 1, 'B': 1, 'C': 1, 'class': 1},
        {'A': 0, 'B': 1, 'C': 0, 'class': 0},
        {'A': 1, 'B': 0, 'C': 1, 'class': 0},
        {'A': 0, 'B': 0, 'C': 0, 'class': 0},
    ]

    all_feature_attributes = ['A', 'B', 'C']
    classification_attribute_name = 'class'

    print("--- Starting Decision Tree Learning (Algorithm 4) ---")
    print(f"Training on {len(training_data_set_my_choice)} examples with attributes: {all_feature_attributes}")

    learned_decision_tree = dt_learning(
        training_data_set_my_choice,
        all_feature_attributes,
        [],
        classification_attribute_name
    )

    print("\n--- Learned Decision Tree Structure ---")
    import json

    print(json.dumps(learned_decision_tree, indent=4))

    def predict_with_tree(tree, example_to_predict):
        if not isinstance(tree, dict):
            return tree

        attribute_to_test = list(tree.keys())[0]

        attribute_value_in_example = example_to_predict.get(attribute_to_test)

        if attribute_value_in_example in tree[attribute_to_test]:
            next_subtree = tree[attribute_to_test][attribute_value_in_example]
            return predict_with_tree(next_subtree, example_to_predict)
        else:
            print(f"Warning: Attribute '{attribute_to_test}' has unexpected value '{attribute_value_in_example}' "
                  f"in the test example. No matching branch found in the tree.")
            return None


    print("\n--- Testing the Learned Tree with New Examples ---")

    test_example_1 = {'A': 1, 'B': 1, 'C': 0}  # Based on training data, expected: 1
    test_example_2 = {'A': 0, 'B': 0, 'C': 1}  # Based on training data, expected: 0
    test_example_3 = {'A': 1, 'B': 0, 'C': 1}  # Based on training data, expected: 0
    test_example_4 = {'A': 0, 'B': 1, 'C': 0}  # Based on training data, expected: 0
    test_example_5 = {'A': 1, 'B': 1, 'C': 1}  # Expected: 1

    print(f"Prediction for {test_example_1}: {predict_with_tree(learned_decision_tree, test_example_1)}")
    print(f"Prediction for {test_example_2}: {predict_with_tree(learned_decision_tree, test_example_2)}")
    print(f"Prediction for {test_example_3}: {predict_with_tree(learned_decision_tree, test_example_3)}")
    print(f"Prediction for {test_example_4}: {predict_with_tree(learned_decision_tree, test_example_4)}")
    print(f"Prediction for {test_example_5}: {predict_with_tree(learned_decision_tree, test_example_5)}")
