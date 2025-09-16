# Tool Usage Configuration Guide

This document outlines the behavior of tool usage based on the `is_enabled` and `tool_choice` configurations for two available tools: `weather` and `dollar_rate`.

## Tools

- **weather**: Provides weather-related information.
- **dollar_rate**: Provides currency exchange rate information for the dollar.

## Configuration Cases

The behavior of tool calls depends on the values of `is_enabled` and `tool_choice`. Below are the defined cases:

### Case 1: `is_enabled: False`, `tool_choice: required`

- **Behavior**: No tool call will occur.
- **Reason**: When `is_enabled` is set to `False`, the tools are not visible to the LLM. The triage agent will provide the response directly without invoking any tools.

### Case 2: `is_enabled: True`, `tool_choice: none`

- **Behavior**: No tool call will occur.
- **Reason**: When `tool_choice` is set to `none`, the LLM is instructed not to use any tools. The triage agent will handle the response directly without invoking any tools.

### Case 3: `is_enabled: True`, `tool_choice: auto`

- **Behavior**: Tool call may occur if needed.
- **Reason**: When `is_enabled` is `True` and `tool_choice` is `auto`, the LLM can decide to call a tool (`weather` or `dollar_rate`) based on the query's requirements.

## Summary Table

| Case | `is_enabled` | `tool_choice` | Tool Call Behavior      | Response Source |
|------|--------------|---------------|-------------------------|-----------------|
| 1    | False        | required      | No tool call            | Triage Agent    |
| 2    | True         | none          | No tool call            | Triage Agent    |
| 3    | True         | auto          | Tool call if needed     | LLM (with tools)|

## Notes

- Ensure that the appropriate configuration is set based on the desired behavior for tool usage.
- The `weather` and `dollar_rate` tools are only invoked when both `is_enabled` is `True` and `tool_choice` allows tool usage (`auto`).