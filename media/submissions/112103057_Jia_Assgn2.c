/* S4 : Delete Node in a BST
Given a root node reference of a BST and a key, delete the node with the given key in 
the BST. Return the root node reference (possibly updated) of the BST.*/

#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node * left, *right;
}node;

//create newnode of binary tree
node * create (int x){
    node * newnode=(node*)malloc(sizeof(node));
    newnode->data=x;
    newnode->left=newnode->right=NULL;
    return newnode;
}

//********************************INSERT NODE IN BST**********************************************//
node * insert(node* root,int x){
    if(root==NULL) return create(x);
    if(x<root->data){
        root->left=insert(root->left,x);
    }
    else if(x>root->data) {
        root->right=insert(root->right,x);
    }
    return root;
}

//********************************DELETE NODE IN BST**********************************************//
int minValue(node * root){
    int min = root->data;
    while(root->left!=NULL){
        min=root->left->data;
        root=root->left;
    }
    return min;
}

node * delete(node * root,int x){
    if(root==NULL) return root;
    if(x<root->data){
        root->left=delete(root->left,x);  // root->left changes then we have to return new root->left
    }
    else if(x>root->data){
        root->right=delete(root->right,x);
    }
    else{
       /* if no children
       if(root->left ==NULL && root->right ==NULL){
            free(root);
            root=NULL;
        }*/
        if(root->left==NULL) {
            node * temp =root;
            root=root->right;
            free(temp);
        }
        else if(root->right==NULL) {
            node * temp =root;
            root=root->left;
            free(temp);
        }
        else{
            //in case of 2 childern
        root->data=minValue(root->right);
        //deleting min value in right subtree whose data is stored in root(which was to be deleted)
        root->right=delete(root->right,root->data);
        }
    }
    return root;
}

void inorder(node * root){
    if (root==NULL) return;
    inorder(root->left);
    printf(" %d ",root->data);
    inorder(root->right);
}

int main(){
    node * root=NULL;
    root=insert(root,11);
    insert(root,6);
    insert(root,8);
    insert(root,19);
    insert(root,4);
    insert(root,10);
    insert(root,5);
    insert(root,17);
    insert(root,43);
    insert(root,49);
    insert(root,21);
    printf("inorder traversal of tree is : \n");
    inorder(root);
    //delete a node
    root=delete(root,11);
    printf("\n after deleting node : \n");
    inorder(root);
    return 0;
}