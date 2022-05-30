//Hw5_10

abstract class PairMap {
    protected String keyArray[];
    protected String valueArray[];
    abstract String get(String key);
    abstract void put(String key, String value);
    abstract String delete(String key);
    abstract int length();
}

class Dictionary extends PairMap {
    private int c = 0;

    Dictionary(int n) {
        keyArray = new String[n];
        valueArray = new String[n];
    }

    @Override
    String get(String key) {
        for (int i = 0; i < keyArray.length; i++) {
            if (key.equals(keyArray[i])) {
                return valueArray[i];
            }
        }
        return null;
    }

    @Override
    void put(String key, String value) {
        for (int i = 0; i < keyArray.length; i++) {
            if (key.equals(keyArray[i])) {
                valueArray[i] = value;
                return;
            }
        }
        keyArray[c] = key;
        valueArray[c] = value;
        c++;
    }
    @Override
    String delete(String key) {
        String result = null;
        for (int i = 0; i < keyArray.length; i++) {
            if (key.equals(keyArray[i])) {
                result = valueArray[i];
                keyArray[i] = null;
                valueArray[i] = null;
            }
        }
        return result;
    }

    @Override
    int length() {
        int count = 0;
        for (int i = 0; i < keyArray.length; i++) {
            if (keyArray[i] != null) {
                count++;
            }
        }
        return count;
    }
}
public class DictionaryApp {
    public static void main(String[] args) {
        Dictionary dic = new Dictionary(10);
        dic.put("황기태", "자바");
        dic.put("이재문", "파이썬");
        dic.put("이재문", "C++");
        System.out.println("이재문의 값은 " + dic.get("이재문"));
        System.out.println(("황기태의 값은 " + dic.get("황기태")));
        dic.delete("황기태");
        System.out.println("황기태의 값은 " + dic.get("황기태"));

    }
}