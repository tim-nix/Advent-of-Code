def readFile(filename):
   lines = []
   try:
      with open(filename, "r") as file:
         line = file.readline()
         while line:
            lines.append(line.replace('\n', ''))
            line = file.readline()

         file.close()
            
   except FileNotFoundError:
      print("Error: File not found!")
   except:
      print("Error: Can't read from file!")
   
   return lines


def parseInput(lines):
   hands1 = [ line.split() for line in lines ]
   # ( type, hand, bid )
   hands2 = [ (hand, int(bid)) for hand, bid in hands1 ]

   hands3 = []
   for hand, bid in hands2:
      hand_type = getType(hand)
      hands3.append((hand_type, hand, bid))

   return hands3


def getType(hand):
   hand_list = list(hand)
   hand_set = set(hand_list)
   hand_type = ''
   if len(hand_set) == 5:
      hand_type = 0 # "High card"
   elif len(hand_set) == 4:
      hand_type = 1 # "One pair"
   elif len(hand_set) == 3:
      max_count = 0
      for card in hand_list:
         if hand_list.count(card) > max_count:
            max_count = hand_list.count(card)
      if max_count == 2:
         hand_type = 2 # "Two pair"
      elif max_count == 3:
         hand_type = 3 # "Three of a kind"
   elif len(hand_set) == 2:
      max_count = 0
      for card in hand_list:
         if hand_list.count(card) > max_count:
            max_count = hand_list.count(card)
      if max_count == 3:
         hand_type = 4 # "Full house"
      elif max_count == 4:
         hand_type = 5 # "Four of a kind"
   elif len(hand_set) == 1:
      hand_type = 6 # "Five of a kind"
   else:
      print("No hand type assigned")
      print("case = " + str(hand))

   return hand_type

def isBigger(hand1, hand2):
   card_order = [ '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A' ]
   hand_list1 = list(hand1)
   hand_list2 = list(hand2)
   for i in range(len(hand_list1)):
      if hand_list1[i] !=  hand_list2[i]:
         index1 = card_order.index(hand_list1[i])
         index2 = card_order.index(hand_list2[i])

         if index1 > index2:
            return True
         else:
            return False

   print("Two hands are identical.")
   return None
   

def sortHands(hands):
   for i in range(len(hands)):
      for j in range(len(hands) - i - 1):
         if hands[j][0] == hands[j + 1][0]:
            if isBigger(hands[j][1], hands[j + 1][1]):
               hands[j], hands[j + 1] = hands[j + 1], hands[j]

   return hands
         

def calcScore(sorted_hands):
   score = 0
   rank = 1
   for hand in sorted_hands:
      score += rank * hand[2]
      rank += 1

   return score


if __name__ == '__main__':
   hand_values = [ "High card", "One pair", "Two pair", "Three of a kind", "Full house", "Four of a kind", "Five of a kind" ]
   lines = readFile("input7b.txt")
   hands = parseInput(lines)
   hands.sort()
   sorted_hands = sortHands(hands)
   for hand in hands:
      print((hand_values[hand[0]], hand[1]))
   score = calcScore(hands)
   print('250512670 is too low')
   print('250719032 is too high')
   print('score = ' + str(score))
