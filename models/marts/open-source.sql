
select * from {{ ref('by_actions')}}
where re_data_version not in {{ cloud_versions() }}