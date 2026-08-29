# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-xwin
%global full_version 0.22.0
%global pkgname cargo-xwin-0.22

Name:           rust-cargo-xwin-0.22
Version:        0.22.0
Release:        %autorelease
Summary:        Rust crate "cargo-xwin"
License:        MIT
URL:            https://github.com/rust-cross/cargo-xwin
#!RemoteAsset:  sha256:c010a0e90e1dc09a90428c8768808bb4ad8cd7523e4df38719418e14579a9e37
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.53
Requires:       crate(cargo-config2-0.1/default) >= 0.1.4
Requires:       crate(cargo-options-0.7/default) >= 0.7.6
Requires:       crate(clap-4/default) >= 4.3.0
Requires:       crate(clap-4/derive) >= 4.3.0
Requires:       crate(clap-4/env) >= 4.3.0
Requires:       crate(clap-4/unstable-styles) >= 4.3.0
Requires:       crate(clap-4/wrap-help) >= 4.3.0
Requires:       crate(dirs-6/default) >= 6.0.0
Requires:       crate(fs-err-3/default) >= 3.0.0
Requires:       crate(humantime-2/default) >= 2.1.0
Requires:       crate(indicatif-0.18/default) >= 0.18.3
Requires:       crate(paste-1/default) >= 1.0.12
Requires:       crate(path-slash-0.2/default) >= 0.2.0
Requires:       crate(serde-1/default) >= 1.0.216
Requires:       crate(serde-1/derive) >= 1.0.216
Requires:       crate(tar-0.4/default) >= 0.4.45
Requires:       crate(tracing-subscriber-0.3/default) >= 0.3.17
Requires:       crate(tracing-subscriber-0.3/fmt) >= 0.3.17
Requires:       crate(ureq-3/gzip) >= 3.0.12
Requires:       crate(ureq-3/json) >= 3.0.12
Requires:       crate(ureq-3/socks-proxy) >= 3.0.12
Requires:       crate(which-8/default) >= 8.0.0
Requires:       crate(xwin-0.9) >= 0.9.0
Requires:       crate(xz2-0.1/default) >= 0.1.7
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "cargo-xwin"

%package     -n %{name}+default
Summary:        Cross compile Cargo project to Windows MSVC target with ease - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rustls-tls) = %{version}
Requires:       crate(xz2-0.1/static) >= 0.1.7
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust cargo-xwin crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls
Summary:        Cross compile Cargo project to Windows MSVC target with ease - feature "native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ureq-3/gzip) >= 3.0.12
Requires:       crate(ureq-3/json) >= 3.0.12
Requires:       crate(ureq-3/native-tls) >= 3.0.12
Requires:       crate(ureq-3/socks-proxy) >= 3.0.12
Provides:       crate(%{pkgname}/native-tls) = %{version}

%description -n %{name}+native-tls
This metapackage enables feature "native-tls" for the Rust cargo-xwin crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls-tls
Summary:        Cross compile Cargo project to Windows MSVC target with ease - feature "rustls-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ureq-3/gzip) >= 3.0.12
Requires:       crate(ureq-3/json) >= 3.0.12
Requires:       crate(ureq-3/platform-verifier) >= 3.0.12
Requires:       crate(ureq-3/rustls) >= 3.0.12
Requires:       crate(ureq-3/socks-proxy) >= 3.0.12
Provides:       crate(%{pkgname}/rustls-tls) = %{version}

%description -n %{name}+rustls-tls
This metapackage enables feature "rustls-tls" for the Rust cargo-xwin crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
