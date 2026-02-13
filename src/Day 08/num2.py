import numpy as np

np.random.seed(1)   # for same output every time
scores = np.random.randint(50, 101, size=(5, 3))

subject_mean = np.mean(scores, axis=0)

centered_scores = scores - subject_mean
print("Original Scores  (5 students x 3 subjects):")
print(scores)

print("\nMean of each subject:")
print(subject_mean)

print("\nCentered (Normalized) Scores:")
print(centered_scores)

print("\nMean after centering (should be ~0):")
print(np.mean(centered_scores, axis=0))

