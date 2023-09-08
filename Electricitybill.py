import java.util.Scanner;
class EB_Bill {
int number;
String name;
int last_reading;
int present_reading;
int total_units;
boolean DomesticCon = false;
double bill;
public void DomesticConnection(){
System.out.println("Domestic Connection Details");
System.out.println("First 100 units - Rs. 1 per unit");
System.out.println("101-200 units - Rs. 2.50 per unit");
System.out.println("201 -500 units - Rs. 4 per unit");
System.out.println("> 501 units - Rs. 6 per unit");
}
public void CommercialConnection() {
System.out.println("Commercial Connection Details");
System.out.println("First 100 units - Rs. 2 per unit");
System.out.println("101-200 units - Rs. 4.50 per unit");
System.out.println("201 -500 units - Rs. 6 per unit");
System.out.println("> 501 units - Rs. 7 per unit");
}
public void Details() {
Scanner inputs = new Scanner(System.in);
System.out.println("EB Calculater\n\n");
System.out.println("Please Enter Your Name : ");
 CS8392 – Object Oriented Programming 711720205053
this.name = inputs.next();
System.out.println("Please Enter Your Consumer Number : ");
this.number = inputs.nextInt();
System.out.println("Please Enter Your Previous Month Reading : ");
this.last_reading = inputs.nextInt();
System.out.println("Please Enter Your Current Month Reading : ");
this.present_reading = inputs.nextInt();
System.out.println("Is this domestic Connection (yes/no) : ");
if(inputs.next().equals("yes"))
this.DomesticCon = true;
}
public void Bill(){
int number_of_units_consumed = this.present_reading - this.last_reading;
this.total_units = number_of_units_consumed;
double tot = 0;
if(DomesticCon == true) {
for (int i = 0; i <= number_of_units_consumed; i++) {
if (i <= 100)
tot = tot + 1;
else if (i > 100 && i <= 200)
tot = tot + 2.5;
else if (i > 200 && i <= 500)
tot = tot + 4;
else
tot = tot + 6;
}
}
else {
for (int i = 0; i <= number_of_units_consumed; i++) {
 CS8392 – Object Oriented Programming 711720205053
if (i <= 100)
tot = tot + 2;
else if (i > 100 && i <= 200)
tot = tot + 4.5;
else if (i > 200 && i <= 500)
tot = tot + 6;
else
tot = tot + 7;
}
}
this.bill = tot;
}
public void displayinfo() {
Bill();
System.out.println("EB Bill");
System.out.println("Consumer Number : "+this.number);
System.out.println("Consumer Name : "+this.name);
System.out.println("Consumer Units Consumed:"+this.total_units);
if(this.DomesticCon == true){
System.out.println("Your are an Domestic Consumer\n\nBill Details ...");
DomesticConnection();
}
else{
System.out.println("You are a Commercial Consumer\n\nBill Details ...");
CommercialConnection();
}
System.out.println("\nAmount Payable is \u20B9: "+this.bill);
}
}
public class Main {
 CS8392 – Object Oriented Programming 711720205053
public static void main(String[] args) {
EB_Bill user = new EB_Bill();
user.Details();
user.displayinfo();
}
}
