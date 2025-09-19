from typing import List,Optional,Dict,Any,Optional



class Sessions():
    def __init__(self):
        self.sessions: Dict[str, List[Dict[str, Any]]] = {}

    def add_to_session(self, session_id: str, input_text: str, sentiment: List,summary:str):
        """Add a text and its sentiment to a session."""
        if session_id not in self.sessions:
            self.sessions[session_id] = []

        self.sessions[session_id].append({
            "Input_text": input_text,
            "Sentiment": sentiment,
            "Summary":summary
        })

    def get_session(self, session_id: str) -> Dict:
        """Retrieve all texts and sentiments for a session."""
        if session_id not in self.sessions:
            return {"error": "Session not found"}
        return {"session_id": session_id, "history": self.sessions[session_id]}

    def clear_session(self, session_id: str) -> Dict:
        """Clear a specific session."""
        if session_id in self.sessions:
            del self.sessions[session_id]
            return {"status": f"Session '{session_id}' cleared"}
        return {"error": "Session not found"}

    def clear_all_sessions(self):
        """Clear all sessions."""
        self.sessions.clear()
        return {"status": "All sessions cleared"}


sessions=Sessions()