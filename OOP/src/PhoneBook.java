import java.util.Scanner;
class Phone {
    private String name, tel;
    public Phone(String name, String tel) {
        this.name = name;
        this.tel = tel;
    }
    public String Name() {
        return name;
    }
    public String Tel() {
        return tel;
    }}
public class PhoneBook {
    Scanner sc = new Scanner(System.in);
    int num;
    Phone phone[];
    String name;
    String tel;
    public void Num() {
        System.out.print("인원수>>");
        num = sc.nextInt();
        phone = new Phone[num];
    }
    public void Info() {
        for(int i=0; i<num; i++) {
            System.out.print("이름과 전화번호(이름과 번호는 빈 칸없이 입력)>>");
            name = sc.next();
            tel = sc.next();
            phone[i] = new Phone(name, tel);
        }
        System.out.println("저장되었습니다...");
    }
    public void Search() {
        boolean state = false;
        while(true) {
            System.out.print("검색할 이름>>");
            name = sc.next();
            if(name.equals("그만")) {
                break;
            }
            for(int i=0; i<num; i++) {
                if(name.equals(phone[i].Name())) {
                    System.out.println(name+"의 번호는 "+phone[i].Tel()+" 입니다.");
                    state = true;
                }
            }
            if(state == false)
                System.out.println(name+" 이 없습니다.");
        }
    }
    public static void main(String args[]) {
        PhoneBook phonebook = new PhoneBook();
        phonebook.Num();
        phonebook.Info();
        phonebook.Search();
    }
}
