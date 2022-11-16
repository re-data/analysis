select 
    {{ dbt_utils.surrogate_key(['os_system', 'dbt_version', 're_data_version', 'python_version']) }} as system_id,
    {{ library_version() }},
    command_exception.*
from {{ source('re_data_python_library', 'command_exception') }} as command_exception


