// const depthFirstPrint = (graph, source) => {
//   const stack = [source];

//   while (stack.length > 0) {
//     current = stack.pop();
//     console.log(current);
//     graph[current].forEach((neighbor) => {
//       stack.push(neighbor);
//     });
//   }
// };

// const depthFirstSearch =(graph, source) => {
//   console.log(source);
//   graph[source].forEach((neighbor) => {
//     depthFirstSearch(graph, neighbor);
//   });
// }

const breadthFirstPrint = (graph, source) => {
  // array.push() adds to the last position of the array
  // array.shift() removes first element
  // array.unshift() adds to the first position of the array
  // array.pop() removes last element
  // We will use the array and the push/shift to implement the queue
  // by adding to the last position (push) and removing from the first position (shift)
  const queue = [source];
  while (queue.length > 0) {
    const current = queue.shift();
    console.log(current);
    graph[current].forEach((neighbor) => {
      queue.push(neighbor);
    });
  }
};

const graph = {
  a: ["c", "b"],
  b: ["d"],
  c: ["e"],
  d: ["f"],
  e: [],
  f: [],
};

// depthFirstPrint(graph, "a");

breadthFirstPrint(graph, "a"); // a, c, b, e, d, f
