# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ctor
%global full_version 1.0.7
%global pkgname ctor-1

Name:           rust-ctor-1
Version:        1.0.7
Release:        %autorelease
Summary:        Rust crate "ctor"
License:        Apache-2.0 OR MIT
URL:            https://github.com/mmastrac/linktime
#!RemoteAsset:  sha256:01334b89b69ff726750c5ce5073fc8bd860e99aa9a8fc5ca11b04730e3aee97a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "ctor"

%package     -n %{name}+default
Summary:        Global, no_std-compatible constructors for all platforms that run before main (like C/C++ __attribute__((constructor))) - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/priority) = %{version}
Requires:       crate(%{pkgname}/proc-macro) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ctor crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+priority
Summary:        Global, no_std-compatible constructors for all platforms that run before main (like C/C++ __attribute__((constructor))) - feature "priority"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(link-section-0.18) >= 0.18.0
Provides:       crate(%{pkgname}/priority) = %{version}

%description -n %{name}+priority
This metapackage enables feature "priority" for the Rust ctor crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro
Summary:        Global, no_std-compatible constructors for all platforms that run before main (like C/C++ __attribute__((constructor))) - feature "proc_macro"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(linktime-proc-macro-0.2/ctor) >= 0.2.0
Requires:       crate(linktime-proc-macro-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/proc-macro) = %{version}

%description -n %{name}+proc-macro
This metapackage enables feature "proc_macro" for the Rust ctor crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
