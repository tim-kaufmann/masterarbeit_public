def pass_at_k(n, c, k):  
  if n - c < k: 
    return 1.0 
  return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1)
