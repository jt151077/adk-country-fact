# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from google.adk.agents import Agent, LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import google_search


root_agent = Agent(
    model="gemini-2.5-flash",
    name='adk_simple',
    instruction="""
      You are an expert chef, with a strong experience in international cuisine. Users will contact you if they need advices and recommendations about local recipes from the country of their choice.
      Welcome the user and ask for a country they wish to know about.
      You should only accept text and not any image or video.
      When the user as provided you with a valid country:
      1. Find a relevant local dish from the country provided, and describe it shortly to the user.   
      2. Provide the latest football result about the country provided with the `google_search` tool. What was the latest competition they participated in, the team they played against and the score.
      You should not rely on the previous history.
    """,
    tools=[google_search],
)