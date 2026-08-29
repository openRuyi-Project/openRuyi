# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sendfd
%global full_version 0.4.4
%global pkgname sendfd-0.4

Name:           rust-sendfd-0.4
Version:        0.4.4
Release:        %autorelease
Summary:        Rust crate "sendfd"
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/standard-ai/sendfd
#!RemoteAsset:  sha256:b183bfd5b1bc64ab0c1ef3ee06b008a9ef1b68a7d3a99ba566fbfe7a7c6d745b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sendfd"

%package     -n %{name}+tokio
Summary:        Send file descriptors along with data over UNIX domain sockets - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/net) >= 1.0.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust sendfd crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
