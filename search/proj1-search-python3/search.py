# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    fringe = util.Stack() # (state, direction, cost)
    explored = [] # previously visited states
    path = [] # current path

    # get start state and its successor(s)
    start = problem.getStartState()
    fringe.push((start, path)) # path should be empty at start
    goalFound = False

    while not goalFound and not fringe.isEmpty():
        # expand this state
        (xyCoord, path) = fringe.pop()
        explored.append(xyCoord)
        # state contains a goal state
        if problem.isGoalState(xyCoord):
            goalFound = True
        # state does not contain a goal state; explore
        else:
            for successors in problem.getSuccessors(xyCoord):
                # take "leftmost" successor state that has yet to be explored
                if successors[0] not in explored:
                    # add data to fringe
                    fringe.push((successors[0], path + [successors[1]]))
    return path
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue() # (state, direction, cost)
    explored = [] # previously visited states
    path = [] # current path

    # get start state and its successor(s)
    start = problem.getStartState()
    fringe.push((start, path)) # path should be empty at start
    goalFound = False
    if fringe.isEmpty():
        gailFound = True

    while not goalFound and not fringe.isEmpty():
        # expand this state
        (xyCoord, path) = fringe.pop()
        explored.append(xyCoord)
        # state contains a goal state
        if problem.isGoalState(xyCoord):
            goalFound = True
        # state does not contain a goal state; explore
        else:
            for successors in problem.getSuccessors(xyCoord):
                # take successor state that has yet to be explored
                if successors[0] not in explored:
                    # explore state
                    explored.append(successors[0])
                    # add data to fringe
                    fringe.push((successors[0], path + [successors[1]]))
    return path
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue() # (state, direction, cost)
    explored = [] # previously visited states
    path = [] # current path
    # get start state
    start = problem.getStartState()
    fringe.push((start, path), problem.getCostOfActions(path)) # path should be empty at start

    goalFound = False
    while not goalFound and not fringe.isEmpty():
        # expand this state
        (xyCoord, path) = fringe.pop()
        # path with higher priority (cheaper cost) found
        if xyCoord not in explored:
            explored.append(xyCoord)
            # state contains a goal state
            if problem.isGoalState(xyCoord):
                goalFound = True
            # state does not contain a goal state; explore
            else:
                for successors in problem.getSuccessors(xyCoord):
                    # take successor state that has yet to be explored
                    if successors[0] not in explored:
                        # add data to fringe
                        fringe.update((successors[0], path + [successors[1]]), problem.getCostOfActions(path + [successors[1]]))
    return path
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    explored = [] # previously visited states
    path = [] # current path
    # get start state
    start = problem.getStartState()
    fringe.push((start, path), (problem.getCostOfActions(path) + heuristic(start, problem))) # path should be empty at start

    goalFound = False
    while not goalFound and not fringe.isEmpty():
        # expand this state
        (xyCoord, path) = fringe.pop()
        # path with higher priority (cheaper cost) found
        if xyCoord not in explored:
            explored.append(xyCoord)
            # state contains a goal state
            if problem.isGoalState(xyCoord):
                goalFound = True
            # state does not contain a goal state; explore
            else:
                for successors in problem.getSuccessors(xyCoord):
                    # take successor state that has yet to be explored
                    if successors[0] not in explored:
                        # add data to fringe
                        fringe.update((successors[0], path + [successors[1]]), (problem.getCostOfActions(path + [successors[1]]) + heuristic(successors[0], problem)))
    return path
    util.raiseNotDefined()



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch