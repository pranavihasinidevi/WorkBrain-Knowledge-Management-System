"""WorkBrain — Demo Data
Design: #0B0F1A bg · #6366F1 accent · Syne + Inter fonts · one emoji per module
"""

DEPT_COLORS = {
    "Engineering":  "#3B82F6",
    "Operations":   "#10B981",
    "HR":           "#8B5CF6",
    "Finance":      "#F59E0B",
    "IT Support":   "#06B6D4",
    "Maintenance":  "#EF4444",
}
DEPARTMENTS = list(DEPT_COLORS.keys())

EMPLOYEES = [
    {"id":1,  "name":"Arjun Mehta",   "initials":"AM","role":"Senior Engineer",    "dept":"Engineering","entries":42,"score":88,"status":"Active","risk":"Critical","email":"arjun@workbrain.io"},
    {"id":2,  "name":"Priya Sharma",  "initials":"PS","role":"HR Manager",         "dept":"HR",         "entries":31,"score":76,"status":"Active","risk":"High",    "email":"priya@workbrain.io"},
    {"id":3,  "name":"Vikram Nair",   "initials":"VN","role":"IT Admin",           "dept":"IT Support", "entries":57,"score":91,"status":"Active","risk":"Critical","email":"vikram@workbrain.io"},
    {"id":4,  "name":"Sneha Patel",   "initials":"SP","role":"Finance Analyst",    "dept":"Finance",    "entries":24,"score":72,"status":"Active","risk":"High",    "email":"sneha@workbrain.io"},
    {"id":5,  "name":"Rohan Gupta",   "initials":"RG","role":"Operations Manager", "dept":"Operations", "entries":18,"score":65,"status":"Active","risk":"Medium",  "email":"rohan@workbrain.io"},
    {"id":6,  "name":"Ananya Reddy",  "initials":"AR","role":"Software Engineer",  "dept":"Engineering","entries":35,"score":83,"status":"Active","risk":"High",    "email":"ananya@workbrain.io"},
    {"id":7,  "name":"Kiran Das",     "initials":"KD","role":"Team Lead",          "dept":"Engineering","entries":29,"score":79,"status":"Inactive","risk":"High", "email":"kiran@workbrain.io"},
    {"id":8,  "name":"Deepa Iyer",    "initials":"DI","role":"Finance Analyst",    "dept":"Finance",    "entries":12,"score":60,"status":"Active","risk":"Medium", "email":"deepa@workbrain.io"},
    {"id":9,  "name":"Arun Kumar",    "initials":"AK","role":"Maintenance Tech",   "dept":"Maintenance","entries":45,"score":85,"status":"Active","risk":"Critical","email":"arun@workbrain.io"},
    {"id":10, "name":"Meena Joshi",   "initials":"MJ","role":"HR Executive",       "dept":"HR",         "entries":8, "score":55,"status":"Active","risk":"Low",    "email":"meena@workbrain.io"},
    {"id":11, "name":"Rajesh Singh",  "initials":"RS","role":"Director",           "dept":"Operations", "entries":22,"score":70,"status":"Active","risk":"Medium", "email":"rajesh@workbrain.io"},
    {"id":12, "name":"Nisha Verma",   "initials":"NV","role":"IT Admin",           "dept":"IT Support", "entries":33,"score":80,"status":"Active","risk":"High",   "email":"nisha@workbrain.io"},
    {"id":13, "name":"Suresh Pillai", "initials":"SU","role":"Maintenance Tech",   "dept":"Maintenance","entries":19,"score":67,"status":"Active","risk":"Medium", "email":"suresh@workbrain.io"},
    {"id":14, "name":"Lakshmi Rao",   "initials":"LR","role":"Senior Analyst",     "dept":"Finance",    "entries":6, "score":50,"status":"Active","risk":"Low",    "email":"lakshmi@workbrain.io"},
    {"id":15, "name":"Manoj Tiwari",  "initials":"MT","role":"Software Engineer",  "dept":"Engineering","entries":14,"score":62,"status":"Active","risk":"Medium", "email":"manoj@workbrain.io"},
]

