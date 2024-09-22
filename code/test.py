from neo4j import GraphDatabase

# Define the Neo4j connection class
class Neo4jConnection:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def execute_query(self, query, parameters=None):
        session = self._driver.session()
        try:
            result = session.run(query, parameters)
            return [record for record in result]
        except Exception as e:
            print(f"Query failed: {e}")
        finally:
            session.close()

# Example usage of the Neo4jConnection class
if __name__ == "__main__":
    # Create a connection to the Neo4j database
    uri = "bolt://localhost:7687"  # Neo4j URI (adjust based on your setup)
    user = "neo4j"                  # Username
    password = "shimul123"           # Password
    
    # Initialize the connection
    conn = Neo4jConnection(uri, user, password)
    
    # Define a simple query (Create nodes or run Cypher queries)
    create_query = """
    CREATE (p:Person {name: $name, age: $age})
    RETURN p
    """
    
    # Define parameters for the query
    parameters = {"name": "Alice", "age": 30}

    # sample query
    sample_query = """
    MATCH (r:Release) WHERE r.id='org.jgrapht:jgrapht-core:1.5.2' RETURN r
    """
    
    # Execute the query
    # result = conn.execute_query(create_query, parameters)
    result = conn.execute_query(sample_query)
    
    # Print the result
    for record in result:
        print(record)

    # Close the connection
    conn.close()
