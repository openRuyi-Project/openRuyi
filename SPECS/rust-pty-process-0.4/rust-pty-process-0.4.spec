# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pty-process
%global full_version 0.4.0
%global pkgname pty-process-0.4

Name:           rust-pty-process-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "pty-process"
License:        MIT
URL:            https://git.tozt.net/pty-process
#!RemoteAsset:  sha256:8749b545e244c90bf74a5767764cc2194f1888bb42f84015486a64c82bea5cc0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.147
Requires:       crate(rustix-0.38/default) >= 0.38.7
Requires:       crate(rustix-0.38/fs) >= 0.38.7
Requires:       crate(rustix-0.38/process) >= 0.38.7
Requires:       crate(rustix-0.38/pty) >= 0.38.7

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pty-process"

%package     -n %{name}+tokio
Summary:        Spawn commands attached to a pty - feature "tokio" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.29.1
Requires:       crate(tokio-1/fs) >= 1.29.1
Requires:       crate(tokio-1/net) >= 1.29.1
Requires:       crate(tokio-1/process) >= 1.29.1
Provides:       crate(%{pkgname}/async) = %{version}
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust pty-process crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "async" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
