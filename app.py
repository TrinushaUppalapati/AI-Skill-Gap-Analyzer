import streamlit as st
from skills_data import job_roles

st.set_page_config(
    page_title="AI Skill Gap Analyzer",
    page_icon="🚀",
    layout="wide"
)

# Page styling
st.title("AI Skill Gap Analyzer")
st.write(
    "Find missing skills and get a learning roadmap for your dream role."
)

@st.cache_data
def get_available_roles():
    """Get list of available job roles."""
    return sorted(list(job_roles.keys()))


def analyze_skills(user_skills_input, selected_role):
    """
    Analyze user skills against required skills for a role.
    
    Args:
        user_skills_input: Comma-separated string of user skills
        selected_role: Selected job role
        
    Returns:
        Dict with analysis results or None if invalid input
    """
    # Validate input
    if not user_skills_input.strip():
        st.warning("Please enter at least one skill.")
        return None
    
    # Clean and normalize user skills
    user_skills = {
        skill.strip().lower()
        for skill in user_skills_input.split(",")
        if skill.strip()
    }
    
    # Get required skills for the role
    required_skills = job_roles[selected_role]
    required_skills_lower = {skill.lower(): skill for skill in required_skills}
    
    # Find matching and missing skills (using set operations for efficiency)
    user_skills_set = user_skills
    required_skills_lower_set = set(required_skills_lower.keys())
    
    matched_lower = user_skills_set & required_skills_lower_set
    matched_skills = [required_skills_lower[skill] for skill in matched_lower]
    missing_skills = [
        required_skills_lower[skill]
        for skill in (required_skills_lower_set - matched_lower)
    ]
    
    # Calculate score
    total_required = len(required_skills)
    score = round((len(matched_skills) / total_required) * 100) if total_required > 0 else 0
    
    return {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "total_required": total_required
    }


# UI Layout
col1, col2 = st.columns([2, 1])

with col1:
    role = st.selectbox(
        "Select Your Dream Role",
        get_available_roles(),
        help="Choose a job role to analyze skills against"
    )

with col2:
    st.write("")  # Spacing for alignment

user_input = st.text_area(
    "Enter Your Skills (comma separated)",
    placeholder="e.g., Python, Machine Learning, Data Analysis, SQL",
    help="List all skills you currently have"
)

if st.button("📊 Analyze Skills", use_container_width=True):
    results = analyze_skills(user_input, role)
    
    if results:
        # Display metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Readiness Score", f"{results['score']}%")
        
        with col2:
            st.metric("Skills Matched", f"{len(results['matched_skills'])}/{results['total_required']}")
        
        with col3:
            st.metric("Skills Missing", len(results['missing_skills']))
        
        st.divider()
        
        # Display results
        if results['matched_skills']:
            st.subheader("✅ Skills You Have")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.success("Great! You have these skills:")
            st.write(", ".join(results['matched_skills']))
        
        st.subheader("❌ Missing Skills")
        if results['missing_skills']:
            st.info(f"You need to develop {len(results['missing_skills'])} skill(s):")
            st.write(", ".join(results['missing_skills']))
        else:
            st.success("✨ You already have all required skills!")
        
        st.subheader("📚 Learning Roadmap")
        
        if results['missing_skills']:
            st.write("Here's a prioritized learning plan:")
            for i, skill in enumerate(results['missing_skills'], start=1):
                st.write(f"**{i}. Learn {skill}**")
            st.divider()
            st.info("💡 Tip: Focus on 1-2 skills at a time for better learning retention.")
        else:
            st.balloons()
            st.success(
                "🎉 Excellent! You already have all required skills for this role!"
            )
