#include <iostream>
using namespace std;

struct Edge { int to; float weight; };              // Edge struct for destination and weight
struct Vertex { int id; Edge* edges; int edgeCount; Vertex() : edges(NULL), edgeCount(0) {} }; // Vertex with dynamic edges

class GraphBase {
public:
    Vertex* vertices = NULL; int vertexCount = 0;  //this line is for Dynamic array of vertices

    virtual ~GraphBase() {                         // Destructor frees dynamic memory
        for (int i = 0; i < vertexCount; i++) delete[] vertices[i].edges;
        delete[] vertices;
    }

    void addVertex(int id) {                       // Add vertex by resizing array and deleting the old array which is smaller than the new one.
        Vertex* temp = new Vertex[vertexCount + 1];
        for (int i = 0; i < vertexCount; i++) temp[i] = vertices[i];
        temp[vertexCount].id = id; temp[vertexCount].edges = NULL; temp[vertexCount].edgeCount = 0;
        delete[] vertices; vertices = temp; vertexCount++;
    }

    void removeVertex(int id) {                     // Remove vertex by using its id
        int idx = -1;
        for (int i = 0; i < vertexCount; i++) if (vertices[i].id == id) { idx = i; break; }
        if (idx == -1) return;                      // if Vertex not found, do nothing
        delete[] vertices[idx].edges;               // Delete edges of removed vertex

        Vertex* temp = new Vertex[vertexCount - 1]; // New array which is the smallest one
        for (int i = 0, j = 0; i < vertexCount; i++)
            if (i != idx) temp[j++] = vertices[i]; // Copy all except removed vertex

        delete[] vertices; vertices = temp; vertexCount--;
    }

    virtual void addEdge(int from, int to, float w) = 0; // Pure virtual for addEdge

    void display() {                                //this will be used to Display vertices and their edges
        for (int i = 0; i < vertexCount; i++) {
            cout << "Vertex " << vertices[i].id << ": ";
            for (int j = 0; j < vertices[i].edgeCount; j++) {
                Edge* e = vertices[i].edges + j;
                cout << "(" << e->to << "," << e->weight << ") ";
            }
            cout << "\n";
        }
    }
};
//derived class directedgraph from base class directedgraph
class DirectedGraph : public GraphBase {
public:
    void addEdge(int from, int to, float w) override { // Add directed edge
        int idx = -1;
        for (int i = 0; i < vertexCount; i++) if (vertices[i].id == from) { idx = i; break; }
        if (idx == -1) return;                        //if the Vertex not found,
        Edge* temp = new Edge[vertices[idx].edgeCount + 1];
        for (int i = 0; i < vertices[idx].edgeCount; i++) temp[i] = vertices[idx].edges[i];
        temp[vertices[idx].edgeCount] = {to, w};     // Add new edge
        delete[] vertices[idx].edges;
        vertices[idx].edges = temp;
        vertices[idx].edgeCount++;
    }
};
//derived class weightedgraph from base class graphbase
class WeightedGraph : public GraphBase {
public:
    void addEdge(int from, int to, float w) override { // Add undirected weighted edge
        addSingleEdge(from, to, w);
        addSingleEdge(to, from, w);
    }
private:
    void addSingleEdge(int from, int to, float w) {
        int idx = -1;
        for (int i = 0; i < vertexCount; i++) if (vertices[i].id == from) { idx = i; break; }
        if (idx == -1) return;
        Edge* temp = new Edge[vertices[idx].edgeCount + 1];
        for (int i = 0; i < vertices[idx].edgeCount; i++) temp[i] = vertices[idx].edges[i];
        temp[vertices[idx].edgeCount] = {to, w};
        delete[] vertices[idx].edges;
        vertices[idx].edges = temp;
        vertices[idx].edgeCount++;
    }
};
//the main function of the program 
int main() {
    int V, E;
    cout << "Vertices? "; cin >> V;
    cout << "Edges? "; cin >> E;

    GraphBase* graphs[2] = { new DirectedGraph(), new WeightedGraph() };

    for (int i = 1; i <= V; i++) {                  //this allows to Add vertices with their ID
        graphs[0]->addVertex(i);
        graphs[1]->addVertex(i);
    }

    for (int i = 0; i < E; i++) {                    //this allows to Add edges from user input
        int f, t; float w;
        cout << "Edge (from to weight): ";
        cin >> f >> t >> w;
        graphs[0]->addEdge(f, t, w);
        graphs[1]->addEdge(f, t, w);
    }

    cout << "\nDirected Graph:\n"; graphs[0]->display();
    cout << "\nWeighted Graph:\n"; graphs[1]->display();

    int removeId;
    cout << "\nEnter a vertex ID to remove (or 0 to skip): ";
    cin >> removeId;

    if (removeId != 0) {                             // this is to exit the program when the user input is 0
        graphs[0]->removeVertex(removeId);
        graphs[1]->removeVertex(removeId);

        cout << "\nDirected Graph after removal:\n"; graphs[0]->display();
        cout << "\nWeighted Graph after removal:\n"; graphs[1]->display();
    }

    delete graphs[0]; delete graphs[1];              // Free memory
    return 0;
}
