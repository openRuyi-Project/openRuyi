# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ctor
%global full_version 0.6.3
%global pkgname ctor-0.6

Name:           rust-ctor-0.6
Version:        0.6.3
Release:        %autorelease
Summary:        Rust crate "ctor"
License:        Apache-2.0 OR MIT
URL:            https://github.com/mmastrac/rust-ctor
#!RemoteAsset:  sha256:424e0138278faeb2b401f174ad17e715c829512d74f3d1e81eb43365c2e0590e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ctor"

%package     -n %{name}+no-warn-on-missing-unsafe
Summary:        __attribute__((constructor)) for Rust - feature "__no_warn_on_missing_unsafe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dtor-0.1/no-warn-on-missing-unsafe) >= 0.1.0
Provides:       crate(%{pkgname}/no-warn-on-missing-unsafe) = %{version}

%description -n %{name}+no-warn-on-missing-unsafe
This metapackage enables feature "__no_warn_on_missing_unsafe" for the Rust ctor crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        __attribute__((constructor)) for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dtor) = %{version}
Requires:       crate(%{pkgname}/no-warn-on-missing-unsafe) = %{version}
Requires:       crate(%{pkgname}/proc-macro) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ctor crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dtor
Summary:        __attribute__((constructor)) for Rust - feature "dtor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dtor-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/dtor) = %{version}

%description -n %{name}+dtor
This metapackage enables feature "dtor" for the Rust ctor crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro
Summary:        __attribute__((constructor)) for Rust - feature "proc_macro"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ctor-proc-macro-0.0.7/default) >= 0.0.7
Requires:       crate(dtor-0.1/proc-macro) >= 0.1.0
Provides:       crate(%{pkgname}/proc-macro) = %{version}

%description -n %{name}+proc-macro
This metapackage enables feature "proc_macro" for the Rust ctor crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+used-linker
Summary:        __attribute__((constructor)) for Rust - feature "used_linker"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dtor-0.1/used-linker) >= 0.1.0
Provides:       crate(%{pkgname}/used-linker) = %{version}

%description -n %{name}+used-linker
This metapackage enables feature "used_linker" for the Rust ctor crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
