# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           redis
%define go_import_path  github.com/go-redis/redis
# TODO: need dependency of redis, do it later - Julian
%define go_test_ignore_failure 1

Name:           go-github-go-redis-redis
Version:        9.18.0
Release:        %autorelease
Summary:        Redis Go client
License:        BSD-2-Clause
URL:            https://github.com/go-redis/redis
#!RemoteAsset:  sha256:d1399106b1d308019858e76c11edd5df44a6957e9a303e14b659aba4ffa71b5d
Source0:        https://github.com/go-redis/redis/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-redis/redis) = %{version}

%description
go-redis is the official Redis client library for
the Go programming language. It offers a straightforward
interface for interacting with Redis servers.

%package        tests
Summary:        Regression tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       go

%description    tests
Go regression test sources for go-github-go-redis-redis.

%files
%exclude /usr/share/gocode/src/github.com/go-redis/redis/async_handoff_integration_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/auth/auth_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/command_digest_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/digest_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/error_wrapping_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/extra/rediscmd/rediscmd_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/extra/redisotel/metrics_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/extra/redisotel/tracing_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/helper/helper_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/auth/streaming/manager_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/auth/streaming/pool_hook_state_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/hashtag/hashtag_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/hscan/hscan_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/internal_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/pool/conn_relaxed_timeout_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/pool/conn_state_alloc_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/pool/conn_state_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/pool/conn_used_at_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/pool/double_freeturn_simple_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/pool/double_freeturn_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/pool/hooks_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/pool/main_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/pool/pool_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/pool/want_conn_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/proto/peek_push_notification_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/proto/proto_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/proto/reader_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/proto/redis_errors_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/routing/aggregator_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/util/convert_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/util/strconv_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/util/unsafe_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal/util_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal_maint_notif_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/internal_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/logging/logging_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/main_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/circuit_breaker_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/config_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/cluster_maintnotif_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/config_autostart_logic_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/scenario_endpoint_types_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/scenario_push_notifications_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/scenario_stress_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/scenario_timeout_configs_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/scenario_tls_configs_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/scenario_unified_injector_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/manager_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/pool_hook_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/push_notification_handler_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/monitor_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/options_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/osscluster_lazy_reload_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/osscluster_maintnotifications_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/osscluster_maintnotifications_unit_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/push/processor_unit_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/push/push_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/redis_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/search_commands_parse_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/sentinel_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/tls_cert_auth_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/tls_standalone_test.go
%exclude /usr/share/gocode/src/github.com/go-redis/redis/vectorset_commands_test.go
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%files tests
/usr/share/gocode/src/github.com/go-redis/redis/async_handoff_integration_test.go
/usr/share/gocode/src/github.com/go-redis/redis/auth/auth_test.go
/usr/share/gocode/src/github.com/go-redis/redis/command_digest_test.go
/usr/share/gocode/src/github.com/go-redis/redis/digest_test.go
/usr/share/gocode/src/github.com/go-redis/redis/error_wrapping_test.go
/usr/share/gocode/src/github.com/go-redis/redis/extra/rediscmd/rediscmd_test.go
/usr/share/gocode/src/github.com/go-redis/redis/extra/redisotel/metrics_test.go
/usr/share/gocode/src/github.com/go-redis/redis/extra/redisotel/tracing_test.go
/usr/share/gocode/src/github.com/go-redis/redis/helper/helper_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/auth/streaming/manager_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/auth/streaming/pool_hook_state_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/hashtag/hashtag_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/hscan/hscan_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/internal_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/pool/conn_relaxed_timeout_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/pool/conn_state_alloc_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/pool/conn_state_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/pool/conn_used_at_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/pool/double_freeturn_simple_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/pool/double_freeturn_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/pool/hooks_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/pool/main_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/pool/pool_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/pool/want_conn_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/proto/peek_push_notification_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/proto/proto_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/proto/reader_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/proto/redis_errors_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/routing/aggregator_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/util/convert_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/util/strconv_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/util/unsafe_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal/util_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal_maint_notif_test.go
/usr/share/gocode/src/github.com/go-redis/redis/internal_test.go
/usr/share/gocode/src/github.com/go-redis/redis/logging/logging_test.go
/usr/share/gocode/src/github.com/go-redis/redis/main_test.go
/usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/circuit_breaker_test.go
/usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/config_test.go
/usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/cluster_maintnotif_test.go
/usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/config_autostart_logic_test.go
/usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/scenario_endpoint_types_test.go
/usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/scenario_push_notifications_test.go
/usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/scenario_stress_test.go
/usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/scenario_timeout_configs_test.go
/usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/scenario_tls_configs_test.go
/usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/e2e/scenario_unified_injector_test.go
/usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/manager_test.go
/usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/pool_hook_test.go
/usr/share/gocode/src/github.com/go-redis/redis/maintnotifications/push_notification_handler_test.go
/usr/share/gocode/src/github.com/go-redis/redis/monitor_test.go
/usr/share/gocode/src/github.com/go-redis/redis/options_test.go
/usr/share/gocode/src/github.com/go-redis/redis/osscluster_lazy_reload_test.go
/usr/share/gocode/src/github.com/go-redis/redis/osscluster_maintnotifications_test.go
/usr/share/gocode/src/github.com/go-redis/redis/osscluster_maintnotifications_unit_test.go
/usr/share/gocode/src/github.com/go-redis/redis/push/processor_unit_test.go
/usr/share/gocode/src/github.com/go-redis/redis/push/push_test.go
/usr/share/gocode/src/github.com/go-redis/redis/redis_test.go
/usr/share/gocode/src/github.com/go-redis/redis/search_commands_parse_test.go
/usr/share/gocode/src/github.com/go-redis/redis/sentinel_test.go
/usr/share/gocode/src/github.com/go-redis/redis/tls_cert_auth_test.go
/usr/share/gocode/src/github.com/go-redis/redis/tls_standalone_test.go
/usr/share/gocode/src/github.com/go-redis/redis/vectorset_commands_test.go

%changelog
%autochangelog
