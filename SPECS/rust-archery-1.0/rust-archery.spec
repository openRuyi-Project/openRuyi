# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name archery
%global full_version 1.2.0
%global pkgname archery-1.0

Name:           rust-archery-1.0
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "archery"
License:        MPL-2.0
URL:            https://github.com/orium/archery
#!RemoteAsset:  sha256:8967cd1cc9e9e1954f644e14fbd6042fe9a37da96c52a67e44a2ac18261f8561
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(static-assertions-1.0/default) >= 1.1.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/fatal-warnings)

%description
Source code for takopackized Rust crate "archery"

%package     -n %{name}+serde
Summary:        Abstract over the atomicity of reference-counting pointers - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.197
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust archery crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+triomphe
Summary:        Abstract over the atomicity of reference-counting pointers - feature "triomphe"
Requires:       crate(%{pkgname})
Requires:       crate(triomphe-0.1) >= 0.1.9
Provides:       crate(%{pkgname}/triomphe)

%description -n %{name}+triomphe
This metapackage enables feature "triomphe" for the Rust archery crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
