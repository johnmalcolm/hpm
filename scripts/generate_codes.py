import json
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
PROCESSED_DATA_PATH = os.path.join(PROJECT_ROOT, "data", "processed")

environmental_practices_iniatives = [
    {
        "original_code": "ENVRTX01",
        "descriptive_name": "Energy Efficiency/Renewable Energy",
        "original_description": "Energy efficiency or renewable energy",
    },
    {
        "original_code": "ENVRTX02",
        "descriptive_name": "Water Efficiency",
        "original_description": "Water efficiency",
    },
    {
        "original_code": "ENVRTX03",
        "descriptive_name": "Reducing Waste in Internal Processes",
        "original_description": "Reducing waste in internal processes (e.g., improving yield or efficiency)",
    },
    {
        "original_code": "ENVRTX04",
        "descriptive_name": "Improving Workforce Environment",
        "original_description": "Improving the workforce environment (e.g., indoor air quality)",
    },
    {
        "original_code": "ENVRTX05",
        "descriptive_name": "Pollution Prevention",
        "original_description": "Pollution prevention (eliminating emissions or waste)",
    },
    {
        "original_code": "ENVRTX06",
        "descriptive_name": "Pollution Control",
        "original_description": "Pollution control (scrubbing, waste treatment)",
    },
    {
        "original_code": "ENVRTX07",
        "descriptive_name": "Remediation Projects",
        "original_description": "Remediation projects, such as cleanup or restoration from past practices",
    },
    {
        "original_code": "ENVRTX08",
        "descriptive_name": "Decreasing Environmental Accident Impact",
        "original_description": "Decreasing the likelihood or impact of an environmental accident",
    },
    {
        "original_code": "ENVRTX09",
        "descriptive_name": "Land Consumption Reduction/Avoidance",
        "original_description": "Reduction/avoidance of land consumption",
    },
    {
        "original_code": "ENVRTX10",
        "descriptive_name": "Inbound Transportation Improvements",
        "original_description": "Improvements in inbound transportation, such as fuel efficiency or load matching",
    },
    {
        "original_code": "ENVRTX11",
        "descriptive_name": "Outbound Transportation Improvements",
        "original_description": "Improvements in outbound transportation, such as fuel efficiency or load matching",
    },
    {
        "original_code": "ENVRTX12",
        "descriptive_name": "ISO14001 Certification",
        "original_description": "Seeking or maintaining ISO14001 certification",
    },
    {
        "original_code": "ENVRTX13",
        "descriptive_name": "Customer Supplier Code Compliance",
        "original_description": "Complying with a customer’s supplier code of conduct",
    },
    {
        "original_code": "ENVRTX14",
        "descriptive_name": "Industry-wide Code Compliance",
        "original_description": "Complying with an industry-wide code of conduct",
    },
    {
        "original_code": "ENVRTX15",
        "descriptive_name": "Plant Compliance/Auditing Program",
        "original_description": "Other compliance or auditing program focused on your plant (not on your suppliers)",
    },
    {
        "original_code": "ENVRTX16",
        "descriptive_name": "Internal Operations Carbon Tracking",
        "original_description": "Carbon tracking/carbon footprint calculation of internal operations",
    },
    {
        "original_code": "ENVRTX17",
        "descriptive_name": "Supply Chain Carbon Tracking",
        "original_description": "Carbon tracking/carbon footprint calculation of supply chain",
    },
    {
        "original_code": "ENVRTX18",
        "descriptive_name": "Customer Environmental Objectives Assistance",
        "original_description": "Working with customers to help them achieve environmental objectives",
    },
    {
        "original_code": "ENVRTX19",
        "descriptive_name": "Product Design for Environmental Consideration",
        "original_description": "Design of your organization’s products for disassembly, recycling, reuse or durability",
    },
    {
        "original_code": "ENVRTX20",
        "descriptive_name": "Life-cycle Analysis",
        "original_description": "Life-cycle analysis of the “cradle to grave” environmental impact of materials/products",
    },
    {
        "original_code": "ENVRTX21",
        "descriptive_name": "Environmentally Preferable Packaging",
        "original_description": "Environmentally preferable packaging for the products that you produce (recycled content, less volume, reusable packaging)",
    },
    {
        "original_code": "ENVRTX22",
        "descriptive_name": "Substituting Environmentally Preferable Direct Materials",
        "original_description": "Substituting environmental preferable direct materials or supplies for harmful or non-renewable ones",
    },
    {
        "original_code": "ENVRTX23",
        "descriptive_name": "Environmental Improvements for Scrap/Excess Material Disposition",
        "original_description": "Environmental improvements in the disposition of your organization’s scrap or excess material (re-use, recycling, etc.)",
    },
    {
        "original_code": "ENVRTX24",
        "descriptive_name": "Environmental Improvements for Equipment Disposition",
        "original_description": "Environmental improvements in the disposition of your organization’s equipment",
    },
    {
        "original_code": "ENVRTX25",
        "descriptive_name": "Prolonging Equipment Useful Life",
        "original_description": "Prolonging the useful life of equipment",
    },
    {
        "original_code": "ENVRTX26",
        "descriptive_name": "Employee Commuting Issues",
        "original_description": "Employee commuting issues (e.g., carpooling, bike garage)",
    },
    {
        "original_code": "ENVRTX27",
        "descriptive_name": "Substituting Environmentally Preferable Indirect Materials",
        "original_description": "Substituting environmentally preferable indirect materials for harmful or non-renewable ones",
    },
    {
        "original_code": "ENVRTX28",
        "descriptive_name": "Environmentally Preferable Inbound Packaging",
        "original_description": "Environmentally preferable inbound packaging, such as (recycled content, less volume or reusable packaging)",
    },
    {
        "original_code": "ENVRTX29",
        "descriptive_name": "Encouraging Supplier Environmental Improvement",
        "original_description": "Encouraging suppliers to improve the environmental performance of their processes",
    },
    {
        "original_code": "ENVRTX30",
        "descriptive_name": "Preference to Third Party Certified Materials",
        "original_description": "Giving preference to materials with third party certifications, such as Green Seal, FSC or Energy Star",
    },
    {
        "original_code": "ENVRTX31",
        "descriptive_name": "Requesting Supplier Environmental Conduct Code",
        "original_description": "Requesting that your suppliers sign a code of environmental conduct",
    },
    {
        "original_code": "ENVRTX32",
        "descriptive_name": "Purchasing from M/WBE Suppliers",
        "original_description": "Purchasing from minority- or women-owned business enterprise (M/WBE) suppliers",
    },
    {
        "original_code": "ENVRTX33",
        "descriptive_name": "Formal M/WBE Supplier Purchase Program",
        "original_description": "Starting or maintaining a formal M/WBE supplier purchase program",
    },
    {
        "original_code": "ENVRTX34",
        "descriptive_name": "Ensuring No Sweatshop Labor in Supplier Plants",
        "original_description": "Visiting suppliers’ plants or ensuring that they are not using sweatshop labor",
    },
    {
        "original_code": "ENVRTX35",
        "descriptive_name": "Ensuring Supplier Child Labor Law Compliance",
        "original_description": "Ensuring that suppliers comply with child labor laws",
    },
    {
        "original_code": "ENVRTX36",
        "descriptive_name": "Asking Suppliers for Living Wage",
        "original_description": "Asking suppliers to pay a “living wage”",
    },
    {
        "original_code": "ENVRTX37",
        "descriptive_name": "Third Party Monitoring of Supplier Working Conditions",
        "original_description": "Using a third party to monitor working conditions at supplier facilities",
    },
    {
        "original_code": "ENVRTX38",
        "descriptive_name": "Environmental Considerations in Supplier Evaluation/Selection",
        "original_description": "Incorporating environmental considerations in evaluating and selecting suppliers",
    },
    {
        "original_code": "ENVRTX39",
        "descriptive_name": "Environmental Design Specifications to Suppliers",
        "original_description": "Providing design specification to suppliers in line with environmental requirements (e.g. green purchasing, black list of raw materials)",
    },
    {
        "original_code": "ENVRTX40",
        "descriptive_name": "Co-development with Suppliers for Environmental Impact",
        "original_description": "Co-development with suppliers to reduce the environmental impact of the product (e.g. eco-design, green packaging, recyclability)",
    },
    {
        "original_code": "ENVRTX41",
        "descriptive_name": "Supplier Involvement in Internal Process Redesign",
        "original_description": "Involvement of suppliers in the re-design of internal processes (e.g. remanufacturing, reduction of by-products)",
    },
    {
        "original_code": "ENVRTX42",
        "descriptive_name": "Cooperative Investments with Suppliers for Sustainable Logistics",
        "original_description": "Cooperative investments with suppliers in order to create a more environmentally sustainable logistics systems (e.g.closed-loop supply chain, reverse logistics)",
    },
]

