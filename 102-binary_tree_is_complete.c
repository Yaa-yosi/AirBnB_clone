#include "binary_trees.h"

/**
 * binary_tree_is_complete - checks if a binary tree is complete
 * @tree: a pointer to the root node of the tree to check
 *
 * Return: 1 if the tree is complete
 *         0 if the tree is not complete
 *         0 if tree is NULL
 */
int binary_tree_is_complete(const binary_tree_t *tree)
{
	size_t size;

	if (!tree)
		return (0);
	size = binary_tree_size(tree);

	return (iscomplete_helper(tree, 0, size));
}

/**
 * btic_helper - checks if a binary tree is complete
 * @tree: a pointer to the root node of the tree to check
 * @index: node index to check
 * @size: number of nodes in the tree
 *
 * Return: 1 if the tree is complete
 *         0 if the tree is not complete
 *         0 if tree is NULL
 */
int iscomplete_helper(const binary_tree_t *tree, size_t index, size_t size)
{
	if (!tree)
		return (1);

	if (index >= size)
		return (0);

	return (iscomplete_helper(tree->left, 2 * index + 1, size) &&
		iscomplete_helper(tree->right, 2 * index + 2, size));
}

/**
 * binary_tree_size - measures the size of a binary tree
 * @tree: pointer to the root node to measure height
 * Return: 0
 */

size_t binary_tree_size(const binary_tree_t *tree)
{
	size_t size_l = 0, size_r = 0, size;

	if (!tree)
		return (0);
	if (tree->left)
		size_l = binary_tree_size(tree->left);
	if (tree->right)
		size_r = binary_tree_size(tree->right);
	size = size_l + size_r + 1;
	return (size);
}
