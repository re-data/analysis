{{
    config(
        re_data_monitored=true,
        re_data_time_filter='timestamp'
    )
}}

select * from {{ source('re_data_python_library', 'command_call') }}