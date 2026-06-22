# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name const_panic
%global full_version 0.2.15
%global pkgname const-panic-0.2

Name:           rust-const-panic-0.2
Version:        0.2.15
Release:        %autorelease
Summary:        Rust crate "const_panic"
License:        Zlib
URL:            https://github.com/rodrimati1992/const_panic/
#!RemoteAsset:  sha256:e262cdaac42494e3ae34c43969f9cdeb7da178bdb4b66fa6a1ea2edb4c8ae652
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(typewit-1) >= 1.9.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/docsrs) = %{version}
Provides:       crate(%{pkgname}/non-basic) = %{version}
Provides:       crate(%{pkgname}/rust-1-64) = %{version}
Provides:       crate(%{pkgname}/rust-1-82) = %{version}
Provides:       crate(%{pkgname}/rust-1-88) = %{version}
Provides:       crate(%{pkgname}/rust-latest-stable) = %{version}
Provides:       crate(%{pkgname}/test) = %{version}

%description
Source code for takopackized Rust crate "const_panic"

%package     -n %{name}+ui-tests
Summary:        Const panic with formatting - feature "__ui_tests"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/test) = %{version}
Requires:       crate(%{pkgname}/trybuild) = %{version}
Provides:       crate(%{pkgname}/ui-tests) = %{version}

%description -n %{name}+ui-tests
This metapackage enables feature "__ui_tests" for the Rust const_panic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+const-panic-proc-macros
Summary:        Const panic with formatting - feature "const_panic_proc_macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(const-panic-proc-macros-0.2/default) >= 0.2.15
Provides:       crate(%{pkgname}/const-panic-proc-macros) = %{version}

%description -n %{name}+const-panic-proc-macros
This metapackage enables feature "const_panic_proc_macros" for the Rust const_panic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Const panic with formatting - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/const-panic-proc-macros) = %{version}
Requires:       crate(%{pkgname}/non-basic) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust const_panic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+trybuild
Summary:        Const panic with formatting - feature "trybuild"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(trybuild-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/trybuild) = %{version}

%description -n %{name}+trybuild
This metapackage enables feature "trybuild" for the Rust const_panic crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
