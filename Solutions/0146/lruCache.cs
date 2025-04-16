public class LRUCache {
    Dictionary<int, int> cache = new Dictionary<int, int>();
    int capacity = 0;
    List<int> queueList = new List<int>();

    public LRUCache(int capacity) {
        this.capacity = capacity;
    }
    
    public int Get(int key) {
        if (queueList.Contains(key)){
            queue(key);
            return (cache[key]);
        } else {
            return (-1);
        }
    }
    
    public void Put(int key, int value) {
        cache[key] = value;
        queue(key);
    }

    public void queue(int key){
        if (queueList.Contains(key)) {
            queueList.Remove(key);
        } else if (queueList.Count == capacity){
            queueList.RemoveAt(0);
        }

        queueList.Add(key);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */