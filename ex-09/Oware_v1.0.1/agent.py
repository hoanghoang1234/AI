import random
from envs.oware import Oware
from agent_interface import AgentInterface
from iterative_deepening import IterativeDeepening

class IDAgent(IterativeDeepening):
    """
    Implementation of iterative deepening
    """
    def __init__(self):
        super().__init__(AgentClass=Agent)

class Agent(AgentInterface):
    """
    An agent who plays the Oware game

    Methods
    -------
    `info` returns the agent's information
    `decide` chooses an action from possible actions
    """

    def __init__(self, depth: int = 7):
        self.depth = depth

    @staticmethod
    def info():
        """
        Return the agent's information

        Returns
        -------
        Dict[str, str]
            `agent name` is the agent's name
            `student name` is the list team members' names
            `student number` is the list of student numbers of the team members
        """
        # -------- Task 1 -------------------------
        # Please complete the following information

        return {"agent name": "XiaoPengYou",  # COMPLETE HERE
                "student name": ["Huang, Jiangyi"],  # COMPLETE HERE
                "student number": ["100114773"]}  # COMPLETE HERE

    def decide(self, state: Oware, actions: list):
        """
        Generate a sequence of increasingly preferable actions

        Given the current `state` and all possible `actions`, this function
        should choose the action that leads to the agent's victory.
        However, since there is a time limit for the execution of this function,
        it is possible to choose a sequence of increasing preferable actions.
        Therefore, this function is designed as a generator; it means it should
        have no return statement, but it should `yield` a sequence of increasing
        good actions.

        IMPORTANT: If no action is yielded within the time limit, the game will
        choose a random action for the player.

        Parameters
        ----------
        state: Oware
            Current state of the game
        actions: list
            List of all possible actions

        Yields
        ------
        action
            the chosen `action`
        """
        # -------- TASK 2 ------------------------------------------------------
        # Your task is to implement an algorithm to choose an action form the
        # given `actions` list. You can implement any algorithm you want.
        # However, you should keep in mind that the execution time of this
        # function is limited. So, instead of choosing just one action, you can
        # generate a sequence of increasing good action.
        # This function is a generator. So, you should use `yield` statement
        # rather than `return` statement. To find more information about
        # generator functions, you can take a look at:
        # https://www.geeksforgeeks.org/generators-in-python/
        #
        # If you generate multiple actions, the last action will be used in the
        # game.
        #
        #
        # Tips
        # ====
        # 0. If you want to develop a new heuristic function, you might need
        #    more information about a state. In this case, the following APIs
        #    will be helpful for you. To explain them better, let suppose we
        #    are in the following state:
        #
        #   =======================================================
        #          Collected stones:
        #               Random: 0
        #               Human: 3
        #          Current player: Human
        #
        #           5  4  3  2  1  0
        #          ╔══╦══╦══╦══╦══╦══╗
        #          ║8 ║8 ║8 ║3 ║1 ║2 ║
        #          ╠══╬══╬══╬══╬══╬══╣
        #          ║1 ║6 ║1 ║2 ║0 ║8 ║
        #          ╚══╩══╩══╩══╩══╩══╝
        #           6  7  8  9  10 11
        #   =======================================================
        #
        #   In this state the current player is the second player (Human).
        #   The indices outside of the box shows the corresponding pit index.
        #   The numbers inside of the box, shows how many stone are inside of
        #   each pit.
        #    
        #       a) `state.get_board()`:
        #               Returns a list of integers, describing how many
        #               stones are in each pit. The first half elements always
        #               correspond to the current player's pits, and the
        #               second half are for the opponents (the order is
        #               counterclockwise).
        #               NOTE: Please keep in mind that the order of elements
        #                     is not absolute; it is relative to the current
        #                     player.
        #
        #               For example, the return value of this API for the above
        #               state is: `[2, 1, 3, 8, 8, 8, 1, 6, 1, 2, 0, 8]`
        #
        #       b) `state.get_collected_stone()`:
        #               Returns a two element list; the first element denotes
        #               How many stones the current player has collected, and
        #               the second element shows the collected stones of the
        #               opponent.
        #               NOTE: Please keep in mind that the order of elements
        #                     is not absolute; it is relative to the current
        #                     player.
        #
        #               For example, the return value for our example state is:
        #               `[3, 0]`.
        #
        #       c) `state.get_turn_number()`:
        #               Returns how many turns has passed since the beginning of
        #               the game.
        #          `state.MAX_TURNS`:
        #               The maximum number of turns that a game can have.
        #
        #               For example, `state.get_turn_number() - state.MAX_TURNS`
        #               specifies how many turns remains in the game.
        #       
        #       d) `state.actions()`:
        #               Returns the list of all possible actions in the current
        #               state.
        #
        #       e) `state.successor(action)`:
        #               Returns the next state after applying the `action` on
        #               the current state.
        #
        #       f) `state.is_winner()`:
        #               Returns:
        #                   `None`  => if the game is not over yet,
        #                   `1`     => if the current player is the winner,
        #                   `0`     => if the game ended in a draw, or,
        #                   `-1`    => if the current player lost the game.
        #
        # 1. `MinimaxAgent` is an example that has used most of those APIs.
        #    Please take a look at `minimax_agent.py` if you feel it might be
        #    helpful.
        #
        # 2. If you need to simulate a game from a specific state to find the
        #    the winner, you can use the following pattern:
        #    ```
        #    simulator = Game(FirstAgent(), SecondAgent())
        #    winner = simulator.play(starting_state=specified_state)
        #    ```
        #    The `MCSAgent` has illustrated a concrete example of this
        #    pattern.
        #
        # 3. You are free to choose what kind of game-playing agent you want to
        #    implement. Some obvious approaches are:
        # 3.1 Implement alpha-beta (and investigate its potential for searching deeper
        #     than what is possible with Minimax). Also, the order in which the actions
        #     are tried in a given node impacts the effectiveness of alpha-beta: you could
        #     investigate different ways of ordering the actions/successor states.
        # 3.2 Try out better heuristics.
        # 3.3 You could try out more advanced Monte Carlo search methods; however, we do
        #     not know whether MCTS is competitive because of the high cost of the full
        #     gameplays.
        # 3.4 You could of course try something completely different if you are willing to
        #     invest more time.
        #
        # GL HF :)
        # ----------------------------------------------------------------------

        # Replace the following lines with your algorithm
        random.shuffle(actions)
        best_action = actions[0]

        max_value = float('-inf')
        for action in actions:
            action_value = self.min_value_alpha_beta(state.successor(action), self.depth - 1, float('-inf'), float('inf'))
            if action_value > max_value:
                max_value = action_value
                best_action = action
        
        yield best_action

    def heuristic(self, state: Oware):
        collected_stones = state.get_collected_stone()
        return collected_stones[0] - collected_stones[1] 
    
    def max_value_alpha_beta(self, state: Oware, depth: int, alpha, beta):
        """
        Get the value of each action by passing its successor to min_value_alpha_beta
        function. Return the maximum value of successors.
        
        `max_value_alpha_beta()` function sees the game from players's perspective, trying
        to maximize the value of next state.
        
        NOTE: when passing the successor to min_value, `depth` must be
        reduced by 1, as we go down the Minimax tree.
        
        NOTE: the player must check if it is the winner (or loser)
        of the game, in which case, a large value (or a negative value) must
        be assigned to the state. Additionally, if the game is not over yet,
        but we have `depth == 0`, then we should return the heuristic value
        of the current state.
        """

        # Termination conditions
        is_winner = state.is_winner()
        if is_winner is not None:
            return is_winner * float('inf')
        if depth == 0:
            return self.heuristic(state)

        # If it is not terminated
        actions = state.actions()
        best = float('-inf')
        for action in actions:
            value = self.min_value_alpha_beta(state.successor(action), depth - 1, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)
            if alpha >= beta:
                break
        return best

    def min_value_alpha_beta(self, state: Oware, depth: int, alpha, beta):
        """
        Get the value of each action by passing its successor to max_value_alpha_beta
        function. Return the minimum value of successors.
        
        `min_value_alpha_beta()` function sees the game from opponent's perspective, trying
        to minimize the value of next state.
        
        NOTE: when passing the successor to max_value, `depth` must be
        reduced by 1, as we go down the Minimax tree.

        NOTE: the opponent must check if it is the winner (or loser)
        of the game, in which case, a negative value (or a large value) must
        be assigned to the state. Additionally, if the game is not over yet,
        but we have `depth == 0`, then we should return the heuristic value
        of the current state.
        """

        # Termination conditions
        is_winner = state.is_winner()
        if is_winner is not None:
            return is_winner * float('-inf')
        if depth == 0:
            return -self.heuristic(state)  # Because heuristic value is calculated for the current player, which is the
                                           # opponent, we should multiply it with -1

        # If it is not terminated
        actions = state.actions()
        best = float('inf')
        for action in actions:
            value = self.max_value_alpha_beta(state.successor(action), depth - 1, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)
            if alpha >= beta:
                break
        return best
