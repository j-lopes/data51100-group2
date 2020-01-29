# -*- coding: utf-8 -*-
"""
This program computes the mean and variance of user inputted values using online algorithms
Students:   Jenna Lopes, Geoffrey Stewart, Ryan Wade
Date:       Jan. 23, 2020
Course:     DATA-51100-002: 	Statistical Programming
Semester:   Spring 2020
Assignment: PROGRAMMING ASSIGNMENT #2

"""


def get_user_input():
    """
    A method to get handle retrieving the user's input for number of clusters.

    :return: the integer, representing the number of clusters as entered by the user
    """
    valid_integer = False
    # loop until a valid input was provided
    while not valid_integer:
        try:
            num_clusters = int(input("Enter the number of clusters: "))
            if num_clusters >= 0:
                valid_integer = True
                return num_clusters
            else:
                print('A negative number was provided, but a positive integer is required.')
                print('')
        except Exception as e:
            print(e)
            print('An invalid number was provided, a positive integer is required.')
            print('')


def distance(centroid, point):
    """
    A method which computes the distance between a centroid and a point

    :param centroid: a float number which is one of the centroids for a cluster of points
    :param point: a float number which is one of the points being clustered
    :return: the distance between the two numbers
    """
    return abs(centroid - point)


def mean(list_of_points):
    """
    A method which calculates the mean value for the provided list of points

    :param list_of_points: the list of points currently assigned to a cluster
    :return: the mean value for the provided list of points
    """
    return sum(list_of_points)/len(list_of_points)


def print_clusters(cluster_points_list):
    """
    A method which prints out the clusters of points according to the assignment requirements

    :param cluster_points_list: the list of clustered points
    """
    for i, cluster_points in enumerate(cluster_points_list):
        print('%d [%s]' % (i, ', '.join(map(str, cluster_points))))
    print('')


def get_final_output(list_of_points, cluster_points_list):
    """
    Generate the final output according to the assignment requirements

    :param list_of_points: the list of input points
    :param cluster_points_list:  the list of clustered points
    :return: output: The output
    """
    output = ''
    for point in list_of_points:
        for i, cluster_points in enumerate(cluster_points_list):
            if point in cluster_points:
                output += 'Point %s in cluster %s\n' % (point, i)
                break
    return output


def main():
    # log the required output header
    print('DATA-51100, Spring 2020')
    print('NAMES: Jenna Lopes, Geoffrey Stewart, Ryan Wade')
    print('PROGRAMMING ASSIGNMENT #2')
    print('')

    # get the value for num_clusters - this is also known as the value "k"
    num_clusters = get_user_input()
    print('')

    # read the input file
    with open('prog2-input-data.txt') as f:
        list_of_points = [float(x.rstrip()) for x in f]

    # print('num_clusters is: %d' % num_clusters)
    # print('list of points is: %s' % list_of_points)

    # the case where the number of clusters is larger than the the number of input values is not supported
    if num_clusters > len(list_of_points):
        print('Having more clusters than the number of input values is not supported.')
        return

    # initialize the list of centroids to the first k input points
    centroids = [list_of_points[x] for x in range(num_clusters)]

    # initialize a new list containing num_clusters (k) empty lists
    cluster_points_list = [[] for i in range(num_clusters)]
    # cluster_points_list_copy will be used to determine the point of convergence
    cluster_points_list_copy = None

    max_kmeans_iterations = 1000
    iteration_count = 1

    # loop while the k-means algorithm has not converged, and the number of iterations is less than the defined max
    while cluster_points_list_copy != cluster_points_list and iteration_count < max_kmeans_iterations:
        # print('centroids are %s' % centroids)
        cluster_points_list_copy = cluster_points_list.copy()
        # again, initialize a new list containing num_clusters (k) empty lists
        cluster_points_list = [[] for i in range(num_clusters)]

        for point in list_of_points:
            # create a dictionary with the distance between all the centroids and the point as the key, and the centroid
            # for the value. This allows to easily get the minimum, and look up which centroid yielded the minimum
            distance_centroid_index_dict = {distance(centroid, point): i for i, centroid in enumerate(centroids)}
            min_centroid_difference = min(distance_centroid_index_dict.keys())
            # get the centroid index from the dictionary using the min_centroid_difference value
            closest_centroid_index = distance_centroid_index_dict[min_centroid_difference]
            # assign the point to the correct cluster using the determined index
            cluster_points_list[closest_centroid_index].append(point)

        print('Iteration %d' % iteration_count)
        print_clusters(cluster_points_list)

        # recompute the centroids and update the list of centroids
        centroids = [mean(cluster_points) for cluster_points in cluster_points_list]
        iteration_count += 1

    # get the final output string
    output = get_final_output(list_of_points, cluster_points_list)
    print(output)

    # write the output to the output file
    with open('prog2-output-data.txt', 'w') as f:
        f.write(output)


if __name__ == "__main__":
    main()