environmental_practices = [
    {
        "original_code": "EPRACX01",
        "descriptive_name": "Certified Environmental Management System",
        "original_description": "Implementation of a certified environmental management system, such as ISO 14000.",
    },
    {
        "original_code": "EPRACX02",
        "descriptive_name": "Internal Environmental Management Procedures",
        "original_description": "Implementation of internal environmental management procedures (e.g. environmental training program, internal environmental audit, newsletter).",
    },
    {
        "original_code": "EPRACX03",
        "descriptive_name": "Cleaner Production Technologies",
        "original_description": "Use of cleaner technologies in the production process (e.g. abatement equipment) to reduce pollution emissions and/or resource use.",
    },
    {
        "original_code": "EPRACX04",
        "descriptive_name": "Environment-Friendly Product Design",
        "original_description": "Environment-friendly product design.",
    },
    {
        "original_code": "EPRACX05",
        "descriptive_name": "Environmental Improvement of Packaging",
        "original_description": "Environmental improvement of packaging.",
    },
    {
        "original_code": "EPRACX06",
        "descriptive_name": "Environment-Friendly Raw Materials",
        "original_description": "Use of environment-friendly raw materials.",
    },
]

environmental_performance = [
    {
        "original_code": "EPERFX01",
        "descriptive_name": "Overall Environmental Performance",
        "original_description": "Overall environmental performance.",
    },
    {
        "original_code": "EPERFX02",
        "descriptive_name": "Raw Materials Consumption",
        "original_description": "Raw materials consumption.",
    },
    {
        "original_code": "EPERFX03",
        "descriptive_name": "Energy Consumption",
        "original_description": "Energy consumption.",
    },
    {
        "original_code": "EPERFX04",
        "descriptive_name": "Water Consumption",
        "original_description": "Water consumption.",
    },
    {
        "original_code": "EPERFX05",
        "descriptive_name": "Emissions to Air",
        "original_description": "Emissions to air.",
    },
    {
        "original_code": "EPERFX06",
        "descriptive_name": "Releases to Water",
        "original_description": "Releases to water.",
    },
    {
        "original_code": "EPERFX07",
        "descriptive_name": "Solid Waste Generation",
        "original_description": "Solid waste generation (e.g. landfill capacity consumed).",
    },
    {
        "original_code": "EPERFX08",
        "descriptive_name": "Waste Recovery",
        "original_description": "Waste recovery (e.g. recycling).",
    },
    {
        "original_code": "EPERFX09",
        "descriptive_name": "Fines or Violations",
        "original_description": "Fines or other violations of environmental rules/regulations.",
    },
]

