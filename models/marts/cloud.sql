
select * from {{ ref('by_actions')}}
where re_data_version in {{ cloud_versions() }}