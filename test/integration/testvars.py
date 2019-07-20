import os, sys

client_config = ('---\n'
'client:\n'
'  hosts: {0}\n'
'  port: {1}\n'
'  url_prefix:\n'
'  use_ssl: False\n'
'  certificate:\n'
'  client_cert:\n'
'  client_key:\n'
'  ssl_no_validate: False\n'
'  http_auth: \n'
'  timeout: 30\n'
'  master_only: False\n'
'\n'
'logging:\n'
'  loglevel: DEBUG\n'
'  logfile:\n'
'  logformat: default\n'
'  blacklist: []\n')

client_conf_logfile = ('---\n'
'client:\n'
'  hosts: {0}\n'
'  port: {1}\n'
'\n'
'logging:\n'
'  loglevel: DEBUG\n'
'  logfile: {2}\n')

client_config_envvars = ('---\n'
'client:\n'
'  hosts: {0}\n'
'  port: {1}\n'
'  timeout: {2}\n'
'  master_only: False\n'
'\n'
'logging:\n'
'  loglevel: DEBUG\n'
'  logfile:\n'
'  logformat: default\n'
'  blacklist: []\n')

bad_client_config = ('---\n'
'misspelled:\n'
'  hosts: {0}\n'
'  port: {1}\n'
'  url_prefix:\n'
'  use_ssl: False\n'
'  certificate:\n'
'  client_cert:\n'
'  client_key:\n'
'  ssl_no_validate: False\n'
'  http_auth: \n'
'  timeout: 30\n'
'  master_only: False\n')

no_logging_config = ('---\n'
'client:\n'
'  hosts: {0}\n'
'  port: {1}\n'
'  url_prefix:\n'
'  use_ssl: False\n'
'  certificate:\n'
'  client_cert:\n'
'  client_key:\n'
'  ssl_no_validate: False\n'
'  http_auth: \n'
'  timeout: 30\n'
'  master_only: False\n')

none_logging_config = ('---\n'
'client:\n'
'  hosts: {0}\n'
'  port: {1}\n'
'  url_prefix:\n'
'  use_ssl: False\n'
'  certificate:\n'
'  client_cert:\n'
'  client_key:\n'
'  ssl_no_validate: False\n'
'  http_auth: \n'
'  timeout: 30\n'
'  master_only: False\n'
'\n'
'logging: \n'
'\n')

alias_add_only = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Add all indices to specified alias"\n'
'    action: alias\n'
'    options:\n'
'      name: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    add:\n'
'      filters:\n'
'        - filtertype: none\n')

alias_add_only_with_extra_settings = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Add all indices to specified alias"\n'
'    action: alias\n'
'    options:\n'
'      name: {0}\n'
'      extra_settings:\n'
'        filter:\n'
'          term:\n'
'            user: kimchy\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    add:\n'
'      filters:\n'
'        - filtertype: none\n')

alias_remove_only = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Remove all indices from specified alias"\n'
'    action: alias\n'
'    options:\n'
'      name: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    remove:\n'
'      filters:\n'
'        - filtertype: none\n')

alias_add_remove = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Add/remove specified indices from designated alias"\n'
'    action: alias\n'
'    options:\n'
'      name: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    remove:\n'
'      filters:\n'
'        - filtertype: pattern\n'
'          kind: prefix\n'
'          value: du\n'
'    add:\n'
'      filters:\n'
'        - filtertype: pattern\n'
'          kind: prefix\n'
'          value: my\n')

alias_remove_index_not_there = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Add/remove specified indices from designated alias"\n'
'    action: alias\n'
'    options:\n'
'      name: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    remove:\n'
'      filters:\n'
'        - filtertype: pattern\n'
'          kind: prefix\n'
'          value: {1}\n')

alias_add_with_empty_remove = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Add/remove specified indices from designated alias"\n'
'    action: alias\n'
'    options:\n'
'      name: {0}\n'
'      warn_if_no_indices: True\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    remove:\n'
'      filters:\n'
'        - filtertype: pattern\n'
'          kind: prefix\n'
'          value: insertrickrollhere\n'
'    add:\n'
'      filters:\n'
'        - filtertype: pattern\n'
'          kind: prefix\n'
'          value: my\n')

alias_remove_with_empty_add = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Add/remove specified indices from designated alias"\n'
'    action: alias\n'
'    options:\n'
'      name: {0}\n'
'      warn_if_no_indices: True\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    remove:\n'
'      filters:\n'
'        - filtertype: pattern\n'
'          kind: prefix\n'
'          value: du\n'
'    add:\n'
'      filters:\n'
'        - filtertype: pattern\n'
'          kind: prefix\n'
'          value: insertrickrollhere\n')

