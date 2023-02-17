{{
    config(
        re_data_monitored=true,
        re_data_time_filter='timestamp'
    )
}}

select 
    {{ dbt_utils.generate_surrogate_key(['os_system', 'dbt_version', 're_data_version', 'python_version']) }} as system_id,
    {{ library_version() }},
    command_exception.*
from {{ source('re_data_python_library', 'command_exception') }} as command_exception


