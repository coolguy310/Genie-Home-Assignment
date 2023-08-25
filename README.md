# Project Setup

## Prerequisites
Install the following tools:
- make
- Python 3.10
- docker-compose to initialize and run the database

## Installation

Install the application dependencies:
```shell
make init
```

## Usage

1. Start the database:
    ```shell
    docker-compose up -d
    ```

2. Start the application in the development mode:
    ```shell
    make run
    ```

After executing the last command, application should start up and expose api at: <http://localhost:8080/graphql>

To filter and paginate use:

`baseAssetSymbol`: is a variable that you can provide to filter trades based on the base asset symbol.

`page`: is a variable for the page number you want to retrieve.

`pageSize`: is a variable for the number of trades per page.

```
{
  management {
    tradeResults(baseAssetSymbol: "", page: 1, pageSize: 10) {
      totalCount
      trades {
        base
        quote
        fee {
          amount
          currency
        }
        transactionTime
        labels {
          key
          value
        }
      }
    }
  }
}
```

