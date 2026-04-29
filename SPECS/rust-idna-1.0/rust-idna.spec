# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name idna
%global full_version 1.1.0
%global pkgname idna-1.0

Name:           rust-idna-1.0
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "idna"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/rust-url/
#!RemoteAsset:  sha256:3b0875f23caa03898994f6ddc501886a45c7d3d62d04d2d90788d47be1b1e4de
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(idna-adapter-1.0/default) >= 1.2.1
Requires:       crate(smallvec-1.0/const-generics) >= 1.15.1
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(utf8-iter-1.0/default) >= 1.0.4
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "idna"

%package     -n %{name}+compiled-data
Summary:        IDNA (Internationalizing Domain Names in Applications) and Punycode - feature "compiled_data"
Requires:       crate(%{pkgname})
Requires:       crate(idna-adapter-1.0/compiled-data) >= 1.2.1
Provides:       crate(%{pkgname}/compiled-data)

%description -n %{name}+compiled-data
This metapackage enables feature "compiled_data" for the Rust idna crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        IDNA (Internationalizing Domain Names in Applications) and Punycode - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/compiled-data)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust idna crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
