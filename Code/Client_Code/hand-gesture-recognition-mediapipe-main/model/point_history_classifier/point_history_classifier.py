#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf
import os

class PointHistoryClassifier(object):
    def __init__(
        self,
        model_path='Code/Client_Code/hand-gesture-recognition-mediapipe-main/model/point_history_classifier/point_history_classifier.tflite',
        score_th=0.5,
        invalid_value=0,
        num_threads=1,
    ):
        model_path = os.path.abspath(model_path)
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")

        self.interpreter = tf.lite.Interpreter(model_path=model_path,
                                               num_threads=num_threads)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.output_details = self.interpreter.get_output_details()

        # Expected input length from model
        self.expected_length = self.input_details[0]['shape'][1]
        self.score_th = score_th
        self.invalid_value = invalid_value

    def __call__(self, point_history):
        # Flatten and pad/truncate to expected length
        point_history = np.array(point_history, dtype=np.float32).flatten()
        if len(point_history) < self.expected_length:
            pad_size = self.expected_length - len(point_history)
            point_history = np.pad(point_history, (0, pad_size), mode='constant')
        elif len(point_history) > self.expected_length:
            point_history = point_history[:self.expected_length]

        # Run inference
        input_index = self.input_details[0]['index']
        self.interpreter.set_tensor(input_index, [point_history])
        self.interpreter.invoke()

        output_index = self.output_details[0]['index']
        result = self.interpreter.get_tensor(output_index)

        result_index = np.argmax(np.squeeze(result))
        if np.squeeze(result)[result_index] < self.score_th:
            result_index = self.invalid_value

        return result_index
