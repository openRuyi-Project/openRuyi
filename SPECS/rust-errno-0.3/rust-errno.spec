# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name errno
%global full_version 0.3.14
%global pkgname errno-0.3

Name:           rust-errno-0.3
Version:        0.3.14
Release:        %autorelease
Summary:        Rust crate "errno"
License:        MIT OR Apache-2.0
URL:            https://github.com/lambda-fairy/rust-errno
#!RemoteAsset:  sha256:39cab71617ae0d63f51a36d69f866391735b51691dbda63cf6f96d042b63efeb
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2) >= 0.2.183
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-diagnostics-debug) >= 0.61.2
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "errno"

%package     -n %{name}+std
Summary:        Cross-platform interface to the `errno` variable - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2/std) >= 0.2.183
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust errno crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
