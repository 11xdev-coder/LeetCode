class Solution:
    def compress(self, chars: list[str]) -> int:
        read = 0
        write = 0
        count = 0
        while read < len(chars):
            ch = chars[read]

            while read < len(chars) and chars[read] == ch:
                count += 1
                read += 1

            chars[write] = ch
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
            
            count = 0

        return write
