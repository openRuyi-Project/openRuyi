# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-uniform-type-identifiers
%global full_version 0.2.2
%global pkgname objc2-uniform-type-identifiers-0.2

Name:           rust-objc2-uniform-type-identifiers-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "objc2-uniform-type-identifiers"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:44fa5f9748dbfe1ca6c0b79ad20725a11eca7c2218bceb4b005cb1be26273bfe
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.5) >= 0.5.2
Requires:       crate(objc2-foundation-0.2) >= 0.2.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/utcoretypes) = %{version}
Provides:       crate(%{pkgname}/utdefines) = %{version}

%description
Source code for takopackized Rust crate "objc2-uniform-type-identifiers"

%package     -n %{name}+nsitemprovider-uttype
Summary:        Bindings to the UniformTypeIdentifiers framework - feature "NSItemProvider_UTType"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsitemprovider) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsprogress) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsitemprovider-uttype) = %{version}

%description -n %{name}+nsitemprovider-uttype
This metapackage enables feature "NSItemProvider_UTType" for the Rust objc2-uniform-type-identifiers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+utadditions
Summary:        Bindings to the UniformTypeIdentifiers framework - feature "UTAdditions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/utadditions) = %{version}

%description -n %{name}+utadditions
This metapackage enables feature "UTAdditions" for the Rust objc2-uniform-type-identifiers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uttagclass
Summary:        Bindings to the UniformTypeIdentifiers framework - feature "UTTagClass"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/uttagclass) = %{version}

%description -n %{name}+uttagclass
This metapackage enables feature "UTTagClass" for the Rust objc2-uniform-type-identifiers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uttype
Summary:        Bindings to the UniformTypeIdentifiers framework - feature "UTType"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/uttype) = %{version}

%description -n %{name}+uttype
This metapackage enables feature "UTType" for the Rust objc2-uniform-type-identifiers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all
Summary:        Bindings to the UniformTypeIdentifiers framework - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/nsitemprovider-uttype) = %{version}
Requires:       crate(%{pkgname}/utadditions) = %{version}
Requires:       crate(%{pkgname}/utcoretypes) = %{version}
Requires:       crate(%{pkgname}/utdefines) = %{version}
Requires:       crate(%{pkgname}/uttagclass) = %{version}
Requires:       crate(%{pkgname}/uttype) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust objc2-uniform-type-identifiers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Bindings to the UniformTypeIdentifiers framework - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5/alloc) >= 0.5.1
Requires:       crate(objc2-0.5/alloc) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/alloc) >= 0.2.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust objc2-uniform-type-identifiers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the UniformTypeIdentifiers framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5) >= 0.5.1
Requires:       crate(objc2-foundation-0.2/block2) >= 0.2.2
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-uniform-type-identifiers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bindings to the UniformTypeIdentifiers framework - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(block2-0.5/std) >= 0.5.1
Requires:       crate(objc2-0.5/std) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/std) >= 0.2.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust objc2-uniform-type-identifiers crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
