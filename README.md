# DD2440-Advanced-Algorithms-project
The group project for the course **DD2440 Advanced Algorithms** at KTH Royal Institute of Technology. The project focused on algorithms to _approximate_ a _Minimum Spanning Forest_. 

In  ["Sublinear-time Algorithms"](https://www.wisdom.weizmann.ac.il/~oded/PTW/sublin.pdf), an algorithm is presented on how to approximate a _Minimum Spanning Tree_ (MST). This algorithm utilizes the edge weights in order to approximate the number of connected components, by iterating from **1** to max weight **W − 1**. We wanted to modify this to suit an approximation for a Minimum Spanning Forest (MSF). This was done by subtracting the number of trees in the forest times the maximum edge weights from the original MST formula. Thus eliminating the edges that should have connected the forest into an MST.

## Team Members

<ul>
    <li>
        <strong>Valdemar Gezelius</strong>
    </li>  
    <li>
        <strong>Maximilian Auer</strong>
    </li>
    <li>
        <strong>Veronica Hage</strong>
    </li>
    <li>
        <strong>Nils Balzar Ekenbäck</strong>
    </li>
</ul>

## Technologies

-   [Python3](https://www.python.org/)
