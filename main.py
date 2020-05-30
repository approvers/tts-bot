"""
TTSをしたり
事前に指定された音源とかを通話に入って流すBOT
"""
from src.client import MainClient

if __name__ == "__main__":
    client = MainClient()
    client.run()