KNOWLEDGE = [
    {"id":1, "title":"Fix Payment Gateway 502 Timeout",    "dept":"Engineering","author":"Arjun Mehta",  "views":421,"rating":4.9,"verified":True, "priority":"Critical","tags":"payment,gateway,502",      "type":"Problem/Solution","date":"2024-03-18","helpful":94,"comments":22,
     "problem":"Payment pods not scaling above 1000 req/s during peak hours, returning 502 to users.",
     "solution":"Set minimum replicas to 5, add Redis circuit breaker caching intent responses 30s. Zero downtime post-deploy."},
    {"id":2, "title":"Kubernetes Pod OOMKilled Fix",        "dept":"Engineering","author":"Arjun Mehta",  "views":312,"rating":4.8,"verified":True, "priority":"High",    "tags":"kubernetes,memory,devops", "type":"Problem/Solution","date":"2024-03-12","helpful":89,"comments":14,
     "problem":"Analytics worker pods OOMKilled nightly due to pandas DataFrame memory leak.",
     "solution":"Added explicit del df + gc.collect(). Set memory limit 2Gi / request 1Gi. Crashes resolved."},
    {"id":3, "title":"Employee Onboarding Checklist SOP",   "dept":"HR",         "author":"Priya Sharma", "views":198,"rating":4.6,"verified":True, "priority":"Medium",  "tags":"onboarding,sop,hr",        "type":"SOP Reference",   "date":"2024-02-28","helpful":67,"comments":8,
     "problem":"New hires taking 2+ weeks to get full system access due to unclear steps.",
     "solution":"5-day checklist: Day 1 IT setup, Day 2 HR docs, Day 3 team intros, Day 4 access, Day 5 first task."},
    {"id":4, "title":"GST Reconciliation Automation",       "dept":"Finance",    "author":"Sneha Patel",  "views":143,"rating":4.5,"verified":True, "priority":"High",    "tags":"gst,automation,python",    "type":"Best Practice",   "date":"2024-01-15","helpful":51,"comments":6,
     "problem":"Monthly GST filing took 3 days of manual work with frequent mismatches.",
     "solution":"Python script auto-reconciles GSTR-1 and GSTR-2B. Down from 3 days to 2 hours."},
    {"id":5, "title":"CRM Lead Scoring Model",              "dept":"Operations", "author":"Rohan Gupta",  "views":267,"rating":4.7,"verified":False,"priority":"High",    "tags":"crm,leads,scoring",        "type":"Best Practice",   "date":"2024-03-01","helpful":73,"comments":11,
     "problem":"Sales team spending equal time on hot and cold leads, missing high-value opportunities.",
     "solution":"Score = company size 30% + engagement 40% + budget fit 30%. Leads >70 go to senior reps."},
    {"id":6, "title":"VPN Remote Access Setup SOP",         "dept":"IT Support", "author":"Vikram Nair",  "views":189,"rating":4.4,"verified":True, "priority":"Medium",  "tags":"vpn,remote,security",      "type":"SOP Reference",   "date":"2024-02-10","helpful":62,"comments":9,
     "problem":"Remote employees unable to securely access internal tools. Setup undocumented.",
     "solution":"Step-by-step for Win/Mac/Linux. Self-service portal delivers credentials within 2 hours."},
    {"id":7, "title":"HVAC Maintenance Protocol",           "dept":"Maintenance","author":"Arun Kumar",   "views":134,"rating":4.3,"verified":True, "priority":"Medium",  "tags":"hvac,maintenance,facility","type":"SOP Reference",   "date":"2024-02-22","helpful":38,"comments":5,
     "problem":"HVAC units failing unexpectedly, causing facility downtime.",
     "solution":"Monthly inspection: filter replacement, coolant checks, error code guide. Downtime down 40%."},
    {"id":8, "title":"SQL Query Optimization Guide",        "dept":"Engineering","author":"Ananya Reddy", "views":289,"rating":4.8,"verified":True, "priority":"Medium",  "tags":"sql,database,performance", "type":"Best Practice",   "date":"2024-03-05","helpful":81,"comments":16,
     "problem":"Reporting module queries taking 15+ seconds causing user frustration.",
     "solution":"Indexing strategies, query plan analysis, N+1 detection. Average query time reduced 60%."},
    {"id":9, "title":"Payroll Processing Workflow",         "dept":"HR",         "author":"Meena Joshi",  "views":112,"rating":4.2,"verified":True, "priority":"High",    "tags":"payroll,compliance,hr",    "type":"SOP Reference",   "date":"2024-01-20","helpful":44,"comments":4,
     "problem":"Payroll errors occurring monthly due to unstandardized process.",
     "solution":"End-to-end checklist: data collection, deductions, payslip generation, bank transfers."},
    {"id":10,"title":"Incident Response Playbook",          "dept":"IT Support", "author":"Vikram Nair",  "views":234,"rating":4.7,"verified":True, "priority":"Critical","tags":"incident,security,response", "type":"Problem/Solution","date":"2024-03-08","helpful":78,"comments":13,
     "problem":"No standardized incident response causing slow recovery and poor communication.",
     "solution":"Playbook: detect → contain → eradicate → recover → review. Escalation matrix included."},
    {"id":11,"title":"CI/CD Pipeline Setup Guide",          "dept":"Engineering","author":"Kiran Das",    "views":345,"rating":4.9,"verified":True, "priority":"High",    "tags":"cicd,devops,pipeline",     "type":"Best Practice",   "date":"2024-03-10","helpful":92,"comments":20,
     "problem":"Manual deployments taking hours, frequent rollback failures.",
     "solution":"GitHub Actions CI/CD with automated testing, Docker build, zero-downtime k8s deploy."},
    {"id":12,"title":"Conveyor Belt Maintenance SOP",       "dept":"Maintenance","author":"Suresh Pillai","views":76, "rating":4.2,"verified":True, "priority":"High",    "tags":"conveyor,maintenance,safety","type":"SOP Reference",  "date":"2024-02-05","helpful":25,"comments":4,
     "problem":"Conveyor belt failures causing production line stoppages.",
     "solution":"Weekly inspection: tension adjustment, roller lubrication, emergency stop testing."},
    {"id":13,"title":"Budget Forecasting Template",         "dept":"Finance",    "author":"Deepa Iyer",   "views":88, "rating":4.0,"verified":False,"priority":"Medium",  "tags":"budget,finance,template",  "type":"Best Practice",   "date":"2024-01-10","helpful":29,"comments":2,
     "problem":"Quarterly budgeting inconsistent across departments.",
     "solution":"Shared template with variance analysis, headcount planning, capex/opex breakdown."},
    {"id":14,"title":"Server RAM Upgrade Procedure",        "dept":"IT Support", "author":"Nisha Verma",  "views":156,"rating":4.5,"verified":True, "priority":"Medium",  "tags":"server,hardware,upgrade",  "type":"SOP Reference",   "date":"2024-02-15","helpful":55,"comments":7,
     "problem":"Servers running out of memory during peak hours.",
     "solution":"ESD precautions, BIOS verification, post-upgrade stress testing procedure."},
    {"id":15,"title":"UPS Battery Replacement SOP",         "dept":"Maintenance","author":"Arun Kumar",   "views":98, "rating":4.1,"verified":False,"priority":"Medium",  "tags":"ups,battery,maintenance",  "type":"SOP Reference",   "date":"2024-01-30","helpful":32,"comments":3,
     "problem":"UPS battery failures causing unexpected shutdowns.",
     "solution":"Load transfer to bypass, disconnection sequence, capacity test, e-waste disposal."},
]

