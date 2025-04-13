"""
transaction.py - Transaction Model for Muzzy Tracker

This module defines the Transaction class, which represents a financial transaction
in the Muzzy Tracker application. It includes methods for validation, categorization,
and data manipulation.
"""

from datetime import datetime
from typing import Dict, Any, Optional, List

class Transaction:
    """
    Represents a financial transaction in the Muzzy Tracker application.
    """
    
    def __init__(self, 
                 transaction_id: str,
                 date: str,
                 description: str,
                 amount: float,
                 category: Optional[str] = None,
                 account: Optional[str] = None,
                 notes: Optional[str] = None,
                 status: str = 'cleared',
                 import_batch_id: Optional[str] = None,
                 import_date: Optional[str] = None):
        """
        Initialize a Transaction object.
        
        Args:
            transaction_id: Unique identifier for the transaction
            date: Transaction date (YYYY-MM-DD format)
            description: Description or merchant name
            amount: Transaction amount (negative for expenses, positive for income)
            category: Transaction category
            account: Source account
            notes: Additional notes
            status: Transaction status (cleared, pending, etc.)
            import_batch_id: ID of the import batch this transaction belongs to
            import_date: Date when this transaction was imported
        """
        self.id = transaction_id
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category
        self.account = account
        self.notes = notes
        self.status = status
        self.import_batch_id = import_batch_id
        self.import_date = import_date
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Transaction':
        """
        Create a Transaction object from a dictionary.
        
        Args:
            data: Dictionary containing transaction data
            
        Returns:
            Transaction: A new Transaction object
        """
        return cls(
            transaction_id=data.get('id'),
            date=data.get('date'),
            description=data.get('description'),
            amount=data.get('amount'),
            category=data.get('category'),
            account=data.get('account'),
            notes=data.get('notes'),
            status=data.get('status', 'cleared'),
            import_batch_id=data.get('import_batch_id'),
            import_date=data.get('import_date')
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Transaction object to a dictionary.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the transaction
        """
        return {
            'id': self.id,
            'date': self.date,
            'description': self.description,
            'amount': self.amount,
            'category': self.category,
            'account': self.account,
            'notes': self.notes,
            'status': self.status,
            'import_batch_id': self.import_batch_id,
            'import_date': self.import_date
        }
    
    def is_expense(self) -> bool:
        """
        Check if the transaction is an expense.
        
        Returns:
            bool: True if the transaction is an expense, False otherwise
        """
        return self.amount < 0
    
    def is_income(self) -> bool:
        """
        Check if the transaction is income.
        
        Returns:
            bool: True if the transaction is income, False otherwise
        """
        return self.amount > 0
    
    def get_formatted_amount(self) -> str:
        """
        Get the transaction amount formatted as a currency string.
        
        Returns:
            str: Formatted amount string
        """
        sign = '-' if self.is_expense() else '+'
        return f"{sign}${abs(self.amount):.2f}"
    
    def get_formatted_date(self, format_str: str = '%b %d, %Y') -> str:
        """
        Get the transaction date formatted according to the specified format.
        
        Args:
            format_str: Date format string
            
        Returns:
            str: Formatted date string
        """
        try:
            date_obj = datetime.strptime(self.date, '%Y-%m-%d')
            return date_obj.strftime(format_str)
        except ValueError:
            return self.date


class TransactionBatch:
    """
    Represents a batch of transactions imported together.
    """
    
    def __init__(self, batch_id: str, transactions: List[Transaction], import_date: str):
        """
        Initialize a TransactionBatch object.
        
        Args:
            batch_id: Unique identifier for the batch
            transactions: List of Transaction objects in the batch
            import_date: Date when the batch was imported
        """
        self.id = batch_id
        self.transactions = transactions
        self.import_date = import_date
    
    @property
    def total_transactions(self) -> int:
        """
        Get the total number of transactions in the batch.
        
        Returns:
            int: Number of transactions
        """
        return len(self.transactions)
    
    @property
    def total_income(self) -> float:
        """
        Get the total income in the batch.
        
        Returns:
            float: Total income
        """
        return sum(t.amount for t in self.transactions if t.is_income())
    
    @property
    def total_expenses(self) -> float:
        """
        Get the total expenses in the batch.
        
        Returns:
            float: Total expenses
        """
        return sum(t.amount for t in self.transactions if t.is_expense())
    
    @property
    def net_amount(self) -> float:
        """
        Get the net amount (income - expenses) in the batch.
        
        Returns:
            float: Net amount
        """
        return self.total_income + self.total_expenses
    
    @property
    def date_range(self) -> Dict[str, str]:
        """
        Get the date range of transactions in the batch.
        
        Returns:
            Dict[str, str]: Dictionary with 'start' and 'end' dates
        """
        if not self.transactions:
            return {'start': None, 'end': None}
        
        dates = [datetime.strptime(t.date, '%Y-%m-%d') for t in self.transactions]
        min_date = min(dates).strftime('%Y-%m-%d')
        max_date = max(dates).strftime('%Y-%m-%d')
        
        return {'start': min_date, 'end': max_date}
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the TransactionBatch object to a dictionary.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the batch
        """
        return {
            'id': self.id,
            'import_date': self.import_date,
            'total_transactions': self.total_transactions,
            'total_income': self.total_income,
            'total_expenses': self.total_expenses,
            'net_amount': self.net_amount,
            'date_range': self.date_range
        }


# In-memory storage for transactions (to be replaced with database in production)
transactions_db = []
transaction_batches_db = []

def add_transaction(transaction: Transaction) -> None:
    """
    Add a transaction to the in-memory database.
    
    Args:
        transaction: Transaction object to add
    """
    transactions_db.append(transaction)

def add_transaction_batch(batch: TransactionBatch) -> None:
    """
    Add a transaction batch to the in-memory database.
    
    Args:
        batch: TransactionBatch object to add
    """
    transaction_batches_db.append(batch)
    for transaction in batch.transactions:
        add_transaction(transaction)

def get_transaction_by_id(transaction_id: str) -> Optional[Transaction]:
    """
    Get a transaction by its ID.
    
    Args:
        transaction_id: ID of the transaction to retrieve
        
    Returns:
        Transaction: Transaction object if found, None otherwise
    """
    for transaction in transactions_db:
        if transaction.id == transaction_id:
            return transaction
    return None

def get_transactions_by_batch_id(batch_id: str) -> List[Transaction]:
    """
    Get all transactions in a batch.
    
    Args:
        batch_id: ID of the batch
        
    Returns:
        List[Transaction]: List of Transaction objects in the batch
    """
    return [t for t in transactions_db if t.import_batch_id == batch_id]

def get_all_transactions() -> List[Transaction]:
    """
    Get all transactions.
    
    Returns:
        List[Transaction]: List of all Transaction objects
    """
    return transactions_db

def get_transaction_batch_by_id(batch_id: str) -> Optional[TransactionBatch]:
    """
    Get a transaction batch by its ID.
    
    Args:
        batch_id: ID of the batch to retrieve
        
    Returns:
        TransactionBatch: TransactionBatch object if found, None otherwise
    """
    for batch in transaction_batches_db:
        if batch.id == batch_id:
            return batch
    return None

def get_all_transaction_batches() -> List[TransactionBatch]:
    """
    Get all transaction batches.
    
    Returns:
        List[TransactionBatch]: List of all TransactionBatch objects
    """
    return transaction_batches_db
