import streamlit as st
from actions import ProblemSolver   
problemsolver = ProblemSolver()

problem = {

    # Initial and goal states for problem b (Sussman Anomaly)
    #'initial': ['space on a', 'a on table', 'space on b', 'b on table2', 'space on c', 'c on table3'],
    #'goal': ['space on a', 'a on b', 'b on c', 'c on table', 'space on table2', 'space on table3'],

    # Initial and goal states for problem a
    'start': ['space on table', 'space on b', 'b on table2', 'space on c', 'c on a', 'a on table3'],
    'finish': ['space on b', 'b on table', 'space on a', 'a on table2', 'space on c', 'c on table3'],

    'ops': [
        {
            'action': 'move a from b to c',
            'preconds': [
                'space on a',
                'space on c',
                'a on b'
            ],
            'add': [
                'a on c',
                'space on b'
            ],
            'delete': [
                'a on b',
                'space on c'
            ]
        },
        {
            'action': 'move a from table to b',
            'preconds': [
                'space on a',
                'space on b',
                'a on table'
            ],
            'add': [
                'a on b',
                'space on table'
            ],
            'delete': [
                'a on table',
                'space on b'
            ]
        },
        {
            'action': 'move a from b to table',
            'preconds': [
                'space on a',
                'space on table',
                'a on b'
            ],
            'add': [
                'a on table',
                'space on b'
            ],
            'delete': [
                'a on b',
                'space on table'
            ]
        },
        {
            'action': 'move a from c to b',
            'preconds': [
                'space on a',
                'space on b',
                'a on c'
            ],
            'add': [
                'a on b',
                'space on c'
            ],
            'delete': [
                'a on c',
                'space on b'
            ]
        },
        {
            'action': 'move a from table to c',
            'preconds': [
                'space on a',
                'space on c',
                'a on table'
            ],
            'add': [
                'a on c',
                'space on table'
            ],
            'delete': [
                'a on table',
                'space on c'
            ]
        },
        {
            'action': 'move a from c to table',
            'preconds': [
                'space on a',
                'space on table',
                'a on c'
            ],
            'add': [
                'a on table',
                'space on c'
            ],
            'delete': [
                'a on c',
                'space on table'
            ]
        },
        ###### START
        {
            'action': 'move a from table to table3',
            'preconds': [
                'space on a',
                'space on table3',
                'a on table'
            ],
            'add': [
                'a on table3',
                'space on table'
            ],
            'delete': [
                'a on table',
                'space on table3'
            ]
        },
        {
            'action': 'move a from table2 to table3',
            'preconds': [
                'space on a',
                'space on table3',
                'a on table2'
            ],
            'add': [
                'a on table3',
                'space on table2'
            ],
            'delete': [
                'a on table2',
                'space on table3'
            ]
        },
        {
            'action': 'move a from b to table3',
            'preconds': [
                'space on a',
                'space on table3',
                'a on b'
            ],
            'add': [
                'a on table3',
                'space on b'
            ],
            'delete': [
                'a on b',
                'space on table3'
            ]
        },
        {
            'action': 'move a from c to table3',
            'preconds': [
                'space on a',
                'space on table3',
                'a on c'
            ],
            'add': [
                'a on table3',
                'space on c'
            ],
            'delete': [
                'a on c',
                'space on table3'
            ]
        },
        {
            'action': 'move a from table3 to table',
            'preconds': [
                'space on a',
                'space on table',
                'a on table3'
            ],
            'add': [
                'a on table',
                'space on table3'
            ],
            'delete': [
                'a on table3',
                'space on table'
            ]
        },
        {
            'action': 'move a from table3 to table2',
            'preconds': [
                'space on a',
                'space on table2',
                'a on table3'
            ],
            'add': [
                'a on table2',
                'space on table3'
            ],
            'delete': [
                'a on table3',
                'space on table2'
            ]
        },
        {
            'action': 'move a from table3 to b',
            'preconds': [
                'space on a',
                'space on b',
                'a on table3'
            ],
            'add': [
                'a on b',
                'space on table3'
            ],
            'delete': [
                'a on table3',
                'space on b'
            ]
        },
        {
            'action': 'move a from table3 to c',
            'preconds': [
                'space on a',
                'space on c',
                'a on table3'
            ],
            'add': [
                'a on c',
                'space on table3'
            ],
            'delete': [
                'a on table3',
                'space on c'
            ]
        },
        {
            'action': 'move a from table2 to table',
            'preconds': [
                'space on a',
                'space on table',
                'a on table2'
            ],
            'add': [
                'a on table',
                'space on table2'
            ],
            'delete': [
                'a on table2',
                'space on table'
            ]
        },
        {
            'action': 'move a from table2 to b',
            'preconds': [
                'space on a',
                'space on b',
                'a on table2'
            ],
            'add': [
                'a on b',
                'space on table2'
            ],
            'delete': [
                'a on table2',
                'space on b'
            ]
        },
        {
            'action': 'move a from table2 to c',
            'preconds': [
                'space on a',
                'space on c',
                'a on table2'
            ],
            'add': [
                'a on c',
                'space on table2'
            ],
            'delete': [
                'a on table2',
                'space on c'
            ]
        },
        {
            'action': 'move a from table to table2',
            'preconds': [
                'space on a',
                'space on table2',
                'a on table'
            ],
            'add': [
                'a on table2',
                'space on table'
            ],
            'delete': [
                'a on table',
                'space on table2'
            ]
        },
        {
            'action': 'move a from b to table2',
            'preconds': [
                'space on a',
                'space on table2',
                'a on b'
            ],
            'add': [
                'a on table2',
                'space on b'
            ],
            'delete': [
                'a on b',
                'space on table2'
            ]
        },
        {
            'action': 'move a from c to table2',
            'preconds': [
                'space on a',
                'space on table2',
                'a on c'
            ],
            'add': [
                'a on table2',
                'space on c'
            ],
            'delete': [
                'a on c',
                'space on table2'
            ]
        },
        ##### END
        {
            'action': 'move b from a to c',
            'preconds': [
                'space on b',
                'space on c',
                'b on a'
            ],
            'add': [
                'b on c',
                'space on a'
            ],
            'delete': [
                'b on a',
                'space on c'
            ]
        },
        {
            'action': 'move b from table to a',
            'preconds': [
                'space on b',
                'space on a',
                'b on table'
            ],
            'add': [
                'b on a',
                'space on table'
            ],
            'delete': [
                'b on table',
                'space on a'
            ]
        },
        {
            'action': 'move b from a to table',
            'preconds': [
                'space on b',
                'space on table',
                'b on a'
            ],
            'add': [
                'b on table',
                'space on a'
            ],
            'delete': [
                'b on a',
                'space on table'
            ]
        },
        {
            'action': 'move b from c to a',
            'preconds': [
                'space on b',
                'space on a',
                'b on c'
            ],
            'add': [
                'b on a',
                'space on c'
            ],
            'delete': [
                'b on c',
                'space on a'
            ]
        },
        {
            'action': 'move b from table to c',
            'preconds': [
                'space on b',
                'space on c',
                'b on table'
            ],
            'add': [
                'b on c',
                'space on table'
            ],
            'delete': [
                'b on table',
                'space on c'
            ]
        },
        {
            'action': 'move b from c to table',
            'preconds': [
                'space on b',
                'space on table',
                'b on c'
            ],
            'add': [
                'b on table',
                'space on c'
            ],
            'delete': [
                'b on c',
                'space on table'
            ]
        },
        ###### START
        {
            'action': 'move b from table to table3',
            'preconds': [
                'space on b',
                'space on table3',
                'b on table'
            ],
            'add': [
                'b on table3',
                'space on table'
            ],
            'delete': [
                'b on table',
                'space on table3'
            ]
        },
        {
            'action': 'move b from table2 to table3',
            'preconds': [
                'space on b',
                'space on table3',
                'b on table2'
            ],
            'add': [
                'b on table3',
                'space on table2'
            ],
            'delete': [
                'b on table2',
                'space on table3'
            ]
        },
        {
            'action': 'move b from c to table3',
            'preconds': [
                'space on b',
                'space on table3',
                'b on c'
            ],
            'add': [
                'b on table3',
                'space on c'
            ],
            'delete': [
                'b on c',
                'space on table3'
            ]
        },
        {
            'action': 'move b from a to table3',
            'preconds': [
                'space on b',
                'space on table3',
                'b on a'
            ],
            'add': [
                'b on table3',
                'space on a'
            ],
            'delete': [
                'b on a',
                'space on table3'
            ]
        },
        {
            'action': 'move b from table3 to table',
            'preconds': [
                'space on b',
                'space on table',
                'b on table3'
            ],
            'add': [
                'b on table',
                'space on table3'
            ],
            'delete': [
                'b on table3',
                'space on table'
            ]
        },
        {
            'action': 'move b from table3 to table2',
            'preconds': [
                'space on b',
                'space on table2',
                'b on table3'
            ],
            'add': [
                'b on table2',
                'space on table3'
            ],
            'delete': [
                'b on table3',
                'space on table2'
            ]
        },
        {
            'action': 'move b from table3 to c',
            'preconds': [
                'space on b',
                'space on c',
                'b on table3'
            ],
            'add': [
                'b on c',
                'space on table3'
            ],
            'delete': [
                'b on table3',
                'space on c'
            ]
        },
        {
            'action': 'move b from table3 to a',
            'preconds': [
                'space on b',
                'space on a',
                'b on table3'
            ],
            'add': [
                'b on a',
                'space on table3'
            ],
            'delete': [
                'b on table3',
                'space on a'
            ]
        },
        {
            'action': 'move b from table2 to table',
            'preconds': [
                'space on b',
                'space on table',
                'b on table2'
            ],
            'add': [
                'b on table',
                'space on table2'
            ],
            'delete': [
                'b on table2',
                'space on table'
            ]
        },
        {
            'action': 'move b from table2 to c',
            'preconds': [
                'space on b',
                'space on c',
                'b on table2'
            ],
            'add': [
                'b on c',
                'space on table2'
            ],
            'delete': [
                'b on table2',
                'space on c'
            ]
        },
        {
            'action': 'move b from table2 to a',
            'preconds': [
                'space on b',
                'space on a',
                'b on table2'
            ],
            'add': [
                'b on a',
                'space on table2'
            ],
            'delete': [
                'b on table2',
                'space on a'
            ]
        },
        {
            'action': 'move b from table to table2',
            'preconds': [
                'space on b',
                'space on table2',
                'b on table'
            ],
            'add': [
                'b on table2',
                'space on table'
            ],
            'delete': [
                'b on table',
                'space on table2'
            ]
        },
        {
            'action': 'move b from c to table2',
            'preconds': [
                'space on b',
                'space on table2',
                'b on c'
            ],
            'add': [
                'b on table2',
                'space on c'
            ],
            'delete': [
                'b on c',
                'space on table2'
            ]
        },
        {
            'action': 'move b from a to table2',
            'preconds': [
                'space on b',
                'space on table2',
                'b on a'
            ],
            'add': [
                'b on table2',
                'space on a'
            ],
            'delete': [
                'b on a',
                'space on table2'
            ]
        },
        ##### END
        {
            'action': 'move c from a to b',
            'preconds': [
                'space on c',
                'space on b',
                'c on a'
            ],
            'add': [
                'c on b',
                'space on a'
            ],
            'delete': [
                'c on a',
                'space on b'
            ]
        },
        {
            'action': 'move c from table to a',
            'preconds': [
                'space on c',
                'space on a',
                'c on table'
            ],
            'add': [
                'c on a',
                'space on table'
            ],
            'delete': [
                'c on table',
                'space on a'
            ]
        },
        {
            'action': 'move c from a to table',
            'preconds': [
                'space on c',
                'space on table',
                'c on a'
            ],
            'add': [
                'c on table',
                'space on a'
            ],
            'delete': [
                'c on a',
                'space on table'
            ]
        },
        {
            'action': 'move c from b to a',
            'preconds': [
                'space on c',
                'space on a',
                'c on b'
            ],
            'add': [
                'c on a',
                'space on b'
            ],
            'delete': [
                'c on b',
                'space on a'
            ]
        },
        {
            'action': 'move c from table to b',
            'preconds': [
                'space on c',
                'space on b',
                'c on table'
            ],
            'add': [
                'c on b',
                'space on table'
            ],
            'delete': [
                'c on table',
                'space on b'
            ]
        },
        {
            'action': 'move c from b to table',
            'preconds': [
                'space on c',
                'space on table',
                'c on b'
            ],
            'add': [
                'c on table',
                'space on b'
            ],
            'delete': [
                'c on b',
                'space on table'
            ]
        },
        ###### START
        {
            'action': 'move c from table to table3',
            'preconds': [
                'space on c',
                'space on table3',
                'c on table'
            ],
            'add': [
                'c on table3',
                'space on table'
            ],
            'delete': [
                'c on table',
                'space on table3'
            ]
        },
        {
            'action': 'move c from table2 to table3',
            'preconds': [
                'space on c',
                'space on table3',
                'c on table2'
            ],
            'add': [
                'c on table3',
                'space on table2'
            ],
            'delete': [
                'c on table2',
                'space on table3'
            ]
        },
        {
            'action': 'move c from b to table3',
            'preconds': [
                'space on c',
                'space on table3',
                'c on b'
            ],
            'add': [
                'c on table3',
                'space on b'
            ],
            'delete': [
                'c on b',
                'space on table3'
            ]
        },
        {
            'action': 'move c from a to table3',
            'preconds': [
                'space on c',
                'space on table3',
                'c on a'
            ],
            'add': [
                'c on table3',
                'space on a'
            ],
            'delete': [
                'c on a',
                'space on table3'
            ]
        },
        {
            'action': 'move c from table3 to table',
            'preconds': [
                'space on c',
                'space on table',
                'c on table3'
            ],
            'add': [
                'c on table',
                'space on table3'
            ],
            'delete': [
                'c on table3',
                'space on table'
            ]
        },
        {
            'action': 'move c from table3 to table2',
            'preconds': [
                'space on c',
                'space on table2',
                'c on table3'
            ],
            'add': [
                'c on table2',
                'space on table3'
            ],
            'delete': [
                'c on table3',
                'space on table2'
            ]
        },
        {
            'action': 'move c from table3 to b',
            'preconds': [
                'space on c',
                'space on b',
                'c on table3'
            ],
            'add': [
                'c on b',
                'space on table3'
            ],
            'delete': [
                'c on table3',
                'space on b'
            ]
        },
        {
            'action': 'move c from table3 to a',
            'preconds': [
                'space on c',
                'space on a',
                'c on table3'
            ],
            'add': [
                'c on a',
                'space on table3'
            ],
            'delete': [
                'c on table3',
                'space on a'
            ]
        },
        {
            'action': 'move c from table2 to table',
            'preconds': [
                'space on c',
                'space on table',
                'c on table2'
            ],
            'add': [
                'c on table',
                'space on table2'
            ],
            'delete': [
                'c on table2',
                'space on table'
            ]
        },
        {
            'action': 'move c from table2 to b',
            'preconds': [
                'space on c',
                'space on b',
                'c on table2'
            ],
            'add': [
                'c on b',
                'space on table2'
            ],
            'delete': [
                'c on table2',
                'space on b'
            ]
        },
        {
            'action': 'move c from table2 to a',
            'preconds': [
                'space on c',
                'space on a',
                'c on table2'
            ],
            'add': [
                'c on a',
                'space on table2'
            ],
            'delete': [
                'c on table2',
                'space on a'
            ]
        },
        {
            'action': 'move c from table to table2',
            'preconds': [
                'space on c',
                'space on table2',
                'c on table'
            ],
            'add': [
                'c on table2',
                'space on table'
            ],
            'delete': [
                'c on table',
                'space on table2'
            ]
        },
        {
            'action': 'move c from b to table2',
            'preconds': [
                'space on c',
                'space on table2',
                'c on b'
            ],
            'add': [
                'c on table2',
                'space on b'
            ],
            'delete': [
                'c on b',
                'space on table2'
            ]
        },
        {
            'action': 'move c from a to table2',
            'preconds': [
                'space on c',
                'space on table2',
                'c on a'
            ],
            'add': [
                'c on table2',
                'space on a'
            ],
            'delete': [
                'c on a',
                'space on table2'
            ]
        }
        ##### END
    ]
}

def main():
    start = problem['start']
    finish = problem['finish']
    ops = problem['ops']

    for actions in problemsolver.mainsolver(start, finish, ops):
        st.write(f"Executing.. {actions}")

if __name__ == '__main__':
    st.title("Block World Problem Solver")
    st.write("************* STARTING ************")
    main()
    st.write("************** FINISH ******************")