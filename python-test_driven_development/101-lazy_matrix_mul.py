#!/usr/bin/python3
"""Module for lazy matrix multiplication using NumPy.

This module provides a function to multiply two matrices
using the NumPy library.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Returns the numpy matrix product of m_a and m_b.
    """
    return np.matmul(m_a, m_b)
