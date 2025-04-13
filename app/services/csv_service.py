"""
csv_service.py - CSV Processing Service for Muzzy Tracker

This module provides functionality for processing CSV files containing financial data.
It includes:
- CSV parsing and validation
- Column mapping
- Date format detection and conversion
- Transaction categorization
- Duplicate detection
"""

import os
import pandas as pd
import uuid
import re
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any

# Define common date formats for automatic detection
DATE_FORMATS = [
    '%Y-%m-%d',  # 2025-04-01
    '%m/%d/%Y',  # 04/01/2025
    '%d/%m/%Y',  # 01/04/2025
    '%m-%d-%Y',  # 04-01-2025
    '%d-%m-%Y',  # 01-04-2025
    '%m/%d/%y',  # 04/01/25
    '%d/%m/%y',  # 01/04/25
    '%b %d, %Y',  # Apr 01, 2025
    '%d %b %Y',   # 01 Apr 2025
]

# Common transaction categories
CATEGORIES = [
    'Food & Dining',
    'Shopping',
    'Transportation',
    'Bills & Utilities',
    'Entertainment',
    'Housing',
    'Income',
    'Health & Fitness',
    'Travel',
    'Education',
    'Personal Care',
    'Gifts & Donations',
    'Investments',
    'Transfer',
    'Other'
]

# Keywords for automatic categorization
CATEGORY_KEYWORDS = {
    'Food & Dining': ['restaurant', 'cafe', 'coffee', 'diner', 'food', 'grocery', 'pizza', 'burger', 'starbucks', 'mcdonalds', 'chipotle', 'uber eats', 'doordash', 'grubhub'],
    'Shopping': ['amazon', 'walmart', 'target', 'costco', 'ebay', 'etsy', 'store', 'shop', 'retail', 'purchase'],
    'Transportation': ['gas', 'fuel', 'uber', 'lyft', 'taxi', 'transit', 'parking', 'toll', 'auto', 'car', 'vehicle', 'train', 'bus', 'subway'],
    'Bills & Utilities': ['bill', 'utility', 'electric', 'water', 'gas', 'internet', 'phone', 'mobile', 'cable', 'tv', 'netflix', 'spotify', 'hulu', 'subscription'],
    'Entertainment': ['movie', 'theater', 'cinema', 'concert', 'event', 'ticket', 'game', 'music', 'spotify', 'netflix', 'hulu', 'disney+', 'hbo'],
    'Housing': ['rent', 'mortgage', 'home', 'apartment', 'house', 'property', 'real estate', 'hoa', 'maintenance'],
    'Income': ['payroll', 'salary', 'deposit', 'income', 'payment', 'wage', 'direct deposit', 'interest', 'dividend', 'refund'],
    'Health & Fitness': ['doctor', 'medical', 'health', 'pharmacy', 'fitness', 'gym', 'wellness', 'dental', 'vision', 'insurance'],
    'Travel': ['hotel', 'flight', 'airline', 'airbnb', 'travel', 'vacation', 'trip', 'booking', 'expedia', 'travelocity'],
    'Education': ['school', 'college', 'university', 'tuition', 'education', 'book', 'course', 'class', 'student', 'loan'],
    'Personal Care': ['salon', 'spa', 'haircut', 'beauty', 'cosmetic', 'personal care'],
    'Gifts & Donations': ['gift', 'donation', 'charity', 'nonprofit', 'present'],
    'Investments': ['investment', 'stock', 'bond', 'mutual fund', 'etf', 'brokerage', 'retirement', '401k', 'ira'],
    'Transfer': ['transfer', 'zelle', 'venmo', 'paypal', 'cash app', 'wire', 'ach', 'withdrawal', 'deposit']
}

