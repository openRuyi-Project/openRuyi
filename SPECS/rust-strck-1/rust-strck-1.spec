# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name strck
%global full_version 1.0.0
%global pkgname strck-1

Name:           rust-strck-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "strck"
License:        MIT
URL:            https://github.com/QnnOkabayashi/strck
#!RemoteAsset:  sha256:42316e70da376f3d113a68d138a60d8a9883c604fe97942721ec2068dab13a9f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "strck"

%package     -n %{name}+ident
Summary:        Checked owned and borrowed strings - feature "ident"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-ident-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/ident) = %{version}

%description -n %{name}+ident
This metapackage enables feature "ident" for the Rust strck crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Checked owned and borrowed strings - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust strck crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
