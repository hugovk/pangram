#!/usr/bin/env python
import argparse

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SET = set(ALPHABET)
TAGS = "tags:\n#pangram\n#Pangram Gutenberg\n#Project Gutenberg"


def contains_pangram(text):
    letter_found = {letter: False for letter in ALPHABET}

    for char in text:
        if char in ALPHABET:
            letter_found[char] = True

    return sum(letter_found.values()) == 26


def printit(left, right, window, best):
    if best:
        print(left, right, len(window), len(best))
    else:
        print(left, right, len(window), 0)


def find_pangram(text):

    # Pointers to left and right indices of window being checked.
    left = 0
    right = 26
    total_length = len(text)
    last_percent = None

    best = None
    best_index = None
    text = text.lower()

    while right <= total_length:

        window = text[left:right]

        # Check window is minimum length.
        if len(window) >= 26:
            # print("Window:")
            # print(window)

            # Initial check.
            found = contains_pangram(window)

            # Move right pointer out until we find a pangram.
            while not found:

                right += 1
                if right > total_length + 1:
                    return best, 0

                window = text[left:right]
                found = contains_pangram(window)

            # print("Found a pangram:")
            # print(window)
            # printit(left, right, window, best)

            # Now move left pointer in to find a smaller one.
            while found:
                left += 1
                window = text[left:right]
                found = contains_pangram(window)

            left -= 1
            window = text[left:right]

#             print "Found a shorter pangram:"
#             print (window)
#             print len(window)
            # printit(left, right, window, best)

            if (not best) or (best and len(window) < len(best)):
                best = window
                best_index = left
                print("New best:", len(best))

        # Move right pointer out one to see if we find any more.
        right += 1

        # Print progress like 8.09%
        percent = "%0.2f%%" % (100.0*right/total_length)
        if last_percent != percent:
            last_percent = percent
            print(percent, end='\r')

    return best, best_index


def print_best(best, left, text):
    if not best:
        print("No pangram found")
        return

    right = left + len(best)

    print("-" * 80)
    print("Shortest pangrammatic window:")
    print(best)
    print("Length:", len(best))
    print("-" * 80)

    print("HTML:\n")

    # Return -1 if not found.
    previous_period = text.rfind(".", 0, left)
    following_period = text.find(".", right)

    # Print the first line, usually contains title and author.
    print(text.split('\n', 1)[0])
    print("-" * 80)

    html = "<p>"

    if previous_period:
        html += text[previous_period+1:left]

    html += "<strong>" + best + "</strong>"

    if following_period:
        html += text[right:following_period+1]
    html += "</p>"

    html += "\n\n<p>Length: " + str(len(best)) + "</p>"

    print(html)
    print(TAGS)


def recursive_find(inspec):
    import fnmatch
    import os
    matches = []
    head, tail = os.path.split(inspec)
    if len(head) == 0:
        head = "."

    for root, dirnames, filenames in os.walk(head):
        for filename in fnmatch.filter(filenames, tail):
            matches.append(os.path.join(root, filename))

    return matches


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Find the shortest pangrammatic window in a text file.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'inspec', nargs='*',
        help='Input file spec')
    parser.add_argument(
        '-t', '--text',
        help='Check this text instead of a file')

    args = parser.parse_args()
    print(args)

    try:
        import timing  # Optional
    except ImportError:
        pass

    if args.text:
        best, index = find_pangram(args.text)
        print_best(best, index, args.text)

    else:
        files = recursive_find(args.inspec[0])
        for filename in files:
            print(filename)
            linestring = open(filename).read()
            print("File length:", len(linestring))
            best, index = find_pangram(linestring)
            print_best(best, index, linestring)

# End of file
