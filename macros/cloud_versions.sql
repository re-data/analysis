{% macro library_version() %}
    case
        when command in ('dbt_docs', 're_data') then 're_cloud'
        else 're_data'
    end as library
{% endmacro %}