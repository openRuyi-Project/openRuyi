# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cc
%global full_version 1.0.96
%global pkgname cc-1.0

Name:           rust-cc-1.0
Version:        1.0.96
Release:        %autorelease
Summary:        Rust crate "cc"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cc-rs
#!RemoteAsset:  sha256:065a29261d53ba54260972629f9ca6bffa69bac13cd1fed61420f7fa68b9f8bd
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(cc) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "cc"

%package     -n %{name}+jobserver
Summary:        Build-time dependency for Cargo build scripts to assist in invoking the native C compiler to compile native C code into a static archive to be linked into Rust code - feature "jobserver"
Requires:       crate(%{pkgname})
Requires:       crate(jobserver-0.1) >= 0.1.30
Provides:       crate(%{pkgname}/jobserver)

%description -n %{name}+jobserver
This metapackage enables feature "jobserver" for the Rust cc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Build-time dependency for Cargo build scripts to assist in invoking the native C compiler to compile native C code into a static archive to be linked into Rust code - feature "libc"
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2) >= 0.2.62
Provides:       crate(%{pkgname}/libc)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust cc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Build-time dependency for Cargo build scripts to assist in invoking the native C compiler to compile native C code into a static archive to be linked into Rust code - feature "once_cell"
Requires:       crate(%{pkgname})
Requires:       crate(once-cell-1.0/default) >= 1.19
Provides:       crate(%{pkgname}/once-cell)

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust cc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parallel
Summary:        Build-time dependency for Cargo build scripts to assist in invoking the native C compiler to compile native C code into a static archive to be linked into Rust code - feature "parallel"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/jobserver)
Requires:       crate(%{pkgname}/libc)
Requires:       crate(%{pkgname}/once-cell)
Provides:       crate(%{pkgname}/parallel)

%description -n %{name}+parallel
This metapackage enables feature "parallel" for the Rust cc crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
