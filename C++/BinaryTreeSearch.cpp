
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

Node* inserSearchNode(Node *root, int value)
{
  
  if (root == NULL)
  {
    root = new Node(value);
    return root;

  }
  if (value > root->data)
    root->right = inserSearchNode(root->right, value);
  if (value < root->data)
    root->left = inserSearchNode(root->left, value);

  return root;

}

int main()
{

  /*create root*/
  struct Node *root = new Node(1);

  root = inserSearchNode(root, 5);
  root = inserSearchNode(root, 7);
  root = inserSearchNode(root, 6);
  root = inserSearchNode(root, 8);
  root = inserSearchNode(root, 8);
  root = inserSearchNode(root, 2);
  root = inserSearchNode(root, 3);
  print2DUtil(root, 0);

  //root->left = new Node(2);
  //root->right = new Node(3);
  //root->left->left = new Node(4);
  //cout << root->left->left->data;

  

  return 0;
}