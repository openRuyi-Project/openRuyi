# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           aardvark-dns
Version:        1.17.1
Release:        %autorelease
License:        Apache-2.0 AND MIT AND Zlib
Summary:        Authoritative DNS server for A/AAAA container records
URL:            https://github.com/containers/aardvark-dns
#!RemoteAsset:  sha256:25b39bfad079a03862825b2f9db8b71b82fc80aad5552a9c76ea912edc9b889e
Source0:        https://github.com/containers/aardvark-dns/archive/v%{version}.tar.gz
BuildSystem:    rust

# Relax the clap requirement to allow compatible 4.x providers.
Patch2000:      2000-fix-version.patch

BuildOption(build):  -- --bin aardvark-dns

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(arc-swap-1/default) >= 1.9.1
BuildRequires:  crate(chrono-0.4/default) >= 0.4.44
BuildRequires:  crate(clap-4/default) >= 4.6.1
BuildRequires:  crate(clap-4/derive) >= 4.6.1
BuildRequires:  crate(flume-0.11/default) >= 0.11.1
BuildRequires:  crate(futures-0.3/default) >= 0.3.32
BuildRequires:  crate(futures-util-0.3) >= 0.3.32
BuildRequires:  crate(hickory-client-0.25/default) >= 0.25.2
BuildRequires:  crate(hickory-proto-0.25/default) >= 0.25.2
BuildRequires:  crate(hickory-proto-0.25/tokio) >= 0.25.2
BuildRequires:  crate(hickory-server-0.25/default) >= 0.25.2
BuildRequires:  crate(inotify-0.11/default) >= 0.11.1
BuildRequires:  crate(libc-0.2/default) >= 0.2.186
BuildRequires:  crate(log-0.4/default) >= 0.4.30
BuildRequires:  crate(nix-0.30/default) >= 0.30.1
BuildRequires:  crate(nix-0.30/fs) >= 0.30.1
BuildRequires:  crate(nix-0.30/net) >= 0.30.1
BuildRequires:  crate(nix-0.30/signal) >= 0.30.1
BuildRequires:  crate(syslog-7/default) >= 7.0.0
BuildRequires:  crate(tokio-1/default) >= 1.52.3
BuildRequires:  crate(tokio-1/macros) >= 1.52.3
BuildRequires:  crate(tokio-1/net) >= 1.52.3
BuildRequires:  crate(tokio-1/rt-multi-thread) >= 1.52.3
BuildRequires:  crate(tokio-1/signal) >= 1.52.3

%description
%{summary}

Forwards other requests to configured resolvers.
Read more about configuration in `src/backend/mod.rs`.

%build -p
%ifarch riscv64
export RUST_MIN_STACK=16777216
export CARGO_PROFILE_RELEASE_OPT_LEVEL=2
%endif

%install
install -Dm0755 target/release/aardvark-dns %{buildroot}%{_libexecdir}/podman/aardvark-dns

%check
# Upstream's integration tests require network namespace setup, bats, and a
# container-oriented environment. Keep the build check minimal here.

%files
%doc README.md
%license LICENSE
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/aardvark-dns

%changelog
%autochangelog
