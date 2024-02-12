## Challenge: Building a Distributed Task Queue

### Description:
You need to develop a distributed task queue system using Python, Django, and any appropriate libraries/frameworks for distributed computing (e.g., Celery, RabbitMQ). The system should allow users to submit tasks, which will be executed asynchronously across multiple worker nodes.

### Requirements:
1. **Web Interface:**
   - Users should be able to submit tasks via a web interface built with Django.
   - The interface should allow users to specify task parameters and any relevant options.
   - Users should be able to view the status and results of their submitted tasks.

2. **Task Queue:**
   - Implement a distributed task queue using Celery and RabbitMQ (or any other suitable technology).
   - Tasks should be stored in a queue and executed asynchronously by worker nodes.
   - Worker nodes should be able to handle multiple tasks concurrently.

3. **Fault Tolerance:**
   - Implement fault tolerance mechanisms to handle worker node failures gracefully.
   - Ensure that tasks are not lost and are retried if a worker node fails during execution.

4. **Monitoring and Logging:**
   - Implement monitoring and logging functionality to track the progress of tasks and diagnose any issues.
   - Users should be able to view logs and monitor the status of their tasks.

5. **Scalability:**
   - Design the system to be scalable, allowing for easy addition/removal of worker nodes to handle varying workloads.

6. **Documentation and Testing:**
   - Provide clear documentation on how to set up and run the system.
   - Write comprehensive unit and integration tests to ensure the reliability and correctness of the system.

### Bonus:
- Implement task prioritization to handle high-priority tasks efficiently.
- Support for scheduling recurring tasks.
- Implement security measures to prevent unauthorized access to the system.
