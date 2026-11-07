# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prost-build
%global full_version 0.9.0
%global pkgname prost-build-0.9

Name:           rust-prost-build-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "prost-build"
License:        Apache-2.0
URL:            https://github.com/tokio-rs/prost
#!RemoteAsset:  sha256:62941722fb675d463659e49c4f3fe1fe792ff24fe5bbaa9c08cd3b98a1c354f5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1) >= 1.0.0
Requires:       crate(heck-0.3/default) >= 0.3.0
Requires:       crate(itertools-0.10/default) >= 0.10.0
Requires:       crate(lazy-static-1/default) >= 1.4.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(multimap-0.8) >= 0.8.0
Requires:       crate(petgraph-0.6) >= 0.6.0
Requires:       crate(prost-0.9) >= 0.9.0
Requires:       crate(prost-types-0.9) >= 0.9.0
Requires:       crate(regex-1/default) >= 1.5.4
Requires:       crate(tempfile-3/default) >= 3.0.0
Requires:       crate(which-4) >= 4.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Requires:       pkgconfig(protobuf)

%prep -a
# Use the system compiler instead of the bundled executables for other hosts.
rm -f third-party/protobuf/protoc-*

%patchlist
# Select the installed Protobuf compiler and headers.
2000-Use-the-system-Protobuf-compiler-and-include-directory.patch

%description
Source code for takopackized Rust crate "prost-build"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
