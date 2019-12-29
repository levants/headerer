# -*- coding: utf-8 -*-
"""
Created on Sep 04, 2019
Generates path to conda environment Python executable
@author: Levan Tsinadze
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
from pathlib import Path


def config():
    """
    Configure for conda environment
    Returns:
        conf: command line configuration parameters
    """
    parser = argparse.ArgumentParser('File name generator from header')
    parser.add_argument('--conda',
                        nargs='+',
                        type=str,
                        default=['/anaconda3'],
                        help='Anaconda installation')
    parser.add_argument('--env',
                        type=str,
                        default='base',
                        help='Conda environment name')
    conf = parser.parse_args()

    return conf


def find_bin(env_name: str, conda_root: Path = Path('/anaconda3')) -> str:
    """
    Find anaconda environment
    Args:
        env_name: environment name
        conda_root: conda installation root

    Returns:
        python_bin: executable of Python interpreter
    """
    conda_bin = conda_root / 'envs' / env_name / 'bin' / 'python'
    python_bin = str(conda_bin)

    return python_bin


if __name__ == '__main__':
    """Modify text for file name"""
    cf = config()
    conda_path = Path(*cf.conda)
    python_path = find_bin(cf.env, conda_root=conda_path)
    os.system(f'echo {python_path}| pbcopy')
    print(python_path)
