import os
import sys
from pathlib import Path

import argparse
sys.path.append(os.path.realpath(Path(__file__).parent))
from infra import url_actions as url_action


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', default="Test", type=str, help='URL address for a screenshot')
    parser.add_argument('--path', default="results", type=str, help='path of directory to save screenshot')
    args = parser.parse_args()
    return args


def run(args):
    """
    Runs the script - validating URL input and sends back a screenshot once it's valid
    """
    _URL = os.environ.get('URL')
    validated_url = url_action.validate_url(_URL or args.url)
    url_action.get_screenshot(
        url_address=validated_url,
        path=args.path
    )


if __name__ == '__main__':
    _args = get_args()
    run(_args)
