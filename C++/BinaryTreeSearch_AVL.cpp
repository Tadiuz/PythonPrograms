
#include <bits/stdc++.h>
using namespace std;

#define COUNT 10

struct Node
{
  int data;
  struct Node *left;
  struct Node *right;

  Node(int val)
  {
    data = val;
    left = NULL;
    right = NULL;
  }
};

void print2DUtil(Node *root, int space)
{
  if (root == NULL)
    return;
  space += COUNT;

  print2DUtil(root->right, space);
  cout << endl;
  for (int i = COUNT; i < space; i++)
    cout << " ";
  cout << root->data << "\n";
  print2DUtil(root->left, space);
}

void print2D(Node *root)
{

  print2DUtil(root, 0);
}

Node *RightRotation(Node *root){
  Node *aux1 = root->left;
  Node *aux2 = root->right;

  aux1->right = root;
  root->left = aux2;

  return aux1;

}

Node *LeftRotation(Node *root){
  Node *aux1 = root->right;
  Node *aux2 = root->left;

  aux1->left = root;
  root->right = aux2;

  return aux1;
}

int height(Node *r)
{
  if (r == NULL)
    return -1;

  return max(height(r->right), height(r->left)) + 1;
}

int balanceFactor(Node *r)
{
  if (r == NULL)
    return -1;

  return height(r->left) - height(r->right);
}


Node *inserSearchNode(Node *root, int value)
{

  if (root == NULL)
  {
    root = new Node(value);
    return root;
  }
  else if (value > root->data)
    root->right = inserSearchNode(root->right, value);
  else if (value < root->data)
    root->left = inserSearchNode(root->left, value);
  
  int bf = balanceFactor(root);
  
  if ( (bf > 1) && (root->left->data > value) ){
    root = RightRotation(root);
  }

  else if ( (bf < -1) && (root->right->data < value) ){
    root = LeftRotation(root);
  }

  else if ( (bf > 1) && (root->left->data < value) ){
    root->left = LeftRotation(root->left);
    root = RightRotation(root);
  }

  else if ( (bf < -1) && (root->right->data > value) ){
  root->right = RightRotation(root->right);
  root = LeftRotation(root);
  }

  return root;
}





int main()
{

  /*create root*/
  // struct Node *root = new Node(1);
  // root = inserSearchNode(root, 5);
  // root = inserSearchNode(root, 7);
  // root = inserSearchNode(root, 6);
  // root = inserSearchNode(root, 8);
  // root = inserSearchNode(root, 8);
  // root = inserSearchNode(root, 2);
  // root = inserSearchNode(root, 3);
  // root = inserSearchNode(root, 0);
  // root = inserSearchNode(root, 10);


  //##########Right Rotation Test##########
  // struct Node *root = new Node(5);
  // root = inserSearchNode(root, 3);
  // root = inserSearchNode(root, 2);
  // cout << "Before rotation" << endl;
  // print2DUtil(root, 0);
  // root = RightRotation(root);
  // cout << "After rotation" << endl;
  // print2DUtil(root, 0);


  //##########Left Rotation Test##########
  // struct Node *root = new Node(5);
  // root = inserSearchNode(root, 6);
  // root = inserSearchNode(root, 7);
  // cout << "Before rotation" << endl;
  // print2DUtil(root, 0);
  // root = LeftRotation(root);
  // cout << "After rotation" << endl;
  // print2DUtil(root, 0);
  // cout << balanceFactor(root) << endl;


  //##########All Right Rotation Test##########
  // struct Node *root = new Node(5);
  // root = inserSearchNode(root, 3);
  // print2DUtil(root, 0);
  // root = inserSearchNode(root, 2);
  // cout << endl << endl;
  // print2DUtil(root, 0);




  //##########All Left Rotation Test##########
  // struct Node *root = new Node(5);
  // root = inserSearchNode(root, 6);
  // print2DUtil(root, 0);
  // root = inserSearchNode(root, 7);
  // cout << endl << endl;
  // print2DUtil(root, 0);


  //##########All Left Right Rotation Test##########
  // struct Node *root = new Node(5);
  // root = inserSearchNode(root, 3);
  // print2DUtil(root, 0);
  // root = inserSearchNode(root, 4);
  // cout << endl << endl;
  // print2DUtil(root, 0);


  //##########All Right Left Rotation Test##########
  // struct Node *root = new Node(5);
  // root = inserSearchNode(root, 7);
  // print2DUtil(root, 0);
  // root = inserSearchNode(root, 6);
  // cout << endl << endl;
  // print2DUtil(root, 0);


  //##########Test Hacker Rotation Test##########
  struct Node *root = new Node(14);
  root = inserSearchNode(root, 25);
  root = inserSearchNode(root, 21);
  root = inserSearchNode(root, 10);
  root = inserSearchNode(root, 23);
  root = inserSearchNode(root, 7);
  root = inserSearchNode(root, 26);
  root = inserSearchNode(root, 12);
  root = inserSearchNode(root, 30);
  root = inserSearchNode(root, 16);


  cout << endl << endl;
  print2DUtil(root, 0);
  cout << endl << endl;
  root = inserSearchNode(root, 19);
  print2DUtil(root, 19);

  return 0;
}