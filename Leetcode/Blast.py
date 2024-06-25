def find_hits(seq1, seq2, k):
    hits = []
    for i in range(len(seq1) - k + 1):
        kmer = seq1[i:i+k]
        for j in range(len(seq2) - k + 1):
            if seq2[j:j+k] == kmer:
                hits.append((i, j, kmer))
    return hits

def extend_hit(seq1, seq2, start1, start2, k):
    max_score = k  # Initial score for the k-mer hit
    best_score = max_score
    best_start = start1
    best_end = start1 + k - 1
    current_score = max_score

    # Extend to the left
    left_i, left_j = start1 - 1, start2 - 1
    while left_i >= 0 and left_j >= 0:
        current_score += 1 if seq1[left_i] == seq2[left_j] else -1
        if current_score > best_score:
            best_score = current_score
        if current_score < best_score - 3:
            break
        left_i -= 1
        left_j -= 1

    best_start = left_i + 1

    # Extend to the right
    right_i, right_j = start1 + k, start2 + k
    while right_i < len(seq1) and right_j < len(seq2):
        current_score += 1 if seq1[right_i] == seq2[right_j] else -1
        if current_score > best_score:
            best_score = current_score
        if current_score < best_score - 3:
            break
        right_i += 1
        right_j += 1

    best_end = right_i - 1

    return best_start, best_end, best_score

def main():
    seq1 = "AATGTCGATCGTGCA"
    seq2 = "TTAGACGAACACATT"
    k = 3

    # Find hits
    hits = find_hits(seq1, seq2, k)
    if not hits:
        print("No hits found.")
        return

    print("Hits found:", hits)

    # Extend the first hit (for simplicity)
    start1, start2, kmer = hits[0]
    best_start, best_end, best_score = extend_hit(seq1, seq2, start1, start2, k)

    print("Hit:", kmer)
    print("Extended Hit:")
    print("Sequence 1:", seq1[best_start:best_end+1])
    print("Sequence 2:", seq2[start2-(start1-best_start):start2-(start1-best_start)+(best_end-best_start+1)])
    print("Total Score:", best_score)

if __name__ == "__main__":
    main()
