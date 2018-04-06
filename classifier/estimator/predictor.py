import tensorflow as tf
import random

from . import model
from . import data


LABELS = data.LABELS
DICTIONARY = data.DICTIONARY


def eval_input_fn(features, labels, batch_size):
    """An input function for prediction"""
    features = dict(features)
    if labels is None:
        # No labels, use only features.
        inputs = features
    else:
        inputs = (features, labels)

    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    # Batch the examples
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)

    # Return the dataset.
    return dataset


def predictFromModel(predict_x):
    classifier, args = model.getModelData()

    # Generate predictions from the model
    predictions = classifier.predict(input_fn=lambda: eval_input_fn(
        predict_x, labels=None, batch_size=args.batch_size))

    results = []
    probabilityArray = []

    for pred_dict in predictions:
        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]
        label = LABELS[class_id]

        # Create unique label array
        if label not in results:
            results.append(label)
            probabilityArray.append(probability)
        else:
            index = results.index(label)
            if probabilityArray[index] < probability:
                probabilityArray[index] = probability

        # Filter only top five probability results
        if len(results) > 5:
            minVal = min(probabilityArray)
            minValIndex = probabilityArray.index(minVal)
            results.pop(minValIndex)
            probabilityArray.pop(minValIndex)

    return results


def contentClassification(string):
    para = string.lower().split(" ")
    wordIndexes = [[], [], [], []]
    pointer = 0

    for word in para:
        try:
            index = DICTIONARY.index(word)
            if index != -1:
                wordIndexes[pointer].append(index)
                if pointer < 3:
                    pointer += 1
                else:
                    pointer = 0
        except ValueError:
            print(word, 'does not exist in dic.')

    maxLength = len(wordIndexes[0])
    if maxLength == 0:
        return []

    for i in range(1, 4):
        if len(wordIndexes[i]) < maxLength:
            randomAtr = wordIndexes[int(random.uniform(0, i))]
            randomItem = randomAtr[int(random.uniform(0, len(randomAtr)))]
            wordIndexes[i].append(randomItem)

    predictAtrs = {
        'Attribute1': wordIndexes[0],
        'Attribute2': wordIndexes[1],
        'Attribute3': wordIndexes[2],
        'Attribute4': wordIndexes[3],
    }

    return predictFromModel(predictAtrs)