sustainability_outcomes = [
    {
        "original_code": "OUTCMX01",
        "descriptive_name": "Environmental performance",
        "original_description": "Environmental performance",
    },
    {
        "original_code": "OUTCMX02",
        "descriptive_name": "Regulatory performance",
        "original_description": "Regulatory performance",
    },
    {
        "original_code": "OUTCMX03",
        "descriptive_name": "Risk of an adverse environmental event (for example, a spill)",
        "original_description": "Risk of an adverse environmental event (for example, a spill)",
    },
    {
        "original_code": "OUTCMX04",
        "descriptive_name": "Cost performance",
        "original_description": "Cost performance",
    },
    {
        "original_code": "OUTCMX05",
        "descriptive_name": "Revenue performance",
        "original_description": "Revenue performance",
    },
    {
        "original_code": "OUTCMX06",
        "descriptive_name": "Product quality",
        "original_description": "Product quality",
    },
    {
        "original_code": "OUTCMX07",
        "descriptive_name": "Product performance",
        "original_description": "Product performance",
    },
    {
        "original_code": "OUTCMX08",
        "descriptive_name": "Supply chain integration and supplier relationships",
        "original_description": "Supply chain integration and supplier relationships",
    },
    {
        "original_code": "OUTCMX09",
        "descriptive_name": "Manufacturing performance",
        "original_description": "Manufacturing performance",
    },
    {
        "original_code": "OUTCMX10",
        "descriptive_name": "Stakeholder (community, investors) relationships",
        "original_description": "Stakeholder (community, investors) relationships",
    },
    {
        "original_code": "OUTCMX11",
        "descriptive_name": "Financial Performance",
        "original_description": "Financial Performance",
    },
    {
        "original_code": "UTCMX12",
        "descriptive_name": "Toxic air emissions (CO2, VOC, COD, NOX, SO2)",
        "original_description": "Toxic air emissions (CO2, VOC, COD, NOX, SO2)",
    },
    {
        "original_code": "OUTCMX13",
        "descriptive_name": "Soil contamination",
        "original_description": "Soil contamination",
    },
    {
        "original_code": "OUTCMX14",
        "descriptive_name": "Water contamination",
        "original_description": "Water contamination",
    },
    {
        "original_code": "OUTCMX15",
        "descriptive_name": "Use of natural resources (energy, water,etc.)",
        "original_description": "Use of natural resources (energy, water,etc.)",
    },
    {
        "original_code": "OUTCMX16",
        "descriptive_name": "Consumption for hazardous/toxic materials",
        "original_description": "Consumption for hazardous/toxic materials",
    },
    {
        "original_code": "OUTCMX17",
        "original_description": "Corporate reputation/image",
        "descriptive_name": "Corporate reputation/image",
    },
]

