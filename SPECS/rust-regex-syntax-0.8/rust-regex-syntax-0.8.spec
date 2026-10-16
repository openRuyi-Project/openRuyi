# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name regex-syntax
%global full_version 0.8.11
%global pkgname regex-syntax-0.8

Name:           rust-regex-syntax-0.8
Version:        0.8.11
Release:        %autorelease
Summary:        Rust crate "regex-syntax"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/regex/tree/master/regex-syntax
#!RemoteAsset:  sha256:d6f6ff9a378485b298a5286656da665ba74413d36db0979633275d2e708145d4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unicode-age) = %{version}
Provides:       crate(%{pkgname}/unicode-bool) = %{version}
Provides:       crate(%{pkgname}/unicode-case) = %{version}
Provides:       crate(%{pkgname}/unicode-gencat) = %{version}
Provides:       crate(%{pkgname}/unicode-perl) = %{version}
Provides:       crate(%{pkgname}/unicode-script) = %{version}
Provides:       crate(%{pkgname}/unicode-segment) = %{version}

%description
Source code for takopackized Rust crate "regex-syntax"

%package     -n %{name}+arbitrary
Summary:        Regular expression parser - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.3.0
Requires:       crate(arbitrary-1/derive) >= 1.3.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust regex-syntax crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Regular expression parser - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/unicode) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust regex-syntax crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Regular expression parser - feature "unicode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/unicode-age) = %{version}
Requires:       crate(%{pkgname}/unicode-bool) = %{version}
Requires:       crate(%{pkgname}/unicode-case) = %{version}
Requires:       crate(%{pkgname}/unicode-gencat) = %{version}
Requires:       crate(%{pkgname}/unicode-perl) = %{version}
Requires:       crate(%{pkgname}/unicode-script) = %{version}
Requires:       crate(%{pkgname}/unicode-segment) = %{version}
Provides:       crate(%{pkgname}/unicode) = %{version}

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust regex-syntax crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
