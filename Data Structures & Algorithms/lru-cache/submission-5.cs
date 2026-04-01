// Least Recently Used = FIFO
public class LRUCache {

    readonly private int _capacity;
    private Dictionary<int, int> _cache;
    private List<int> _lruQueue;

    public LRUCache(int capacity) {
        _capacity = capacity;
        _cache = new Dictionary<int, int>(capacity);
        _lruQueue = new List<int>();
    }
    
    public int Get(int key) {
        if (_cache.TryGetValue(key, out var value))
        {
            _lruQueue.Remove(key);
            _lruQueue.Add(key);
            return value;
        }

        return -1;
    }
    
    public void Put(int key, int value) {
        if (!_cache.TryAdd(key, value))
        {
            _lruQueue.Remove(key);
            _cache[key] = value;
        }
        
        _lruQueue.Add(key);

        if (_cache.Count > _capacity)
        {
            int poppedKey = _lruQueue[0];
            _cache.Remove(poppedKey);
            _lruQueue.RemoveAt(0);
        }
    }
}