jit_practices = [
    {
        "original_code": "LAYOUTN01",
        "descriptive_name": "Equipment Layout - Proximity",
        "original_description": "We have laid out the shop floor so that processes and machines are in close proximity to each other.",
    },
    {
        "original_code": "LAYOUTN02",
        "descriptive_name": "Equipment Layout - Low Inventories",
        "original_description": "The layout of our shop floor facilitates low inventories and fast throughput.",
    },
    {
        "original_code": "LAYOUTN03",
        "descriptive_name": "Equipment Layout - Minimized Handling",
        "original_description": "Our processes are located close together, so that material handling and part storage are minimized.",
    },
    {
        "original_code": "LAYOUTN04",
        "descriptive_name": "Equipment Layout - JIT Production",
        "original_description": "We have located our machines to support JIT production flow.",
    },
    {
        "original_code": "JITDELN01",
        "descriptive_name": "JIT Delivery by Suppliers - Timely Delivery",
        "original_description": "Our suppliers deliver to us on a just-in-time basis.",
    },
    {
        "original_code": "JITDELN02",
        "descriptive_name": "JIT Delivery by Suppliers - Daily Shipments",
        "original_description": "We receive daily shipments from most suppliers.",
    },
    {
        "original_code": "JITDELN03",
        "descriptive_name": "JIT Delivery by Suppliers - Pull System",
        "original_description": "Our suppliers are linked with us by a pull system.",
    },
    {
        "original_code": "KANBANN01",
        "descriptive_name": "Kanban - Supplier Containers",
        "original_description": "Suppliers fill our kanban containers, rather than filling purchase orders.",
    },
    {
        "original_code": "KANBANN02",
        "descriptive_name": "Kanban - Production Control Pull System",
        "original_description": "We use a kanban pull system for production control.",
    },
    {
        "original_code": "KANBANN03",
        "descriptive_name": "Kanban - Production Control Signals",
        "original_description": "We use kanban squares, containers or signals for production control.",
    },
    {
        "original_code": "LINKCN01",
        "descriptive_name": "Our customers receive just-in-time deliveries from us.",
        "original_description": "Our customers receive just-in-time deliveries from us."
    },
    {
        "original_code": "LINKCN02",
        "descriptive_name": "We always deliver on time to our customers.",
        "original_description": "We always deliver on time to our customers."
    },
    {
        "original_code": "LINKCN03",
        "descriptive_name": "We can adapt our production schedule to sudden production stoppages by our",
        "original_description": "We can adapt our production schedule to sudden production stoppages by our customers."
    },
    {
        "original_code": "LINKCN04",
        "descriptive_name": "Our customers have a pull type link with us.",
        "original_description": "Our customers have a pull type link with us."
    },
    {
        "original_code": "LINKCN05",
        "descriptive_name": "Our customers are linked with us via JIT systems.",
        "original_description": "Our customers are linked with us via JIT systems."
    },
    {
        "original_code": "SCHEDN01",
        "descriptive_name": "We usually meet the production schedule each day.",
        "original_description": "We usually meet the production schedule each day."
    },
    {
        "original_code": "SCHEDN02",
        "descriptive_name": "We usually complete our daily schedule as planned.",
        "original_description": "We usually complete our daily schedule as planned."
    },
    {
        "original_code": "SCHEDR03",
        "descriptive_name": "We build extra slack into our daily schedule, to allow for catching up.",
        "original_description": "We build extra slack into our daily schedule, to allow for catching up."
    },
    {
        "original_code": "SETUPN01",
        "descriptive_name": "We are aggressively working to lower setup times in our plant.",
        "original_description": "We are aggressively working to lower setup times in our plant."
    },
    {
        "original_code": "SETUPN02",
        "descriptive_name": "We have low setup times of equipment in our plant.",
        "original_description": "We have low setup times of equipment in our plant."
    },
    {
        "original_code": "SETUPN03",
        "descriptive_name": "Our workers practice setups, in order to reduce the time required.",
        "original_description": "Our workers practice setups, in order to reduce the time required."
    }
]

employees = {
    "original_code": "ACCTGX51",
    "descriptive_name": "Employees",
    "original_description": "Number of personnel employed",
}

# merge all the codes
all_codes = (
    environmental_practices_iniatives
    + environmental_practices
    + environmental_performance
    + jit_practices
    + [employees]
    + sustainability_outcomes
)

with open(os.path.join(PROCESSED_DATA_PATH, "codes.json"), "w") as f:
    json.dump(all_codes, f, indent=4)
