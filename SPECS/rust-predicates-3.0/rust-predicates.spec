# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name predicates
%global full_version 3.1.3
%global pkgname predicates-3.0

Name:           rust-predicates-3.0
Version:        3.1.3
Release:        %autorelease
Summary:        Rust crate "predicates"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/predicates-rs
#!RemoteAsset:  sha256:a5d19ee57562043d37e82899fade9a22ebab7be9cef5026b07fda9cdd4293573
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1.0/default) >= 1.0.14
Requires:       crate(predicates-core-1.0/default) >= 1.0.9
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/color)
Provides:       crate(%{pkgname}/unstable)

%description
Source code for takopackized Rust crate "predicates"

%package     -n %{name}+default
Summary:        Boolean-valued predicate functions - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/color)
Requires:       crate(%{pkgname}/diff)
Requires:       crate(%{pkgname}/float-cmp)
Requires:       crate(%{pkgname}/normalize-line-endings)
Requires:       crate(%{pkgname}/regex)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust predicates crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+diff
Summary:        Boolean-valued predicate functions - feature "diff"
Requires:       crate(%{pkgname})
Requires:       crate(difflib-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/diff)

%description -n %{name}+diff
This metapackage enables feature "diff" for the Rust predicates crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+float-cmp
Summary:        Boolean-valued predicate functions - feature "float-cmp"
Requires:       crate(%{pkgname})
Requires:       crate(float-cmp-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/float-cmp)

%description -n %{name}+float-cmp
This metapackage enables feature "float-cmp" for the Rust predicates crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+normalize-line-endings
Summary:        Boolean-valued predicate functions - feature "normalize-line-endings"
Requires:       crate(%{pkgname})
Requires:       crate(normalize-line-endings-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/normalize-line-endings)

%description -n %{name}+normalize-line-endings
This metapackage enables feature "normalize-line-endings" for the Rust predicates crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Boolean-valued predicate functions - feature "regex"
Requires:       crate(%{pkgname})
Requires:       crate(regex-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/regex)

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust predicates crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