ANNOUNCEMENTS = [
    {"id":1,"title":"Mandatory Cybersecurity Training — April 15","body":"All employees must complete the 2024 cybersecurity awareness module before April 15. Non-completion will be escalated.","author":"Vikram Nair","date":"2024-03-20","type":"Compliance","priority":"Urgent","reads":38},
    {"id":2,"title":"New Leave Policy Effective April 1st","body":"Revised policy introduces 2 additional casual leaves and menstrual leave. Full details in HR portal.","author":"Priya Sharma","date":"2024-03-18","type":"Policy","priority":"High","reads":45},
    {"id":3,"title":"Q1 All-Hands Meeting — March 28 at 3 PM IST","body":"Agenda: product roadmap, department wins, open Q&A. Zoom link shared by your manager.","author":"Arjun Mehta","date":"2024-03-15","type":"Event","priority":"Normal","reads":50},
    {"id":4,"title":"WorkBrain Knowledge Drive — Win Prizes!","body":"Top 3 contributors win exclusive rewards. Submit entries, get verified, climb the leaderboard. Ends March 31.","author":"Ananya Reddy","date":"2024-03-12","type":"Training","priority":"Normal","reads":42},
    {"id":5,"title":"ISO 9001 Audit — April 10","body":"External auditors on April 10. All department heads must ensure documentation is current and accessible.","author":"Rajesh Singh","date":"2024-03-05","type":"Compliance","priority":"Urgent","reads":29},
]

