const hasPath = (graph, src, dst) => {
  if (src === dst) return true;
  graph[src].array.forEach((neighbor) => {
    if (hasPath(graph, neighbor, dst) === true) {
      return true;
    }
  });
  return false;
};

// const hasPath = (graph, src, dst) => {
//   const queue = [src];
//   while (queue.length > 0) {
//     const current = queue.shift();
//     if (current === dst) return true;
//     graph[current].array.forEach((neighbor) => {
//       queue.push(neighbor);
//     });
//   }
//   return false;
// };
