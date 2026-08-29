# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           asciinema
Version:        3.2.1
Release:        %autorelease
Summary:        Terminal session recorder, streamer and player
License:        GPL-3.0-or-later
URL:            https://asciinema.org
VCS:            git:https://github.com/asciinema/asciinema.git
#!RemoteAsset:  sha256:e7e49a09c664a76afc5bc25ca09871eb090bfbe68a2ddbc72750d3cb215d36f1
Source:         https://github.com/asciinema/asciinema/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  rust-rpm-macros
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  crate(anyhow-1/default) >= 1.0.0
BuildRequires:  crate(async-trait-0.1/default) >= 0.1.0
BuildRequires:  crate(avt-0.18/default) >= 0.18.0
BuildRequires:  crate(axum-0.8/http1) >= 0.8.0
BuildRequires:  crate(axum-0.8/ws) >= 0.8.0
BuildRequires:  crate(bytes-1/default) >= 1.11.0
BuildRequires:  crate(clap-4) >= 4.0.0
BuildRequires:  crate(clap-4/default) >= 4.0.0
BuildRequires:  crate(clap-4/derive) >= 4.0.0
BuildRequires:  crate(clap-4/wrap-help) >= 4.0.0
BuildRequires:  crate(clap-complete-4) >= 4.0.0
BuildRequires:  crate(clap-mangen-0.2) >= 0.2.0
BuildRequires:  crate(config-0.15/toml) >= 0.15.0
BuildRequires:  crate(futures-util-0.3/sink) >= 0.3.0
BuildRequires:  crate(nix-0.30/default) >= 0.30.0
BuildRequires:  crate(nix-0.30/fs) >= 0.30.0
BuildRequires:  crate(nix-0.30/poll) >= 0.30.0
BuildRequires:  crate(nix-0.30/process) >= 0.30.0
BuildRequires:  crate(nix-0.30/signal) >= 0.30.0
BuildRequires:  crate(nix-0.30/term) >= 0.30.0
BuildRequires:  crate(rand-0.9/default) >= 0.9.0
BuildRequires:  crate(reqwest-0.12/blocking) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/gzip) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/json) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/multipart) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/rustls-tls-native-roots) >= 0.12.0
BuildRequires:  crate(reqwest-0.12/stream) >= 0.12.0
BuildRequires:  crate(rgb-0.8) >= 0.8.0
BuildRequires:  crate(rust-embed-8/default) >= 8.8.0
BuildRequires:  crate(rustls-0.23/ring) >= 0.23.0
BuildRequires:  crate(rustyline-17) >= 17.0.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(signal-hook-0.3) >= 0.3.0
BuildRequires:  crate(signal-hook-tokio-0.3/default) >= 0.3.0
BuildRequires:  crate(signal-hook-tokio-0.3/futures-v0-3) >= 0.3.0
BuildRequires:  crate(tempfile-3/default) >= 3.23.0
BuildRequires:  crate(tokio-1/default) >= 1.40.0
BuildRequires:  crate(tokio-1/fs) >= 1.40.0
BuildRequires:  crate(tokio-1/net) >= 1.40.0
BuildRequires:  crate(tokio-1/process) >= 1.40.0
BuildRequires:  crate(tokio-1/rt-multi-thread) >= 1.40.0
BuildRequires:  crate(tokio-1/sync) >= 1.40.0
BuildRequires:  crate(tokio-1/time) >= 1.40.0
BuildRequires:  crate(tokio-stream-0.1/sync) >= 0.1.0
BuildRequires:  crate(tokio-stream-0.1/time) >= 0.1.0
BuildRequires:  crate(tokio-tungstenite-0.28/connect) >= 0.28.0
BuildRequires:  crate(tokio-tungstenite-0.28/rustls-tls-native-roots) >= 0.28.0
BuildRequires:  crate(tokio-util-0.7/default) >= 0.7.0
BuildRequires:  crate(tokio-util-0.7/rt) >= 0.7.0
BuildRequires:  crate(tower-http-0.6/compression-gzip) >= 0.6.0
BuildRequires:  crate(tower-http-0.6/default) >= 0.6.0
BuildRequires:  crate(tower-http-0.6/trace) >= 0.6.0
BuildRequires:  crate(tracing-0.1) >= 0.1.0
BuildRequires:  crate(tracing-subscriber-0.3/env-filter) >= 0.3.20
BuildRequires:  crate(tracing-subscriber-0.3/fmt) >= 0.3.20
BuildRequires:  crate(url-2) >= 2.5.0
BuildRequires:  crate(url-2/default) >= 2.5.0
BuildRequires:  crate(uuid-1/default) >= 1.6.0
BuildRequires:  crate(uuid-1/v4) >= 1.6.0
BuildRequires:  crate(which-8/default) >= 8.0.0
BuildRequires:  bash-completion
# For Tests
BuildRequires:  pkgconfig(python3)

Recommends:     agg

%description
asciinema (aka asciinema CLI or asciinema recorder) is a command-line tool
for recording and live streaming terminal sessions.

%build -p
# Generate man pages and shell completion files
export ASCIINEMA_GEN_DIR=assets

%install
install -Dpm 0755 target/release/asciinema %{buildroot}%{_bindir}/asciinema
install -Dpm 0644 assets/man/*.1 -t %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 assets/completion/asciinema.bash -t %{buildroot}/%{bash_completions_dir}

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/asciinema
%{_mandir}/man1/asciinema*.1*
%{bash_completions_dir}/asciinema.bash

%changelog
%autochangelog
