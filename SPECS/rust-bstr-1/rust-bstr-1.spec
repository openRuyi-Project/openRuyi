# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bstr
%global full_version 1.12.1
%global pkgname bstr-1

Name:           rust-bstr-1
Version:        1.12.1
Release:        %autorelease
Summary:        Rust crate "bstr"
License:        MIT OR Apache-2.0
URL:            https://github.com/BurntSushi/bstr
#!RemoteAsset:  sha256:63044e1ae8e69f3b5a92c736ca6269b8d12fa7efe39bf34ddb06d102cf0e2cab
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2) >= 2.7.1
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "bstr"

%package     -n %{name}+alloc
Summary:        String type that is not required to be valid UTF-8 - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2/alloc) >= 2.7.1
Requires:       crate(serde-1/alloc) >= 1.0.85
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust bstr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        String type that is not required to be valid UTF-8 - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/unicode) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bstr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        String type that is not required to be valid UTF-8 - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.85
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bstr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        String type that is not required to be valid UTF-8 - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(memchr-2/std) >= 2.7.1
Requires:       crate(serde-1/std) >= 1.0.85
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bstr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        String type that is not required to be valid UTF-8 - feature "unicode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-automata-0.4/dfa-search) >= 0.4.1
Provides:       crate(%{pkgname}/unicode) = %{version}

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust bstr crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
