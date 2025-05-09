import json
import copy


def filter_spec_for_json_body(input_spec_path, output_spec_path):
    """
    Loads an OpenAPI spec, removes non-JSON request body content types,
    and saves the modified spec.
    """
    try:
        with open(input_spec_path, 'r', encoding='utf-8') as f:
            spec = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_spec_path}")
        return
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {input_spec_path}: {e}")
        return

    # Deep copy to avoid modifying the original dict if loaded elsewhere
    modified_spec = copy.deepcopy(spec)

    if 'title' in modified_spec:
        modified_spec['directline'] = modified_spec.pop('title')
    elif 'info' in modified_spec and 'title' in modified_spec['info']:
        modified_spec['info']['title'] = 'directline'

    if 'paths' in modified_spec:
        for path, methods in modified_spec['paths'].items():
            for method, operation in methods.items():
                if 'requestBody' in operation and 'content' in operation['requestBody']:
                    original_content = operation['requestBody']['content']
                    filtered_content = {}

                    # Keep only application/json (and optionally text/json)
                    if 'application/json' in original_content:
                        filtered_content['application/json'] = original_content['application/json']
                    # You might also want to keep 'text/json' as it's often treated the same
                    # if 'text/json' in original_content:
                    #     filtered_content['text/json'] = original_content['text/json']

                    # If we found JSON types, replace the content, otherwise remove requestBody?
                    # For simplicity, just replace. If no JSON was found, content will be empty.
                    # The generator should hopefully handle this gracefully (e.g., not generate body params).
                    operation['requestBody']['content'] = filtered_content

                    # Optional: If filtering resulted in empty content, remove the requestBody entirely
                    if not filtered_content:
                        del operation['requestBody']
                        print(
                            f"WARN: Removed requestBody from {method.upper()} {path} as no JSON content type found after filtering.")

    # Also filter components/requestBodies if necessary (like the TokenParameters example)
    if 'components' in modified_spec and 'requestBodies' in modified_spec['components']:
        for rb_name, request_body in modified_spec['components']['requestBodies'].items():
            if 'content' in request_body:
                original_content = request_body['content']
                filtered_content = {}
                if 'application/json' in original_content:
                    filtered_content['application/json'] = original_content['application/json']
                # if 'text/json' in original_content:
                #     filtered_content['text/json'] = original_content['text/json']

                request_body['content'] = filtered_content
                if not filtered_content:
                    # This might be problematic for $ref'd requestBodies, handle with care
                    print(
                        f"WARN: Request body component '{rb_name}' has no JSON content after filtering.")

    try:
        with open(output_spec_path, 'w', encoding='utf-8') as f:
            json.dump(modified_spec, f, indent=4, ensure_ascii=False)
        print(f"Successfully created filtered spec: {output_spec_path}")
    except IOError as e:
        print(f"Error writing filtered spec to {output_spec_path}: {e}")


# --- Usage ---
input_file = 'directline-client.json'
output_file = 'directline-client.json'
filter_spec_for_json_body(input_file, output_file)
