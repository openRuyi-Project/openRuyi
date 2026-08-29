# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name typewit
%global full_version 1.15.2
%global pkgname typewit-1

Name:           rust-typewit-1
Version:        1.15.2
Release:        %autorelease
Summary:        Rust crate "typewit"
License:        Zlib
URL:            https://github.com/rodrimati1992/typewit/
#!RemoteAsset:  sha256:214ca0b2191785cbc06209b9ca1861e048e39b5ba33574b3cedd58363d5bb5f6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/adt-const-marker) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/const-marker) = %{version}
Provides:       crate(%{pkgname}/const-marker-extra-impls) = %{version}
Provides:       crate(%{pkgname}/docsrs) = %{version}
Provides:       crate(%{pkgname}/generic-const-exprs) = %{version}
Provides:       crate(%{pkgname}/mut-refs) = %{version}
Provides:       crate(%{pkgname}/nightly-mut-refs) = %{version}
Provides:       crate(%{pkgname}/rust-1-61) = %{version}
Provides:       crate(%{pkgname}/rust-1-65) = %{version}
Provides:       crate(%{pkgname}/rust-1-83) = %{version}
Provides:       crate(%{pkgname}/rust-stable) = %{version}
Provides:       crate(%{pkgname}/test-doc-lints) = %{version}

%description
Source code for takopackized Rust crate "typewit"

%package     -n %{name}+test-serde
Summary:        Type-witness-based abstractions, mostly for emulating polymorphism in const fns - feature "__test_serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/postcard) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/test-serde) = %{version}

%description -n %{name}+test-serde
This metapackage enables feature "__test_serde" for the Rust typewit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Type-witness-based abstractions, mostly for emulating polymorphism in const fns - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/const-marker-extra-impls) = %{version}
Requires:       crate(%{pkgname}/proc-macros) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust typewit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+postcard
Summary:        Type-witness-based abstractions, mostly for emulating polymorphism in const fns - feature "postcard"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(postcard-1) >= 1.0.0
Provides:       crate(%{pkgname}/postcard) = %{version}

%description -n %{name}+postcard
This metapackage enables feature "postcard" for the Rust typewit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-
Summary:        Type-witness-based abstractions, mostly for emulating polymorphism in const fns - feature "serde_" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.200
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-) = %{version}

%description -n %{name}+serde-
This metapackage enables feature "serde_" for the Rust typewit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde" feature.

%package     -n %{name}+serde-json
Summary:        Type-witness-based abstractions, mostly for emulating polymorphism in const fns - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust typewit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+trybuild
Summary:        Type-witness-based abstractions, mostly for emulating polymorphism in const fns - feature "trybuild" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(trybuild-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/trybuild) = %{version}
Provides:       crate(%{pkgname}/ui-tests) = %{version}

%description -n %{name}+trybuild
This metapackage enables feature "trybuild" for the Rust typewit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "__ui_tests" feature.

%package     -n %{name}+typewit-proc-macros
Summary:        Type-witness-based abstractions, mostly for emulating polymorphism in const fns - feature "typewit_proc_macros" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(typewit-proc-macros-1/default) >= 1.8.1
Provides:       crate(%{pkgname}/proc-macros) = %{version}
Provides:       crate(%{pkgname}/typewit-proc-macros) = %{version}

%description -n %{name}+typewit-proc-macros
This metapackage enables feature "typewit_proc_macros" for the Rust typewit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "proc_macros" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