class CSVService:
    """Service for processing CSV files with financial data."""
    
    def __init__(self, upload_folder='temp_uploads'):
        """
        Initialize the CSV service.
        
        Args:
            upload_folder: Directory to store temporary uploaded files
        """
        self.upload_folder = upload_folder
        os.makedirs(upload_folder, exist_ok=True)
    
    def save_uploaded_file(self, file) -> str:
        """
        Save an uploaded file to the temporary directory.
        
        Args:
            file: The uploaded file object
            
        Returns:
            str: The path to the saved file
        """
        # Generate a unique filename to prevent collisions
        filename = f"{uuid.uuid4().hex}.csv"
        file_path = os.path.join(self.upload_folder, filename)
        file.save(file_path)
        return file_path
    
    def read_csv(self, file_path: str) -> pd.DataFrame:
        """
        Read a CSV file into a pandas DataFrame.
        
        Args:
            file_path: Path to the CSV file
            
        Returns:
            pd.DataFrame: The CSV data as a DataFrame
        """
        try:
            # Try to detect the delimiter automatically
            with open(file_path, 'r') as f:
                sample = f.read(4096)  # Read a sample to detect delimiter
            
            # Count occurrences of common delimiters
            delimiters = [',', ';', '\t', '|']
            counts = {d: sample.count(d) for d in delimiters}
            delimiter = max(counts, key=counts.get)
            
            # Read the CSV with the detected delimiter
            df = pd.read_csv(file_path, delimiter=delimiter)
            return df
        except Exception as e:
            raise ValueError(f"Error reading CSV file: {str(e)}")
    
    def detect_date_format(self, date_sample: str) -> Optional[str]:
        """
        Detect the format of a date string.
        
        Args:
            date_sample: A sample date string
            
        Returns:
            str: The detected date format, or None if not detected
        """
        for date_format in DATE_FORMATS:
            try:
                datetime.strptime(date_sample, date_format)
                return date_format
            except ValueError:
                continue
        return None
    
    def convert_dates(self, df: pd.DataFrame, date_column: str, date_format: str) -> pd.DataFrame:
        """
        Convert a date column to datetime format.
        
        Args:
            df: The DataFrame containing the data
            date_column: The name of the date column
            date_format: The format of the dates in the column
            
        Returns:
            pd.DataFrame: The DataFrame with converted dates
        """
        try:
            df[date_column] = pd.to_datetime(df[date_column], format=date_format)
            return df
        except Exception as e:
            raise ValueError(f"Error converting dates: {str(e)}")
    
    def suggest_column_mapping(self, df: pd.DataFrame) -> Dict[str, str]:
        """
        Suggest mappings from CSV columns to standard fields.
        
        Args:
            df: The DataFrame containing the CSV data
            
        Returns:
            Dict[str, str]: Suggested mappings from CSV columns to standard fields
        """
        columns = df.columns.tolist()
        mapping = {}
        
        # Look for date columns
        date_columns = [col for col in columns if any(kw in col.lower() for kw in ['date', 'time', 'day'])]
        if date_columns:
            mapping['date'] = date_columns[0]
        
        # Look for description columns
        desc_columns = [col for col in columns if any(kw in col.lower() for kw in ['description', 'desc', 'merchant', 'payee', 'name', 'transaction'])]
        if desc_columns:
            mapping['description'] = desc_columns[0]
        
        # Look for amount columns
        amount_columns = [col for col in columns if any(kw in col.lower() for kw in ['amount', 'sum', 'total', 'payment', 'debit', 'credit'])]
        if amount_columns:
            mapping['amount'] = amount_columns[0]
        
        # Look for category columns
        category_columns = [col for col in columns if any(kw in col.lower() for kw in ['category', 'type', 'classification'])]
        if category_columns:
            mapping['category'] = category_columns[0]
        
        # Look for account columns
        account_columns = [col for col in columns if any(kw in col.lower() for kw in ['account', 'source', 'card', 'bank'])]
        if account_columns:
            mapping['account'] = account_columns[0]
        
        return mapping
    
    def apply_column_mapping(self, df: pd.DataFrame, mapping: Dict[str, str]) -> pd.DataFrame:
        """
        Apply column mapping to standardize the DataFrame.
        
        Args:
            df: The DataFrame containing the CSV data
            mapping: Mapping from CSV columns to standard fields
            
        Returns:
            pd.DataFrame: Standardized DataFrame
        """
        # Create a new DataFrame with standardized columns
        result = pd.DataFrame()
        
        # Copy mapped columns to the new DataFrame
        for standard_field, csv_column in mapping.items():
            if csv_column in df.columns:
                result[standard_field] = df[csv_column]
        
        return result
    
    def suggest_category(self, description: str) -> str:
        """
        Suggest a category based on the transaction description.
        
        Args:
            description: The transaction description
            
        Returns:
            str: The suggested category
        """
        description = description.lower()
        
        for category, keywords in CATEGORY_KEYWORDS.items():
            if any(keyword.lower() in description for keyword in keywords):
                return category
        
        return 'Other'
    
    def categorize_transactions(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add or update categories for transactions based on descriptions.
        
        Args:
            df: The DataFrame containing transaction data
            
        Returns:
            pd.DataFrame: DataFrame with categorized transactions
        """
        # If category column doesn't exist, create it
        if 'category' not in df.columns:
            df['category'] = None
        
        # For each transaction without a category, suggest one
        for idx, row in df.iterrows():
            if pd.isna(row['category']) and 'description' in df.columns:
                df.at[idx, 'category'] = self.suggest_category(str(row['description']))
        
        return df
    
    def normalize_amounts(self, df: pd.DataFrame, amount_format: str) -> pd.DataFrame:
        """
        Normalize transaction amounts based on the specified format.
        
        Args:
            df: The DataFrame containing transaction data
            amount_format: Format of the amounts ('negative_expense' or 'separate_columns')
            
        Returns:
            pd.DataFrame: DataFrame with normalized amounts
        """
        if 'amount' not in df.columns:
            return df
        
        # Convert amount strings to float, handling currency symbols and commas
        df['amount'] = df['amount'].astype(str).str.replace('[$,]', '', regex=True).astype(float)
        
        if amount_format == 'separate_columns' and 'debit' in df.columns and 'credit' in df.columns:
            # Convert debit and credit columns to float
            df['debit'] = df['debit'].astype(str).str.replace('[$,]', '', regex=True).astype(float)
            df['credit'] = df['credit'].astype(str).str.replace('[$,]', '', regex=True).astype(float)
            
            # Combine debit and credit into a single amount column
            df['amount'] = df['credit'] - df['debit']
        
        return df
    
    def validate_data(self, df: pd.DataFrame) -> List[Dict[str, Any]]:
        """
        Validate the transaction data and identify potential issues.
        
        Args:
            df: The DataFrame containing transaction data
            
        Returns:
            List[Dict[str, Any]]: List of validation issues
        """
        issues = []
        
        # Check for missing required fields
        required_fields = ['date', 'description', 'amount']
        for field in required_fields:
            if field not in df.columns:
                issues.append({
                    'type': 'missing_field',
                    'field': field,
                    'message': f"Required field '{field}' is missing"
                })
        
        # Check for invalid dates
        if 'date' in df.columns:
            invalid_dates = df[df['date'].isna()]
            if not invalid_dates.empty:
                issues.append({
                    'type': 'invalid_dates',
                    'count': len(invalid_dates),
                    'rows': invalid_dates.index.tolist(),
                    'message': f"Found {len(invalid_dates)} transactions with invalid dates"
                })
        
        # Check for missing categories
        if 'category' in df.columns:
            missing_categories = df[df['category'].isna()]
            if not missing_categories.empty:
                issues.append({
                    'type': 'missing_categories',
                    'count': len(missing_categories),
                    'rows': missing_categories.index.tolist(),
                    'message': f"Found {len(missing_categories)} transactions with missing categories"
                })
        
        # Check for unusually large amounts
        if 'amount' in df.columns:
            # Define thresholds for unusually large amounts
            large_threshold = 5000  # $5,000
            large_amounts = df[df['amount'].abs() > large_threshold]
            if not large_amounts.empty:
                issues.append({
                    'type': 'large_amounts',
                    'count': len(large_amounts),
                    'rows': large_amounts.index.tolist(),
                    'message': f"Found {len(large_amounts)} transactions with unusually large amounts (>${large_threshold})"
                })
        
        return issues
    
    def generate_preview(self, df: pd.DataFrame, issues: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate a preview of the transaction data with validation results.
        
        Args:
            df: The DataFrame containing transaction data
            issues: List of validation issues
            
        Returns:
            Dict[str, Any]: Preview data with statistics and issues
        """
        # Calculate date range
        date_range = {}
        if 'date' in df.columns and not df.empty:
            min_date = df['date'].min()
            max_date = df['date'].max()
            if pd.notna(min_date) and pd.notna(max_date):
                date_range = {
                    'start': min_date.strftime('%b %d, %Y'),
                    'end': max_date.strftime('%b %d, %Y')
                }
        
        # Calculate financial statistics
        stats = {}
        if 'amount' in df.columns:
            income = df[df['amount'] > 0]['amount'].sum() if not df.empty else 0
            expenses = df[df['amount'] < 0]['amount'].sum() if not df.empty else 0
            stats = {
                'total_transactions': len(df),
                'income': round(income, 2),
                'expenses': round(expenses, 2),
                'net': round(income + expenses, 2)
            }
        
        # Prepare sample data (first 10 rows)
        sample_data = []
        if not df.empty:
            for _, row in df.head(10).iterrows():
                sample_row = {}
                for col in df.columns:
                    value = row[col]
                    if col == 'date' and pd.notna(value):
                        value = value.strftime('%b %d, %Y')
                    sample_row[col] = value
                sample_data.append(sample_row)
        
        # Compile preview data
        preview = {
            'date_range': date_range,
            'stats': stats,
            'issues': issues,
            'sample_data': sample_data
        }
        
        return preview
    
    def process_import(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Process the final import and prepare data for storage.
        
        Args:
            df: The DataFrame containing transaction data
            
        Returns:
            Dict[str, Any]: Processed transaction data ready for storage
        """
        # Generate a unique batch ID for this import
        batch_id = uuid.uuid4().hex
        
        # Prepare transactions for storage
        transactions = []
        for _, row in df.iterrows():
            transaction = {
                'id': uuid.uuid4().hex,
                'import_batch_id': batch_id,
                'import_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            # Copy data from DataFrame
            for col in df.columns:
                value = row[col]
                if col == 'date' and pd.notna(value):
                    value = value.strftime('%Y-%m-%d')
                transaction[col] = value
            
            transactions.append(transaction)
        
        # Calculate import summary
        summary = {
            'batch_id': batch_id,
            'total_transactions': len(transactions),
            'date_range': {
                'start': min(t['date'] for t in transactions if 'date' in t),
                'end': max(t['date'] for t in transactions if 'date' in t)
            } if transactions else {},
            'income': sum(t['amount'] for t in transactions if 'amount' in t and t['amount'] > 0),
            'expenses': sum(t['amount'] for t in transactions if 'amount' in t and t['amount'] < 0)
        }
        
        return {
            'transactions': transactions,
            'summary': summary
        }
    
    def cleanup_temp_file(self, file_path: str) -> None:
        """
        Remove a temporary file after processing.
        
        Args:
            file_path: Path to the temporary file
        """
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            # Log the error but don't raise it
            print(f"Error removing temporary file: {str(e)}")
