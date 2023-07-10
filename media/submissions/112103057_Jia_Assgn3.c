#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    char value;
    struct node *left;
    struct node *right;
} node;

node *create_node(char value) {
    node *new_node = (node *)malloc(sizeof(node));
    new_node->value = value;
    new_node->left = NULL;
    new_node->right = NULL;
    return new_node;
}

void push(node **stack, int *top, node *new_node) {
    (*top)++;
    stack[*top] = new_node;
}

node *pop(node **stack, int *top) {
    node *popped_node = stack[*top];
    (*top)--;
    return popped_node;
}

node *build_expression_tree(char *postfix_expression) {
    int top = -1;
    node *stack[100];
    for (int i = 0; postfix_expression[i] != '\0'; i++) {
        char element=postfix_expression[i];
        if (element=='+' || element =='-' || element== '*' || element =='/') {
            node *new_node = create_node(postfix_expression[i]);
            new_node->right = pop(stack, &top);
            new_node->left = pop(stack, &top);
            push(stack, &top, new_node);
        } else {
            node *new_node = create_node(postfix_expression[i]);
            push(stack, &top, new_node);
        }
    }
    return pop(stack, &top);
}

int evaluate_expression_tree(node *root) {
    if (root->left == NULL && root->right == NULL) {
        return (root->value - '0');
    }
    int left_value = evaluate_expression_tree(root->left);
    int right_value = evaluate_expression_tree(root->right);
    switch (root->value) {
        case '+': return left_value + right_value;
        case '-': return left_value - right_value;
        case '*': return left_value * right_value;
        case '/': return left_value / right_value;
        default: return 0;
    }
}

void inorder(node * root){
    if (root==NULL) return;
    inorder(root->left);
    printf(" %c ",root->value);
    inorder(root->right);
}

int main() {
    char postfix_expression[] = "34+2*7/";
    node *root = build_expression_tree(postfix_expression);
    //print inorder of tree
    inorder(root);
    int result = evaluate_expression_tree(root);
    printf("\n Result: %d\n", result);
    return 0;
}
