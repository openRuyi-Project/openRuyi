# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rend
%global full_version 0.4.2
%global pkgname rend-0.4

Name:           rust-rend-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "rend"
License:        MIT
URL:            https://github.com/djkoloski/rend
#!RemoteAsset:  sha256:71fe3824f5629716b1589be05dacd749f6aa084c87e00e016714a8cdfccc997c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rend"

%package     -n %{name}+bytecheck
Summary:        Endian-aware primitives for Rust - feature "bytecheck" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytecheck-0.6) >= 0.6.7
Provides:       crate(%{pkgname}/bytecheck) = %{version}
Provides:       crate(%{pkgname}/validation) = %{version}

%description -n %{name}+bytecheck
This metapackage enables feature "bytecheck" for the Rust rend crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "validation" feature.

%package     -n %{name}+bytemuck
Summary:        Endian-aware primitives for Rust - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/derive) >= 1.4.0
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust rend crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Endian-aware primitives for Rust - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytecheck-0.6/std) >= 0.6.7
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rend crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
