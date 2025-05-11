from typing import List

def maximumWealth(self, accounts: List[List[int]]) -> int:
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    # Initialize the maximum wealth to 0
    max_wealth = 0
    
    # Iterate through each customer's account
    for account in accounts:
        # Calculate the sum of the current customer's wealth
        current_wealth = sum(account)
        
        # Update max_wealth if current_wealth is greater
        max_wealth = max(max_wealth, current_wealth)
    
    return max_wealth