alias_add_remove_empty = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Add/remove specified indices from designated alias"\n'
'    action: alias\n'
'    options:\n'
'      name: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    remove:\n'
'      filters:\n'
'        - filtertype: pattern\n'
'          kind: prefix\n'
'          value: {1}\n'
'    add:\n'
'      filters:\n'
'        - filtertype: pattern\n'
'          kind: prefix\n'
'          value: {2}\n')

alias_no_add_remove = ('---\n'
'actions:\n'
'  1:\n'
'    description: "No add or remove should raise an exception"\n'
'    action: alias\n'
'    options:\n'
'      name: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n')

alias_no_alias = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Removing alias from options should result in an exception"\n'
'    action: alias\n'
'    options:\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    remove:\n'
'      filters:\n'
'        - filtertype: pattern\n'
'          kind: prefix\n'
'          value: du\n'
'    add:\n'
'      filters:\n'
'        - filtertype: pattern\n'
'          kind: prefix\n'
'          value: my\n')

allocation_test = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Allocate by key/value/allocation_type"\n'
'    action: allocation\n'
'    options:\n'
'      key: {0}\n'
'      value: {1}\n'
'      allocation_type: {2}\n'
'      wait_for_completion: {3}\n'
'      wait_interval: 1\n'
'      max_wait: -1\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n')


allocation_count_test = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Allocate by key/value/allocation_type"\n'
'    action: allocation\n'
'    options:\n'
'      key: {0}\n'
'      value: {1}\n'
'      allocation_type: {2}\n'
'      wait_for_completion: {3}\n'
'      wait_interval: 1\n'
'      max_wait: -1\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: count\n'
'        use_age: True\n'
'        source: name\n'
'        timestring: \'%Y.%m.%d\'\n'
'        count: 2\n'
'        exclude: False\n')

cluster_routing_test = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Alter cluster routing by routing_type/value"\n'
'    action: cluster_routing\n'
'    options:\n'
'      routing_type: {0}\n'
'      value: {1}\n'
'      setting: enable\n')

optionless_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Act on indices as filtered"\n'
'    action: {0}\n'
'    options:\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n')

no_options_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Act on indices as filtered"\n'
'    action: {0}\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n')

actionless_proto = ('---\n'
'actions:\n'
'  1:\n'
'    options:\n'
'      continue_if_exception: False\n'
'      disable_action: False\n')

disabled_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Act on indices as filtered"\n'
'    action: {0}\n'
'    options:\n'
'      continue_if_exception: False\n'
'      ignore_empty_list: True\n'
'      disable_action: True\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n'
'  2:\n'
'    description: "Act on indices as filtered"\n'
'    action: {1}\n'
'    options:\n'
'      continue_if_exception: False\n'
'      ignore_empty_list: True\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: log\n')

continue_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Create named index"\n'
'    action: create_index\n'
'    options:\n'
'      name: {0}\n'
'      continue_if_exception: {1}\n'
'      disable_action: False\n'
'  2:\n'
'    description: "Act on indices as filtered"\n'
'    action: {2}\n'
'    options:\n'
'      continue_if_exception: {3}\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: log\n')

close_delete_aliases = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Close indices as filtered"\n'
'    action: close\n'
'    options:\n'
'      delete_aliases: True\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n')

close_skip_flush = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Close indices as filtered"\n'
'    action: close\n'
'    options:\n'
'      skip_flush: True\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n')

delete_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Delete indices as filtered"\n'
'    action: delete_indices\n'
'    options:\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: {0}\n'
'        source: {1}\n'
'        direction: {2}\n'
'        timestring: {3}\n'
'        unit: {4}\n'
'        unit_count: {5}\n'
'        field: {6}\n'
'        stats_result: {7}\n'
'        epoch: {8}\n')

delete_pattern_proto = ('---\n'
                'actions:\n'
                '  1:\n'
                '    description: "Delete indices as filtered"\n'
                '    action: delete_indices\n'
                '    options:\n'
                '      continue_if_exception: False\n'
                '      disable_action: False\n'
                '    filters:\n'
                '      - filtertype: {0}\n'
                '        source: {1}\n'
                '        direction: {2}\n'
                '        timestring: {3}\n'
                '        unit: {4}\n'
                '        unit_count: {5}\n'
                '        unit_count_pattern: {6}\n')


delete_period_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Delete indices as filtered"\n'
'    action: delete_indices\n'
'    options:\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'    - filtertype: {0}\n'
'      source: {1}\n'
'      range_from: {2}\n'
'      range_to: {3}\n'
'      timestring: {4}\n'
'      unit: {5}\n'
'      field: {6}\n'
'      stats_result: {7}\n'
'      intersect: {8}\n'
'      epoch: {9}\n'
'      week_starts_on: {10}\n')

