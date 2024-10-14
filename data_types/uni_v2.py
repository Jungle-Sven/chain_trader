from pydantic import BaseModel, Field
from datetime import datetime

# Define the Pydantic model for token info
class TokenInfo(BaseModel):
    token0: str
    token1: str
    pool_address: str
    block_number: int
    name0: str 
    symbol0: str
    reserve0: float
    name1: str 
    symbol1: str
    reserve1: float

# Define the Pydantic model for swaps
class Swap(BaseModel):
    ts_datetime: datetime
    type: str
    block_number: int
    block_hash: str
    timestamp: int
    from_: str = Field(..., alias="from")
    to: str
    amount0_in: float
    amount1_in: float
    amount0_out: float
    amount1_out: float


'''
# Example usage
token_data = {
    "token0": "ETH",
    "token1": "USDC",
    "pool_address": "0xabc123",
    "block_number": 123456,
    "reserve0": 100.0,
    "reserve1": 2000.0,
    "name0": 'poh',
    "name1": 'poh1',
    "symbol0": 'POH',
    "symbol1": 'POH111'
}

token = TokenInfo(**token_data)
print(token)
'''

if __name__ == '__main__':
    pass 
