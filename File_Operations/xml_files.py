"""
XML stands for eXtensible Markup Language

XML was designed to store and transport data

XML was designed to be both Human and Machine Readable

XML is extremely useful for keeping track of small to medium amounts of data
without requiring a SQL-Based Backbone



<?xml version="1.0" encoding="UTF-8"?>  # 1. Declaration

<contact-information>  # 2. Root Element or Parent Element or Start Tag
    <name>Keshav Kummari</name> # 3. Child Element
    <designation> DevOps Engineer
        <department>Python Development</department> # 4. Sub-Child Element
    </designation>
    <phone> +91 0099099090 </phone>
    <address> Hyderabad </address>

</contact-information> # Root Element is ending or Parent Element or Start Tag is ending
"""

SAX = Simple API for XML
    - Read Only
    - Low Memory
    - Event-Based

DOM = Document Object Model

    - Reading and Writing (Manipulation to xml files)
    - Based on the file size
    - Tree-Based
    - CRUD - Create, Read, Update & Delete


