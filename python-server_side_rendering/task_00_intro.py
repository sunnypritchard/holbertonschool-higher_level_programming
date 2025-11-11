import os


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and attendee data.

    Args:
        template: A string containing the invitation template with
                  placeholders
        attendees: A list of dictionaries containing attendee information
    """
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template is not a string")
        return

    # Check if attendees is a list
    if not isinstance(attendees, list):
        print("Error: Attendees is not a list")
        return

    # Check if all items in attendees are dictionaries
    if attendees and not all(isinstance(attendee, dict)
                             for attendee in attendees):
        print("Error: Attendees is not a list of dictionaries")
        return

    # Check if template is empty
    if not template:
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Start with a copy of the template
        output_content = template

        # Replace placeholders with actual values or "N/A"
        name = attendee.get('name')
        event_title = attendee.get('event_title')
        event_date = attendee.get('event_date')
        event_location = attendee.get('event_location')

        # Replace with actual values or "N/A" if missing/None
        output_content = output_content.replace(
            '{name}', str(name) if name is not None else 'N/A')
        output_content = output_content.replace(
            '{event_title}',
            str(event_title) if event_title is not None else 'N/A')
        output_content = output_content.replace(
            '{event_date}',
            str(event_date) if event_date is not None else 'N/A')
        output_content = output_content.replace(
            '{event_location}',
            str(event_location) if event_location is not None else 'N/A')

        # Generate output filename
        output_filename = f'output_{index}.txt'

        # Check if file already exists
        if os.path.exists(output_filename):
            print(f"Warning: {output_filename} already exists, skipping.")
            continue

        # Write to file
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(output_content)
            print(f"Generated {output_filename}")
        except Exception as e:
            print(f"Error writing {output_filename}: {e}")
