"""Logger module for HTTP request/response logging."""

import datetime
import json
import pathlib
from pathlib import Path

from requests import Response


class Logger:
    """Logs HTTP requests and responses to file for debugging."""

    dir_path = pathlib.Path(__file__).parent.parent
    file_name = f"log_{str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))}.log"
    logs_dir = Path(dir_path, "./logs")
    file_path = Path(logs_dir, file_name)

    @classmethod
    def _ensure_logs_dir(cls):
        """Create logs directory if it doesn't exist."""
        cls.logs_dir.mkdir(parents=True, exist_ok=True)

    @classmethod
    def write_log_to_file(cls, data: str):
        """Writes log data to file."""
        cls._ensure_logs_dir()
        with open(cls.file_path, "a", encoding="utf-8") as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, test_name: str, url: str, method: str, body=None):
        """Logs request details: method, URL, body."""
        data_to_add = "\n-----\n"
        data_to_add += f"Task: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        if body:
            if isinstance(body, dict):
                data_to_add += f"Request Body: {json.dumps(body, indent=2)}\n"
            else:
                data_to_add += f"Request Body: {body}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, result: Response, task_result: str = None):
        """Logs response details: status code, headers, body."""
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_to_add = f"Task result: {task_result}\n"
        data_to_add += f"Response code: {result.status_code}\n"
        data_to_add += f"Response text: {result.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += "\n-----\n"

        cls.write_log_to_file(data_to_add)