delete_ignore_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Delete indices as filtered"\n'
'    action: delete_indices\n'
'    options:\n'
'      ignore_empty_list: True\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: {0}\n'
'        source: {1}\n'
'        direction: {2}\n'
'        timestring: {3}\n'
'        unit: {4}\n'
'        unit_count: {5}\n'
'        field: {6}\n'
'        stats_result: {7}\n'
'        epoch: {8}\n')

filter_by_alias = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Delete indices as filtered"\n'
'    action: delete_indices\n'
'    options:\n'
'      ignore_empty_list: True\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: alias\n'
'        aliases: {0}\n'
'        exclude: {1}\n')

bad_option_proto_test = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Should raise exception due to extra option"\n'
'    action: {0}\n'
'    options:\n'
'      invalid: this_should_not_be_here\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: none\n')

replicas_test = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Increase replica count to provided value"\n'
'    action: replicas\n'
'    options:\n'
'      count: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n')

forcemerge_test = ('---\n'
'actions:\n'
'  1:\n'
'    description: "forceMerge segment count per shard to provided value with optional delay"\n'
'    action: forcemerge\n'
'    options:\n'
'      max_num_segments: {0}\n'
'      delay: {1}\n'
'      timeout_override: 300\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n')

snapshot_test = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Snapshot selected indices"\n'
'    action: snapshot\n'
'    options:\n'
'      repository: {0}\n'
'      name: {1}\n'
'      wait_interval: {2}\n'
'      max_wait: {3}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: none\n')

delete_snap_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Delete snapshots as filtered"\n'
'    action: delete_snapshots\n'
'    options:\n'
'      repository: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: {1}\n'
'        source: {2}\n'
'        direction: {3}\n'
'        timestring: {4}\n'
'        unit: {5}\n'
'        unit_count: {6}\n'
'        epoch: {7}\n')

create_index = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Create index as named"\n'
'    action: create_index\n'
'    options:\n'
'      name: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n')

create_index_with_extra_settings = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Create index as named with extra settings"\n'
'    action: create_index\n'
'    options:\n'
'      name: {0}\n'
'      extra_settings:\n'
'        settings:\n'
'          number_of_shards: 1\n'
'          number_of_replicas: 0\n'
'      continue_if_exception: False\n'
'      disable_action: False\n')

restore_snapshot_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: Restore snapshot as configured\n'
'    action: restore\n'
'    options:\n'
'      repository: {0}\n'
'      name: {1}\n'
'      indices: {2}\n'
'      include_aliases: {3}\n'
'      ignore_unavailable: {4}\n'
'      include_global_state: {5}\n'
'      partial: {6}\n'
'      rename_pattern: {7}\n'
'      rename_replacement: {8}\n'
'      extra_settings: {9}\n'
'      wait_for_completion: {10}\n'
'      skip_repo_fs_check: {11}\n'
'      timeout_override: {12}\n'
'      wait_interval: {13}\n'
'      max_wait: {14}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'    - filtertype: none\n')

test_687 = ('---\n'
'actions:\n'
'  1:\n'
'    action: snapshot\n'
'    description: >-\n'
'      Create a snapshot with the last week index.\n'
'    options:\n'
'      repository: {0}\n'
'      name: {1}\n'
'      ignore_unavailable: False\n'
'      include_global_state: True\n'
'      partial: False\n'
'      wait_for_completion: True\n'
'      skip_repo_fs_check: False\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'    - filtertype: pattern\n'
'      kind: prefix\n'
'      value: logstash-\n'
'      exclude:\n'
'    - filtertype: age\n'
'      source: creation_date\n'
'      direction: younger\n'
'      epoch: 1467020729\n'
'      unit: weeks\n'
'      unit_count: 2\n'
'      exclude:\n'
'    - filtertype: age\n'
'      source: creation_date\n'
'      direction: younger\n'
'      epoch: 1467020729\n'
'      unit: weeks\n'
'      unit_count: 1\n'
'      exclude: True\n'
'  2:\n'
'    action: delete_indices\n'
'    description: >-\n'
'      Remove indices starting with logstash- older than 5 weeks\n'
'    options:\n'
'      ignore_empty_list: True\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'    - filtertype: pattern\n'
'      kind: prefix\n'
'      value: logstash-\n'
'      exclude:\n'
'    - filtertype: age\n'
'      source: creation_date\n'
'      epoch: 1467020729\n'
'      direction: older\n'
'      unit: weeks\n'
'      unit_count: 5\n'
'      exclude:\n')

test_682 = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Snapshot selected indices"\n'
'    action: snapshot\n'
'    options:\n'
'      repository: {0}\n'
'      name: {1}\n'
'      ignore_empty_list: {2}\n'
'      wait_interval: {3}\n'
'      max_wait: {4}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'    - filtertype: pattern\n'
'      kind: prefix\n'
'      value: notlogstash-\n'
'      exclude:\n'
'  2:\n'
'    description: "Delete selected indices"\n'
'    action: delete_indices\n'
'    options:\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'    - filtertype: pattern\n'
'      kind: prefix\n'
'      value: logstash-\n'
'      exclude:\n')

