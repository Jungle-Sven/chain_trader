# chain_trader

## Description
This is a custom event-driven onchain trading backtesting framework for testing and executing onchain trading strategies.

## Features
- 

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Jungle-Sven/chain_trader/tree/main.git
    cd your-repo-name
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## File Structure
```markdown
/chain_trader
│
├── /core
│   ├── __init__.py
│   ├── event_processor.py        # Handles incoming swap events and processes them per block.
│   ├── strategy.py               # Base class for defining trading strategies.
│   ├── risk_manager.py           # Handles stop losses, take profits, and sizing logic.
│   ├── metrics.py                # Performance metrics like Sharpe ratio, max drawdown, etc.
│   ├── order_executor.py         # Handles mock trade executions (buy/sell orders).
│   ├── position_manager.py       # Tracks open positions, P&L, and trading history.
│   ├── fees.py                   # Handles fees related to trades.
│   ├── utils.py                  # Utility functions (e.g., reading data, formatting).
│
├── /data
│   ├── __init__.py
│   ├── data_handler.py           # Loads and processes historical data for backtesting.
│   ├── swap_events.py            # Processes swap events from the DataFrame.
│
├── /live_execution
│   ├── __init__.py
│   ├── execution_manager.py      # For future use: executing real trades live.
│   ├── live_event_processor.py   # Processing live swap events and price feeds.
│
├── /data_types
│   ├── __init__.py
│   ├── token_info.py             # Data structure for tokens and pools.
│   ├── swaps.py                  # Data structure for swap events.
│
├── /examples
│   ├── simple_strategy.py        # Example of a simple trading strategy using the framework.
│
├── /tests
│   ├── test_strategy.py          # Unit tests for strategy backtesting.
│   ├── test_metrics.py           # Unit tests for performance metrics.
│
├── setup.py                      # Setup script for installing the library.
├── README.md                     # Library documentation.
├── LICENSE                       # License for the library.
└── requirements.txt              # Python dependencies.

## License
Licensed under the MIT License.
