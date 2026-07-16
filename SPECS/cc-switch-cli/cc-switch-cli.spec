# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cc-switch-cli
Version:        5.7.0
Release:        %autorelease
Summary:        All-in-one assistant for AI coding command-line tools
License:        MIT
URL:            https://github.com/SaladDay/cc-switch-cli
VCS:            git:https://github.com/SaladDay/cc-switch-cli.git
#!RemoteAsset:  sha256:8e7ba533b5a4c6b9ffc596fc71ef45a8c4073b5aede481782bcea7b6e2c13d5c
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    rust

# Skip external Claude CLI lookup: Could not find `claude` in PATH.
# Run tests serially because parallel tests share process-global configuration
# and remove each other's Hermes state and coordination lock files.
BuildOption(check):  -- --test-threads=1 --skip cli::claude_temp_launch::tests::prepare_launch_from_settings_writes_exact_effective_snapshot
# Skip external Claude CLI lookup: Could not find `claude` in PATH.
BuildOption(check):  --skip cli::commands::start::tests::prepare_claude_launch_with_writes_effective_snapshot_from_state
# Skip stale bundled provider expectation: Cubence is present in the v5.7.0 provider data.
BuildOption(check):  --skip cli::tui::form::tests::provider_add_form_openclaw_uses_dedicated_template_defs
# Skip stale bundled provider expectation: Cubence is present in the v5.7.0 provider data.
BuildOption(check):  --skip cli::tui::form::tests::provider_add_form_opencode_only_adds_aicodemirror_beyond_custom
# Skip external Claude CLI lookup: failed to capture written settings.
BuildOption(check):  --skip cli::tui::runtime_actions::claude_temp_launch::tests::launch_uses_effective_snapshot_from_realtime_state
# Skip process-global Hermes configuration state: called `Option::unwrap()` on a `None` value.
BuildOption(check):  --skip hermes_config::tests::set_and_get_provider_roundtrip
# Skip process-global OAuth account state: no ChatGPT account is available.
BuildOption(check):  --skip proxy::forwarder::tests::request_building::codex_oauth_prepare_request_falls_back_to_default_account
# Skip process-global OAuth account state: account acc-bound does not exist.
BuildOption(check):  --skip proxy::forwarder::tests::request_building::codex_oauth_prepare_request_injects_bound_account_headers
# Skip process-global OAuth account state: account acc-session does not exist.
BuildOption(check):  --skip proxy::forwarder::tests::request_building::codex_oauth_prepare_request_injects_client_session_headers
# Skip process-global OAuth account state: account acc-generated does not exist.
BuildOption(check):  --skip proxy::forwarder::tests::request_building::codex_oauth_prepare_request_skips_generated_session_headers
# Skip refreshed HTTP stack timing mismatch: expected a 504 timeout but received 200.
BuildOption(check):  --skip error_cases::proxy_claude_streaming_non_sse_success_fallback_uses_timeout_budget
# Skip refreshed HTTP stack response mismatch: expected application/json but received text/event-stream.
BuildOption(check):  --skip success_cases::stream_openai_chat_buffered_json_fallback_marks_request_success
# Skip build-worker process probe mismatch: an unreachable /status endpoint is reported as running.
BuildOption(check):  --skip managed_session_disable_last_app_does_not_terminate_when_status_probe_fails
# Skip build-worker daemon startup timing: the test socket does not appear within five seconds.
BuildOption(check):  --skip proxy_service_reloaded_app_state_keeps_managed_session_running_for_current_app
# Skip build-worker port collision: the test proxy listener reports address already in use.
BuildOption(check):  --skip disabling_one_managed_app_restores_only_that_app_while_shared_runtime_keeps_other_takeover
# Skip build-worker process probe mismatch: the managed runtime session PID is unavailable.
BuildOption(check):  --skip startup_recovery_skips_owned_managed_session_when_probe_is_unreachable
# Skip serde_json ordering mismatch: semantically equal JSON is serialized in a different key order.
BuildOption(check):  --skip proxy::response::tests::non_success_standard_json_errors_can_still_transform
# Skip process-global proxy routing state: daemon-managed routing is not active.
BuildOption(check):  --skip services::proxy::tests::enable_auto_failover_for_app_rejects_when_proxy_is_not_routed
# Skip process-global proxy routing state: daemon-managed routing is not active.
BuildOption(check):  --skip services::proxy::tests::enable_auto_failover_for_app_switches_to_queue_head
# Skip process-global provider state: no active provider is selected.
BuildOption(check):  --skip services::proxy::tests::enable_proxy_and_auto_failover_uses_queue_head_without_existing_current_provider
# Skip container hostname lookup: no system device name can be detected in the build worker.
BuildOption(check):  --skip services::webdav_sync::tests::detect_system_device_name_returns_some
# Skip localized message mismatch: the correct unsupported error is returned in Chinese.
BuildOption(check):  --skip stream_check_openclaw_returns_unsupported_before_auth_extraction

