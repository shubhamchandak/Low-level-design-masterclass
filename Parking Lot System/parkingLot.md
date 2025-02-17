# Low-Level Design: Parking Lot System in Python

In this tutorial, we dive deep into the low-level design of a Parking Lot System using Python. We cover every aspect—from gathering requirements and evaluating design approaches to detailed class design with UML (using Mermaid diagrams) and complete, production-ready code.

The goal is to help you learn the valuable concepts, thought process, and architectural decision-making required to design and structure code for real-world systems.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Requirements Gathering](#requirements-gathering)
3. [Architectural Decision-Making](#architectural-decision-making)
    - [Top-Down vs. Bottom-Up vs. Hybrid Approach](#top-down-vs-bottom-up-vs-hybrid-approach)
4. [Design Principles and Best Practices](#design-principles-and-best-practices)
    - [SOLID Principles](#solid-principles)
    - [Strategy Pattern](#strategy-pattern)
    - [Usage of Enums](#usage-of-enums)
    - [Concurrency Handling](#concurrency-handling)
5. [Class Identification and Responsibilities](#class-identification-and-responsibilities)
6. [UML & Mermaid Diagrams](#uml--mermaid-diagrams)
7. [Python Code Implementation](#python-code-implementation)
8. [Conclusion and Key Takeaways](#conclusion-and-key-takeaways)

---

## 1. Introduction

Designing a scalable and maintainable parking lot system might sound trivial, but it involves many design decisions. This tutorial will help you:

- Understand how to translate business requirements into a robust design.
- Evaluate different design approaches.
- Choose the right design patterns and architectural components.
- Write clean, thread-safe, and extendable code.

---

## 2. Requirements Gathering

### Functional Requirements
- **Vehicle Management:**  
  - Allow vehicles to enter (park) and exit (unpark).
  - Support multiple vehicle types (e.g., Car, Bike, Truck).
- **Slot Allocation:**  
  - Allocate appropriate parking slots based on vehicle type.
- **Fee Calculation:**  
  - Calculate parking fees based on duration and vehicle type.
- **Ticketing System:**  
  - Generate tickets for parked vehicles to track time and fees.

### Non-Functional Requirements
- **Scalability:**  
  - The design should support future extensions (more floors, more vehicle types).
- **Maintainability:**  
  - Follow modular design and SOLID principles.
- **Concurrency:**  
  - Handle multiple vehicles entering/exiting concurrently with thread-safe mechanisms.
- **Extensibility:**  
  - Easily integrate new pricing strategies or additional vehicle types without major code changes.

---

## 3. Architectural Decision-Making

### Top-Down vs. Bottom-Up vs. Hybrid Approach

#### **Top-Down Approach**
- **Process:** Start by outlining the overall system (e.g., ParkingLot, Floors) and then break it down into components.
- **Pros:** Provides a clear high-level picture; ensures that the overall architecture aligns with requirements.
- **Cons:** May postpone the discovery of low-level issues until later stages.

#### **Bottom-Up Approach**
- **Process:** Begin with designing individual components (e.g., ParkingSlot, Vehicle) and integrate them to form the complete system.
- **Pros:** Early focus on detailed implementation and potential pitfalls.
- **Cons:** Risk of losing sight of the system’s overall structure.

#### **Hybrid Approach (Recommended)**
- **Process:**  
  1. **Top-Down:** Define the main components (ParkingLot, ParkingFloor, etc.) to cover all requirements.
  2. **Bottom-Up:** Develop each component with detailed design and testing, ensuring they are generic and adhere to SOLID principles.
- **Why Hybrid?**  
  - Balances overall system vision with component-level robustness.
  - Helps identify and mitigate potential issues early in the development process.

---

## 4. Design Principles and Best Practices

### SOLID Principles
- **Single Responsibility Principle (SRP):**  
  Each class should have one responsibility (e.g., `ParkingSlot` manages only slot state).
- **Open/Closed Principle (OCP):**  
  Classes should be open for extension but closed for modification. (e.g., Fee calculation strategies can be extended without altering the core logic.)
- **Liskov Substitution Principle (LSP):**  
  Subclasses (e.g., `Car`, `Bike`) should be substitutable for their base class `Vehicle`.
- **Interface Segregation Principle (ISP):**  
  Favor small, specific interfaces rather than a large, general-purpose one.
- **Dependency Inversion Principle (DIP):**  
  Depend on abstractions rather than concrete implementations.

### Strategy Pattern
- **Usage:**  
  - Implement fee calculation using the Strategy Pattern.
  - This allows you to plug in different pricing algorithms without changing the core ParkingLot logic.

### Usage of Enums
- **Purpose:**  
  - Provide a controlled vocabulary for vehicle types (e.g., `VehicleType`) and slot statuses (e.g., `ParkingSlotStatus`).
  - Enhance code readability and reduce errors from using magic strings.

### Concurrency Handling
- **Challenge:**  
  - Multiple threads might try to park or unpark vehicles simultaneously.
- **Solution:**  
  - Use Python’s `threading.Lock` for fine-grained (per-slot) and coarse-grained (system-wide) locking to ensure thread safety.

---

## 5. Class Identification and Responsibilities

Below are the primary classes with their responsibilities:

- **`ParkingLot`:**  
  - Manages multiple floors.
  - Oversees global parking and unparking operations.
  - Ensures thread-safe operations using a global lock.

- **`ParkingFloor`:**  
  - Represents a single floor containing multiple parking slots.
  - Responsible for providing free slots for parking.

- **`ParkingSlot`:**  
  - Represents an individual parking space.
  - Manages its own state (free/occupied) and handles concurrent assignments using a local lock.

- **`Vehicle` (and subclasses `Car`, `Bike`, etc.):**  
  - Represents a vehicle.
  - Subclasses specify the type and possibly other vehicle-specific attributes.

- **`FeeCalculationStrategy`:**  
  - Abstract class/interface for fee calculation.
  - Concrete implementations (like `DefaultFeeCalculationStrategy`) compute fees based on duration and custom rules.

---

## 6. UML & Mermaid Diagrams

### Component Diagram
Below is a diagram showing the overall architecture:
