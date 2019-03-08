function isSolution(charSet, charMap) {
    return Object.keys(
}
function longestSubstring(str, chars) {
    let end = 0, begin = 0;
    // char map: store characters in a "window" and their count
    let charMap = {};
    // [low..high] maintains sliding window boundaries
    for (let low = 0, high = 0; high < str.length; high++) {
        if (!chars.has(str[high])) {
            continue;
        }
        charMap[str[high]] = (charMap[str[high]] || 0) + 1;

        // if window size is more than k, remove characters from left
        while (Object.keys(charMap).length > chars.length) {
            // if frequency of leftmost character becomes 0 after
            // removing it from the window, remove it from charMap
            if (--charMap[str[low]] == 0) {
                delete charMap[low];
            }
            // reduce window size
            low++;
        }
        // update maximum window size as necessary
        if (end - begin < high - low) {
            end = high;
            begin = low;
        }
    }
    return str.slice(begin, end + 1);
}

console.log(longestSubstring("abcbdbdbdbdcdabd", new Set(["a"])));
console.log(longestSubstring("abcbdbdbdbdcdabd", new Set(["a", "b"])));
console.log(longestSubstring("abcbdbdbdbdcdabd", new Set(["a", "b", "c"])));
console.log(longestSubstring("abcbdbdbdbdcdabd", new Set(["a", "b", "d"])));