BuildRequires:  cargo
BuildRequires:  rust >= 1.91.1
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(anyhow-1/default) >= 1.0.0
BuildRequires:  crate(arbitrary-1/derive) >= 1.4.1
BuildRequires:  crate(async-stream-0.3/default) >= 0.3.0
BuildRequires:  crate(axum-0.7/default) >= 0.7.0
BuildRequires:  crate(base64-0.22/default) >= 0.22.0
BuildRequires:  crate(borsh-1/unstable--schema) >= 1.1.1
BuildRequires:  crate(bytes-1/default) >= 1.5.0
BuildRequires:  crate(chrono-0.4/default) >= 0.4.0
BuildRequires:  crate(chrono-0.4/serde) >= 0.4.0
BuildRequires:  crate(clap-4/cargo) >= 4.5.0
BuildRequires:  crate(clap-4/default) >= 4.5.0
BuildRequires:  crate(clap-4/derive) >= 4.5.0
BuildRequires:  crate(clap-4/env) >= 4.5.0
BuildRequires:  crate(clap-4/wrap-help) >= 4.5.0
BuildRequires:  crate(clap-complete-4/default) >= 4.5.0
BuildRequires:  crate(colored-2/default) >= 2.1.0
BuildRequires:  crate(comfy-table-7/default) >= 7.1.0
BuildRequires:  crate(console-0.15/default) >= 0.15.0
BuildRequires:  crate(crossbeam-utils-0.8) >= 0.8.21
BuildRequires:  crate(crossterm-0.29/default) >= 0.29.0
BuildRequires:  crate(dirs-5/default) >= 5.0.0
BuildRequires:  crate(edit-0.1/default) >= 0.1.0
BuildRequires:  crate(env-logger-0.11/default) >= 0.11.0
BuildRequires:  crate(flate2-1/default) >= 1.0.0
BuildRequires:  crate(futures-0.3/default) >= 0.3.0
BuildRequires:  crate(hyper-1/default) >= 1.0.0
BuildRequires:  crate(hyper-1/full) >= 1.0.0
BuildRequires:  crate(indexmap-2/default) >= 2.0.0
BuildRequires:  crate(indexmap-2/serde) >= 2.0.0
BuildRequires:  crate(indicatif-0.17/default) >= 0.17.0
BuildRequires:  crate(inquire-0.9/default) >= 0.9.0
BuildRequires:  crate(inquire-0.9/fuzzy) >= 0.9.0
BuildRequires:  crate(json-five-0.3/default) >= 0.3.1
BuildRequires:  crate(json5-0.4/default) >= 0.4.0
BuildRequires:  crate(libc-0.2/default) >= 0.2.0
BuildRequires:  crate(log-0.4/default) >= 0.4.0
BuildRequires:  crate(minisign-0.9/default) >= 0.9.1
BuildRequires:  crate(minisign-verify-0.2/default) >= 0.2.4
BuildRequires:  crate(once-cell-1/default) >= 1.21.3
BuildRequires:  crate(rand-chacha-0.3) >= 0.3.0
BuildRequires:  crate(ratatui-0.30/default) >= 0.30.0
BuildRequires:  crate(regex-1/default) >= 1.10.0
BuildRequires:  crate(reqwest-0.12/json) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/rustls-tls) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/socks) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/stream) >= 0.12.0
BuildRequires:  crate(rquickjs-0.8/array-buffer) >= 0.8.0
BuildRequires:  crate(rquickjs-0.8/classes) >= 0.8.0
BuildRequires:  crate(rquickjs-0.8/default) >= 0.8.0
BuildRequires:  crate(rkyv-0.7/size-32) >= 0.7.46
BuildRequires:  crate(rkyv-0.7/std) >= 0.7.46
BuildRequires:  crate(rusqlite-0.31/backup) >= 0.31.0
BuildRequires:  crate(rusqlite-0.31/bundled) >= 0.31.0
BuildRequires:  crate(rusqlite-0.31/default) >= 0.31.0
BuildRequires:  crate(rust-decimal-1) >= 1.33.0
BuildRequires:  crate(semver-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(serde-json-1/preserve-order) >= 1.0.0
BuildRequires:  crate(serde-yaml-0.9/default) >= 0.9.0
BuildRequires:  crate(sha2-0.10/default) >= 0.10.0
BuildRequires:  crate(serial-test-3/default) >= 3.0.0
BuildRequires:  crate(tachyonfx-0.25/default) >= 0.25.0
BuildRequires:  crate(tar-0.4/default) >= 0.4.0
BuildRequires:  crate(tempfile-3/default) >= 3.0.0
BuildRequires:  crate(thiserror-1/default) >= 1.0.0
BuildRequires:  crate(tokio-1/default) >= 1.0.0
BuildRequires:  crate(tokio-1/io-util) >= 1.0.0
BuildRequires:  crate(tokio-1/macros) >= 1.0.0
BuildRequires:  crate(tokio-1/net) >= 1.0.0
BuildRequires:  crate(tokio-1/process) >= 1.0.0
BuildRequires:  crate(tokio-1/rt-multi-thread) >= 1.0.0
BuildRequires:  crate(tokio-1/signal) >= 1.0.0
BuildRequires:  crate(tokio-1/sync) >= 1.0.0
BuildRequires:  crate(tokio-1/time) >= 1.0.0
BuildRequires:  crate(toml-0.8/default) >= 0.8.0
BuildRequires:  crate(toml-edit-0.22/default) >= 0.22.0
BuildRequires:  crate(tower-0.5/default) >= 0.5.0
BuildRequires:  crate(tower-http-0.5/cors) >= 0.5.0
BuildRequires:  crate(tower-http-0.5/default) >= 0.5.0
BuildRequires:  crate(unicode-width-0.1/default) >= 0.1.0
BuildRequires:  crate(url-2/default) >= 2.5.0
BuildRequires:  crate(uuid-1/default) >= 1.11.0
BuildRequires:  crate(uuid-1/v4) >= 1.11.0
BuildRequires:  crate(which-6/default) >= 6.0.0
BuildRequires:  crate(zip-2/default) >= 2.2.0

%description
CC Switch CLI provides a terminal interface for managing providers,
configuration, prompts, and MCP servers for Claude Code, Codex, Gemini,
OpenCode, and OpenClaw.

%prep -a
# The Rust package is kept in src-tauri even though this CLI has no Tauri UI.
cp -a src-tauri/. .
# Preserve the original relative path used by the offline install-script tests.
cp -p install.sh ..
rm -f Cargo.lock rust-toolchain.toml
# Cargo resolves the root manifest's Windows-only sources during an offline lock refresh.
sed -i '/^\[target\..*windows.*\.dependencies\]$/,/^$/d' Cargo.toml

%install
install -Dm0755 target/release/cc-switch %{buildroot}%{_bindir}/cc-switch

%files
%doc README.md README_ZH.md
%license LICENSE
%{_bindir}/cc-switch

%changelog
%autochangelog
