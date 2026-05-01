import streamlit as st

st.set_page_config(
    page_title="AI Helpdesk System",
    page_icon="🤖",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align:center;'>🤖 AI Helpdesk Ticket Triage System</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Realistic Employee + IT Admin Workflow</p>",
    unsafe_allow_html=True
)
st.markdown("---")

if "tickets" not in st.session_state:
    st.session_state.tickets = []

def classify_ticket(text):
    t = text.lower()

    if "wifi" in t or "internet" in t or "vpn" in t:
        return "Network", "High", "Network Team", "wifi / internet / vpn"

    elif "password" in t or "login" in t or "account" in t:
        return "Account", "High", "Account Support", "password / login / account"

    elif "printer" in t or "scanner" in t or "device" in t:
        return "Device", "Medium", "IT Support", "printer / scanner / device"

    elif "slow" in t or "freezing" in t or "performance" in t:
        return "Performance", "High", "IT Support", "slow / freezing / performance"

    elif "install" in t or "request" in t or "access" in t:
        return "Request", "Low", "Service Desk", "install / request / access"

    else:
        return "General", "Low", "Service Desk", "general issue"

left, right = st.columns(2)

with left:
    st.subheader("👤 Employee Portal")
    employee_name = st.text_input("Employee Name")
    ticket_text = st.text_area("Describe your IT issue:", height=150)

    if st.button("Submit Ticket"):
        if ticket_text.strip() == "":
            st.warning("Please enter a ticket.")
        else:
            category, urgency, department, keywords = classify_ticket(ticket_text)

            st.session_state.tickets.append({
                "employee": employee_name if employee_name else "Unknown",
                "ticket": ticket_text,
                "category": category,
                "urgency": urgency,
                "department": department,
                "keywords": keywords,
                "status": "Open"
            })

            st.success("✅ Ticket submitted successfully!")
            st.info("Your ticket was sent to the IT team.")

with right:
    st.subheader("👨‍💻 IT Admin Panel")

    if len(st.session_state.tickets) == 0:
        st.info("No tickets submitted yet.")
    else:
        for i, ticket in enumerate(st.session_state.tickets, start=1):
            st.markdown(
                f"""
                <div style='background-color:#f0f8ff; padding:15px; border-radius:10px; margin-bottom:12px;'>
                    <h4>Ticket #{i}</h4>
                    <b>Employee:</b> {ticket['employee']}<br>
                    <b>Issue:</b> {ticket['ticket']}<br><br>
                    <b>Predicted Category:</b> {ticket['category']}<br>
                    <b>Urgency:</b> {ticket['urgency']}<br>
                    <b>Assigned Department:</b> {ticket['department']}<br>
                    <b>Key Words:</b> {ticket['keywords']}<br>
                    <b>Status:</b> {ticket['status']}
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown("---")

st.subheader("📊 Dashboard Summary")
total = len(st.session_state.tickets)
high = sum(1 for t in st.session_state.tickets if t["urgency"] == "High")
open_tickets = sum(1 for t in st.session_state.tickets if t["status"] == "Open")

col1, col2, col3 = st.columns(3)
col1.metric("Total Tickets", total)
col2.metric("High Urgency", high)
col3.metric("Open Tickets", open_tickets)

st.caption("Demo version - AI-Based IT Helpdesk Ticket Triage System")
