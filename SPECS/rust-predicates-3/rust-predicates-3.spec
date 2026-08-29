# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name predicates
%global full_version 3.1.4
%global pkgname predicates-3

Name:           rust-predicates-3
Version:        3.1.4
Release:        %autorelease
Summary:        Rust crate "predicates"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/predicates-rs
#!RemoteAsset:  sha256:ada8f2932f28a27ee7b70dd6c1c39ea0675c55a36879ab92f3a715eaa1e63cfe
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1/default) >= 1.0.0
Requires:       crate(predicates-core-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/color) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "predicates"

%package     -n %{name}+default
Summary:        Boolean-valued predicate functions - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/color) = %{version}
Requires:       crate(%{pkgname}/diff) = %{version}
Requires:       crate(%{pkgname}/float-cmp) = %{version}
Requires:       crate(%{pkgname}/normalize-line-endings) = %{version}
Requires:       crate(%{pkgname}/regex) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust predicates crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+diff
Summary:        Boolean-valued predicate functions - feature "diff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(difflib-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/diff) = %{version}

%description -n %{name}+diff
This metapackage enables feature "diff" for the Rust predicates crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+float-cmp
Summary:        Boolean-valued predicate functions - feature "float-cmp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(float-cmp-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/float-cmp) = %{version}

%description -n %{name}+float-cmp
This metapackage enables feature "float-cmp" for the Rust predicates crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+normalize-line-endings
Summary:        Boolean-valued predicate functions - feature "normalize-line-endings"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(normalize-line-endings-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/normalize-line-endings) = %{version}

%description -n %{name}+normalize-line-endings
This metapackage enables feature "normalize-line-endings" for the Rust predicates crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Boolean-valued predicate functions - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust predicates crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
