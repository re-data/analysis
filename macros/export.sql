
{% macro export_exceptions() %}
    {% set query %}
        select * from {{ ref('exceptions_by_day')}}
    {% endset %}
    {% set result = run_query(query) %}
    {% do result.to_json('views/exceptions.json') %}
{% endmacro %}