# Kafka Email Demo

This project demonstrates an event-driven architecture where a **Producer** generates email update events and a **Consumer** processes them in real-time using Apache Kafka.

## Prerequisites

1. **Python 3.8+** installed.
2. **Apache Kafka** installed and running locally.

## 1. Start Kafka (Windows)

Before running the Python scripts, ensure your Kafka broker is running.

If you are using KRaft mode (no ZooKeeper), run the following from your Kafka installation directory (e.g., `A:\XAMPP\kafka_2.13-4.1.1`):

```powershell
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

> **Note**: Ensure your `server.properties` is configured correctly for KRaft and listening on `localhost:9092`.

## 2. Project Setup

Open a terminal in the project root (`c:\kafka-email-demo`).

### Create and Activate Virtual Environment

It is recommended to use a virtual environment to manage dependencies locally.

**Windows (PowerShell Only):**

> **Important:** The following activation script must be run in a **PowerShell** terminal.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

*(If you are using Command Prompt (cmd), use `.venv\Scripts\activate.bat` instead)*

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Running the Application

You will need two separate terminal windows (both with the virtual environment activated).

### Terminal 1: Start the Consumer
The consumer listens for messages on the topic `user-email-updates`. Start it first so it's ready to receive data.

```bash
python -m src.consumer
```

### Terminal 2: Start the Producer
The producer simulates user actions and sends events to Kafka.

```bash
python -m src.producer
```

## 4. What to Expect

1. The **Producer** will start printing:
   ```text
   Produced event to user-email-updates key=101
   Produced event to user-email-updates key=104
   ...
   ```

2. The **Consumer** will immediately react and print:
   ```text
   --- Consumer listening on 'user-email-updates' ---
   -> ACTION: Updating system records for User 101 to user101.45@example.com
   -> ACTION: Updating system records for User 104 to user104.99@example.com
   ```

## Project Structure

- `src/config.py`: Configuration for Kafka connections (brokers, topic names).
- `src/producer.py`: Generates fake user email change events.
- `src/consumer.py`: Listens for email update events and processes them.