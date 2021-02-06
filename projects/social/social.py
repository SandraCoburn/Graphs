import random
import time
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'User({repr(self.name)}'

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        self.counter = 0

    def add_friendship(self, user_id, friend_id):
        self.counter += 1
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
    

    def reset(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def populate_graph(self, num_users, avg_friendships): # O(1/2 * n^2) == O(n^2)
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.reset()

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create friendships
        possible_friendships = []
        
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)

        for i in range(num_users * avg_friendships // 2):
            friendships = possible_friendships[i]
            self.add_friendship(friendships[0], friendships[1])

        '''
        total_friendships = num_users * avg_friendships
        # Add users
        ## use num_users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        friendships =[]
        for user in range(1, self.last_id +1):
            for friend in range(user + 1, num_users + 1):
                friendship = (user, friend)
                friendships.append(friendship)

        ## make a list with all posible friendships
        # 5 users: [(1,2), (1,2), ()]
        ### shuffle the list 
        self.

        ### Take as many as we need
        total_friendships = num_users * avg_friendships
        random_friendships = friendships[:total_friendships//2]

        ## add to self.frienships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])
        '''
    def populate_graph_linear(self, num_users, avg_friendships):
        # Reset graph
        self.reset()

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create friendships
        target_friendships = num_users * avg_friendships
        friendships_successfully_added = 0
        failures = 0
        
        #Continue this till we have the number of friendships as we need:
        while friendships_successfully_added < target_friendships:
            ## Choose two random numbers (integers) between 1 and self.last_id
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            ## Try to make that friendship
            added_friendship = self.add_friendship(user_id, friend_id)
            ## If it works increment the friendship's counter
            if added_friendship:
                friendships_successfully_added += 2
            else:
                failures += 1
        print(f"failures: {failures}")

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # Use BFS to touch every single node with the shortest path
        # Bring the queue 
        queue = Queue()
        path = [user_id]
        queue.enqueue(path)

        while queue.size() > 0:
            current_path = queue.dequeue()
            new_user_id = current_path[-1]

            if new_user_id not in visited:
                visited[new_user_id] = current_path
                print("visited: ", visited)
                #iterate through the frienships of current user
                friends = self.friendships[new_user_id]
                for friend in friends:
                    #make a copy of the path
                    path_copy = list(current_path)
                    path_copy.append(friend)
                    queue.enqueue(path_copy)
                    print("friends: ", path_copy)
        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()

    start_time = time.time()
    sg.populate_graph(10, 5)
    end_time = time.time()
    total_time = end_time - start_time
    print(f'Quadratic time: {total_time} seconds')

    start_time = time.time()
    sg.populate_graph_linear(10, 5)
    end_time = time.time()
    total_time = end_time - start_time
    print(f'Linear time: {total_time} seconds')

    # connections = sg.get_all_social_paths(1)
    # total_paths_length = 0
    # for user_id in connections:
    #     total_paths_length += len(connections[user_id])
    # average_separation = total_paths_length / len(connections)
    # print("separation: ", average_separation)
    # print("connections: ",connections)
    # #print("users: ", sg.users)
    # print("friendships: ", sg.friendships)
    # print("Counter: ", sg.counter)
