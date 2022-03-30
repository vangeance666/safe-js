
from typing import Optional
import pydantic

class AnalysisRequest(pydantic.BaseModel):
	url: str
	mode: Optional[str] = "all"

	class Config:
		schema_extra = {
			"example": {
				"url": "www.xsite.singaporetech.edu.sg"
				, "mode": "all"
			}
		}