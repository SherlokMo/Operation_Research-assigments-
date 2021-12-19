from abstract_data_type import *


def knapsack_branch_and_bound(items, weight_limit):
    sorted_items = Items(sorted(items, key=lambda item: item.value_to_weight_ratio, reverse=True))

    lower = lambda *args: knapsack_greedy_whole_items(*args).value
    upper = knapsack_greedy_fractional_items
    initial_state = SearchState(float('-inf'), float('inf'), sorted_items, frozenset(), weight_limit, 0)
    priority_queue = Heap([initial_state],
                          key=lambda state: (-state.upper_bound, -state.lower_bound, len(state.remaining_items)))

    while priority_queue:
        # Questions:
        # * Will this process end? That is, will we always eventuall get `state.upper_bound == state.lower_bound`?
        #    Yes! Eventually, remaining_items.rest() will be empty and we'll get right_upper == right_lower == right_value below.
        state = priority_queue.pop()

        if state.upper_bound == state.lower_bound:
            solution_items = state.packed_items | knapsack_greedy_whole_items(state.remaining_items, state.weight_limit).items
            return knapsack_solution(solution_items)
        else:
            assert not state.remaining_items.empty()
            first = state.remaining_items.first()
            rest = state.remaining_items.rest()

            # branch "left": take first item
            left_items = state.packed_items | {first}
            left_weight = state.weight_limit - first.weight
            left_value = state.value + first.value
            left_upper = upper(rest, left_weight) + left_value
            left_lower = lower(rest, left_weight) + left_value
            left_state = SearchState(left_upper, left_lower, rest, left_items, left_weight, left_value)

            if left_state.weight_limit >= 0:
                priority_queue.push(left_state)

            # branch "right": throw away first item
            right_items = state.packed_items
            right_weight = state.weight_limit
            right_value = state.value
            right_upper = upper(rest, right_weight) + right_value
            right_lower = lower(rest, right_weight) + right_value
            right_state = SearchState(right_upper, right_lower, rest, right_items, right_weight, right_value)

            priority_queue.push(right_state)


def knapsack_greedy_whole_items(items, weight_limit):
    sorted_items_list = sorted(items, key=lambda item: item.value_to_weight_ratio, reverse=True)
    collected_items = set()

    for item in sorted_items_list:
        if item.weight <= weight_limit:
            weight_limit -= item.weight
            collected_items.add(item)

    return KnapsackSolution(frozenset(collected_items), sum(item.value for item in collected_items))


def knapsack_greedy_fractional_items(items, weight_limit):
    sorted_items_list = sorted(items, key=lambda item: item.value_to_weight_ratio, reverse=True)
    value = 0

    for item in sorted_items_list:
        if item.weight <= weight_limit:
            weight_limit -= item.weight
            value += item.value
        else:
            fraction = float(weight_limit) / item.weight
            value = fraction * item.value
            weight_limit = 0

    return value