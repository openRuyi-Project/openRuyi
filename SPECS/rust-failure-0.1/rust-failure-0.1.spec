# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name failure
%global full_version 0.1.8
%global pkgname failure-0.1

Name:           rust-failure-0.1
Version:        0.1.8
Release:        %autorelease
Summary:        Rust crate "failure"
License:        MIT OR Apache-2.0
URL:            https://rust-lang-nursery.github.io/failure/
#!RemoteAsset:  sha256:d32e9bd16cc02eae7db7ef620b392808b89f6a5e16bb3497d159c6b92a0f4f86
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "failure"

%package     -n %{name}+backtrace
Summary:        Experimental error handling abstraction - feature "backtrace" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(backtrace-0.3/default) >= 0.3.3
Provides:       crate(%{pkgname}/backtrace) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+backtrace
This metapackage enables feature "backtrace" for the Rust failure crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std" feature.

%package     -n %{name}+default
Summary:        Experimental error handling abstraction - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust failure crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+failure-derive
Summary:        Experimental error handling abstraction - feature "failure_derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(failure-derive-0.1/default) >= 0.1.7
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/failure-derive) = %{version}

%description -n %{name}+failure-derive
This metapackage enables feature "failure_derive" for the Rust failure crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
