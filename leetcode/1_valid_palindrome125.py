import re
class Solution(object):
    def isPalindrome(self, s) :
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        is_palindrome = cleaned_s == cleaned_s[::-1]
        print(f"Cleaned String: '{cleaned_s}'")  # Debug: Show the cleaned string
        if is_palindrome:
            print(f"✅ '{s}' is a palindrome.")
        else:
            print(f"❌ '{s}' is not a palindrome.")
        return is_palindrome
if __name__ == "__main__":
    user_input = input("Enter a string to check if it's a palindrome: ")
    solution = Solution()
    solution.isPalindrome(user_input)