# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-symbols
%global full_version 0.2.2
%global pkgname objc2-symbols-0.2

Name:           rust-objc2-symbols-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "objc2-symbols"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:0a684efe3dec1b305badae1a28f6555f6ddd3bb2c2267896782858d5a78404dc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.5) >= 0.5.2
Requires:       crate(objc2-foundation-0.2) >= 0.2.2
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "objc2-symbols"

%package     -n %{name}+nssymboleffect
Summary:        Bindings to the Symbols framework - feature "NSSymbolEffect" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/all) = %{version}
Provides:       crate(%{pkgname}/nssymboleffect) = %{version}

%description -n %{name}+nssymboleffect
This metapackage enables feature "NSSymbolEffect" for the Rust objc2-symbols crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "all" feature.

%package     -n %{name}+alloc
Summary:        Bindings to the Symbols framework - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-0.5/alloc) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/alloc) >= 0.2.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust objc2-symbols crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bindings to the Symbols framework - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(objc2-0.5/std) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/std) >= 0.2.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust objc2-symbols crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
