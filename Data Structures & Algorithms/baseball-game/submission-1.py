class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for i in range(len(operations)):
            if(operations[i] == "+"):
                # record.append(record[-1] + record[-2])
                a, b = record.pop(), record.pop()
                c = a + b
                record.append(b)
                record.append(a)
                record.append(c)
            elif(operations[i] == "D"):
                record.append(record[-1] * 2)
            elif(operations[i] == "C"):
                record.pop()
            else:
                record.append(int(operations[i]))
        return sum(record)