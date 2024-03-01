#include "binary_trees.h"

/**
 * binary_trees_ancestor -  finds the lowest common ancestor of two nodes
 * @first: pointer to first node
 * @second: pointer to second node
 * Return: ancestor node or NULL
 */

binary_tree_t *binary_trees_ancestor(const binary_tree_t *first, const binary_tree_t *second)
{
	size_t depth_1, depth_2;

	if (!first || !second)
		return (NULL);
	depth_1 = binary_tree_depth(first);
	depth_2 = binary_tree_depth(second);

	while (depth_1 > depth_2)
	{
		first = first->parent;
		depth_1--;
	}
	while (depth_2 > depth_1)
	{
		second = second->parent;
		depth_2--;
	}
	while (first && second)
	{
		if (first == second)
			return ((binary_tree_t *)first);
		first = first->parent;
		second = second->parent;
	}
	return ((binary_tree_t *)first);
}



/**
 * binary_tree_depth - measures the height of a binary tree
 * @tree: pointer to the root node to measure height
 * Return: 0
 */

size_t binary_tree_depth(const binary_tree_t *tree)
{
        size_t depth = 0;

        if (!tree)
                return (0);
        if (tree->parent)
                depth = 1 + binary_tree_depth(tree->parent);
        return (depth);
}
