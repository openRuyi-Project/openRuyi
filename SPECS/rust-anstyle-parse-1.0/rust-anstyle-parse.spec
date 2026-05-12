# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name anstyle-parse
%global full_version 1.0.0
%global pkgname anstyle-parse-1.0

Name:           rust-anstyle-parse-1.0
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "anstyle-parse"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-cli/anstyle.git
#!RemoteAsset:  sha256:52ce7f38b242319f7cabaa6813055467063ecdc9d355bbb4ce0c68908cd8130e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "anstyle-parse"

%package     -n %{name}+core
Summary:        Parse ANSI Style Escapes - feature "core"
Requires:       crate(%{pkgname})
Requires:       crate(arrayvec-0.7) >= 0.7.6
Provides:       crate(%{pkgname}/core)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust anstyle-parse crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+utf8
Summary:        Parse ANSI Style Escapes - feature "utf8" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(utf8parse-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/utf8)

%description -n %{name}+utf8
This metapackage enables feature "utf8" for the Rust anstyle-parse crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
