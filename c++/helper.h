// Please donot edit anything in this file
#include<iostream>
using namespace std;

class node{
    public:
    string data;
    node* next;  //pointer pointing towards the next node

    node(string val){
        data=val;
        next=NULL;
    }
};

void print(node* head){
    node* temp=head;
    while(temp!=NULL){
        cout<<temp->data;
        temp=temp->next;
    }
}

void SolveQuiz(node* head);


int main(){

    node *e = new node("ht");
    node *e1  =  new node("ht");
    node *e2  =  new node("tps:");
    node *e3  =  new node("//");
    node *e4  =  new node("for");
    node *e5  =  new node("tps:");
    node *e6  =  new node("ms");
    node *e7  =  new node(".");
    node *e8  =  new node("for");
    node *e9  =  new node("lumos");
    node *e10  = new node("//");
    node *e11  = new  node("ht");
    node *e12  = new  node("labs.");
    node *e13  = new  node("ms");
    node *e14  = new  node("co");
    node *e15  = new  node("/su");
    node *e16  = new  node("rvey");
    node *e17  = new  node("for");
    node *e18  = new  node("/");
    node *e19  = new  node("labs.");
    node *e20  = new  node("t/");
    node *e21  = new  node("65a5a0c3");
    node *e22  = new  node("-15b9");
    node *e23  = new  node("-42");
    node *e24  = new  node("65a5a0c3");
    node *e25  = new  node("da");
    node *e26  = new  node("-a99c");
    node *e27  = new  node("-");
    node *e28  = new  node("06622");
    node *e29  = new  node("e0c7");
    node *e30  = new  node("bac/");
    node *e31  = new  node("r/");
    node *e32  = new  node("o");
    node *e33  = new  node("//");
    node *e34  = new  node("/su");
    node *e35  = new  node("labs.");
    node *e36  = new  node("ms");
    node *e37  = new  node("bac/");
    node *e38  = new  node("/su");
    node *e39  = new  node(".");
    node *e40  = new  node("65a5a0c3");
    node *e41  = new  node("rvey");
    node *e42  = new  node("-15b9");
    node *e43  = new  node("bac/");
    node *e44  = new  node("lumos");
    node *e45  = new  node("-42");
    node *e46  = new  node("bac/");
    node *e47  = new  node("-");
    node *e48  = new  node("bac/");
    node *e49  = new  node("rvey");
    node *e50  = new  node("r/");
    node *e51  = new  node("o");
    node *e52  = new  node(".");
    node *e53  = new  node("for");
    node *e54  = new  node("-15b9");
    node *e55  = new  node("-a99c");
    node *e56  = new  node("bac/");
    node *e57  = new  node("t/");
    node *e58  = new  node("lumos");
    node *e59  = new  node("da");
    node *e60  = new  node("da");

    e->next = e1;
    e1->next = e2;
    e2->next = e3;
    e3->next = e4;
    e4->next = e5;
    e5->next = e6;
    e6->next = e7;
    e7->next = e8;
    e8->next = e9;
    e9->next = e10;
    e10->next = e11;
    e11->next = e12;
    e12->next = e13;
    e13->next = e14;
    e14->next = e15;
    e15->next = e16;
    e16->next = e17;
    e17->next = e18;
    e18->next = e19;
    e19->next = e20;
    e20->next = e21;
    e21->next = e22;
    e22->next = e23;
    e23->next = e24;
    e24->next = e25;
    e25->next = e26;
    e26->next = e27;
    e27->next = e28;
    e28->next = e29;
    e29->next = e30;
    e30->next = e31;
    e31->next = e32;
    e32->next = e33;
    e33->next = e34;
    e34->next = e35;
    e35->next = e36;
    e36->next = e37;
    e37->next = e38;
    e38->next = e39;
    e39->next = e40;
    e40->next = e41;
    e41->next = e42;
    e42->next = e43;
    e43->next = e44;
    e44->next = e45;
    e45->next = e46;
    e46->next = e47;
    e47->next = e48;
    e48->next = e49;
    e49->next = e50;
    e50->next = e51;
    e51->next = e52;
    e52->next = e53;
    e53->next = e54;
    e54->next = e55;
    e55->next = e56;
    e56->next = e57;
    e57->next = e58;
    e58->next = e59;
    e59->next = e60;

    cout<<"This is what the unsolved quest looks like: \n";
    print(e);
    cout<<"\n\nPlease keep inmind that this is a linked list and we have used arrows to depict the different nodes.";
    cout<<"All you need to do is complete the SolveQuiz() function that takes the head of the linked list as an argument. Please ensure that this function also prints solved quest where you figure how to remove duplicate nodes. \n\n";
    cout<<"Hurray! I was able to solve the quest - here is my output: \n";
    SolveQuiz(e);


    return 0;
}