HANDOVERS = [
    {"id":1,"employee":"Kiran Das","initials":"KD","dept":"Engineering","role":"Team Lead","lastDay":"2024-04-15","status":"Pending Approval","completion":65,"manager":"Arjun Mehta",
     "responsibilities":"Frontend architecture, CI/CD pipelines, junior dev mentoring, sprint planning",
     "projects":"Dashboard redesign (70%), API migration (30%)",
     "pending":"Q1 performance reviews, vendor contract renewals",
     "contacts":"Arun Kumar — backend lead | Meena Joshi — design",
     "lessons":"Document env configs separately from code. Daily standups catch blockers early.",
     "recommendations":"Hire senior DevOps engineer before Q3. Move legacy auth to OAuth2."},
    {"id":2,"employee":"Deepa Iyer","initials":"DI","dept":"Finance","role":"Finance Analyst","lastDay":"2024-03-31","status":"Approved","completion":100,"manager":"Priya Sharma",
     "responsibilities":"GST filing, payroll processing, vendor payments, monthly P&L",
     "projects":"All tasks handed over successfully",
     "pending":"None — everything closed",
     "contacts":"Rajesh CA firm | Meena accounts payable",
     "lessons":"Keep invoice PDFs organized by vendor-month for quick audits.",
     "recommendations":"Automate GST reconciliation with Python script in /finance/tools."},
    {"id":3,"employee":"Suresh Pillai","initials":"SU","dept":"Maintenance","role":"Maintenance Tech","lastDay":"2024-05-01","status":"Draft","completion":30,"manager":"Arun Kumar",
     "responsibilities":"HVAC servicing, boiler maintenance, diesel generator weekly checks",
     "projects":"Cooling tower upgrade (planning stage only)",
     "pending":"March maintenance schedule, spare parts inventory audit",
     "contacts":"Sharma HVAC vendor +91-9876543210",
     "lessons":"Always log every service call with timestamp and parts used.",
     "recommendations":"Train second technician on boiler systems immediately."},
]

QR_MACHINES = [
    {"id":1,"name":"CNC Machine M-102",     "type":"Machine",       "dept":"Maintenance","scans":89, "code":"WB-MNT-001","icon":"⚙️"},
    {"id":2,"name":"Payment Gateway Module","type":"Software",       "dept":"Engineering","scans":134,"code":"WB-ENG-001","icon":"💳"},
    {"id":3,"name":"Server Room Rack-A",    "type":"Infrastructure","dept":"IT Support", "scans":67, "code":"WB-IT-001", "icon":"🖥️"},
    {"id":4,"name":"Boiler Unit B-04",      "type":"Machine",       "dept":"Maintenance","scans":45, "code":"WB-MNT-002","icon":"🔥"},
    {"id":5,"name":"GST Filing Process",    "type":"Process",       "dept":"Finance",    "scans":78, "code":"WB-FIN-001","icon":"📋"},
]

def calc_risk():
    result = {}
    for dept in DEPARTMENTS:
        emps  = [e for e in EMPLOYEES if e["dept"] == dept]
        total = sum(e["entries"] for e in emps)
        srt   = sorted(emps, key=lambda x: x["entries"], reverse=True)
        top2  = sum(e["entries"] for e in srt[:2])
        conc  = round((top2 / total * 100) if total else 0, 1)
        risk  = "High" if conc > 70 else ("Medium" if conc > 45 else "Low")
        result[dept] = {
            "total": total, "emps": emps, "sorted": srt,
            "concentration": conc, "risk": risk,
            "score": round(100 - conc),
        }
    concs = [v["concentration"] for v in result.values()]
    avg   = round(sum(concs) / len(concs), 1)
    return result, ("High" if avg > 65 else "Medium" if avg > 45 else "Low"), avg

RISK_STATS, COMPANY_RISK, AVG_CONC = calc_risk()