CRA_all = {
    u'persistent':{},
    u'transient':{u'cluster':{u'routing':{u'allocation':{u'enable':u'all'}}}}
}

rollover_one = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Rollover selected alias/index"\n'
'    action: rollover\n'
'    options:\n'
'      name: {0}\n'
'      conditions: \n'
'        {1}: {2}\n'
'      extra_settings:\n'
'        index.number_of_shards: 1\n'
'        index.number_of_replicas: 0\n')

rollover_both = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Rollover selected alias/index"\n'
'    action: rollover\n'
'    options:\n'
'      name: {0}\n'
'      conditions: \n'
'        max_age: {1}\n'
'        max_docs: {2}\n'
'      extra_settings:\n'
'        index.number_of_shards: 1\n'
'        index.number_of_replicas: 0\n')

rollover_bad_settings = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Rollover selected alias/index"\n'
'    action: rollover\n'
'    options:\n'
'      name: {0}\n'
'      conditions: \n'
'        max_age: {1}\n'
'        max_docs: {2}\n'
'      extra_settings:\n'
'        foo: 1\n'
'        bar: 0\n')

rollover_with_name = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Rollover selected alias/index"\n'
'    action: rollover\n'
'    options:\n'
'      name: {0}\n'
'      conditions: \n'
'        {1}: {2}\n'
'      new_index: {3}\n'
'      extra_settings:\n'
'        index.number_of_shards: 1\n'
'        index.number_of_replicas: 0\n')

reindex = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Reindex"\n'
'    action: reindex\n'
'    options:\n'
'      allow_ilm_indices: true\n'
'      wait_interval: {0}\n'
'      max_wait: {1}\n'
'      request_body:\n'
'        source:\n'
'          index: {2}\n'
'        dest:\n'
'          index: {3}\n'
'    filters:\n'
'    - filtertype: none\n')

reindex_empty_list = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Reindex"\n'
'    action: reindex\n'
'    options:\n'
'      ignore_empty_list: {0}\n'
'      wait_interval: {1}\n'
'      max_wait: {2}\n'
'      request_body:\n'
'        source:\n'
'          index: REINDEX_SELECTED\n'
'        dest:\n'
'          index: {3}\n'
'    filters:\n'
'    - filtertype: pattern\n'
'      kind: prefix\n'
'      value: notfound\n')

remote_reindex = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Reindex from remote"\n'
'    action: reindex\n'
'    options:\n'
'      wait_interval: {0}\n'
'      max_wait: {1}\n'
'      request_body:\n'
'        source:\n'
'          remote:\n'
'            host: {2}\n'
'          index: {3}\n'
'        dest:\n'
'          index: {4}\n'
'      remote_filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: {5}\n'
'    filters:\n'
'    - filtertype: none\n')
migration_reindex = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Reindex from remote"\n'
'    action: reindex\n'
'    options:\n'
'      wait_interval: {0}\n'
'      max_wait: {1}\n'
'      migration_prefix: {2}\n'
'      migration_suffix: {3}\n'
'      request_body:\n'
'        source:\n'
'          remote:\n'
'            host: {4}\n'
'          index: {5}\n'
'        dest:\n'
'          index: {6}\n'
'      remote_filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: {7}\n'
'    filters:\n'
'    - filtertype: none\n')
test_945 = ('---\n'
'actions:\n'
'  1:\n'
'    action: delete_indices\n'
'    description: >-\n'
'      Delete indices older than 7 days\n'
'    options:\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'    - filtertype: pattern\n'
'      kind: prefix\n'
'      value: logstash-\n'
'      exclude:\n'
'      - filtertype: age\n'
'        source: name\n'
'        direction: older\n'
'        unit: days\n'
'        unit_count: 7\n')
index_settings = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Act on indices as filtered"\n'
'    action: index_settings\n'
'    options:\n'
'      index_settings:\n'
'        index:\n'
'          {0}: {1}\n'
'      ignore_unavailable: {2}\n'
'      preserve_existing: {3}\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n')

ilm_delete_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Delete indices as filtered"\n'
'    action: delete_indices\n'
'    options:\n'
'      allow_ilm_indices: {9}\n'
'    filters:\n'
'      - filtertype: {0}\n'
'        source: {1}\n'
'        direction: {2}\n'
'        timestring: {3}\n'
'        unit: {4}\n'
'        unit_count: {5}\n'
'        field: {6}\n'
'        stats_result: {7}\n'
'        epoch: {8}\n')
