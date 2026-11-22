# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name annotate-snippets
%global full_version 0.12.13
%global pkgname annotate-snippets-0.12

Name:           rust-annotate-snippets-0.12
Version:        0.12.13
Release:        %autorelease
Summary:        Rust crate "annotate-snippets"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/annotate-snippets-rs
#!RemoteAsset:  sha256:74fc7650eedcb2fee505aad48491529e408f0e854c2d9f63eb86c1361b9b3f93
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1) >= 1.0.13
Requires:       crate(unicode-width-0.2/default) >= 0.2.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/testing-colors) = %{version}

%description
Source code for takopackized Rust crate "annotate-snippets"

%package     -n %{name}+simd
Summary:        Format diagnostic reports, including highlighting snippets of text - feature "simd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2) >= 2.8.0
Provides:       crate(%{pkgname}/simd) = %{version}

%description -n %{name}+simd
This metapackage enables feature "simd" for the Rust annotate-snippets crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Format diagnostic reports, including highlighting snippets of text - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anstyle-1/std) >= 1.0.13
Requires:       crate(memchr-2/std) >= 2.8.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust annotate-snippets crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%license %{_datadir}/cargo/registry/%{crate_name}-%{version}/LICENSE-APACHE
%license %{_datadir}/cargo/registry/%{crate_name}-%{version}/LICENSE-MIT
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
