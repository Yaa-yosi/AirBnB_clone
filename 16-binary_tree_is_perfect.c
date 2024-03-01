#include "binary_trees.h"
#include <math.h>
/**
 * binary_tree_is_perfect - checks if a binary tree is perfect
 * @tree: pointer to the root of the tree to check
 * Return: 0
 */

int binary_tree_is_perfect(const binary_tree_t *tree)
{
	size_t height, nodes, size;

	if (!tree)
		return (0);
	if (!tree->left && !tree->right)
		return (1);
	height = binary_tree_height(tree);
	size = binary_tree_size(tree);
	nodes = (size_t)_pow(2, height + 1);

	return (nodes - 1 == size);
}

/**
 * max_nodes - checks the max nodes of a tree
 * @x: base
 * @y: exponent
 * Return: x**y or -1 
 * */

int _pow(int x, int y)
{
	if (y < 0)
		return (-1);
	if (y == 0)
		return (1);
	else
		return (x * _pow(x, y - 1));
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

/**
 * binary_tree_height - measures the height of a binary tree
 * @tree: pointer to the root node to measure height
 * Return: 0
 */

size_t binary_tree_height(const binary_tree_t *tree)
{
	size_t height_l = 0, height_r = 0;

	if (!tree)
		return (0);
	if (tree->left)
		height_l = 1 + binary_tree_height(tree->left);
	if (tree->right)
		height_r = 1 + binary_tree_height(tree->right);
	if (height_l > height_r)
		return (height_l);

	else
		return (height_r);
}
