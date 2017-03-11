# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from util import Node
from util import GraphQueue
from util import GraphStack
from util import PriorityQueue
from util import PriorityQueueWithFunction
from util import manhattanDistance

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).

  You do not need to change anything in this class, ever.
  """

  def getStartState(self):
     """
     Returns the start state for the search problem
     """
     util.raiseNotDefined()

  def isGoalState(self, state):
     """
       state: Search state

     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state

     For a given state, this should return a list of triples,
     (successor, action, stepCost), where 'successor' is a
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take

     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()


def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Returns a solution or failure

  Search the deepest nodes in the search tree first
  """
  #Initalise Frontier Using Initial State of Problem
  frontier = GraphStack()
  startNode = Node((problem.getStartState(), None, None))

  #Check if start node is goal
  if problem.isGoalState(startNode.state):
      return []

  for successors in problem.getSuccessors(problem.getStartState()):
      newNode = Node(successors, startNode)
      frontier.push(newNode)

  #initialize the explored set to be empty
  explored = list()
  explored.append(startNode.state)

  while not frontier.isEmpty():
      #choose a leaf node and remove it from the frontier
      leafNode = frontier.pop()
      #if the node contains a goal state then return the corresponding solution
      if problem.isGoalState(leafNode.state):
          return leafNode.getPath()
      #add state visited node to the explored set
      explored.append(leafNode.state)
      #expand the chosen node, adding the resulting nodes to the frontier if not in the frontier or explored set
      for successor in problem.getSuccessors(leafNode.state):
          newNode = Node(successor, leafNode)
          if newNode.state not in frontier.stateList and newNode.state not in explored:
              frontier.push(newNode)
  #if the frontier is empty then return failure
  return []

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  """
  frontier = GraphQueue()
  startNode = Node((problem.getStartState(), None, None))

  #Check if start node is goal
  if problem.isGoalState(startNode.state):
      return []

  for successors in problem.getSuccessors(problem.getStartState()):
      newNode = Node(successors, startNode)
      frontier.push(newNode)

  explored = list()
  explored.append(startNode.state)

  while not frontier.isEmpty():
      leafNode = frontier.pop()
      if problem.isGoalState(leafNode.state):
          return leafNode.getPath()
      explored.append(leafNode.state)
      for successor in problem.getSuccessors(leafNode.state):
          newNode = Node(successor, leafNode)
          if newNode.state not in frontier.stateList and newNode.state not in explored:
              frontier.push(newNode)
  print "No solution found"
  return []

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  frontier = PriorityQueue()
  startNode = Node((problem.getStartState(), None, None))

  #Check if start node is goal
  if problem.isGoalState(startNode.state):
      return []

  for successors in problem.getSuccessors(problem.getStartState()):
      newNode = Node(successors, startNode)
      frontier.push(newNode, 0)

  explored = list()
  explored.append(startNode.state)

  while not frontier.isEmpty():
      leafNode = frontier.pop()
      if problem.isGoalState(leafNode.state):
          return leafNode.getPath()
      explored.append(leafNode.state)
      for successor in problem.getSuccessors(leafNode.state):
          newNode = Node(successor, leafNode)
          if newNode.state not in frontier.stateList and newNode.state not in explored:
              frontier.push(newNode, newNode.pathCost)
  return []

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  frontier = PriorityQueueWithFunction(heuristic, problem)
  startNode = Node((problem.getStartState(), None, None))

  #Check if start node is goal
  if problem.isGoalState(startNode.state):
      return []

  for successors in problem.getSuccessors(problem.getStartState()):
      newNode = Node(successors, startNode)
      frontier.push(newNode)

  explored = list()
  explored.append(startNode.state)

  while not frontier.isEmpty():
      leafNode = frontier.pop()
      if problem.isGoalState(leafNode.state):
          return leafNode.getPath()
      explored.append(leafNode.state)
      for successor in problem.getSuccessors(leafNode.state):
          newNode = Node(successor, leafNode)
          if newNode.state not in frontier.stateList and newNode.state not in explored:
              frontier.push(newNode)
  return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
