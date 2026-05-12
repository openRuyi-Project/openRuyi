# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fastrand
%global full_version 2.3.0
%global pkgname fastrand-2.0

Name:           rust-fastrand-2.0
Version:        2.3.0
Release:        %autorelease
Summary:        Rust crate "fastrand"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/fastrand
#!RemoteAsset:  sha256:37909eebbb50d72f9059c3b6d82c0463f2ff062c9e95845c43a6c9c0355411be
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "fastrand"

%package     -n %{name}+getrandom
Summary:        Simple and fast random number generator - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(getrandom-0.2/default) >= 0.2.0
Requires:       crate(getrandom-0.2/js) >= 0.2.0
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust fastrand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+js
Summary:        Simple and fast random number generator - feature "js"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/getrandom)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/js)

%description -n %{name}+js
This metapackage enables feature "js" for the Rust fastrand crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
