import unittest
from unittest.mock import patch, mock_open, Mock

from src.mock_up import *




class TestMockUp(unittest.TestCase):
    ''' MockUp unittest class '''

    @patch('builtins.open', new_callable=mock_open, read_data="file content")
    def test_read_data_from_file_success(self, mock_open):
        filename = "something.txt"
        elreturn = read_data_from_file(filename)
        mock_open.assert_called_with(filename, 'r')
        # didnt understand the mock_open thing, but it works
        # either this mock_open().read
        mock_open().read.assert_called_once()
        self.assertEqual(elreturn, "file content")
    

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_read_data_from_file_not_found(self, mock_open):
        filename = "soething.txt"
        with self.assertRaises(FileNotFoundError):
            read_data_from_file(filename)
        mock_open.assert_called_with(filename, 'r')


    @patch('subprocess.run')
    def test_execute_command_success(self, mock_run):
        mock_run.return_value = Mock(stdout="command output")
        result = execute_command(["echo", "Hello"])
        
        mock_run.assert_called_with(["echo", "Hello"], capture_output=True, text=True)
        
        self.assertEqual(result, "command output")

    
    @patch('subprocess.run')
    def test_execute_command_failure(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(returncode=1, cmd="echo Hello")
        
        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["echo", "Hello"])
        
        mock_run.assert_called_with(["echo", "Hello"], capture_output=True, text=True)

    
    @patch('time.time', return_value=5)  
    def test_action_a(self, mock_time):
        result = perform_action_based_on_time()
        
        self.assertEqual(result, 'Action A')

    @patch('time.time', return_value=15) 
    def test_action_b(self, mock_time):
        result = perform_action_based_on_time()
        
        self.assertEqual(result, 'Action B')