import io
import csv
from fastapi.responses import StreamingResponse

from src.data.mongodb import query_operation


def get_stream(operation: str):
    operations_list = query_operation(operation)
    if not operations_list:
        return
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=operations_list[0].keys())
    writer.writeheader()
    writer.writerows(operations_list)
    output.seek(0)
    return StreamingResponse(output, media_type="text/csv")
